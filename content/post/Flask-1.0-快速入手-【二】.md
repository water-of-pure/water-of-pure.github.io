+++
date = '2025-07-29T10:09:16.454700+08:00'
draft = false
title = 'Flask 1.0 快速入手 【二】'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1556417065/walkerfree/wf_148.jpg"
+++

## 静态文件

动态web应用也需要静态文件。通常包括CSS和Javascript文件。理想情况下，你的服务器配置为为你自己服务的，但是在开发环境Flask也能做到这些，只要创建一个static文件夹在包里面或者在你模块的旁边创建一个static文件夹，在应用中通过`/static`调用的方式就会起作用

为了给static文件生成一个URLs，可以使用一个特殊的`static`节点，如下

```py

url_for('static', filename='style.css')

```

## 模板渲染

从Python中生成HTML并不好玩，而且实际上非常麻烦，你必须自己进行HTML转义以保证应用程序的安全。因此Flask自动为你配置了[Jinja2](http://jinja.pocoo.org/)模板引擎。

为了渲染一个模板你可以使用 **render\_template()** 方法。你必须传递一个模板的名字和你想要传递给模板的变量到模板引擎作为关键字参数。下面这个是一个简单例子，演示了如何渲染一个模板

```py

from flask import render_template

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

```

Flask将在`templates`文件夹中寻找对应的模板，如果你的应用是一个模块，这个文件夹将在模块的同一级，如果你的应用是一个包的话，则这个文件夹应该在包的里面，如下例子 例子1： 一个模块

```bash

/application.py
/templates
    /hello.html

```

例子2：一个包

```bash

/application
    /__init__py
    /templates
        /hello.html

```

对于模板，您可以使用Jinja2模板的全部功能。有关更多信息，请访问官方[Jinja2模板文档](http://jinja.pocoo.org/docs/templates)。

下面是一个模板的例子

```html

<!doctype html>
<title>
	Hello from Flask
</title>
{% if name %}
	<h1>Hello {{ name }}!</h1>
{% else %}
	<h1>Hello, World!</h1>
{% endif %}

```

在模板内部你可以访问[request](http://flask.pocoo.org/docs/1.0/api/#flask.request),[session](http://flask.pocoo.org/docs/1.0/api/#flask.session)和[g](http://flask.pocoo.org/docs/1.0/api/#flask.g)[1]对象，并且还可以使用[get\_flasjed\_message()](http://flask.pocoo.org/docs/1.0/api/#flask.get_flashed_messages)函数

模板的继承是非常有用的。如果你想要知道如何工作的，可以访问[模板继承](http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/#template-inheritance)模式文档。基本上，模板继承可以在每个页面上保留某些元素（例如头部，导航和底部）

模板启动了自动转移功能，因为如果name中含有HTML，则会自动转义。如果你信任一个变量并且你知道它是一个安全的HTML（例如，它来自将wiki标记转换为HTML的模块）你可以使用Markup类标记他是安全的，或者通过使用`|safe`过滤下在模板中，有关更多示例，请访问[Jinja 2文档](http://jinja.pocoo.org/)

下面是一个简单的介绍，关于如何使用Markup类

```bash

>>> from flask import Markup
>>> Markup('<string>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<string>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')
>>> Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')
>>> Markup('<em>Marked up</em> &raquo; Html').striptags()
'Marked up » Html'

```

更改日志 在0.5版本修改：不再为所有的模板启动自动转义。以`.html`,`.htm`,`.xml`,`.xhtml`扩展的模板将自动触发转义过滤。从字符串加载的模板将禁用自动转义。

**[1]** 不知道g对象是什么？它是一个你能存储你需要的信息的东西,有关详细信息，请查看该对象的文档（[g](http://flask.pocoo.org/docs/1.0/api/#flask.g)）和[使用带有Flask的SQLite 3](http://flask.pocoo.org/docs/1.0/patterns/sqlite3/#sqlite3)。

## 访问请求数据

对于web应用程序，对客户端发送到服务器的数据做出相应是非常重要的，在Flask中这些信息通过全局[request](http://flask.pocoo.org/docs/1.0/api/#flask.request)对象提供。如果你有一些Python开发经验，你也许想要知道改对象如何是全局的以及如何Flask如何设置他仍然是线程安全的。答案是上下文本地化

### 上下文本地化

---

如果你想知道它是如何工作的，并且想知道它是如何实现的，请阅读这部分否则跳过继续

---

Flask中的某些对象是全局对象，但是不是通常的对象。这些对象实际上是一个协议，而且能够本地化到一个特定的上下文。非常绕，但是实际上很容易理解。

想象下，这个上下文是一个处理中的线程。一个请求过来后服务器端决定产生一个新的线程（或其他东西，底层对象能够处理除线程之外的并发系统）。当Flask启动它的内部请求去处理它时，他会判断出当前线程是活动上下文并将当前应用程序和WSGI环境绑定到改上下文（线程）。它以智能的方式实现了这个逻辑，以便一个应用程序可以在不中断情况下调用另一个应用程序。

这对于你意味着什么呢？基本上你能完全忽略这个情况，除非你做了一些事情比如单元测试，你将注意到因为没有请求对象导致依赖于对象请求的代码将突然中断。这个解决方案就是你自己创建了一个请求对象然后绑定它到上下文，最简单的单元测试解决方案是使用[test\_request\_context()](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_request_context)上下文管理器。结合`with`语句时，它将会绑定一个测试请求使你能够跟它进行交互。下面是一个例子：

```py

from flask import request

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'

```

其他可能的情况是传入整个WSGI环境的到request\_context()方法

```py

from flask import request

with app.request_context(env):
    assert request.method == 'POST'

```

## 请求对象

请求对象被记录在API部分，这里暂时不做全覆盖的介绍，具体详情可以看[Request](http://flask.pocoo.org/docs/1.0/api/#flask.Request)或者看我后面的介绍，这里暂时只介绍下普通情况下用的比较频繁的操作，首先我们必须从flask模块导入它

```py

from flask import request

```

通过使用method属性可以获取当前请求的方式。为了访问到表单数据（数据通过`POST`或者`PUT`方式请求）你可以使用form属性。这里是一个完整的例子，关于这两个属性的

```py

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
    else:
        error = 'Invalid username/password'

    return render_template('login.html', error=error)

```

如果form的属性中没有对应的key会发生什么呢？这种情况下将会抛出一个KeyError异常。你可以像标准KeyError一样捕获它，但如果不这样做，则会显示HTTP 400错误请求错误页面。所以很多情况下你没必要处理这个问题。

要访问URL(?key=value)中提交的参数，可以使用args属性

```py

key = request.args.get('key')

```

建议使用get或捕获KeyError来访问URL参数，因为用户可能会更改URL并向他们显示400个错误请求页面，在这种情况下体验并不友好。

有关请求对象的方法和属性的完整列表，请转到[Request](http://flask.pocoo.org/docs/1.0/api/#flask.Request)文档。

## 文件上传

你能很容易的使用Flask处理上传的文件。只要确保在提交的表单中不要忘记设置`enctype="multipart/form-data"`属性，否则浏览器将不会传递你的提交的文件

上传到文件存储在内存或者文件系统的一个临时的位置。你能通过request对象的**files**这个属性访问这些文件。每个上传的文件存储在一个字典中。它的行为就想标准的Python文件对象一样，但是也有一个\*\*save()\*\*方法，这个防范允许你将文件存储到服务器的文件系统中。下面是一个简单的演示例子

```py

from flask import request

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/var/www/uploads/upload.txt')

```

如果您想知道文件在上传到您的应用程序之前在客户端上的命名方式，你可以通过访问filename属性。但请记住，这个价值可以伪造，所以永远不要相信这个价值。如果你想要使用客户端的文件名去存储到服务器上，通过Werkzeug为您提供的\*\*secure\_filename()\*\*函数传递它。

```py

from flask import request
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/var/www/upload/' + secure_filename(f.filename))

```

有关更好的示例，请查看[上传文件](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/#uploading-files)章节。
