+++
date = '2025-07-29T10:56:14.800927+08:00'
draft = false
title = 'Flask 1.0 进阶 - 请求上下文'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

请求上下文在请求期间跟踪请求级数据。而不是将请求对象传递给在请求期间运行的每个函数，而是访问 [**request**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request) 和 [**会话**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.session) 代理。

这类似于应用程序上下文，它独立于请求跟踪应用程序级数据。当推送请求上下文时，推送相应的应用程序上下文。

### 上下文的目的

当 [**Flask**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask) 应用程序处理请求时，它会根据从WSGI服务器收到的环境创建一个 [**Request**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Request) 对象。由于*worker*（线程，进程或协程取决于服务器）一次只处理一个请求，因此在该请求期间可以将请求数据视为该工作者的全局请求。Flask为此使用术语*context local*。

Flask在处理请求时自动推送请求上下文。查看函数，错误处理程序以及在请求期间运行的其他函数将有权访问 [**request**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request) 代理，该代理指向当前请求的请求对象。

### 上下文的生命周期

当Flask应用程序开始处理请求时，它会push请求上下文，这也会push [应用程序上下文](https://flask.palletsprojects.com/en/1.0.x/appcontext/) 。当请求结束时，它会pop请求上下文，然后pop应用程序上下文。

上下文对于每个线程（或其他worker类型）是唯一的。[request](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request) 无法传递给另一个线程，另一个线程将具有不同的上下文堆栈，并且不会知道父线程指向的请求。

上下文本地在Werkzeug中实现。有关其内部工作原理的更多信息，请参阅[上下文本地](https://werkzeug.palletsprojects.com/en/0.15.x/local/)。

### 手动推送上下文

如果您尝试在请求上下文之外访问请求或使用它的任何内容，您将收到以下错误消息：

```bash

RuntimeError: Working outside of request context.

This typically means that you attempted to use functionality that
needed an active HTTP request. Consult the documentation on testing
for information about how to avoid this problem.

```

通常只有在测试需要active请求的代码时才会发生这种情况。一种选择是使用[**test client**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.test_client) 来模拟完整请求。或者，您可以在with块中使用[**test\_request\_context()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.test_request_context) ，并且块中运行的所有内容都可以访问[请求](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request) ，并填充测试数据。

```py

def generate_report(year):
    format = request.args.get('format')
    ...

with app.test_request_context(
        '/make_report/2017', data={'format': 'short'}):
    generate_report()

```

如果您在代码中的其他位置看到与测试无关的错误，则很可能表示您应该将该代码移动到视图函数中。

有关如何使用交互式Python shell中的请求上下文的信息，请参阅[使用命令行管理程序](https://flask.palletsprojects.com/en/1.0.x/shell/)。

### 上下文如何运作

调用[**Flask.wsgi\_app()**](http://localhost:6419/)方法来处理每个请求。它在请求期间管理上下文。在内部，请求和应用程序上下文用作堆栈，[**\_request\_ctx\_stack**](https://flask.palletsprojects.com/en/1.0.x/api/#flask._request_ctx_stack) 和[**\_app\_ctx\_stack**](https://flask.palletsprojects.com/en/1.0.x/api/#flask._app_ctx_stack) 。当上下文被压入堆栈时，依赖于它们的代理是可用的，并指向来自堆栈顶部上下文的信息

当请求开始时，创建并pushed [**RequestContext**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.ctx.RequestContext)，如果该应用程序的上下文不是顶层上下文，则首先创建并pushes [AppContext](https://flask.palletsprojects.com/en/1.0.x/api/#flask.ctx.AppContext)。在推送这些上下文时，[current\_app](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app)，[g](https://flask.palletsprojects.com/en/1.0.x/api/#flask.g)，[request](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request)和[session](https://flask.palletsprojects.com/en/1.0.x/api/#flask.session)代理可用于处理请求的原始线程。

因为上下文是堆栈，所以可以推送其他上下文以在请求期间更改代理。虽然这不是一种常见的模式，但它可以在高级应用程序中使用，例如，进行内部重定向或将不同的应用程序链接在一起。

在调度请求并生成并发送响应之后，将poped请求上下文，然后popped应用程序上下文。在popped它们之前，执行[**teardown\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_request) 和[**teardown\_appcontext()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_appcontext) 函数。即使在发送期间发生未处理的异常，它们也会执行。

### 回调和错误

Flask在多个阶段调度请求，这可能会影响请求，响应以及如何处理错误。在所有这些阶段中，上下文都是活跃的。

[Blueprint](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Blueprint) 可以为这些特定于blueprint的事件添加处理程序。如果blueprint拥有与请求匹配的路由，则将运行blueprint处理程序。

1. 在每个请求之前，调用[**before\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.before_request) 函数。如果其中一个函数返回一个值，则跳过其他函数。返回值被视为响应，并且不调用视图函数。
2. 如果[**before\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.before_request)函数未返回响应，则调用匹配路由的视图函数并返回响应。
3. 视图的返回值将转换为实际响应对象并传递给[**after\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.after_request)函数。每个函数都返回一个修改的或新的响应对象。
4. 返回响应后，弹出上下文，调用[**teardown\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_request)和[**teardown\_appcontext()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_appcontext)函数。即使在上面的任何点引发了未处理的异常，也会调用这些函数。

如果在拆卸函数之前引发异常，Flask会尝试将其与[**errorhandler()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.errorhandler)函数匹配以处理异常并返回响应。如果未找到错误处理程序，或者处理程序本身引发异常，Flask将返回通用的`500内部服务器错误`响应。仍然会调用拆卸函数，并传递异常对象。

如果启用了调试模式，则未处理的异常不会转换为`500`响应，而是传播到WSGI服务器。这允许开发服务器向交互式调试器提供回溯。

### Teardown回调

teardown回调与请求分派无关，而是在popped时由上下文调用。即使在调度期间存在未处理的异常，也会调用函数，以及手动推送的上下文。这意味着无法保证请求调度的任何其他部分首先运行。请务必以不依赖于其他回调的方式编写这些函数，并且不会失败。

在测试期间，在请求结束后推迟popped上下文可能很有用，这样可以在测试函数中访问它们的数据。使用test\_client()作为with块来保留上下文，直到with块退出。

```py

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    print('during view')
    return 'Hello, World!'

@app.teardown_request
def show_teardown(exception):
    print('after with block')

with app.test_request_context():
    print('during with block')

# teardown functions are called after the context with block exits

with app.test_client():
    client.get('/')
    # the contexts are not popped even though the request ended
    print(request.path)

# the contexts are popped and teardown functions are called after
# the client with block exists

```

### Signals

如果[**signals\_available**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.signals.signals_available)为true，则发送以下信号：

1. [**request\_started**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_started) 在调用[**before\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.before_request) 函数之前发送。
2. 在调用[**after\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.after_request)函数之后发送[**request\_finished**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_finished)。
3. 在开始处理异常时，但在查找或调用[**errorhandler()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.errorhandler) 之前发送[**got\_request\_exception**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.got_request_exception) 。
4. 在调用[teardown\_request()](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.teardown_request) 函数之后发送[request\_tearing\_down](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_tearing_down) 。

### 上下文保留错误

在请求结束时，将popped请求上下文，并销毁与其关联的所有数据。如果在开发过程中发生错误，则延迟销毁数据以进行调试非常有用。

当开发服务器以开发模式运行时（`FLASK_ENV`环境变量设置为`'development'`），错误和数据将被保留并显示在交互式调试器中。

可以使用 [**PRESERVE\_CONTEXT\_ON\_EXCEPTION**](https://flask.palletsprojects.com/en/1.0.x/config/#PRESERVE_CONTEXT_ON_EXCEPTION) 配置控制此行为。如上所述，它在开发环境中默认为`True`。

不要在生产中启用 [**PRESERVE\_CONTEXT\_ON\_EXCEPTION**](https://flask.palletsprojects.com/en/1.0.x/config/#PRESERVE_CONTEXT_ON_EXCEPTION) ，因为它会导致应用程序在异常时泄漏内存。

### 关于代理的注意事项

Flask提供的一些对象是其他对象的代理。对于每个工作线程，代理以相同的方式访问，但指向此页面中描述的绑定到幕后每个worker的唯一对象。

大多数情况下你不必关心它，但有一些例外情况，知道这个对象是一个真正的代理是很好的：

* 代理对象不能伪造其类型作为实际对象类型。如果要执行实例检查，则必须对要代理的对象执行此操作。
* 如果特定对象引用很重要，例如发送信号或将数据传递给后台线程。

如果需要访问代理的基础对象，请使用[**\_get\_current\_object()**](https://werkzeug.palletsprojects.com/en/0.15.x/local/#werkzeug.local.LocalProxy._get_current_object)方法：

```py

app = current_app._get_current_object()
my_signal.send(app)
```
