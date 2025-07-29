+++
date = '2025-07-29T10:09:23.583194+08:00'
draft = false
title = 'Flask 1.0 快速入手 【四】'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

## Sessions

除了请求对象之外，还有一个叫做[session](http://flask.pocoo.org/docs/1.0/api/#flask.session)的第二个对象，它允许您将特定于某个用户的信息从一个请求存储到下一个请求。这是在cookie的基础上实现的，并以加密方式对cookie进行签名。这意味着用户可以查看cookie的内容但不能修改它，除非他们知道用于签名的密钥。

要使用session的话，您必须设置一个密钥。以下是session的工作方式：

```py

from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = b'\xbc\xf6\x8aTP\xba\xe7\xf8*\xcc\xa7\xbe\xb2S\xd5\x83'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])

    return 'You are not logged in'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
		<form method="post">
			<p><input type='text' name='username' /></p>
			<p><input type='submit' value='Login' /></p>
		</form>
	'''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

```

如果你没有使用模板引擎（如本例所示），这里提到的[escape()](http://flask.pocoo.org/docs/1.0/api/#flask.escape)会为你做转义处理。

---

### 如何生成一个好一点的密钥

密钥应尽可能随机。您的操作系统可以基于加密随机生成器生成相当随机的数据。使用以下命令快速生成一个值给Flask.secret\_key (或者 [SECRET\_KEY](http://flask.pocoo.org/docs/1.0/config/#SECRET_KEY)):

```bash

$ python -c 'import os; print(os.urandom(16))'
b'\xbc\xf6\x8aTP\xba\xe7\xf8*\xcc\xa7\xbe\xb2S\xd5\x83'
```

---

关于基于cookie的会话的说明：Flask将获取您放入session对象的值，并将它们序列化为cookie。如果您发现某些值不会在请求中保留，则确实启用了Cookie，并且您没有收到明确的错误消息，请检查页面响应中的Cookie大小与Web浏览器支持的大小相比较。

除了默认的基于客户端的session，如果你想在服务器端处理session，有几个Flask扩展支持这个。

## 即时消息

好的应用和用户体验是关于反馈的，如果用户没有得到足够的反馈，他们可能最终会厌恶应用程序，Flask提供了一种使用即时系统向用户提供反馈的简单方法。即时系统基本上可以在请求结束时记录消息，并在下一个（也是下一个）请求中访问它。这通常与布局模板结合使用以显示消息。

要使用[flash()](http://flask.pocoo.org/docs/1.0/api/#flask.flash)方法添加一个即时消息，要获取即时消息，可以使用[get\_flashed\_messages()](http://flask.pocoo.org/docs/1.0/api/#flask.get_flashed_messages)的方法，这些消息也可以在模板中使用。查看[即时消息](http://flask.pocoo.org/docs/1.0/patterns/flashing/#message-flashing-pattern)以获取完整示例。

## 日志

有时您可能处理的数据应该是正确的，但事实并非如此。例如，您可能有一些客户端代码向服务器发送HTTP请求，但显然格式不正确。这可能是由用户篡改数据或客户端代码失败引起的。在大多数情况下，在这种情况下回复`400 Bad Request`是可以的，但有时不会这样做，而且代码必须继续工作。

您可能仍想记录发生了可疑的事情。这是loggers派上用场的地方。从Flask 0.3开始，预先配置了一个logger供您使用。

以下是一些日志调用示例：

```py

app.logger.debug('A value for debuging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('A error occurred')

```

附加自带的[logger](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.logger)是标准的[Logger](https://docs.python.org/3/library/logging.html#logging.Logger)，因此请访问官方[logging文档](https://docs.python.org/library/logging.html)以获取更多信息。

详细了解[应用程序错误](http://flask.pocoo.org/docs/1.0/errorhandling/#application-errors)

## 挂钩WSGI中间件

如果要将WSGI中间件添加到应用程序，可以包装内部WSGI应用程序。例如，如果你想使用Werkzeug包中的一个中间件来处理lighttpd中的bug，你可以这样做

```py

from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)

```

## 使用Flask Extensions

扩展程序是帮助您完成常见任务的程序包。例如，Flask-SQLAlchemy提供SQLAlchemy支持，使其易于与Flask一起使用。

有关Flask扩展的更多信息，请查看[扩展](http://flask.pocoo.org/docs/1.0/extensions/#extensions)。

## 部署到Web服务器

准备部署新的Flask应用了吗？转到“[部署选项](http://flask.pocoo.org/docs/1.0/deploying/#deployment)”。
