+++
date = '2025-07-29T10:09:44.628092+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 模板'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

经过上篇文章，我们已经为应用程序编写了身份验证视图，当时当我们运行服务并且试着去访问其中任何一个URL的时候，将会看到`TemplateNotFound`的错误。那是因为视图调用了[**render\_template()**](http://flask.pocoo.org/docs/1.0/api/#flask.render_template)函数，但是我们还没有创建对应的模板。模板文件将被存储在`baby`包中的`templates`文件夹中。

模板是包含静态数据和动态数据占位符的文件。一个模板使用特定数据呈现以生成最终文档。Flask使用[Jinja](http://jinja.pocoo.org/docs/templates/)模板库来渲染模板。

在应用程序中，将使用templates去渲染将在用户浏览器上显示的[HTML](https://developer.mozilla.org/docs/Web/HTML)，在Flask中，Jinja被配置为自动转移将在HTML模板中渲染的任何数据。这意味着用户的输入将被安全的渲染，他们输入的任何字符都可能破坏HTML。例如`<`和`>`将转义为安全值，这些值在浏览器中看起来相同，但不会造成不必要的影响。

Jinja的外观和行为都很像Python。使用特殊的分隔符将Jinja语法与模板中的静态数据区分开来，`{{`和`}}`的表达式符号表示他们之间的任何内容都是将输出到最终文档。`{%`和`%}`符号表示类似if和for的控制流语句。不像Python，块由开始和结束标记表示，而不是缩进，因为块内的静态文本可以更改缩进。

## 基础布局

在应用程序中每个页面都有一个类似的基础布局包裹着不同的body。而不是在每个模板中编写整个HTML结构，每个模板将会继承基础布局然后重写具体的部分。

baby/templates/base.html

```html

<!DOCTYPE html>
<title>{% block title %}{% endblock %} - Baby</title>
<link rel="stylesheet" href="{{url_for('static', filename='app.css')}}" />
<nav>
  <h1>Baby</h1>
  <ul>
    {% if g.user %}
    <li><span>{{g.user['username']}}</span></li>
    <li><a href="{{url_for('auth.logout')}}">Log Out</a></li>
    {% else %}
    <li><a href="{{url_for('auth.register')}}">Register</a></li>
    <li><a href="{{url_for('auth.login')}}">Log In</a></li>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
  <div class="flash">{{message}}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>

```

[**g**](http://flask.pocoo.org/docs/1.0/api/#flask.g)在模板中将会自动可用，基于`g.user`设置用户(从`load_logged_in_user`)，要么显示用户名和注销链接，要么显示注册和登录链接。[**url\_for()**](http://flask.pocoo.org/docs/1.0/api/#flask.url_for)也将会自动可用，并且被用于生成URL，而不是手动将他们写出来。

在页面title的后面，并且在content的前面，模板循环调用[**get\_flashed\_messages()**](http://flask.pocoo.org/docs/1.0/api/#flask.get_flashed_messages)返回的每个信息。您在视图中使用[flash()](http://flask.pocoo.org/docs/1.0/api/#flask.flash)来显示错误消息，下面的代码将显示它们。

这里的有三个被定义的块，在其他模板中将被重写。

1. `{% block title %}`将改变在浏览器标签显示的标题和窗口的标题
2. `{% block header %}`类似于`title`，但是会改变在页面上显示的标题
3. `{% block content %}`是每个页面的内容所在，例如登录表单或博客文章

基础模板直接在模板的目录下面。为了保持其他模板的组织，蓝图的模板将被放置在与蓝图同名的目录中

## 注册

baby/templates/auth/register.html

```html

{% extends 'base.html' %}

{% block header %}
<h1>{% block title %}Register{% endblock %}</h1>
{% endblock %}

{% block content %}
<form method="POST">
  <label for="username">Username</label>
  <input name="username" id="username" required />
  <label for="password">Password</label>
  <input type="password" name="password"" id="password" required/>
  <input type="submit" value="Register" />
</form>
{% endblock %}

```

`{% extends 'base.html' %}`告诉Jinja这个模板应该替换掉基础模板中的block。所有渲染的内容都必须出现在`{% block %}`标记中，这些标记覆盖基础模板中的块。

这里使用的一个有用模式是将`{% block title %}`放在`{% block header %}`中。这将设置title块，然后将其值输出到header块中，这样窗口和页面就可以共享相同的标题，而不需要编写两次标题。

input标签有一个required属性，这是在告诉浏览器知道所有的输入框都填入数据才能被提交。如果用户使用的是老版本的浏览器并且不支持这个属性，或者使用了除了浏览器之外其他的工具做了请求操作，你仍然应该在视图中去验证数据。始终在服务器上完全验证数据是很重要的，即使客户机也执行一些验证。

## 登录

这与注册模板相同，除了标题和提交按钮。

baby/templates/auth/login.html

```html

{% extends "base.html" %}

{% block header %}
<h1>{% block title %}Login In{% endblock %}</h1>
{% endblock %}

{% block content %}
<form method="POST">
  <label for="username">Username</label>
  <input id="username" name="username" required />
  <label for="password">Password</label>
  <input type="password" id="password" name="password" required />
  <input type="submit" value="Login In" />
</form>
{% endblock %}

```

## 注册一个用户

现在身份认证模块已经写完，你可以注册一个用户。确保服务器仍在运行(如果没有运行，执行`flask run`)，然后访问`http://127.0.0.1:5000/auth/register`。 试着在没有填写任何内容的情况下点击“注册”按钮，然后应该可以看到浏览器的错误提示信息。试着从`register.html`模板中将`required`属性移除，然后点击再次点击“注册”按钮。与浏览器显示错误不同，页面将重新加载，视图中的[**flash()**](http://flask.pocoo.org/docs/1.0/api/#flask.flash)将显示错误信息。

填充一个username和password，然后你将被重定向到一个登录页面，试着输入一个错误的username或者是正确的username和错误的password。如果你登录进去后，你将会得到一个错误因为还没有一个`index`视图去跳转。

下一期继续 - [静态文件](https://www.walkerfree.com/article/157)
