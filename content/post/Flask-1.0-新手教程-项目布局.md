+++
date = '2025-07-29T10:09:32.017330+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 项目布局'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

首先创建一个目录，并进入到目录里面

```bash

mkdir baby
cd baby

```

然后参考[安装说明](https://www.walkerfree.com/article/146/)来设置Python虚拟环境并且为项目安装Flask

本教程假设您从现在开始使用baby目录，每个代码块顶部的文件名都与该目录相关。

---

Flask应用程序可以像单个文件一样简单。

hello.py

```py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

```

然而随着项目越来复杂，所有代码放在一个文件将会变得越来越臃肿。Python项目使用包将代码组织成多个模块，可以在需要的地方导入，本教程也会这样做。

本教程项目目录将会包括如下内容：

* `baby/`，一个包含应用程序代码和文件的Python包
* `tests/`，一个包含测试模块的目录
* `.env3`，一个Flask和其他依赖库被安装的Python虚拟环境
* 安装文件告诉Python如何安装项目。
* 版本控制配置，例如git。您应养成给所有项目使用某种类型的版本控制的习惯，无论大小如何。
* 您将来可能添加的任何其他项目文件

最后，您的项目布局将如下所示：

```bash

/Users/durban/python/baby
├── tests
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_blog.py
│   ├── test_auth.py
│   ├── data.sql
│   └── conftest.py
├── setup.py
├── setup.cfg
├── gunicorn.example.conf
├── gunicorn.conf
├── baby
│   ├── templates
│   │   ├── blog
│   │   │   ├── update.html
│   │   │   ├── index.html
│   │   │   └── create.html
│   │   ├── base.html
│   │   └── auth
│   │       ├── register.html
│   │       └── login.html
│   ├── static
│   │   └── app.css
│   ├── schema.sql
│   ├── db.py
│   ├── blog.py
│   ├── auth.py
│   └── __init__.py
├── README.md
└── MANIFEST.in

```

如果你使用了版本控制，应忽略在运行项目时生成的以下文件。根据您使用的编辑器，可能还有其他文件。通常，忽略您未编写的文件。例如，使用git：

.gitignore

```bash

.env3/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/

```

下一期继续 - [应用程序设置](https://www.walkerfree.com/article/153)
