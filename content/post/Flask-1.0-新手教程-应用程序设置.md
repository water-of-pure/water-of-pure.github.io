+++
date = '2025-07-29T10:09:35.432547+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 应用程序设置'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

Flask应用程序是一个[Flask](http://flask.pocoo.org/docs/1.0/api/#flask.Flask)类的实例。关于应用的任何事情，例如配置和URLs都将通过这个类来注册。

最直截了当的方式创建一个Flask应用是直接在代码顶部通过创建一个全局的Flask实例，就像上一篇教程的“Hello，World！”示例一样。虽然这在某些情况下很简单且有用，但随着项目的增长，它可能会导致一些棘手的问题。

在函数内创建Flask实例，而不是全局创建[Flask](http://flask.pocoo.org/docs/1.0/api/#flask.Flask)实例。此功能称为*应用程序工厂*。应用程序需要的任何配置，注册和其他设置都将在函数内部进行，然后将返回应用程序。

## 应用程序工厂

是时候开始编码了！创建`baby`目录并添加`__init__.py`文件。`__init__.py`提供双重任务：它将包含应用工厂，并且它将告诉Python，`baby`目录将被作为一个包来对待。

```bash

make baby

```

baby/**init**.py

```py

#! _*_ coding: utf-8 _*_

import os

from flask import Flask

def create_app(test_config=None):
    # 创建和配置应用程序
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'baby.sqlite')
    )

    if test_config is None:
        # 加载实例配置（如果存在），不测试时
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 如果传入则加载测试配置
        app.config.from_mapping(test_config)

    # 确保实例文件夹存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 一个简单的页面
    @app.route('/hello')
    def index():
        return 'Hello, World!'

    return app

application = create_app()

if __name__ == "__main__":
    application.run()

```

`create_app`是应用程序工厂函数。您将在本教程的后面添加它，但它已经做了很多

1. `app = Flask(__name__, instance_relative_config=True)`创建Flask实例

   * `__name__`是当前Python模块的的名称。应用程序需要知道它所在的位置以设置一些路径，并`__name__`是告诉它的一种方便的方法
   * `instance_relative_config=True`告诉应用程序配置文件是相对于[instance文件夹](http://flask.pocoo.org/docs/1.0/config/#instance-folders)的。这个instance文件夹位于baby包外面并且可以保存本地数据，且数据不能被提交到版本库，例如配置密码和数据库文件。
2. [**app.config.from\_mapping()**](http://flask.pocoo.org/docs/1.0/api/#flask.Config.from_mapping)设置一些应用程序将会使用的默认配置：

   * **[SECRET\_KEY](http://flask.pocoo.org/docs/1.0/config/#SECRET_KEY)** 被Flask和扩展使用用来保证数据的安全。它被设置为'dev'以在开发期间提供方便的值，但在部署时应该用随机值覆盖它。
   * `DATABASE` 是保存SQLite数据库文件的路径。它位于app.instance\_path下，这是Flask为实例文件夹选择的路径。您将在下一篇教程中了解有关数据库的更多信息。
3. [**app.config.from\_pyfile()**](http://flask.pocoo.org/docs/1.0/api/#flask.Config.from_pyfile)使用从instance文件夹中的`config.py`文件获取的值覆盖默认配置（如果存在）。例如当部署的时候，将被用于设置一个真实的`SECRET_KEY`。

   * `test_config`也可以传递给工厂，而不是实例配置。这样您将在本教程后面编写的测试可以独立于您配置的任何开发值进行配置
4. [**os.makedirs()**]确保[**app.instance\_path**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.instance_path)存在。Flask不会自动创建一个instance文件夹，但是它需要被创建，因为你的项目将在这创建SQLite数据库文件。
5. [**@app.route()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.route)创建了一个简单的路由，以便在进入本教程的其余部分之前可以看到应用程序正常工作。它在URL `/hello`和返回响应的函数之间创建了一个连接，在这种情况下响应函数会返回一个字符串'Hello，World！'

## 运行应用程序

现在可以通过Flask命令运行应用程序。通过终端，告诉Flask在哪里找到你的应用程序，然后通过开发者模式运行

开发者模式，只要页面引发异常，就显示一个交互式调试器，在改变代码的时候重启服务器。您可以让它保持运行，只需按照教程重新加载浏览器页面即可。

对于Linux和Mac：

```bash

export FLASK_APP=baby
export FLASK_ENV=development
flask run

```

对于Windows cmd，使用`set`而不是`export`：

```bash

set FLASK_APP=baby
set FLASK_ENV=development
flask run

```

对于Windows PowerShell，请使用`$env`：而不是`export`：

```bash

$env:FLASK_APP = "baby"
$env:FLASK_ENV = "development"
flask run

```

你会看到与此类似的输出：

```bash

$ flask run
 * Serving Flask app "baby" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 390-520-193

```

在浏览器中访问<http://127.0.0.1:5000/hello>，您应该看到“Hello，World！”消息。恭喜，您现在正在运行Flask Web应用程序！

下一期继续 - [定义和访问数据库](https://www.walkerfree.com/article/154)
