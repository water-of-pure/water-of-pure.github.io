+++
date = '2025-07-29T10:09:10.039707+08:00'
draft = false
title = 'Flask 1.0 - 安装'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1555568104/walkerfree/wf_146.jpg"
+++

## Python版本要求

Flask从1.0开始支持Python 3，Flask支持Python 3.4和最新版本，以及Python 2.7和PyPy，同时官方建议使用Python 3的最新版本，由此可以看出Flask 从1.0开始拥抱Python 3

## 包依赖

* [Werkzeug](http://werkzeug.pocoo.org/) 实现WSGI，它是应用程序和服务器之间的标准Python接口
* [Jinja](http://jinja.pocoo.org/) 一种模板语言，用于呈现应用程序所服务的页面
* [MarkupSafe](https://pypi.org/project/MarkupSafe/) 附带Jinja. 它在渲染模板时逃避不受信任的输入以避免注入攻击。
* [ItsDangerous](https://pythonhosted.org/itsdangerous/) 安全地签署数据以确保其完整性。这用于保护Flask的会话cookie。
* [Click](http://click.pocoo.org/) 是一个用于编写命令行应用程序的框架。它提供flask命令并允许添加自定义管理命令。

这些包会在安装Flask后自动安装

## 其他可选包

* [Blinker](https://pythonhosted.org/blinker/) 为[Signals](http://flask.pocoo.org/docs/1.0/signals/#signals)提供支持.
* [SimpleJSON](https://simplejson.readthedocs.io/) 是一个快速的JSON实现，与Python的json模块兼容。如果安装了JSON操作，则首选它。
* [python-dotenv](https://github.com/theskumar/python-dotenv#readme) 在运行flask命令时启用对 [dotenv的环境变量](http://flask.pocoo.org/docs/1.0/cli/#dotenv) 的支持。
* [Watchdog](https://pythonhosted.org/watchdog/) 为开发服务器提供更快，更高效的重新加载器。

以上的可选包不会自动安装，不过，如果你安装了的话，Flask将自动监测并使用他们

## 虚拟环境

建议在开发和生产中使用虚拟环境来管理你项目的依赖库。

虚拟环境能解决什么问题呢？如果你拥有Python的项目越多，你需要使用不同版本的Python库的可能性就越大，甚至是Python本身。一个较新版本的Python库可能会打破另一个项目的兼容性

虚拟环境是独立的Python库组合，每个项目一个。一个项目安装的软件包不会影响其他项目或操作系统的软件包。

Python 3已经绑定了[venv](https://docs.python.org/3/library/venv.html#module-venv)模块用来创建虚拟环境。如果你使用的是Python 3，可以继续下面的操作。

如果你使用的是Python 2，首先先看下“安装virtualenv”

### 创建虚拟环境

创建一个项目目录然后添加一个.venv\_baby文件夹，当然这个文件夹你也可以根据自己的需要来定义：

```bash

mkdir baby
cd baby
python3 - venv .venv_baby

```

Windows环境下的操作

```bash

py -3 -m venv .venv_baby

```

如果您使用的是旧版本的Python，您需要安装virtualenv，请使用一下命令：

```bash

virtualenv .venv_baby

```

Windows环境下的操作

```bash

\Python27\Scripts\virtualenv.exe .venv_baby

```

### 激活环境

在你的项目中工作前，激活相应的环境

```bash

. .venv_baby/bin/activate

```

在Windows环境下

```bash

.venv_baby\Scripts\activate

```

你的shell提示中将显示激活环境的名称

## 安装Flask

在激活的环境中使用下面的命令安装Flask

```bash

pip install Flask

```

如果您希望在发布之前使用最新的Flask代码，请安装或更新主分支中的代码：

```bash

pip install -U https://github.com/pallets/flask/archive/master.tar.gz

```

## 安装virtualenv

如果你使用的是Python 2，venv模块是不可用的，因此需要安装virtualenv 在Linux系统中，virtualenv由包管理器提供

```bash

# Debian, Ubuntu
sudo apt-get install python-virtualenv

# CentOS, Fedora
sudo yum install python-virtualenv

# Arch
sudo pacman -S python-virtualenv

```

如果你的系统是Mac OS或者Windows，先下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)，然后执行下面的代码

```bash

sudo python2 Downloads/get-pip.py
sudo python2 -m pip install virtualenv

```

在Windows系统上，已administrator的身份执行

```bash

\Python27\python.exe Downloads\get-pip.py
\Python27\python.exe -m pip install virtualenv

```

现在返回到上面的“创建虚拟环境”.
