+++
date = '2025-07-29T10:55:45.491821+08:00'
draft = false
title = 'Flask 1.0 进阶 - 测试Flask应用程序'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

"未经测试的东西被打破了"

这句话的起源是未知的，虽然它并不完全正确，但它也离真相不远。未经测试的应用程序使得现有代码难以改进，未经测试的应用程序的开发人员往往变得非常偏执。如果应用程序具有自动化测试，您可以安全地进行更改，并立即知道是否有任何中断。

Flask提供了一种方法来测试您的应用程序，方法是暴露Werkzeug测试[**Client**](http://werkzeug.pocoo.org/docs/test/#werkzeug.test.Client)并为您处理上下文本地。然后，您可以将其与您喜欢的测试解决方案一起使用。

在本分享中，我们将使用[pytest](https://pytest.org/)包作为测试的基础框架。您可以使用pip安装它，如下所示：

```bash

pip install pytest

```

### 应用程序

首先，我们需要一个应用程序来测试;我们将使用[教程](http://flask.pocoo.org/docs/1.0/tutorial/#tutorial)中的应用程序。如果您还没有该应用程序，请从[示例中](https://github.com/durban89/flask-baby)获取源代码。

### 测试骨架搭建

我们首先在应用程序根目录下添加一个tests目录(如果有的话可以不用创建)。然后创建一个Python文件来存储我们的测试（`test_baby.py`）。当我们格式化文件名如`test_*.py`时，它将被pytest自动发现。

接下来，我们创建一个名为 **client()** 的[pytest fixture](https://docs.pytest.org/en/latest/fixture.html)，它配置应用程序以进行测试并初始化一个新的数据库，代码如下：

```py

#! _*_ coding: utf-8 _*_
#
#

import os
import tempfile
import pytest
from baby import create_app
from baby.db import init_db, get_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'DATABASE': db_path,
        'TESTING': True
    })

    client = app.test_client()

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

```

每个单独的测试将调用此client fixture。它为我们提供了一个简单的应用程序接口，我们可以在其中触发对应用程序的测试请求。client还将为我们跟踪cookie。

在设置过程中，TESTING配置标志被激活。这样做是在请求处理期间禁用错误捕获，以便在对应用程序执行测试请求时获得更好的错误报告。

因为SQLite3是基于文件系统的，所以我们可以轻松地使用[**tempfile**](https://docs.python.org/3/library/tempfile.html#module-tempfile)模块来创建临时数据库并对其进行初始化。[**mkstemp()**](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp)函数为我们做了两件事：它返回一个低级文件句柄和一个随机文件名，后者我们用作数据库名。我们必须保持db\_fd，以便我们可以使用 **os.close()** 函数来关闭文件。

要在测试后删除数据库，fixture会关闭文件并将其从文件系统中删除。

如果我们现在运行测试组件，我们应该看到以下输出：

```bash

$ pytest tests/test_baby.py
======================================== test session starts ======================================
platform darwin -- Python 3.6.5, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
rootdir: /Users/durban/python/baby, inifile: setup.cfg
collected 0 items

==================================== no tests ran in 0.05 seconds =================================

```

即使它没有运行任何实际测试，我们已经知道我们的flaskr应用程序在语法上是有效的，否则导入将因异常而结束。

### 测试数据库

现在是时候开始测试应用程序的功能了。如果我们访问应用程序的根目录（/），让我们检查应用程序是否显示“Baby”。为此，我们向test\_baby.py添加了一个新的测试函数，如下所示：

```py

def test_empty_db(client):
    rv = client.get('/')
    assert b'Baby' in rv.data

```

请注意，我们的测试函数以单词test开头;这允许pytest自动将函数识别为要运行的测试。

通过使用`client.get`，我们可以使用给定路径向应用程序发送HTTP `GET`请求。返回值将是[**response\_class**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.response_class)对象。我们现在可以使用[**data**](http://werkzeug.pocoo.org/docs/wrappers/#werkzeug.wrappers.BaseResponse.data)属性来检查应用程序的返回值（作为字符串）。在这种情况下，我们确保“No entries here so far”是输出的一部分。

再次运行它，您应该看到一个通过测试：

```bash

$ pytest -v tests/test_baby.py
======================= test session starts ========================
platform darwin -- Python 3.6.5, pytest-4.4.0, py-1.8.0, pluggy-0.9.0 -- /Users/durban/python/baby/.env3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/durban/python/baby, inifile: setup.cfg
collected 1 item

tests/test_baby.py::test_empty_db PASSED                     [100%]

===================== 1 passed in 0.10 seconds =====================

```

### 测试登录和注销

我们的应用程序的大部分功能仅适用于管理用户，因此我们需要一种方法来将我们的测试客户端记录到应用程序中。为此，我们使用所需的表单数据（用户名和密码）向登录和注销页面发出一些请求。并且由于登录和注销页面重定向，我们告诉客户端follow\_redirects

将以下类添加到test\_baby.py文件中：

```py

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

```

现在，我们可以轻松地测试登录和注销是否正常工作，以及它是否因无效凭据而失败。添加这个新的测试功能：

```py

def test_login(client, auth):
    auth.login('test', 'test')
    with client:
        client.get('/')
        assert session['user_id'] == 1

    rv = auth.login('testx', 'test')
    print(rv.data)
    assert b'Incorrect username' in rv.data

    rv = auth.login('test', 'testx')
    print(rv.data)
    assert b'Incorrect password' in rv.data

def test_logout(client, auth):
    auth.login('test', 'test')
    with client:
        rv = auth.logout()
        assert 'user_id' not in session

```

再次运行测试得到如下结果

```bash

$ pytest -v tests/test_baby.py
=========================== test session starts ============================
platform darwin -- Python 3.6.5, pytest-4.4.0, py-1.8.0, pluggy-0.9.0 -- /Users/durban/python/baby/.env3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/durban/python/baby, inifile: setup.cfg
collected 3 items

tests/test_baby.py::test_empty_db PASSED                             [ 33%]
tests/test_baby.py::test_login PASSED                                [ 66%]
tests/test_baby.py::test_logout PASSED                               [100%]

========================= 3 passed in 0.71 seconds =========================

```

### 测试添加帖子

我们还应该测试添加帖子是否有效。添加一个新的测试函数，如下所示：

```py

def test_add_post(client, auth):
    auth.login()
    with client:
        rv = client.post('/create', data=dict(
            title='<Hello>',
            body='<strong>Html</strong> is here'
        ), follow_redirects=True)

        assert b'&lt;strong&gt;Html&lt;/strong&gt; is here' in rv.data

        assert b'&lt;Hello&gt;' in rv.data

```

在这里，我们检查文本中是否允许HTML，而不是标题中的HTML，这是预期的行为。

运行它现在应该给我们四个通过测试：

```bash

$ pytest -v tests/test_baby.py
=================== test session starts ====================
platform darwin -- Python 3.6.5, pytest-4.4.0, py-1.8.0, pluggy-0.9.0 -- /Users/durban/python/baby/.env3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/durban/python/baby, inifile: setup.cfg
collected 4 items

tests/test_baby.py::test_empty_db PASSED             [ 25%]
tests/test_baby.py::test_login PASSED                [ 50%]
tests/test_baby.py::test_logout PASSED               [ 75%]
tests/test_baby.py::test_add_post PASSED             [100%]

================= 4 passed in 0.71 seconds =================

```

### 其他测试技巧

除了使用如上所示的测试client之外，还有[**test\_request\_context()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_request_context)方法，该方法可以与`with`语句结合使用以临时激活请求上下文。通过这种方式，您可以访问[**request**](http://flask.pocoo.org/docs/1.0/api/#flask.request)，[**g**](http://flask.pocoo.org/docs/1.0/api/#flask.g)和[**session**](http://flask.pocoo.org/docs/1.0/api/#flask.session)对象，例如视图函数。以下是演示此方法的完整示例：

```py

import flask

app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    assert flask.request.path == '/'
    assert flask.request.args['name'] == 'Peter'

```

可以以相同的方式使用上下文绑定的所有其他对象。

如果要使用不同的配置测试应用程序并且似乎没有好的方法，请考虑切换到应用程序工厂（请参阅[应用程序工厂](http://flask.pocoo.org/docs/1.0/patterns/appfactories/#app-factories)）。

但请注意，如果使用测试请求上下文，则不会自动调用[**before\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.before_request)和[**after\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.after_request)函数。但是，当测试请求上下文离开`with`块时，确实执行了[**teardown\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.teardown_request)函数。如果你确实想要调用[**before\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.before_request)函数，你需要自己调用[**preprocess\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.preprocess_request)：

```py

app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    app.preprocess_request()
    ...

```

根据应用程序的设计方式，这可能是打开数据库连接或类似连接所必需的。

如果要调用[**after\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.after_request)函数，则需要调用[**preprocess\_request()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.preprocess_request)，但是要求您将响应对象传递给它：

```py

app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    resp = Response('...')
    resp = app.process_response(resp)
    ...

```

这通常不太有用，因为此时您可以直接开始使用测试客户端。

### 伪造资源和上下文

一种非常常见的模式是在应用程序上下文或flask.g对象上存储用户授权信息和数据库连接。一般的模式是在第一次使用时将对象放在那里，然后在拆卸时将其移除。想象一下这个代码来获取当前用户：

```py

def get_user():
    user = getattr(g, 'user', None)
    if user is None:
        user = fetch_current_user_from_database()
        g.user = user
    return user

```

对于测试，从外部覆盖此用户而不必更改某些代码将是很好的。这可以通过挂钩[flask.appcontext\_pushed](http://flask.pocoo.org/docs/1.0/api/#flask.appcontext_pushed)信号来完成：

```py

from contextlib import contextmanager
from flask import appcontext_pushed, g

@contextmanager
def user_set(app, user):
    def handler(sender, **kwargs):
        g.user = user
    with appcontext_pushed.connected_to(handler, app):
        yield

```

然后想下面这样使用它

```py

from flask import json, jsonify

@app.route('/users/me')
def users_me():
    return jsonify(username=g.user.username)

with user_set(app, my_user):
    with app.test_client() as c:
        resp = c.get('/users/me')
        data = json.loads(resp.data)
        self.assert_equal(data['username'], my_user.username)

```

### 保持上下文环境

有时触发常规请求保持上下文环境会有所帮助，但仍会将上下文保持一段时间，以便进行额外的内省。使用Flask 0.4，可以使用带有`with`块的[**test\_client()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_client)：

```py

app = flask.Flask(__name__)

with app.test_client() as c:
    rv = c.get('/?tequila=42')
    assert request.args['tequila'] == '42'

```

如果您只使用不带with块的[**test\_client()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_client)，则断言将失败并显示错误，因为请求不再可用（因为您尝试在实际请求之外使用它）。

### 访问和修改会话

有时，从测试客户端访问或修改会话非常有用。通常有两种方法。如果您只是想确保某个会话将某些键设置为某些值，您可以保持上下文并访问[**flask.session**](http://flask.pocoo.org/docs/1.0/api/#flask.session)：

```py

with app.test_client() as c:
    rv = c.get('/')
    assert flask.session['foo'] == 42

```

但是，这无法在发出请求之前修改会话或访问会话。从Flask 0.8开始，我们提供了一个所谓的“会话事务”，它模拟在测试客户端上下文中打开会话的相应调用并对其进行修改。在事务结束时存储会话。这与所使用的会话后端无关：

```py

with app.test_client() as c:
    with c.session_transaction() as sess:
        sess['a_key'] = 'a value'

    # once this is reached the session was stored

```

请注意，在这种情况下，您必须使用sess对象而不是flask.session代理。然而，对象本身将提供相同的接口。

### 测试JSON API

Flask非常支持JSON，是构建JSON API的流行选择。使用JSON数据发出请求并检查响应中的JSON数据非常方便：

```py

from flask import request, jsonify

@app.route('/api/auth')
def auth():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return jsonify(token=generate_token(email, password))

with app.test_client() as c:
    rv = c.post('/api/auth', json={
        'username': 'flask', 'password': 'secret'
    })
    json_data = rv.get_json()
    assert verify_token(email, json_data['token'])

```

在测试客户端方法中传递`json`参数将请求数据设置为JSON序列化对象，并将内容类型设置为`application/json`。您可以使用`get_json`从请求或响应中获取JSON数据。

### 测试CLI命令

Click附带了用于测试CLI命令的实用程序。CliRunner独立运行命令并捕获[**Result**](http://click.pocoo.org/api/#click.testing.Result)对象中的输出。

Flask提供了[**test\_cli\_runner()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_cli_runner)来创建[**FlaskCliRunner**](http://flask.pocoo.org/docs/1.0/api/#flask.testing.FlaskCliRunner)，它自动将Flask应用程序传递给CLI。使用其[**invoke()**](http://flask.pocoo.org/docs/1.0/api/#flask.testing.FlaskCliRunner.invoke)方法以与从命令行调用命令相同的方式调用命令。

```py

import click

@app.cli.command('hello')
@click.option('--name', default='World')
def hello_command(name)
    click.echo(f'Hello, {name}!')

def test_hello():
    runner = app.test_cli_runner()

    # invoke the command directly
    result = runner.invoke(hello_command, ['--name', 'Flask'])
    assert 'Hello, Flask' in result.output

    # or by name
    result = runner.invoke(args=['hello'])
    assert 'World' in result.output

```

在上面的示例中，按名称调用命令很有用，因为它验证命令是否已正确注册到应用程序。

如果要测试命令如何解析参数而不运行命令，请使用其make\_context()方法。这对于测试复杂的验证规则和自定义类型很有用。

```py

def upper(ctx, param, value):
    if value is not None:
        return value.upper()

@app.cli.command('hello')
@click.option('--name', default='World', callback=upper)
def hello_command(name)
    click.echo(f'Hello, {name}!')

def test_hello_params():
    context = hello_command.make_context('hello', ['--name', 'flask'])
    assert context.params['name'] == 'FLASK'
```
