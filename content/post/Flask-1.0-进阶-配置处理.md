+++
date = '2025-07-29T10:55:58.233465+08:00'
draft = false
title = 'Flask 1.0 进阶 - 配置处理'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

应用程序需要某种配置。您可能希望更改不同的设置，具体取决于应用程序环境，例如切换调试模式，设置密钥以及其他此类特定于环境的内容。

Flask的设计方式通常要求在应用程序启动时配置可用。您可以对代码中的配置进行硬编码，对于许多小型应用程序而言，实际上并不是那么糟糕，但有更好的方法。

无论您如何加载配置，都有一个可用的配置对象，它保存已加载的配置值： [**Flask**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask) 对象的 [config](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.config) 属性。这是Flask本身放置某些配置值的地方，也是扩展可以放置其配置值的地方。但这也是您可以拥有自己的配置的地方。

## 基础配置

[**config**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.config) 实际上是字典的子类，可以像任何字典一样进行修改：

```py

app = Flask(__name__)
app.config['TESTING'] = True

```

某些配置值也会转发到 [**Flask**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask) 对象，以便您可以从那里读取和写入它们：

```py

app.testing = True

```

要一次更新多个密钥，可以使用 [**dict.update()**](https://docs.python.org/3/library/stdtypes.html#dict.update) 方法：

```py

app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
)

```

## 环境和调试功能

[**ENV**](https://flask.palletsprojects.com/en/1.0.x/config/#ENV) 和 [**DEBUG**](https://flask.palletsprojects.com/en/1.0.x/config/#DEBUG) 配置值是特殊的，因为如果在应用程序开始设置后更改，它们可能会表现不一致。为了可靠地设置环境和调试模式，Flask使用环境变量。

该环境用于指示Flask，扩展和其他程序，如Sentry，Flask正在运行的上下文。它由 **FLASK\_ENV** 环境变量控制，默认为`production`。

将**FLASK\_ENV**设置为`development`将启用调试模式。`flask run`将在调试模式下默认使用交互式调试器和重新加载器。要与环境分开控制，请使用 **FLASK\_DEBUG** 标志。

要将Flask切换到开发环境并启用调试模式，请设置 **FLASK\_ENV**：

```bash

export FLASK_ENV=development
flask run

```

建议使用上述环境变量。虽然可以在配置或代码中设置 [**ENV**](https://flask.palletsprojects.com/en/1.0.x/config/#ENV) 和 [**DEBUG**](https://flask.palletsprojects.com/en/1.0.x/config/#DEBUG) ，但强烈建议不要这样做。使用flask命令无法及早读取它们，并且某些系统或扩展可能已根据先前的值配置了自身。

## 内置配置值

Flask在内部使用以下配置值，这里只是简单介绍下比较常用的几个，具体的详细的配置值可以去 [官网查看](https://flask.palletsprojects.com/en/1.0.x/config/)

### ENV

应用程序运行的环境。 Flask和扩展可以启用基于环境的行为，例如启用调试模式。[**env**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.env) 属性映射到此配置键。这是由FLASK\_ENV环境变量设置的，如果在代码中设置，可能不会按预期运行。

**在生产环境中部署时不要启用开发模式**。

默认值：`'production'`

### DEBUG

是否启用调试模式。 当使用`flask run`启动开发服务器时，将显示一个交互式调试器，用于未处理的异常，并在代码更改时重新加载服务器。[**debug**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.debug) 属性映射到此配置键。当[**ENV**](https://flask.palletsprojects.com/en/1.0.x/config/#ENV) 为`'development'`并被FLASK\_DEBUG环境变量覆盖时，将启用此功能。如果在代码中设置，它可能不会按预期运行。

**在生产中部署时，请勿启用调试模式。**

默认值：如果ENV为`'development'`时值为`True`，否则为`False`

### TESTING

启用测试模式。 异常传播而不是由应用程序的错误处理程序处理。扩展也可能会改变其行为，以方便测试。您应该在自己的测试中启用它。

默认值：`False`

### PROPAGATE\_EXCEPTIONS

异常被重新引发而不是由应用程序的错误处理程序处理。

如果没有设置，在启用了TESTING或DEBUG，则隐含为true。

默认值: `None`

### PRESERVE\_CONTEXT\_ON\_EXCEPTION

发生异常时不要弹出请求上下文。

如果未设置，在DEBUG为true时，则为true。这允许调试器在错误上内省请求数据，通常不需要直接设置。

默认值: `None`

### SECRET\_KEY

用于安全签名会话cookie的密钥，可用于扩展或您的应用程序的任何其他安全相关需求。它应该是一个长的随机字节串，尽管也接受unicode。例如，将其输出复制到您的配置：

```bash

python -c 'import os; print(os.urandom(16))'
b'_5#y2L"F4Q8z\n\xec]/'

```

**提交问题或提交代码时不要泄露密钥。**

默认值: `None`

## 从文件配置

如果您可以将其存储在单独的文件中，理想情况下位于实际应用程序包之外，则配置会变得更有用。这使得可以通过各种包处理工具（[使用Setuptools进行部署](https://flask.palletsprojects.com/en/1.0.x/patterns/distribute/#distribute-deployment)）来打包和分发应用程序，最后修改配置文件。

所以一个常见的模式是：

```py

app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

```

首先从 *yourapplication.default\_settings* 模块加载配置，然后使用**YOURAPPLICATION\_SETTINGS**环境变量指向的文件内容覆盖值。在启动服务器之前，可以使用shell中的export命令在Linux或OS X上设置此环境变量：

```bash

$ export YOURAPPLICATION_SETTINGS=/path/to/settings.cfg
$ python run-app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader...

```

在Windows系统上使用内置的 *set* 代替：

```bash

>set YOURAPPLICATION_SETTINGS=\path\to\settings.cfg

```

配置文件本身就是实际的Python文件。以后只有大写的值实际存储在配置对象中。因此，请确保为配置键使用大写字母。

以下是配置文件的示例：

```py

# Example configuration
DEBUG = False
SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'

```

确保尽早加载配置，以便扩展能够在启动时访问配置。配置对象上还有其他方法可以从单个文件加载。有关完整参考，请阅读 [**Config**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Config) 对象的文档。

## 从环境变量配置

除了使用环境变量指向配置文件之外，您可能会发现直接从环境控制配置值很有用（或必要）。

在启动服务器之前，可以使用shell中的export命令在Linux或OS X上设置环境变量：

```bash

$ export SECRET_KEY='5f352379324c22463451387a0aec5d2f'
$ export MAIL_ENABLED=false
$ python run-app.py
 * Running on http://127.0.0.1:5000/

```

在Windows系统上使用内置的`set`代替：

```bash

>set SECRET_KEY='5f352379324c22463451387a0aec5d2f'

```

虽然这种方法很容易使用，但重要的是要记住环境变量是字符串 - 它们不会自动反序列化为Python类型。

以下是使用环境变量的配置文件的示例：

```py

import os

_mail_enabled = os.environ.get("MAIL_ENABLED", default="true")
MAIL_ENABLED = _mail_enabled.lower() in {"1", "t", "true"}

SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")

```

请注意，除了空字符串之外的任何值都将被解释为Python中的布尔值`True`，如果环境显式设置了值为`False`的值，则需要注意。

确保尽早加载配置，以便扩展能够在启动时访问配置。配置对象上还有其他方法可以从单个文件加载。有关完整参考，请阅读 [**Config**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Config) 类文档。

## 配置最佳实践

前面提到的方法的缺点是它使测试更加困难。一般来说，这个问题没有单一的100％解决方案，但是您可以记住以下几点来改善这种体验：

1. 在函数中创建应用程序并在其上注册blueprint。这样，您可以创建应用程序的多个实例，并附加不同的配置，这使得单元测试变得更加容易。您可以根据需要使用它来传递配置。
2. 不要在导入时编写需要配置的代码。如果您将自己限制为仅对请求进行配置访问，则可以根据需要稍后重新配置对象。

## 开发/生产

大多数应用程序需要多个配置。生产服务器和开发期间使用的配置至少应该是单独的配置。处理此问题的最简单方法是使用始终加载的默认配置和版本控制的一部分，以及根据上述示例中提到的必要覆盖值的单独配置：

```py

app = Flask(__name__)
app.config.from_object('yourapplication.default_settings')
app.config.from_envvar('YOURAPPLICATION_SETTINGS')

```

然后你只需要添加一个单独的config.py文件并导出YOURAPPLICATION\_SETTINGS=/path/to/config.py就完成了。然而，也有其他方法。例如，您可以使用导入或子类化。

Django世界中非常流行的是通过将`yourapplication.default_settings import *`添加到文件顶部然后手动覆盖更改，在配置文件中显式导入。您还可以检查环境变量，如YOURAPPLICATION\_MODE，并将其设置为生产，开发等，并根据该变量导入不同的硬编码文件。

一个有趣的模式也是使用类和继承进行配置：

```py

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

```

要启用此类配置，您只需调用from\_object()：

```py

app.config.from_object('configmodule.ProductionConfig')

```

请注意，from\_object()不会实例化类对象。如果需要实例化类，例如访问属性，则必须在调用from\_object()之前执行此操作：

```py

from configmodule import ProductionConfig
app.config.from_object(ProductionConfig())

# Alternatively, import via string:
from werkzeug.utils import import_string
cfg = import_string('configmodule.ProductionConfig')()
app.config.from_object(cfg)

```

实例化配置对象允许您在配置类中使用`@property`：

```py

class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    DB_SERVER = '192.168.1.56'

    @property
    def DATABASE_URI(self):         # Note: all caps
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)

class ProductionConfig(Config):
    """Uses production database server."""
    DB_SERVER = '192.168.19.32'

class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True

class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    DATABASE_URI = 'sqlite:///:memory:'

```

有许多不同的方法，由您决定如何管理配置文件。不过这里列出了很好的建议：

1. 在版本控制中保留默认配置。使用此默认配置填充配置，或者在覆盖值之前将其导入您自己的配置文件中。
2. 使用环境变量在配置之间切换。这可以从Python解释器外部完成，并使开发和部署变得更加容易，因为您可以快速轻松地在不同的配置之间切换而无需触摸代码。如果您经常在不同的项目上工作，您甚至可以创建自己的源代码脚本来激活virtualenv并为您导出开发配置。
3. 在生产中使用类似[fabric](http://www.fabfile.org/)的工具将代码和配置分别推送到生产服务器。有关如何执行此操作的一些详细信息，请转到[使用Fabric进行部署模式](https://flask.palletsprojects.com/en/1.0.x/patterns/fabric/#fabric-deployment)。

## 实例文件夹

Flask 0.8引入了实例文件夹。Flask很长一段时间可以直接引用相对于应用程序文件夹的路径（通过 **Flask.root\_path** ）。这也是有很多开发人员加载了存储在应用程序旁边的配置。不幸的是，这只适用于应用程序不是包的情况，在这种情况下根路径引用包的内容。

随着Flask 0.8引入了一个新属性： **Flask.instance\_path** 。它指的是一个名为“实例文件夹”的新概念。实例文件夹旨在不受版本控制，并且是特定于部署的。它是丢弃在运行时或配置文件中更改的东西的理想场所。

您可以在创建Flask应用程序时显式提供实例文件夹的路径，也可以让Flask自动检测实例文件夹。对于显式配置，请使用 *instance\_path* 参数：

```py

app = Flask(__name__, instance_path='/path/to/instance/folder')

```

请记住，提供时此路径必须是绝对的。

如果未提供 *instance\_path* 参数，则使用以下默认位置：

* 未安装模块：

```bash

/myapp.py
/instance

```

* 未安装包：

```bash

/myapp
    /__init__.py
/instance

```

* 已安装的模块或包装：

```bash

$PREFIX/lib/python2.X/site-packages/myapp
$PREFIX/var/myapp-instance

```

`$PREFIX`是Python安装的前缀。这可以是`/usr`或virtualenv的路径。您可以打印`sys.prefix`的值以查看前缀的设置。

由于配置对象提供了从相对文件名加载配置文件，因此我们可以通过文件名将加载更改为相对于实例路径（如果需要）。配置文件中相对路径的行为可以在“相对于应用程序根目录”（默认）到“相对于实例文件夹”之间通过 *instance\_relative\_config* 切换到应用程序构造函数：

```py

app = Flask(__name__, instance_relative_config=True)

```

下面是一个完整的示例，说明如何配置Flask以从模块预加载配置，然后从实例文件夹中的文件覆盖配置（如果存在）：

```py

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('yourapplication.default_settings')
app.config.from_pyfile('application.cfg', silent=True)

```

可以通过 **Flask.instance\_path** 找到实例文件夹的路径。Flask还提供了使用 **Flask.open\_instance\_resource()** 从实例文件夹中打开文件的快捷方式。

两者的示例用法：

```py

filename = os.path.join(app.instance_path, 'application.cfg')
with open(filename) as f:
    config = f.read()

# or via open_instance_resource:
with app.open_instance_resource('application.cfg') as f:
    config = f.read()
```
