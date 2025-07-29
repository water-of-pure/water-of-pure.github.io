+++
date = '2025-07-29T10:55:35.937407+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 部署到生产环境'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

这部分假设你有一台可以部署你应用的服务器，它概述了如何创建分发文件并进行安装，但不会详细介绍要使用的服务器或软件。您可以在开发计算机上设置新环境以尝试以下说明，但可能不应将其用于托管真实的公共应用程序。有关托管应用程序的许多不同方法的列表，请参阅[部署选项](http://flask.pocoo.org/docs/1.0/deploying/)。

### 构建和安装

如果要在其他位置部署应用程序，可以构建分发文件。Python发行版的当前标准是*wheel*格式，扩展名为.whl。确保首先安装了wheel库。

```bash

pip install wheel

```

使用Python运行`setup.py`为您提供了一个命令行工具来发出与构建相关的命令。bdist\_wheel命令将构建一个wheel分配文件。

```bash

python setup.py bdist_wheel

```

运行完之后，将会在目录dist下发现一个文件`baby-1.0.0-py3-none-any.whl`。文件名是项目的名称，版本以及有关该文件的一些标记可以安装。

将此文件复制到另一台计算机，[设置一个新的virtualenv](http://flask.pocoo.org/docs/1.0/installation/#install-create-env)，然后使用pip安装该文件。

```bash

pip install baby-1.0.0-py3-none-any.whl

```

Pip将安装您的项目及其依赖项。

由于这是一台不同的机器，因此需要再次运行`init-db`以在instance文件夹中创建数据库。

```bash

export FLASK_APP=baby
flask init-db

```

当Flask检测到它已安装（不是可编辑模式）时，它会为instance文件夹使用不同的目录。你可以在`venv/var/baby-instance`找到它。

### 配置私钥（Secret Key）

在本教程的第一篇分享中，为SECRET\_KEY提供了默认值。生产环境中应该改为一些随机字节。否则，攻击者可以使用公共“dev”密钥来修改会话cookie或使用密钥的任何其他内容。

您可以使用以下命令输出随机密钥：

```bash

python -c 'import os; print(os.urandom(16))'
b'\x05\x81\xb5\xa2xln&\\\xb8\xda\xecY\x94\xef\xb5'

```

在instance文件夹中创建config.py文件，如果存在，工厂将从中读取该文件。将生成的值复制到其中。

venv/var/baby-instance/config.py

```bash

SECRET_KEY=b'\x05\x81\xb5\xa2xln&\\\xb8\xda\xecY\x94\xef\xb5'

```

你也可以在这里设置任何其他必要的配置，虽然SECRET\_KEY是Baby唯一需要的配置。

### 运行生产环境服务器

在生产环境中而不是在开发环境中运行时，不应使用内置开发服务器（`flask run`）。开发服务器由Werkzeug提供以方便使用，但其设计不是特别高效，稳定或安全。

而是使用生产WSGI服务器。例如，要使用[Waitress](https://docs.pylonsproject.org/projects/waitress/)，请先在虚拟环境中安装它：

```bash

pip install waitress

```

您需要告诉Waitress您的应用程序，但它不像Flask运行那样使用FLASK\_APP。您需要告诉它导入并调用应用程序工厂以获取应用程序对象。

```bash

waitress-serve --call 'baby:create_app'
Serving on http://0.0.0.0:8080

```

有关托管应用程序的许多不同方法的列表，请参阅[部署选项](http://flask.pocoo.org/docs/1.0/deploying/)。Waitress只是一个例子，因为它同时支持Windows和Linux。您可以为项目选择更多WSGI服务器和部署选项。

下一期继续 - [继续开发](https://www.walkerfree.com/article/162)！
