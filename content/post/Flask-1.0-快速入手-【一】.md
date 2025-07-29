+++
date = '2025-07-29T10:09:13.555264+08:00'
draft = false
title = 'Flask 1.0 快速入手 【一】'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1556014814/walkerfree/wf_147.jpg"
+++

是不是已经很想快点尝试下Flask了，本次分享将尽量全面的介绍Flask，继续下面的内容之前请确保您已经安装了Flask，如果你还没有安装的话，请回到前面的部分“Flask 1.0安装”再了解下如何安装。

## 一个小的应用

一个小应用的代码看起来像是下面这个样子

```py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return "hello world"

```

下面解释下这段代码做了什么

1. 首先我们导入了[Flask](http://flask.pocoo.org/docs/1.0/api/#flask.Flask)类，这个类的实例将是我们WSGI应用的实例
2. 下面创建这个类的实例。第一个参数是应用的模块或者包的名称。如果你使用一个单独的模块（比如这里的例子），你应该使用`__name__`，因为这个取决于应用是否作为一个应用程序启动还是作为一个模块导入，它的名称将是不同的（`__main__`与实际导入的名称相对应）。这个是必须要传入的参数，会让Flask知道去哪里查找模板、静态文件等等，有关于更多的信息可以查看[Flask](http://flask.pocoo.org/docs/1.0/api/#flask.Flask)的官方文档
3. 我们使用[route()](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.route)装饰器去告诉Flask什么样的URL路由将会触发我们的函数
4. hello\_world这个函数的名称也是有用的，后面在生成URLs的时候会有特殊的功能，而且函数的返回值将展示在用户的浏览器上。

只需要保存上面的代码到文件hello.py或者是其他的名称带有后缀.py的文件即可，同时确保文件的名称不能叫做flask.py，因为这样会是的自己的文件脚本跟Flask自己冲突。

为了运行应用程序，你既可以使用flask命令也可以使用python的-m启动Flask.不过在你运行程序前你应该在终端导入一个环境变量FALSK\_APP，如下：

```bash

$ export FLASK_APP=hello.py
$ flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

如果您使用的是Windows，则环境变量语法取决于命令行解释程序。在命令提示符上:

```bash

C:\path\to\app>set FLASK_APP=hello.py

```

在PowerShell上：

```bash

PS C:\path\to\app> $env:FLASK_APP = "hello.py"

```

另外你也可以使用`python -m flask`

```bash

$ export FLASK_APP=hello.py
$ python -m flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

### 外部可见服务器

这将运行一个非常简单的内置服务器，对于开发和测试是足够用了，但是不是你想在生产环境使用的东西。后面会有相关部署环节的介绍。

如果你启动了上面的程序的话，你将会注意到，运行起来的服务只能你自己的电脑才能访问，网络上其他的电脑是没有办法访问的。在debug模式中这是默认的行为，只允许你自己在你自己的电脑上随意的执行Python代码

如果你禁止了debug模式或者新人在在同一网络上的用户，你可以公开你的服务，只需要简单的在命令行中加入`--host=0.0.0.0`

```bash

flask run --host=0.0.0.0

```

这个操作将会告诉你的电脑，去监听所有公开的网络ip

## 如果服务没有启动该做什么

一旦`python -m flask`启动失败或者flask不存在，这总情况可能有多种原因，首先你需要仔细看一下报错的错误信息

### 旧的flask版本

Flask版本小于0.11的话会有不同的方式启动应用，简而言之，flask命令不存在，而且也没有`python -m flask`。这种情况下有两种选择，一是将Flask升级到新版本，二是看下这个[开发服务器](http://flask.pocoo.org/docs/1.0/server/#server)文档遭到启动服务器的替代方法

### 导入名称无效

FLASK\_APP环境变量是在`flask run`的时候导入的模块的名称，在这种情况下，模块的名称是错误的话你将得到一个启动时导入错误提示（或者，如果导航到应用程序时启用了调试），它将告诉你试图导入的内容以及失败的原因。

最常见的错误是拼写错误或者是因为你实际上并没有创建一个应用程序对象

## 调试模式

(想要记录错误和堆栈跟踪？请看[应用程序错误](http://flask.pocoo.org/docs/1.0/errorhandling/#application-errors)) flask脚本能够很适合启动一个本地的开发服务器，但是每次更改代码后都需要重新启动服务器。这不是很好，Flask能做的更好，如果启动了调试支持，服务器将在代码改动后自动重新加载，如果出现问题，他还会提供一个有用的调试器。

为了启用所有开发功能（包括调试模式），你需要在启动服务器前导入FLASK\_ENV环境变量并且设置它的值为`development`

```bash

$ export FLASK_ENV=development
$ flask run

```

（在Windows环境中需要用`set`代替`export`）

这样做有以下几点：

1. 它激活了调试器
2. 它激活了自动重新加载器
3. 它启用了Flask应用程序上的调试模式。

你也能通过导入变量FLASK\_DEBUG=1来单独控制调试模式

在[开发服务器](http://flask.pocoo.org/docs/1.0/server/#server)中有更多关于参数的介绍

---

### 注意

尽管交互调试器不能在工作在分叉环境中（几乎不可能在生产环境中使用），他仍然允许执行任务的代码，这就使得服务器非常的不安全，所以绝对不要在生产服务上使用

---

下面是一个调试器的截图

![文章 - Walkerfree](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1556014807/walkerfree/wx_141_1.png)

有关使用调试器的更多信息，请参阅[Werkzeug文档](http://werkzeug.pocoo.org/docs/debug/#using-the-debugger)。 还有另一个调试器吗？请参阅[使用调试器](http://flask.pocoo.org/docs/1.0/errorhandling/#working-with-debuggers)。

## 路由

现代的web应用使用更加有意义的URLs去帮助用户，如果页面使用有意义的并且用户可以记住的URL，用户可能会更喜欢这个页面并返回来直接访问该页面。

使用route()装饰器来绑定一个函数到一个URL地址上：

```py

@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
	return 'Hello World'

```

你可以做得更多！可以将URL的一部分动态化并将多个规则附加到函数。

### 变量规则

使用`<variable_name>`标记部分添加变量部分到URL。你的函数将接收到`<variable_name>`作为关键字参数。你也可以一个转换器，来定义具体的参数类型像这样`<converter:variable_name>`(可选)

```py

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return 'Showpath %s' % subpath

```

转换器类型：

| 类型 | 描述 |
| --- | --- |
| string | 接收任意字符串除了斜杠（默认情况下接收string类型） |
| int | 接收正整数 |
| float | 接收正浮点值 |
| path | 类似string但是也接受斜杠 |
| uuid | 接收UUID字符串 |

### 唯一URL地址/重定向行为

下面的两个规则在使用尾部斜杠的时候有所不同

```py

@app.route('/projects/')
def projects():
	return 'The project page.'

@app.route('/about')
def about():
	return 'The about page.'

```

`projects`的规范路由最后部分有斜杠，类似于一个文件系统的文件夹。如果你访问这个URL地址不带有最后的斜杠，Flask则重定向到一个尾部带有斜杠的规范路由

`about`的规范路由最后部分没有斜杠，类似于一个文件的文件路径名。如果你访问这个URL地址最后带有斜杠的话，会产生一个404“Not Found”错误。这有助于保持URL对这些资源的唯一性，并且保持搜索引擎避免两次索引同一页面

### URL构建

为了构建一个URL地址到一个具体的函数，使用[url\_for()](http://flask.pocoo.org/docs/1.0/api/#flask.url_for)函数。它接收一个函数的名字作为第一个参数和任意数量的关键字参数，每一个对应到URL规则变量的对应部分。未知的变量部分作为查询参数附加到URL

为什么要使用URL转换函数[url\_for()](http://flask.pocoo.org/docs/1.0/api/#flask.url_for)来构建URL，而不是用硬编码的方式写在模板里面

1. 转换要比硬编码十分具有描述性
2. 你可以一次性修改网址而不比记住它手动去修改硬编码的URL网址
3. URL构建处理特殊字符和Unicode数据的转义
4. 产生的网址路径都是绝对的，避免了不必要的相对路径的麻烦
5. 如果您的应用程序位于URL根目录之外，例如，在`/myapplication`而不是`/`，`url_for()`能够妥善处理这些问题

例如下面我们使用`test_request_context()`方法来测试`url_for().test_request_context()`告诉Flask。即使我们使用Python shell，它也会像处理请求一样。 请参阅[上下文本地](http://flask.pocoo.org/docs/1.0/quickstart/#context-locals)。

```py

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/login')
def login():
    return 'Login page'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Durban'))
```

```bash
/
/login
/login?next=%2F
/user/Durban

```

### HTTP方法

Web应用程序在访问URL时使用不同的HTTP方法，在使用Flask开发时，你自己应该熟悉HTTP方法，默认情况下，一个路由只回应一个GET请求，你可以使用route()装饰器的第二个参数来处理不同的HTTP方法

```py

from flask import Flask

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'do the login'
	else:
		return 'show the login form'

```

如果存在GET，Flask会自动添加对HEAD方法的支持，并根据[HTTP RFC](https://www.ietf.org/rfc/rfc2068.txt)处理HEAD请求。同样，OPTIONS会自动为您实施
