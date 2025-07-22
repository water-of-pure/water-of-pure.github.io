+++
date = '2025-07-22T18:31:31.683949+08:00'
draft = false
title = 'Flask之更新表结构'
categories = [
    "技术",

]

tags = [
    "Flask",
    "Python"
]
+++

使用Flask的过程中，对于操作数据库这一块会用到Flask-SqlAlchemy,项目开始的时候是没有什么问题的，但是在后面由于业务需求会涉及到修改表的操作，那么问题来了，表的结构被修改之后，又如何才能同步到生产环境的数据库呢。

这里推荐使用一个Flask的插件-Flask-Migrage.下面掩饰一下如何去操作。

Flask-Migrate的安装：

```bash
pip install flask-migrate
```

创建app.py，代码如下：

```py
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

if __name__ == '__main__':
    manager.run()  

```

保存如何代码后，实行如下代码：

```bash
python app.py db init  

```

这个动作是说，初始化migrate需要的环境，接下来生成一个数据表操作的代码文件：

```bash
python app.py db migrate  

```

如果没有报错的话，会出现一系列的提示信息，这里具体情况不一样，我就不一列出来了。

如果上面执行后没有问题的话，就可以进行数据库表的更新了。

```bash
python app.py db upgrade  

```

执行上面的代码，就可以更新数据库表的结构了。
