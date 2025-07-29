+++
date = '2025-07-29T10:09:41.271791+08:00'
draft = false
title = 'Flask 1.0 新手教程 - Blueprint和视图'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

视图函数是我们编写用于响应对应的应用程序的请求的代码。Flask使用模式将传入的请求URL与应该处理它的视图相匹配。该视图返回Flask转换后的响应数据。Flask也可以转向另一个方向，并根据其名称和参数生成视图的URL。

## 创建Blueprint

[Blueprint](http://flask.pocoo.org/docs/1.0/api/#flask.Blueprint)是一种组织一组相关视图和其他代码的方法。他们不是直接在应用程序中注册视图和其他代码，而是使用蓝图进行注册。然后，当它在工厂功能中可用时，蓝图就会在应用程序中注册。

baby将会有两个Blueprint，一个用于身份验证功能，另一个用于博客帖子功能。每个蓝图的代码都将在一个单独的模块中。由于博客需要了解身份验证，因此首先要编写身份验证的部分。

baby/auth.py

```py

#! _*_ coding: utf-8 _*_
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash
from baby.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

```

上面的代码创建了一个名为'auth'的[Blueprint](http://flask.pocoo.org/docs/1.0/api/#flask.Blueprint)，像应用程序对象一样，blueprint需要知道它是在哪里定义的，因此传递一个`__name__`作为第二个参数。`url_prefix`的值将被追加到所有与blueprint有关的URLs的前面。

在工厂函数中，使用app.register\_blueprint()导入并注册blueprint。放置新的代码在工厂函数末尾，在返回app之前。

baby/**init**.py

```py

def create_app():
    app = ///
    # 忽略已存在的代码

    from . import auth
    app.register_blueprint(auth.bp)

    return app

```

身份认证功能的blueprint会有几个试图，注册新用户的视图、登录的视图、登出的视图。

## 第一个视图：注册

当用户访问`/auth/register`的URL时，`register`视图将返回一个[HTML](https://developer.mozilla.org/docs/Web/HTML)表单以供用户填写。当用户提交表单时，视图函数将会验证用户的输入，如果验证失败将会显示一个带有错误信息的表单，如果验证成功则创建一个新用户，并进入到登录页面。

现在我们先写一部分视图代码，在下一篇分享中，将介绍如何用模板去生成一个HTML表单。

baby/auth.py

```py

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'user {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)', 
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')

```

下面解说下这个`register`视图函数正在做的

1. [**@bp.route()**](http://flask.pocoo.org/docs/1.0/api/#flask.Blueprint.route)将URL`/register`与`register`视图函数相关联。当Flask收到对`/auth/register`的请求时，它将调用`register`视图并使用返回值作为响应。
2. 如果用户提交了表单，[**request.method**](http://flask.pocoo.org/docs/1.0/api/#flask.Request.method)将是`'POST'`，在这种情况下，请开始验证输入
3. [**request.form**](http://flask.pocoo.org/docs/1.0/api/#flask.Request.form)是一种特殊类型的[**dict**](https://docs.python.org/3/library/stdtypes.html#dict)映射，提交了表单键和值。用户将输入他们的`username`和`password`。
4. 验证`username`和`password`不为空。
5. 通过查询数据库并通过返回的结果验证`username`是否已经被注册过了。[db.execute](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute)采用SQL查询`?`任何用户输入的占位符，以及用于替换占位符的值元组。数据库库将负责转义值，因此您不容易受到*SQL注入攻击*。

   [**fetchone()**](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchone)从查询中返回一行。如果查询没有返回结果，它会返回None。稍后，使用[**fetchall()**](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchall)，它返回所有结果的列表。
6. 如果验证成功了则插入新用户的数据到数据库。为了安考虑，密码永远都不要用明文还自己存储，而是使用[**generate\_password\_hash()**](http://werkzeug.pocoo.org/docs/utils/#werkzeug.security.generate_password_hash)安全地将明文密码机型哈希处理，然后存储哈希值。由于此查询修改数据，因此需要在之后调用[**db.commit()**](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit)以保存更改。
7. 存储用户之后，被重定向到登录页面。[url\_for()](http://flask.pocoo.org/docs/1.0/api/#flask.url_for)根据其名称生成一个登录视图URL。这比直接编写URL更好，因为它允许您稍后更改URL而不更改链接到它的所有代码。[redirect()](http://flask.pocoo.org/docs/1.0/api/#flask.redirect)生成对生成的URL的重定向响应。
8. 如果验证失败，错误信息将被显示给用户。flash()存储的信息，在模板渲染的时候能被检索出来。
9. 当用户最初导航到`auth/register`，或者存在验证错误时，应显示带有注册表单的HTML页面。[**render\_template()**](http://flask.pocoo.org/docs/1.0/api/#flask.render_template)将呈现包含HTML的模板，您将在本教程的下一步中编写该模板。

## 第二个视图：登录

该视图遵循与上面的`register`视图相同的模式。

baby/auth.py

```py

@bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('auth/login.html')

```

这个视图与`register`视图有一些不同之处：

1. 首先查询用户并将其存储在变量中以供以后使用。
2. [**check\_password\_hash()**](http://werkzeug.pocoo.org/docs/utils/#werkzeug.security.check_password_hash)以存储的哈希相同的方式哈希处理提交的密码并安全地比较它们。如果匹配，则密码有效。
3. session是一个跨请求存储数据的字典。验证成功后，用户的`id`将存储在新会话中。数据存储在发送到浏览器的*cookie*中，然后浏览器将其与后续请求一起发回。Flask安全地对数据进行签名，以便不会被篡改。

现在用户的id存储在会话中，它将在后续请求中可用。在每个请求开始时，如果用户已登录，则应加载其信息并使其可供其他视图使用。

baby/auth.py

```py

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

```

[**bp.before\_app\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Blueprint.before_app_request)注册一个在视图函数之前运行的函数，无论请求什么URL。`load_logged_in_user`检查用户id是否存储在`session`中并从数据库中获取该用户的数据，并将其存储在[**g.user**](http://flask.pocoo.org/docs/1.0/api/#flask.g)上，该持续时间为请求的长度。如果没有用户ID，或者id不存在，则`g.user`将为`None`。

## 第三个视图：登出/退出

要注销，需要从会话中删除用户ID。然后load\_logged\_in\_user将不会在后续请求中加载用户。

baby/auth.py

```py

@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('blog.index'))

```

## 在其他视图中需要身份验证

创建，编辑和删除博客帖子将需要用户登录。装饰器可用于检查它应用于的每个视图。

baby/auth.py

```py

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

```

这个装饰器返回一个新的视图函数，它包装了它应用的原始视图。新函数检查用户是否已加载，未加载的话将重定向到登录页面。如果加载了用户，则调用原始视图并继续正常运行。在编写博客视图时，您将使用此装饰器。

## Endpoint和URL

[url\_for()](http://flask.pocoo.org/docs/1.0/api/#flask.url_for)函数根据名称和参数生成视图的URL。与视图关联的名称也称为endpoint，默认情况下，它与视图函数的名称相同。

例如，在本教程前面添加到app工厂的`hello()`视图名为`'hello'`，可以链接到`url_for('hello')`。如果这个视图函数带了一个参数，这部分将在后面的教程中看到，他将被连接到`url_for('hello', who='World')`。

使用blueprint时，blueprint的名称将附加到函数的名称前面，因此上面写入的登录函数的endpoint是`'auth.login'`，因为我们将其添加到`'auth'` blueprint中。

下一期继续 - [模板](https://www.walkerfree.com/article/156)
