+++
date = '2025-07-29T10:55:51.977918+08:00'
draft = false
title = 'Flask 1.0 进阶 - 日志'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

Flask使用标准的Python日志记录。所有与Flask相关的消息都记录在'flask'记录器命名空间下。Flask.logger返回名为“flask.app”的记录器，可用于记录应用程序的消息。

```py

from flask import current_app

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
            current_app.logger.info('%s logged fail', username)
        elif not check_password_hash(user['password'], password):
            app.logger.info('%s logged fail', username)
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            current_app.logger.info('%s logged successfully', username)
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('auth/login.html')

```

## 基础配置

如果要为项目配置日志记录，则应在程序启动时尽快执行。如果在配置日志记录之前访问 [**app.logger**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.logger) ，它将添加默认处理程序。如果可能，在创建应用程序对象之前配置日志记录

此示例使用 [**dictConfig()**](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig) 创建类似于Flask默认的日志记录配置，但所有日志除外：

```py

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s \
in %(module)s: %(message)s ',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

```

## 默认配置

如果您没有自己配置日志记录，Flask会自动将一个 [**StreamHandler**](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler) 添加到 [**app.logger**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.logger) 。在请求期间，它将在`environ ['wsgi.errors']`（通常是 [**sys.stderr**](https://docs.python.org/3/library/sys.html#sys.stderr) ）中写入由WSGI服务器指定的流。在请求之外，它将记录到 [**sys.stderr**](https://docs.python.org/3/library/sys.html#sys.stderr) 。

## 移除默认的Handler

如果您在访问 [**app.logger**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.logger) 后配置了日志记录，并且需要删除默认处理程序，则可以导入和删除它：

```py

from flask.logging import default_handler

app.logger.removeHandler(default_handler)

```

## 向管理员发送电子邮件错误

在远程服务器上运行应用程序进行生产时，您可能不会经常查看日志消息。WSGI服务器可能会将日志消息发送到文件，如果用户告诉您出错，只要检查该文件就可以了。

要主动发现和修复错误，您可以配置 [**logging.handlers.SMTPHandler**](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler) 以在记录错误和更高错误时发送电子邮件。

```py

import logging
from logging.handlers import SMTPHandler

mail_handler = SMTPHandler(
    (
        'server',
        'server_port'
    ),
    fromaddr='[email protected]',
    toaddrs=['[email protected]'],
    subject='Application Error',
    (
        'username',
        'password'
    )
)

mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s \
in %(module)s: %(message)s '))

if not app.debug:
    app.logger.addHandler(mail_handler)

```

这要求您在同一服务器上设置SMTP服务器。有关配置处理程序的更多信息，请参阅Python文档。

## 注入请求信息

查看有关请求的更多信息（例如IP地址）可能有助于调试某些错误。您可以将 [**logging.Formatter**](https://docs.python.org/3/library/logging.html#logging.Formatter) 子类化为注入可以在消息中使用的自己的字段。您可以更改Flask的默认处理程序，上面定义的邮件处理程序或任何其他处理程序的格式化程序。

```py

from flask.logging import default_handler

from flask import (
    has_request_context,
    request
)

def logging_common_formatter():
    class RequestFormatter(logging.Formatter):

        def format(self, record):
            if has_request_context():
                record.url = request.url
                record.remote_addr = request.remote_addr
            else:
                record.url = None
                record.remote_addr = None

            return super().format(record)

    formatter = RequestFormatter(
        '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
        '%(levelname)s in %(module)s: %(message)s'
    )

    return formatter

formatter = logging_common_formatter()
mail_handler.setFormatter(formatter)
default_handler.setFormatter(formatter)

```

## 其他库

其他库可能会广泛使用日志记录，您也希望从这些日志中查看相关消息。最简单的方法是将处理程序添加到root记录器而不是仅添加应用程序记录器。

```py

from flask.logging import default_handler

root = logging.getLogger()
root.addHandler(default_handler)
root.addHandler(mail_handler)

```

根据您的项目，配置您关注的每个记录器可能更有用，而不是仅配置root记录器。

```py

for logger in (
    app.logger,
    logging.getLogger('sqlalchemy'),
    logging.getLogger('other_package'),
):
    logger.addHandler(default_handler)
    logger.addHandler(mail_handler)

```

## Werkzeug

Werkzeug将基本请求/响应信息记录到`'werkzeug'`记录器。如果root记录器没有配置处理程序，Werkzeug会将 [**StreamHandler**](https://docs.python.org/3/library/logging.handlers.html#logging.StreamHandler) 添加到其记录器中。

## Flask扩展

根据具体情况，扩展程序可以选择记录到app.logger或其自己的命名记录程序。有关详细信息，请参阅每个扩展的文档。
