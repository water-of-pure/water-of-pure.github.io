+++
date = '2025-07-29T10:55:48.923348+08:00'
draft = false
title = 'Flask 1.0 进阶 - 应用程序错误'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

应用程序失败，服务器失败迟早你会看到生产中的例外情况。即使您的代码100％正确，您仍会不时看到异常。为什么？因为所涉及的一切都会失败。以下是一些完美的代码可能导致服务器错误的情况：

* 客户端提前终止了请求，应用程序仍然从传入的数据中读取
* 数据库服务器挂了，无法处理查询
* 文件系统已满
* 一个硬盘崩溃了
* 一个后端服务器挂了
* 正在使用的库中出现了编程错误
* 服务器与另一个系统的网络连接失败

这只是您可能面临的一小部分问题。那么我们如何处理这类问题呢？默认情况下，如果您的应用程序在生产模式下运行，Flask将为您显示一个非常简单的页面，并将异常记录到 [**logger**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.logger) 中。

但是你可以做的更多，我们将介绍一些更好的设置来处理错误。

## 错误记录工具

如果有足够多的用户遇到错误并且通常从不查看日志文件，那么发送错误邮件（即使仅针对关键邮件）也会变得无法控制。这就是我们建议使用[Sentry](https://www.getsentry.com/)处理应用程序错误的原因。它可以在[GitHub](https://github.com/getsentry/sentry)上作为开源项目使用，也可以作为托管版本使用，您可以免费试用。Sentry聚合重复错误，捕获完整堆栈跟踪和本地变量以进行调试，并根据新错误或频率阈值向您发送邮件。

要使用Sentry，您需要安装具有额外Flask依赖性的raven客户端：

```bash

pip install raven[flask]

```

然后将其添加到Flask应用中：

```py

from raven.contrib.flask import Sentry
sentry = Sentry(app, dsn='YOUR_DSN_HERE')

```

或者，如果您正在使用工厂，您也可以稍后启动它：

```py

from raven.contrib.flask import Sentry
sentry = Sentry(dsn='YOUR_DSN_HERE')

def create_app():
    app = Flask(__name__)
    sentry.init_app(app)
    ...
    return app

```

需要使用从Sentry安装获得的DSN值替换YOUR\_DSN\_HERE值。

之后故障会自动报告给Sentry，您可以从那里收到错误通知。

## 错误处理程序

您可能希望在发生错误时向用户显示自定义错误页面。这可以通过注册错误处理程序来完成。

错误处理程序是返回响应的普通视图函数，但它不是为路由注册，而是注册在尝试处理请求时引发的异常或HTTP状态代码。

### 注册

通过使用[**errorhandler()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.errorhandler) 装饰函数来注册处理程序。或者使用 [**register\_error\_handler()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.register_error_handler) 稍后注册该函数。请记住在返回响应时设置错误代码。

```py

@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

# or, without the decorator
app.register_error_handler(400, handle_bad_request)

```

[**werkzeug.exceptions.HTTPException**](http://werkzeug.pocoo.org/docs/exceptions/#werkzeug.exceptions.HTTPException) 子类如 [BadRequest](http://werkzeug.pocoo.org/docs/exceptions/#werkzeug.exceptions.BadRequest) 及其HTTP代码在注册处理程序时是可互换的。（`BadRequest.code == 400`）

代码无法注册非标准HTTP代码，因为Werkzeug不知道它们。相反，使用适当的代码定义 [**HTTPException**](http://werkzeug.pocoo.org/docs/exceptions/#werkzeug.exceptions.HTTPException) 的子类并注册并引发该异常类。

```py

class InsufficientStorage(werkzeug.exceptions.HTTPException):
    code = 507
    description = 'Not enough storage space.'

app.register_error_handler(InsuffcientStorage, handle_507)

raise InsufficientStorage()

```

可以为任何异常类注册处理程序，而不仅仅是HTTPException子类或HTTP状态代码。可以为特定类或父类的所有子类注册处理程序。

### 处理

当Flask在处理请求时捕获到异常时，首先按代码查找。如果没有为代码注册处理程序，则按类层次结构查找;选择最具体的处理程序。如果未注册任何处理程序，则[**HTTPException**](http://werkzeug.pocoo.org/docs/exceptions/#werkzeug.exceptions.HTTPException) 子类显示有关其代码的通用消息，而其他异常则转换为通用500内部服务器错误。

例如，如果引发了 [**ConnectionRefusedError**](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError) 的实例，并且为 [**ConnectionError**](https://docs.python.org/3/library/exceptions.html#ConnectionError) 和 [**ConnectionRefusedError**](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError) 注册了处理程序，则使用异常实例调用更具体的 [**ConnectionRefusedError**](https://docs.python.org/3/library/exceptions.html#ConnectionRefusedError) 处理程序以生成响应。

在blueprint上注册的处理程序优先于在应用程序上全局注册的处理程序，假设blueprint正在处理引发异常的请求。但是，blueprint无法处理404路由错误，因为404可以在确定blueprint之前发生在路由级别。

> 版本0.11： 处理程序的优先级取决于它们注册的异常类的特殊性，而不是它们注册的顺序

### 日志记录

有关如何记录异常的信息，请参阅[记录](http://flask.pocoo.org/docs/1.0/logging/#logging)，例如通过电子邮件将其发送给管理员。

## 调试应用程序错误

对于生产应用程序，使用[应用程序错误](http://flask.pocoo.org/docs/1.0/errorhandling/#application-errors)中所述的日志记录和通知配置应用程序。本节提供了调试部署配置和深入挖掘全功能Python调试器的指针。

## 当有疑问时，手动运行

在为生产配置应用程序时遇到问题？如果您具有对主机的shell访问权限，请验证您是否可以从部署环境中的shell手动运行应用程序。请确保在与配置的部署相同的用户帐户下运行，以解决权限问题。您可以在生产主机上使用带有 *debug = True* 的Flask内置开发服务器，这有助于捕获配置问题，但 **请务必在受控环境中暂时执行此操作** 。不要使用 *debug = True* 在生产中运行。

## 使用调试器

为了深入挖掘，可能需要跟踪代码执行，Flask提供了一个开箱即用的调试器（参见[调试模式](http://flask.pocoo.org/docs/1.0/quickstart/#debug-mode)）。如果您想使用其他Python调试器，请注意调试器会相互干扰。您必须设置一些选项才能使用您喜欢的调试器：

* `debug` - 是否启用调试模式和捕获异常
* `use_debugger` - 是否使用内部Flask调试器
* `use_reloader` - 是否在异常时重新加载和分叉进程

`debug`必须为True（即必须捕获异常）才能使其他两个选项具有任何值。

如果您使用Aptana/Eclipse进行调试，则需要将`use_debugger`和`use_reloader`都设置为False。

一个可能有用的配置模式是在config.yaml中设置以下内容（当然，根据您的应用程序更改块）：

```yaml

FLASK:
    DEBUG: True
    DEBUG_WITH_APTANA: True

```

然后在你的应用程序的入口点（main.py），你可以有类似的东西：

```py

if __name__ == "__main__":
    # To allow aptana to receive errors, set use_debugger=False
    app = create_app(config="config.yaml")

    if app.debug: use_debugger = True
    try:
        # Disable Flask's debugger if external debugger is requested
        use_debugger = not(app.config.get('DEBUG_WITH_APTANA'))
    except:
        pass

    app.run(use_debugger=use_debugger, debug=app.debug,
            use_reloader=use_debugger, host='0.0.0.0')
```
