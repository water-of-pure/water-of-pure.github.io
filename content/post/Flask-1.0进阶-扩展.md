+++
date = '2025-07-30T09:56:50.667101+08:00'
draft = false
title = 'Flask 1.0进阶 - 扩展'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

扩展是为flask应用程序添加功能的额外包。例如，扩展可能会添加对发送电子邮件或连接到数据库的支持。一些扩展添加了全新的框架来帮助构建某些类型的应用程序，比如REST API。

### 查找扩展

Flask扩展通常命名为“Flask-Foo”或“Foo-Flask”。您可以在PyPI中搜索带有 [Framework :: Flask](https://pypi.org/search/?c=Framework+%3A%3A+Flask) 标记的包。

### 使用扩展

关于每个扩展的安装、配置和使用说明，请查询他们的文档。通常，扩展从 [**app.config**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.config) 获取他们自己的配置参数并在初始化的时候传参到应用程序实例中。举个例子，比如扩展“Flask-Foo”的使用方式可能如下：

```py

from flask_foo import Foo

foo = Foo()

app = Flask(__name__)
app.config.update(
    FOO_BAR='baz',
    FOO_SPAM='eggs',
)

foo.init_app(app)

```

### 创建扩展

尽管PyPI包含了许多Flask扩展，但是仍没有找到适合你的扩展。如果是这样的话，你可以创建一个你自己的扩展。请参考[Flask Extension Development](https://flask.palletsprojects.com/en/1.0.x/extensiondev/#extension-dev)来开发你自己的Flask扩展。

## 命令行界面

安装Flask后，会默认安装`flask`脚本的，这个脚本一个[Click](https://click.palletsprojects.com/)命令行接口会被安装到虚拟环境中。

通过终端，这个脚本可以访问内建的命令、扩展的命令和程序定义的命令。使用`--help`选项可以获取到更多关于命令的信息和关于命令的选项

### 应用程序发现

`flask`命令是被Flask安装的，不是你的应用安装的。为了使用这个命令，必须告诉你的应用程序在哪里。`FLASK_APP`环境变量则是用来告诉在哪里能找到应用程序

使用方式如下：

> Unix Bash (Linux, Mac, etc.):

```bash

$ export FLASK_APP=hello
$ flask run

```

> Windows CMD:

```bash

> set FLASK_APP=hello
> flask run

```

> Windows PowerShell:

```bash

> $env:FLASK_APP = "hello"
> flask run

```

`FLASK_APP`支持多种形式的选项来具体化你的应用程序，大多数都是用比较简单的方式。

下面是一些比较典型的例子

(不做任何设置)

```bash

wsgi.py文件将被导入，并自动的检查是否有app(```app```)，它提供了最简单的方式去创建了一个带有额外参数的工厂函数

```

`FLASK_APP=hello` 名字将被导入，并自动检查是否有app(`app`)或者工厂函数(`create_app`)

---

`FLASK_APP`有三个部分：一个设置了当前工作目录的可选路径，一个Python文件或者有点的导入路径和一个可选的实例或者工厂函数变量名。如果是一个工厂函数的话可以通过小括号传入需要的参数，下面看下具体的例子

`FLASK_APP=src/hello`

```bash

设置当前目录的src目录并导入hello

```

`FLASK_APP=hello.web`

```bash

导入```hello.web```路径

```

`FLASK_APP=hello:app2`

```bash

使用在hello中的```app2``` Flask实例

```

`FLASK_APP="hello:create_app('dev')"`

```bash

```create_app```工厂函数在```hello```中被调用并传递参数```'dev'```字符串

```

如果`FLASK_APP`没有设置，执行命令时将尝试导入“app”或者“wsgi”（作为一个“.py”文件，或者包）并尝试去检查一个应用实例或者工厂

如果导入的信息被设置了，即`FLASK_APP`被设置了的话。执行命令时，程序查找一个应用实例名字叫做`app`或者`application`，它是一个应用的实例。如果没有找到实例，程序会查找一个工厂行数，名称是`create_app`或者`make_app`，它会返回一个实例

当应用工厂函数被调用，如果工厂函数带有一个名字叫做`script_info`的参数，则[ScriptInfo](https://flask.palletsprojects.com/en/1.1.x/api/#flask.cli.ScriptInfo)实例会作为一个关键字参数传递进去。如果工厂函数只带有一个参数并且没有圆括号跟在工厂函数名字后面，则ScriptInfo实例将作为一个位置参数传递进去。如果圆括号跟在工厂函数后面的话，他们的内容将被解析喂Python字符串并作为参数传入到函数中。这意味着字符串始终在引号中。

### 启动开发服务器

`run`命令将启动一个开发服务器，在许多情况下替代了 **[Flask.run()](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.run)** 方法

```bash

$ flask run
 * Serving Flask app "baby" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 267-735-523

```

> 注意

不要使用`run`命令再生产环境中，只使用开发服务器在开发环境中。开发服务器虽然提供了便利，但是不是安全的、不是稳定的、不是高效率的。

**进阶结束更新说明**

先说下此系列的进阶，主要是以官方文档为主线，边阅读边实践，并记录分享，其中有部分官方的实例是有问题的，但是没有找到反馈入口，也出于没有人访问的情况，所以结束继续分享。如果有疑问可以转到官方文档[这里](https://flask.palletsprojects.com/en/1.1.x/)去查看
