+++
date = '2025-07-29T10:09:50.935429+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 博客Blueprint'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

写博客的Blueprint跟写身份认证的Blueprint所使用的技术是一样的。博客应该列出所有的帖子，允许登录的用户去创建帖子，允许发帖用户去编辑或者删除帖子。

当我们实现每个视图的时候，请保持服务器一直处于运行状态。在保存更改时，请尝试访问浏览器中的URL并进行测试。

## Blueprint

在应用程序工厂中定义blueprint并注册它

baby/blog.py

```py

#! _*_ coding: utf-8 _*_

from flask import (
    Blueprint, flash, g, redirect, request, render_template, url_for
)

from werkzeug.exceptions import abort
from baby.auth import login_required
from baby.db import get_db

bp = Blueprint('blog', __name__)

```

使用[**app.register\_blueprint()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.register_blueprint)在工厂中导入并注册blueprint。放下面的代码在工厂的底部，在返回变量app之前。

baby/**init**.py

```py

def create_app(test_config=None):
    # 忽略已经有的部分代码

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

```

不像身份认证blueprint，博客blueprint没有使用`url_prefix`，因此index视图将被放在`/`路由上，`create`视图位于`/create`，依此类推。博客是Baby的主要特色，因此博客索引将成为主要索引。

但是，下面定义的`index`视图的endpoint将是`blog.index`。一些身份验证视图引用了普通`index`endpoint。[**app.add\_url\_rule()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.add_url_rule)将endpoint名称为`'index'`与`/`url相关联，以便`url_for('index')`或`url_for('blog.index')`都可以工作，生成相同`/`URL的方式。

在另一个应用程序中，您可以为博客blueprint提供`url_prefix`，并在应用程序工厂中定义单独的`index`视图，类似于`hello`视图。然后`index`和`blog.index`endpoint和URL会有所不同。

## Index视图

index视图将显示所有的帖子，最近的一个。这里使用了`JOIN`，可以关联user表来获得用户的信息在结果中展示。

baby/blog.py

```py

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

```

baby/templates/blog/index.html

```html

{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Posts{% endblock %}</h1>
  {% if g.user %}
    <a class="action" href="{{url_for('blog.create')}}">New</a>
  {% endif %}
{% endblock %}

{% block content %}
  {% for post in posts %}
    <article class="post">
      <header>
        <div>
          <h1>{{ post['title'] }}</h1>
          <div class="about">by {{ post['username'] }} on {{ post['created'].strftime('%Y-%m-%d') }}
        </div>
        {% if g.user['id'] == post['author_id'] %}
          <a class="action" href="{{ url_for('blog.update', id=post['id']) }}">Edit</a>
        {% endif %}
      </header>
      <p class="body">{{ post['body'] }}</p>
    </article>
    {% if not loop.last %}
    <hr />
    {% endif %}
  {% endfor %}
{% endblock %}

```

当用户登录后，`header`部分会添加一个`create`视图的链接，当用户是帖子的作者，将会看到一个指向`update`视图的'Edit'链接。`loop.last`是[Jinja for loops](http://jinja.pocoo.org/docs/2.10/templates/#for)中的一个可用的特殊变量。它用于在每个帖子之后显示除最后一个之外的一行，以便在视觉上将它们分开。

## Create视图

`create`视图与身份认证`register`视图的工作方式相同。显示表单，或验证发布的数据，并将帖子添加到数据库或显示错误。之前编写的`login_required`装饰器用于博客视图。一个用户必须在登录后才能访问这些视图，否则用户将被重定向到登录页面。

baby/blog.py

```py

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?,?,?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

```

baby/templates/blog/create.html

```html

{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}New Posts{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="POST">
    <label for="title">Title</label>
    <input id='title' name='title' value="{{ request.form['title'] }}" required/>
    <label for="body">body</label>
    <textarea id='body' name='body' value="{{ request.form['body'] }}"></textarea>
    <input type="submit" value="Save" />
  </form>
{% endblock %}

```

## Update视图

update和delete视图需要通过id获取post，并且检查post的作者与登录用户是否匹配。为了避免代码重复，可以写一个函数来获取post，并且每个视图都能调用。

baby/blog.py

```py

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

```

[abort()](http://flask.pocoo.org/docs/1.0/api/#flask.abort)将引发一个返回HTTP状态代码的特殊异常。它需要一个可选的消息来显示错误，否则使用默认消息。 `404`意味着“Not Found”，`403`意味着“Forbidden”（`401`意味着“Unauthorized”，但是我们应该重定向到登录页面而不是返回该状态。）

定义的`check_author`参数，以便该函数可用于获取帖子而无需检查作者。如果您编写一个视图来显示页面上的单个帖子，用户无关紧要，因为他们没有修改帖子，这将非常有用。

baby/blog.py

```py

@bp.route('/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

```

这个视图跟前面的视图不太一样，`update`函数需要传递一个参数`id`，这对应于路径中的`<int:id>`。真实的URL看起来像这个`/1/update/`，Flask将会捕捉到`1`，并保证它是个int，并且传递它作为id参数。如果不是一个具体的`int:`而是一个`<id>`，获取到的参数将会是一个String。为了生成一个URL地址到update页面，`url_for`需要传递一个`id`参数，比如`url_for('blog.update', id=post['id'])`。这个也可以在上面的`index.html`中看到。

create和update视图看起来很像，最大的不同是update视图使用一个post对象并且`UPDATE`代替了`INSERT`。通过一些巧妙的重构，你可以使用一个视图和模板替换掉create和update视图，但是由于是新手教程，保持两个视图分离看起来会比较清晰。

baby/templates/blog/update.html

```html baby/templates/blog/update.html

{% extends 'base.html' %}

{% block header %}
  <h1>{% block title %}Edit "{{ post['title'] }}"{% endblock %}</h1>
{% endblock %}

{% block content %}
  <form method="POST">
    <label for="title">Title</label>
    <input id="title" name="title" value="{{ request.form['title'] or post['title']}}" required />
    <label for="body">Body</label>
    <textarea name="body" id="body">{{ request.form['body'] or post['body'] }}</textarea>
    <input type="submit" value="Save" />
  </form>
  <hr />
  <form method="POST" action="{{url_for('blog.delete', id=post['id'])}}">
    <input class="danger" type="submit" value="Delete" onclick="return confirm('Are you sure?');" />
  </form>
{% endblock %}

```

`{{ request.form['title'] or post['title'] }}`用来选择表单中显示的数据，当表单没有被提交时，原始的post的数据将会显示，但是如果无效的表单数据被提交，我们希望显示这个错误的数据，并让用户去修改此错误，因此使用`request.form['title']`。[**request**](http://flask.pocoo.org/docs/1.0/api/#flask.request)是另一个变量，可以自动在模板中使用。

## Delete视图

delete视图没有自己的模板，delete按钮是`update.html`s的一部分并发布到`/<id>/delete`网址。因此没有模板，它只是处理`POST`方法并且重定向到`index`视图。

baby/blog.py

```py baby/blog.py

@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute(
        'DELETE FROM post where id = ?', (id,)
    )
    db.commit()
    return redirect(url_for('blog.index'))

```

到这里我们就已经完成了如何开发一个应用程序的新手教程，可喜可贺，花一些时间在浏览器上试试所有的功能。然而到这里在项目完成之前还是有很多要做的。

下一期继续 - [使项目可安装](https://www.walkerfree.com/article/159)
