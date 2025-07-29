+++
date = '2025-07-29T10:56:08.899802+08:00'
draft = false
title = 'Flask 1.0 进阶 - 应用程序上下文'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

应用程序上下文在请求，CLI命令或其他活动期间跟踪应用程序级数据。而不是将应用程序传递给每个函数，而是访问[**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 和[**g**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.g) 代理。

这类似于[请求上下文](https://flask.palletsprojects.com/en/1.0.x/reqcontext/) ，它在请求期间跟踪请求级数据。当推送请求上下文时，推送相应的应用程序上下文。

### 上下文的目的

[**Flask**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask) 应用程序对象具有诸如[**config**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.config) 之类的属性，这些属性对于在视图和[CLI命令](https://flask.palletsprojects.com/en/1.0.x/cli/) 中进行访问很有用。但是，在项目中的模块中导入`app`实例很容易出现循环导入问题。使用[应用工厂模式](https://flask.palletsprojects.com/en/1.0.x/patterns/appfactories/) 或编写可重复使用的[蓝图](https://flask.palletsprojects.com/en/1.0.x/blueprints/) 或[扩展](https://flask.palletsprojects.com/en/1.0.x/extensions/) 时，根本不会导入`app`实例。

Flask使用 *应用程序上下文* 解决了这个问题。您可以使用[**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 代理，而不是直接引用应用程序，该代理指向处理当前活动的应用程序。

Flask在处理请求时自动 *推送* 应用程序上下文。视图函数，错误处理程序以及在请求期间运行的其他函数将具有对 [**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 的访问权限。

使用`@app.cli.command()`运行在 [**Flask.cli**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.cli) 中注册的CLI命令时，Flask还会自动推送应用程序上下文。

### 上下文的生命周期

必要时创建并销毁应用程序上下文。当Flask应用程序开始处理请求时，它会pushes应用程序上下文和[请求上下文](https://flask.palletsprojects.com/en/1.0.x/reqcontext/) 。当请求结束时，它会pops请求上下文，然后pops应用程序上下文。通常，应用程序上下文与请求具有相同的生命周期。

有关上下文如何工作以及请求的完整生命周期的更多信息，请参阅[请求上下文](https://flask.palletsprojects.com/en/1.0.x/reqcontext/)。

### 手动Push一个上下文

如果您尝试在应用程序上下文之外访问[**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 或使用它的任何内容，您将收到以下错误消息：

```bash

RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that
needed to interface with the current application object in some way.
To solve this, set up an application context with app.app_context().

```

如果在配置应用程序时发现错误，例如初始化扩展时，您可以手动push上下文，因为您可以直接访问`app`。在`with`块中使用 [**app\_context()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.app_context) ，块中运行的所有内容都可以访问 [**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 。

```py

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app

```

如果您在代码中的其他位置看到与配置应用程序无关的错误，则很可能表示您应将该代码移动到视图函数或CLI命令中。

### 存储数据

应用程序上下文是在请求或CLI命令期间存储公共数据的好地方。Flask为此提供了[**g object**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.g) 。它是一个简单的命名空间对象，其生命周期与应用程序上下文相同。

> ### 注意：
>
> g名称代表“全局”，但这指的是在上下文中是全局的数据。上下文结束后g上的数据丢失，并且它不是在请求之间存储数据的合适位置。使用 [**会话(session)**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.session) 或数据库跨请求存储数据。

g的常见用途是在请求期间管理资源。

1. 如果资源X不存在，则`get_X()`创建资源`X`，将其缓存为`g.X`.
2. 如果资源存在，`teardown_X()`将关闭或以其他方式释放资源。它被注册为 [**teardown\_appcontext()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_appcontext) 处理程序。

例如，您可以使用此模式管理数据库连接：

```py

from flask import g

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()

    return g.db

@app.teardown_appcontext
def teardown_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()

```

在请求期间，每次调用`get_db()`都将返回相同的连接，并在请求结束时自动关闭。

您可以使用 [**LocalProxy**](https://werkzeug.palletsprojects.com/en/0.15.x/local/#werkzeug.local.LocalProxy) 从`get_db()`创建一个新的本地上下文：

```py

from werkzeug.local import LocalProxy
db = LocalProxy(get_db)

```

访问`db`将在内部调用`get_db`，方法与 [**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 的工作方式相同。

如果您正在编写扩展名，则应为用户代码保留 [**g**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.g) 。您可以将内部数据存储在上下文中，但请确保使用足够唯一的名称。使用[**\_app\_ctx\_stack.top**](https://flask.palletsprojects.com/en/1.0.x/api/#flask._app_ctx_stack) 访问当前上下文。有关更多信息，请参阅[Flask Extension Development](https://flask.palletsprojects.com/en/1.0.x/extensiondev/)。

### 事件和信号

当弹出应用程序上下文时，应用程序将调用[teardown\_appcontext()](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_appcontext) 注册的函数。
