+++
date = '2025-07-29T10:56:01.379251+08:00'
draft = false
title = 'Flask 1.0 进阶 - 信号(Signals)'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

从Flask 0.6开始，Flask中集成了对信号的支持。这种支持由优秀的 [blinker](https://pypi.org/project/blinker/) 库提供，如果不可用，将优雅地退回。

什么是信号？信号通过在核心框架或其他Flask扩展中的其他位置发生操作时发送通知来帮助您解耦应用程序。简而言之，信号允许某些发送者通知订阅者发生了什么事。

Flask附带了几个信号，其他扩展可能提供更多信号。另请注意，信号旨在通知订阅者，不应鼓励订阅者修改数据。您会注意到有些信号看起来像一些内置装饰器那样做（例如： [**request\_started**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_started) 与 [**before\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.before_request) 非常相似）。但是，它们的工作方式存在差异。例如，核心 [**before\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.before_request) 处理程序以特定顺序执行，并且能够通过返回响应来提前中止请求。相反，所有信号处理程序都以未定义的顺序执行，不会修改任何数据。

信号优于处理程序的一大优势是，您可以一瞬间安全地订阅它们。例如，这些临时订阅有助于单元测试。假设您想知道哪些模板作为请求的一部分呈现：信号允许您完全执行此操作。

### 订阅信号

要订阅信号，您可以使用信号的 [**connect()**](https://pythonhosted.org/blinker/index.html#blinker.base.Signal.connect) 方法。第一个参数是在发出信号时应该调用的函数，可选的第二个参数指定发送者。要取消订阅信号，可以使用 [**disconnect()**](https://pythonhosted.org/blinker/index.html#blinker.base.Signal.disconnect) 方法。

对于所有核心Flask信号，发送方是发出信号的应用程序。订阅信号时，除非您真的想要收听来自所有应用程序的信号，否则请务必提供发件人。如果您正在开发扩展，则尤其如此。

例如，这里有一个帮助器上下文管理器，可以在单元测试中使用它来确定呈现了哪些模板以及将哪些变量传递给模板：

```py

from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

```

现在可以轻松地与测试客户端配对：

```py

with captured_templates(app) as templates:
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert len(templates) == 1
    template, context = templates[0]
    assert template.name == 'index.html'
    assert len(context['items']) == 10

```

确保订阅额外的`**extra`参数，以便在Flask为信号引入新参数时，您的调用不会失败。

现在，应用程序 *app* 在`with`块体中发出的代码中的所有模板呈现都将记录在templates变量中。每当呈现模板时，模板对象以及上下文都会附加到其上。

此外，还有一个方便的辅助方法（ [**connected\_to()**](https://pythonhosted.org/blinker/index.html#blinker.base.Signal.connected_to) ），它允许您使用上下文管理器临时为函数订阅函数。因为无法以这种方式指定上下文管理器的返回值，所以必须将列表作为参数传递：

```py

from flask import template_rendered

def captured_templates(app, recorded, **extra):
    def record(sender, template, context):
        recorded.append((template, context))
    return template_rendered.connected_to(record, app)

```

上面的例子如下所示：

```py

templates = []
with captured_templates(app, templates, **extra):
    ...
    template, context = templates[0]

```

### 创建信号

如果要在自己的应用程序中使用信号，可以直接使用blinker库。最常见的用例是自定义 [**Namespace**](https://pythonhosted.org/blinker/index.html#blinker.base.Namespace) 中的命名信号。这是大多数时候建议的：

```py

from blinker import Namespace
my_signals = Namespace()

```

现在您可以创建这样的新信号：

```py

model_saved = my_signals.signal('model-saved')

```

此处信号的名称使其独一无二，并简化了调试。您可以使用name属性访问信号的名称。

> ####To扩展开发者:
>
> 如果您正在编写Flask扩展，并且希望对缺少的blinker安装进行优雅降级，则可以使用flask.signals.Namespace类来执行此操作。

### 发送信号

如果要发出信号，可以通过调用 [**send()**](https://pythonhosted.org/blinker/index.html#blinker.base.Signal.send) 方法来实现。它接受发送方作为第一个参数，并可选择接收一些转发给信号订阅者的关键字参数：

```py

class Model(object):
    ...

    def save(self):
        model_saved.send(self)

```

尽量选择一个好的发送者。如果您有一个发出信号的类，请将self作为发送者传递。如果从随机函数发出信号，则可以将`current_app._get_current_object()`作为发送方传递。

> ### 将代理作为发送者传递
>
> 永远不要将 [**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 作为发送者传递给信号。请改用`current_app._get_current_object()`。原因是 [**current\_app**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.current_app) 是代理而不是真正的应用程序对象。

### 信号和Flask的请求上下文

信号在接收信号时完全支持[请求上下文](https://flask.palletsprojects.com/en/1.0.x/reqcontext/#request-context)。在 [**request\_started**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_started) 和 [**request\_finished**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_finished) 之间始终可以使用上下文局部变量，因此您可以根据需要依赖于 [**flask.g**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.g) 和其他变量。请注意 [发送信号](https://flask.palletsprojects.com/en/1.0.x/signals/#signals-sending) 和 [**request\_tearing\_down**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.request_tearing_down) 信号中描述的限制。

### 基于装饰器的信号订阅

使用Blinker 1.1，您还可以使用新的 **connect\_via()** 装饰器轻松订阅信号：

```py

from flask import template_rendered

@template_rendered.connect_via(app)
def when_template_rendered(sender, template, context, **extra):
    print 'Template %s is rendered with %s' % (template.name, context)

```

### 核心信号

查看[信号](https://flask.palletsprojects.com/en/1.0.x/api/#core-signals-list) 以获取所有内置信号的列表。
