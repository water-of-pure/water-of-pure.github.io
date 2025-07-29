+++
date = '2025-07-29T10:09:38.314566+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 定义和访问数据库'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

本教程的应用程序将使用SQLite数据库来存储用户和帖子，Python在sqlite3模块中内置了对SQLite的支持

SQLite是很方便的，因为他不需要设置单独的数据库服务器并且内置与Python中。然而如果并发请求同时试着写入数据，随着每次写入顺序发生，它们会变慢。

小应用程序不会注意到这一点。一旦变大，您可能希望切换到其他数据库。

本教程不会详细介绍SQL。如果您不熟悉它，SQLite文档会描述该[语言](https://sqlite.org/lang.html)。

## 连接数据库

使用SQLite数据库（以及大多数其他Python数据库）时要做的第一件事就是创建一个连接。使用连接执行任何查询和操作，该连接在工作完成后关闭。

在Web应用程序中，此连接通常与请求相关联。它在处理请求时在某个时刻创建，并在发送响应之前关闭。

baby/db.py

```py

#! _*_ coding: utf-8 _*_
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

```

[g](http://flask.pocoo.org/docs/1.0/api/#flask.g)是一个特殊对象，对每个请求都是唯一的。它用于存储请求期间可能由多个函数访问的数据。

如果在同一请求中第二次调用`get_db`，则会存储并重用连接，而不是创建新连接。

[current\_app](http://flask.pocoo.org/docs/1.0/api/#flask.current_app)是另一个指向处理请求的Flask应用程序的特殊对象。由于您使用的是应用程序工厂，因此在编写其余代码时没有应用程序对象。创建应用程序并处理请求时将调用`get_db`，因此可以使用[current\_app](http://flask.pocoo.org/docs/1.0/api/#flask.current_app)

[sqlite3.connect()](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect)建立与DATABASE配置键指向的文件的连接。此文件尚不存在，并且在您稍后初始化数据库之前不会存在。

[sqlite3.Row](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row)告诉连接返回行为类似于dicts的行。这允许按名称访问列。

`close_db`通过检查是否已设置`g.db`来检查是否创建了连接。如果连接存在，则关闭。再往下，您将告诉您的应用程序有关应用程序工厂中的`close_db`函数，以便在每次请求后调用它。

## 建表

在SQLite中，数据存储在*表*和*列*中。这些需要在存储和检索数据之前创建。Baby项目将用户存储在用户表中，并在post表中存储帖子。使用创建空表所需的SQL命令创建一个文件：

baby/schema.sql

```sql

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
)

```

将运行这些SQL命令的Python函数添加到db.py文件中：

baby/db.py

```py baby/db.py

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables"""
    init_db()
    click.echo('Initialized the database.')

```

[open\_resource()](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.open_resource)打开一个相对于`baby`包的文件，这很有用，因为在以后部署应用程序时你不一定知道该位置在哪里。`get_db`返回数据库连接，用于执行从文件读取的命令。

[click.command()](http://click.pocoo.org/api/#click.command)定义了一个名为`init-db`的命令行命令，该命令调用`init_db`函数并向用户显示成功消息。您可以[阅读命令行界面](http://flask.pocoo.org/docs/1.0/cli/#cli)以了解有关编写命令的更多信息。

## 注册应用程序

close\_db和init\_db\_command函数需要在应用程序中被注册，否则他们将不会被应用程序调用。但是，由于您使用的是工厂函数，因此在编写函数时该实例不可用。相反，编写一个接受应用程序并进行注册的函数。

baby/db.py

```py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

```

[app.teardown\_appcontext()](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.teardown_appcontext)告诉Flask在返回响应后清理时调用该函数。

[app.cli.add\_command()](http://click.pocoo.org/api/#click.Group.add_command)添加了一个可以使用flask命令调用的新命令。

从工厂导入并调用此功能。在返回应用程序之前，将新代码放在工厂函数的末尾。

baby/**init**.py

```py

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'baby.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/baby')
    def index():
        return 'Baby'

    # 新加
    from . import db
    db.init_app(app)

    return app

```

## 初始化数据库文件

现在已经在应用程序中注册了`init-db`，可以使用`flask`命令调用它，类似于上一节的`run`命令。

---

### 注意：

如果您仍在从上一页运行服务器，则可以停止服务器，也可以在新终端中运行此命令。如果您使用新终端，请记住更改到项目目录并激活env，如[激活环境](http://flask.pocoo.org/docs/1.0/installation/#install-activate-env)中所述。您还需要设置FLASK\_APP和FLASK\_ENV，如上一节所示。

---

运行`init-db`命令

```bash

flask init-db
Initialized the database

```

现在，项目中的实例文件夹中将有一个baby.sqlite文件。

下一期继续 - [Blueprint和视图](https://www.walkerfree.com/article/155)
