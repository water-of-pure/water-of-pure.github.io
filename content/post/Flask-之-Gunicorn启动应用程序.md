+++
date = '2025-07-22T18:31:35.555111+08:00'
draft = false
title = 'Flask 之 Gunicorn启动应用程序'
categories = [
    "技术",

]

tags = [
    "Flask",
    "Gunicorn",
    "Python"
]
+++

Gunicorn的介绍我就不锁了，但是我这里简单记录一下我自己是如何使用Gunicorn的。

首先安装Gunicorn

```bash
pip install gunicorn
```

然后添加一下gunicorn的启动文件-gunicorn.conf

```bash
workers = 8
bind = '127.0.0.1:3041'
daemon = True
accesslog = './walkerfree/logs/access.log'
errorlog = './walkerfree/logs/error.log'  

```

上面的log路径可以根据自己的情况进行修改，bind的内容也是一样的

最后启动自己的web应用

```bash
gunicorn wsgi:application -c gunicorn.conf
```

到这里会有一个疑问是：wsgi:application，是这样的，首先创建一个wsgi文件，是的就是这个文件，这个跟python的包有关

```py
# _*_ coding=utf-8 _*_

from walkerfree import app
from walkerfree.config import config
from walkerfree import bootstrap
from walkerfree import mail
from walkerfree import moment
from walkerfree import db
from walkerfree import cache
from walkerfree import dispatch_handlers, register_blueprints, register_jinja_env, configure_assets, configure_logging

def create_app(config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    cache.init_app(app)

    dispatch_handlers(app)
    register_blueprints(app)
    register_jinja_env(app)
    configure_logging(app)
    configure_assets(app)

    return app

application = create_app('production')

if __name__ == '__main__':
    application.run()  

```

我这里的代码，是根据自己的情况定义的。
