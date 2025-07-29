+++
date = '2025-07-29T10:09:19.608913+08:00'
draft = false
title = 'Flask 1.0 快速入手 【三】'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1557969152/walkerfree/wf_149.jpg"
+++

## Cookies

你可以通过[cookies](http://flask.pocoo.org/docs/1.0/api/#flask.Request.cookies)这个属性来访问到cookies，可以使用响应对象的[set\_cookie](http://flask.pocoo.org/docs/1.0/api/#flask.Response.set_cookie)方法来设置cookies。请求对象的[cookies](http://flask.pocoo.org/docs/1.0/api/#flask.Request.cookies)属性是一个字典类型，它包含了所有从客户端传递过来的cookies数据。如果你想使用cookies，不要直接使用cookies，而是使用Flask中的[Sessions](http://flask.pocoo.org/docs/1.0/quickstart/#sessions)，它为您在cookies的上一层添加了一些安全的处理。

读取cookies

```py

from flask import request

@app.route('/')
def index()：
    username = request.cookies.get('username')
    # 为了避免键值不存在的情况，使用cookies.get(key)替换cookies[key]

```

存储cookies

```py

from flask import make_response

@app.route('/')
def index():
    resp = make_response(render_template('....'))
    resp.set_cookie('username', 'the other username')
    return resp

```

请注意，cookies是在响应对象中设置的。由于我们通常只是从视图函数返回字符串，Flask会为你将它们转换为响应对象。如果您明确要这样做，可以使用make\_response()函数然后修改它。

有时您可能希望在响应对象尚不存在的位置设置cookie，这可以通过使用[延迟请求回调](http://flask.pocoo.org/docs/1.0/patterns/deferredcallbacks/#deferred-callbacks)模式来实现。

为此，请参阅[关于响应](http://flask.pocoo.org/docs/1.0/quickstart/#about-responses)。

## 重定向和错误

将用户重定向到另一个端点，使用[redirect()](http://flask.pocoo.org/docs/1.0/api/#flask.redirect)函数。用一个错误代码提前中止请求，使用[abort()](http://flask.pocoo.org/docs/1.0/api/#flask.abort)函数。

```py

from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()

```

这是一个毫无意义的例子，因为它将一个用户从index页面重定向到了一个不能访问的401页面，但是这个例子演示了如何使用的。

默认情况下，每一个错误码都会显示一个黑白的错误页面，如果你想自定义这个错误页面，可以使用[errorhandler()](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.errorhandler)装饰器

```py

from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', error=error), 404

```

请注意[render\_template()](http://flask.pocoo.org/docs/1.0/api/#flask.render_template)调用后的`404`。这将告诉Flask页面的状态码是404，404意味着页面不存在。默认情况下，页面状态码为200，意思是：一切正常。

有关详细信息，请参阅[错误处理程序](http://flask.pocoo.org/docs/1.0/errorhandling/#error-handlers)

## 关于响应

视图函数返回的值被自动转换为一个响应对象。如果返回值是一个字符串，它将被转换为一个带有该字符串的响应对象作为响应体，状态码200和一个text/htmlMIME类型。Flask转换返回值为一个响应对象的逻辑如下：

1. 如果返回一个正确类型的响应对象，这个响应对象将会从视图函数直接返回。
2. 如果返回一个字符串，一个影响对象将携带改字符串和默认的参数被创建。
3. 如果返回元组，则元组中的项可以提供额外信息。这样的元组必须采用`(response, status, headers)`或`(response, headers)`的形式，其中至少有一个项目必须在元组中。`status`值将覆盖状态代码，`headers`可以是其他标头值的列表或字典。
4. 如果这些都不起作用，Flask将假定返回值是有效的WSGI应用程序并将其转换为响应对象。

如果要在视图中获取生成的响应对象，可以使用[make\_response()](http://flask.pocoo.org/docs/1.0/api/#flask.make_response)函数。

假如你有一个像下面这样的视图

```py

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', 404)

```

您只需要使用[make\_response()](http://flask.pocoo.org/docs/1.0/api/#flask.make_response)包装返回表达式并获取响应对象以对其进行修改，然后将其返回：

```py

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```
