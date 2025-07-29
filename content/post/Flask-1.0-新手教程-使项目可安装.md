+++
date = '2025-07-29T10:09:53.865913+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 使项目可安装'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

使项目可安装意味着您可以构建分发文件并将其安装在另一个环境中，就像在项目环境中安装Flask一样。这使得部署项目与安装任何其他库相同，因此您使用所有标准Python工具来管理所有内容。

安装还带来了其他一些好处，这些好处可能在教程中或作为新的Python用户不明显，包括：

* 目前，Python和Flask只了解如何使用baby包，因为你是从项目目录运行的。安装意味着无论您从何处运行，都可以导入它。
* 您可以像管理其他软件包一样管理项目的依赖项，因此请安装yourproject.whl安装它们。
* 测试工具可以将您的测试环境与开发环境隔离开来。

---

### 注意

这是在本教程后期介绍的，但是在您将来的项目中，您应该始终从这开始。

---

## 项目描述

setup.py文件描述了您的项目以及属于它的文件。

setup.py

```py

#! _*_ coding: utf-8 _*_

from setuptools import find_packages, setup

setup(
    name='baby',
    version='1.0.0',
    author='张大鹏',
    author_email='[email protected]',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask'
    ]
)

```

`packages`告诉Python要包含哪些包目录（以及它们包含的Python文件）。`find_packages()`自动查找这些目录，因此您不必键入它们。要包含其他文件，例如static和templates目录，请设置`include_package_data`。Python需要另一个名为`MANIFEST.in`的文件来告诉其他数据是什么。

MANIFEST.in

```bash

include baby/schema.sql
graft baby/static
graft baby/templates
global-exclude *.pyc

```

这告诉Python复制`static`和`template`目录以及`schema.sql`文件中的所有内容，但要排除所有字节码文件。

有关所用文件和选项的其他说明，请参阅[官方包装指南](https://packaging.python.org/tutorials/distributing-packages/)。

## 安装项目

使用pip在虚拟环境中安装项目。

```bash

pip install -e .

```

这告诉pip在当前目录中找到setup.py并将其安装在可编辑或开发模式下。可编辑模式意味着当您对本地代码进行更改时，如果更改有关项目的元数据（例如其依赖项），则只需重新安装。

您可以观察到项目现在已安装了`pip list`。

```bash

$ pip list
Package           Version Location
----------------- ------- -------------------------
astroid           2.2.5
atomicwrites      1.3.0
attrs             19.1.0
autopep8          1.4.3
baby              1.0.0   /Users/durban/python/baby
Click             7.0
coverage          4.5.3
Flask             1.0.2
gunicorn          19.9.0
isort             4.3.16
itsdangerous      1.1.0
Jinja2            2.10
lazy-object-proxy 1.3.1
MarkupSafe        1.1.1
mccabe            0.6.1
more-itertools    7.0.0
pip               19.1.1
pluggy            0.9.0
py                1.8.0
pycodestyle       2.5.0
pylint            2.3.1
pytest            4.4.0
setuptools        39.0.1
six               1.12.0
typed-ast         1.3.1
waitress          1.2.1
Werkzeug          0.15.1
wheel             0.33.1
wrapt             1.11.1

```

到目前为止，您运行项目的方式没有任何变化。`FLASK_APP`仍然设置为`baby`并且`flask run`仍然运行应用程序。

下一期继续 - [测试覆盖率](https://www.walkerfree.com/article/160)
