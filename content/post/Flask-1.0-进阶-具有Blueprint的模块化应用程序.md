+++
date = '2025-07-29T10:56:19.071437+08:00'
draft = false
title = 'Flask 1.0 进阶 - 具有Blueprint的模块化应用程序'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask",
    "Blueprint"
]
+++

## 具有Blueprint的模块化应用程序

Flask使用蓝图概念来制作应用程序组件，并在应用程序或应用程序中支持常见模式。蓝图可以极大地简化大型应用程序的工作方式，并为Flask扩展提供注册应用程序操作的核心方法。 [**Blueprint**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Blueprint) 对象与 [**Flask**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask) 应用程序对象的工作方式类似，但它实际上并不是一个应用程序。相反，它是如何构建或扩展应用程序的蓝图。

### 为何选择蓝图？

Flask中的蓝图适用于以下情况：

* 将应用程序纳入一组蓝图中。这是大型应用的理想选择;项目可以实例化一个应用程序对象，初始化几个扩展，并注册一组蓝图。
* 在URL前缀和/或子域中的应用程序上注册蓝图。URL前缀/子域中的参数成为蓝图中所有视图函数的公共视图参数（具有默认值）。
* 在具有不同URL规则的应用程序上多次注册蓝图。
* 通过蓝图提供模板过滤器，静态文件，模板和其他实用程序。蓝图不必实现应用程序或查看功能。
* 在初始化Flask扩展时，在应用程序中为任何这些情况注册蓝图。

Flask中的蓝图不是一个可插拔的应用程序，因为它实际上不是一个应用程序 - 它是一组可以在应用程序上注册的操作，甚至多次。为什么没有多个应用程序对象？您可以这样做（请参阅[应用程序调度](https://flask.palletsprojects.com/en/1.0.x/patterns/appdispatch/#app-dispatch)），但您的应用程序将具有单独的配置，并将在WSGI层进行管理。

相反，蓝图在Flask级别提供分离，共享应用程序配置，并且可以根据需要在注册时更改应用程序对象。缺点是，一旦创建应用程序，您无法取消注册蓝图，而不必销毁整个应用程序对象。

### 蓝图的概念

蓝图的基本概念是它们记录在应用程序上注册时要执行的操作。在分派请求和从一个端点到另一个端点生成URL时，Flask将视图函数与蓝图相关联。

### 我的第一份蓝图

这是一个非常基本的蓝图。在这种情况下，我们希望实现一个简单渲染静态模板的蓝图：

```py

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

```

在`@simple_page.route`装饰器的帮助下绑定函数时，蓝图将记录在应用程序稍后注册时在应用程序上注册函数`show`的意图。此外，它将为函数的端点添加蓝图的名称，该蓝图的名称是给予 [**Blueprint**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Blueprint) 构造函数的（在本例中也是`simple_page`）。蓝图的名称不会修改URL，只会修改endpoint。

### 注册蓝图

那么你如何注册这个蓝图？像这样：

```py

from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)

```

如果您检查在应用程序上注册的规则，您会发现：

```bash

[<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>]

```

第一个显然来自应用程序本身的静态文件。另外两个用于`simple_page`蓝图的 *show* 函数。如您所见，它们还以蓝图的名称为前缀，并以点（`.`）分隔。

然而，蓝图也可以安装在不同的位置：

```py

app.register_blueprint(simple_page, url_prefix='/pages')

```

然后，生成的规则对应如下：

```bash

[<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/pages/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/pages/' (HEAD, OPTIONS, GET) -> simple_page.show>]

```

最重要的是，您可以多次注册蓝图，但并非每个蓝图都可以正确响应。实际上，如果蓝图可以多次安装，它取决于蓝图的实现方式。

### 蓝图资源

蓝图也可以提供资源。有时您可能只想为其提供的资源引入蓝图。

### 蓝图资源文件夹

与常规应用程序一样，蓝图被认为包含在文件夹中。虽然多个蓝图可以来自同一个文件夹，但并非必须如此，通常不建议这样做。

该文件夹是从 [**Blueprint**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Blueprint) 的第二个参数推断出来的，通常是\***name**\*。此参数指定哪个逻辑Python模块或包对应于蓝图。如果它指向一个实际的Python包，那么包（它是文件系统上的文件夹）就是资源文件夹。如果它是一个模块，则包含模块的包将是资源文件夹。您可以访问 [**Blueprint.root\_path**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Blueprint.root_path) 属性以查看资源文件夹是什么：

```bash

>>> simple_page.root_path
'/Users/username/TestProject/yourapplication'

```

要从此文件夹快速打开源，您可以使用 [**open\_resource()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Blueprint.open_resource) 函数：

```py

with simple_page.open_resource('static/style.css') as f:
    code = f.read()

```

### 静态文件

蓝图可以通过使用`static_folder`参数提供文件系统上文件夹的路径来公开具有静态文件的文件夹。它是绝对路径或相对于蓝图的位置：

```py

admin = Blueprint('admin', __name__, static_folder='static')

```

默认情况下，路径的最右边部分是它在Web上公开的位置。可以使用`static_url_path`参数更改此设置。因为此处的文件夹名为`static`，所以它将在蓝图+`/static`的`url_prefix`中提供。如果蓝图具有前缀`/admin`，则静态URL将为`/admin/static`。

endpoint名为`blueprint_name.static`。您可以使用 [**url\_for()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.url_for) 生成URL，就像使用应用程序的静态文件夹一样：

```py

url_for('admin.static', filename='style.css')

```

但是，如果蓝图没有`url_prefix`，则无法访问蓝图的静态文件夹。这是因为在这种情况下URL将是`/static`，并且应用程序的`/static`路由优先。与模板文件夹不同，如果应用程序静态文件夹中不存在该文件，则不会搜索蓝图静态文件夹。

### 模板

如果您希望蓝图公开模板，可以通过向Blueprint构造函数提供*template\_folder*参数来实现：

```py

admin = Blueprint('admin', __name__, template_folder='templates')

```

对于静态文件，路径可以是蓝图资源文件夹的绝对路径或相对路径。

模板文件夹添加到模板的搜索路径中，但优先级低于实际应用程序的模板文件夹。这样，您可以轻松覆盖蓝图在实际应用程序中提供的模板。这也意味着如果您不希望意外覆盖蓝图模板，请确保没有其他蓝图或实际应用程序模板具有相同的相对路径。当多个蓝图提供相同的相对模板路径时，注册的第一个蓝图优先于其他蓝图。

因此，如果您在`yourapplication/admin`中的文件夹中有蓝图，并且您希望呈现模板`'admin/index.html'`并且您提供了`templates`作为*template\_folder*，则必须创建如下文件：`yourapplication/admin/templates/admin/index.html`的。额外`admin`文件夹的原因是为了避免在实际应用程序模板文件夹中使用名为`index.html`的模板覆盖我们的模板。

为了进一步重申这一点：如果你有一个名为`admin`的蓝图，并且你想渲染一个名为`index.html`的模板，这个模板是特定于这个蓝图的，那么最好的想法就是像这样布置你的模板：

```bash

yourpackage/
    blueprints/
        admin/
            templates/
                admin/
                    index.html
            __init__.py

```

然后，当您想要渲染模板时，使用`admin/index.html`作为名称来查找模板。如果您在加载正确的模板时遇到问题，请启用`EXPLAIN_TEMPLATE_LOADING`配置变量，该变量将指示Flask打印出在每次`render_template`调用时定位模板的步骤。

### 构建网址

如果你想从一个页面链接到另一个页面，你可以使用 [**url\_for()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.url_for) 函数，就像你通常只需要在URL端点前面加上蓝图的名称和点（`.`）：

```py

url_for('admin.index')

```

此外，如果您处于蓝图或渲染模板的视图功能中并且想要链接到同一蓝图的另一个端点，则可以通过在端点前面添加一个点来使用相对重定向：

```py

url_for('.index')

```

这将链接到`admin.index`，例如，以防当前请求被分派到任何其他管理蓝图端点。

### 错误处理程序

蓝图支持`errorhandler`装饰器，就像 [**Flask**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask) 应用程序对象一样，因此很容易制作特定于蓝图的自定义错误页面。

以下是“404找不到页面”异常的示例：

```py

@simple_page.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html')

```

大多数错误处理程序将按预期工作;但是，有关404和405例外处理程序的警告。这些错误处理程序仅从相应的`raise`语句或另一个蓝图视图函数中的`abort`调用中调用;例如，无效的URL访问不会调用它们。这是因为蓝图不“拥有”某个URL空间，因此如果给定无效的URL，应用程序实例无法知道它应该运行哪个蓝图错误处理程序。如果您希望基于URL前缀对这些错误执行不同的处理策略，可以使用请求代理对象在应用程序级别定义它们：

```py

@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(ex):
    if request.path.startswith('/api/'):
        return jsonify_error(ex)
    else:
        return ex

```

有关错误处理的更多信息请参阅[自定义错误页](https://flask.palletsprojects.com/en/1.0.x/patterns/errorpages/#errorpages)
