+++
date = '2025-07-29T10:55:32.324377+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 测试覆盖率'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

为我们开发的程序写单元测试是为了检查我们写的代码能够按照我们希望的逻方式去运行。Flask提供了一个测试客户端来模拟请求到应用程序然后返回响应的数据。

您应该尽可能多地测试代码。函数中的代码仅在调用函数时运行，分支中的代码（如`if`块）仅在满足条件时运行。您希望确保使用涵盖每个分支的数据测试每个函数。

您越接近100％覆盖率，您就越容易做出改变,而这个改变不会意外地改变其他行为。但是，100％的覆盖率并不能保证您的应用程序没有错误。特别是，它不能监测到用户如何在浏览器中与应用程序交互。尽管如此，测试覆盖率是开发过程中使用的重要工具。

---

### 注意

这是在本教程后期介绍的，但在您将来的项目中，您应该在开发时进行测试。

---

您将使用pytest和coverage来测试和测量代码，安装命令如下：

```bash

pip install pytest coverage

```

## Setup和Fixtures

测试代码放在了`tests`目录中，这个目录跟baby包同层级，不在包里面。tests/conftest.py文件包含了设置函数。`tests/conftest.py`文件包含每个测试将使用的称为*fixture*的设置函数。测试是在以`test_`开头的Python模块中，并且这些模块中的每个测试函数也以`test_`开头。

每个测试都将创建一个新的临时数据库文件，并填充将在测试中使用的一些数据。编写一个SQL文件来插入该数据。

tests/data.sql

```sql

INSERT INTO user (username, password)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO post (title, body, author_id, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, '2019-01-01 00:00:00');

```

应用程序fixture将调用工厂并传递`test_config`以配置应用程序和数据库以进行测试，而不是使用本地开发配置。

tests/conftest.py

```py

#! _*_ coding: utf-8 _*_
import os
import tempfile

import pytest
from baby import create_app
from baby.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

```

[**tempfile.mkstemp()**](https://docs.python.org/3/library/tempfile.html#tempfile.mkstemp)创建并打开一个临时文件，返回文件对象及其路径。重写DATABASE路径，因此它指向此临时路径而不是实例文件夹。设置路径后，将创建数据库表并插入测试数据。测试结束后，临时文件将被关闭并删除。

[**TESTING**](http://flask.pocoo.org/docs/1.0/config/#TESTING)告诉Flask应用程序处于测试模式。Flask更改了一些内部行为，因此更容易测试，而其他扩展也可以使用该标志来更轻松地测试它们。

`client`fixture使用`app`fixture创建的应用程序对象调用[**app.test\_client()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_client)。测试将使用客户端向应用程序发出请求而不运行服务器。

`runner`fixture与`client`类似。[**app.test\_cli\_runner()**](http://flask.pocoo.org/docs/1.0/api/#flask.Flask.test_cli_runner)创建一个可以调用在应用程序中注册的Click命令的runner。

Pytest通过将其函数名称与测试函数中的参数名称进行匹配来使用fixture。例如，您接下来要编写的test\_hello函数将使用`client`参数。Pytest与`client`fixture函数匹配，调用它，并将返回的值传递给测试函数。

## 工厂

关于工厂本身的测试并不多。大多数代码都将针对每个测试执行，因此如果某些内容失败，其他测试将会受到影响。

唯一可以改变的行为是传递测试配置。如果未传递config，则应该有一些默认配置，否则应该重写配置。

tests/test\_factory.py

```py

#! _*_ coding: utf-8 _*_

from baby import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_baby(client):
    response = client.get('/baby')
    assert response.data == b'Baby'

```

在本教程开头编写工厂时，您添加了baby路由作为示例。它返回“Baby”，因此测试检查响应数据是否匹配。

## 数据库

在应用程序上下文中，`get_db`应在每次调用时返回相同的连接。在上下文之后，应该关闭连接。

tests/test\_db.py

```py

#! _*_ coding: utf-8 _*_
import sqlite3

import pytest

from baby.db import get_db

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e)

```

`init-db`命令应调用`init_db`函数并输出消息。

```py

def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('baby.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called

```

此测试使用Pytest的`monkeypatch`fixture将`init_db`函数替换为记录它已被调用的函数。您在上面编写的`runner`命令用于按名称调用`init-db`命令。

## 认证

对于大多数视图，用户需要登录。在测试中执行此操作的最简单方法是使用客户端向`login`视图发出`POST`请求。您可以编写一个包含方法的类，而不是每次都写出来，并使用fixture将每个测试的客户端传递给它。

tests/conftest.py

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

@pytest.fixture
def auth(client):
    return AuthActions(client)

```

使用`auth`fixture，您可以在测试中调用`auth.login()`以作为测试用户登录，该测试用户作为测试数据的一部分插入到app fixture中。

`register`视图应在`GET`上成功渲染。在具有有效表单数据的POST上，它应该重定向到登录URL，并且用户的数据应该在数据库中。无效数据应显示错误消息。

tests/test\_auth.py

```py

#! _*_ coding: utf-8 _*_

import pytest

from flask import g, session
from baby.db import get_db

def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username':'a','password':'a'}
    )
    assert 'http://localhost/auth/login' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'"
        ).fetchone() is not None

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required'),
    ('a', '', b'Password is required'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username':username, 'password': password}
    )
    assert message in response.data

```

[**client.get()**](http://werkzeug.pocoo.org/docs/test/#werkzeug.test.Client.get)发出`GET`请求并返回Flask返回的[**Response**](http://flask.pocoo.org/docs/1.0/api/#flask.Response)对象。类似地，[**client.post()**](http://werkzeug.pocoo.org/docs/test/#werkzeug.test.Client.post)发出`POST`请求，将`data`字典转换为表单数据。

要测试页面是否渲染成功，可以发出一个简单的请求并检查`200 OK`[**状态码**](http://flask.pocoo.org/docs/1.0/api/#flask.Response.status_code)。如果渲染失败，Flask将返回`500内部服务器错误代码`。

当注册视图重定向到登录视图时，[**header**](http://flask.pocoo.org/docs/1.0/api/#flask.Response.headers)将是一个带有登录URL的`Location`标头。

[**data**](http://flask.pocoo.org/docs/1.0/api/#flask.Response.data)包含响应的主体作为字节。如果您希望在页面上呈现某个值，请检查它是否在数据中。必须将字节与字节进行比较。如果要比较Unicode文本，请改用[**get\_data(as\_text = True)**](http://werkzeug.pocoo.org/docs/wrappers/#werkzeug.wrappers.BaseResponse.get_data)。

`pytest.mark.parametrize`告诉Pytest使用不同的参数运行相同的测试函数。您可以在此处使用它来测试不同的无效输入和错误消息，而无需编写相同的代码三次。

`login`视图的测试与`register`的测试非常相似。[**session**](http://flask.pocoo.org/docs/1.0/api/#flask.session)应该在登录后设置`user_id`，而不是测试数据库中的数据。

tests/test\_auth.py

```py

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert 'http://localhost/' == response.headers['Location']

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'

@pytest.mark.parametrize(('username', 'password', 'message'),(
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data

```

在with块中使用client允许在返回响应后访问上下文变量，例如[**session**](http://flask.pocoo.org/docs/1.0/api/#flask.session)。通常，访问请求之外的`session`会引发错误。

测试`logout`与`login`相反。注销后，[**session**](http://flask.pocoo.org/docs/1.0/api/#flask.session)不应包含`user_id`。

tests/test\_auth.py

```py

def test_logout(client, auth):
    auth.login()
    with client:
        auth.logout()
        assert 'user_id' not in session

```

## 博客

所有博客视图都使用之前编写的`auth` fixture。调用`auth.login()`以及来自客户端的后续请求将作为测试用户登录。

`index`视图应显示有关随测试数据添加的帖子的信息。以作者身份登录时，应该有一个链接来编辑帖子。

还可以在测试`index`视图时测试更多身份验证行为。未登录时，每个页面都会显示登录或注册的链接。登录后，会有一个注销链接。

tests/test\_blog.py

```py

#! _*_ coding: utf-8 _*_

import pytest
from baby.db import get_db

def test_index(client, auth):
    response = client.get('/')
    assert b'Log In' in response.data
    assert b'Register' in response.data

    auth.login()
    response = client.get('/')

    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2019-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data

```

`create`,`update`,`delete`视图必须在用户登录后才能访问，`update`和`delete`视图必须在登录的用户是帖子的作者时才能被访问，否则返回`403 Forbidden`状态。如果post请求是给传递的id不存在，则`update`和`delete`视图应该返回`404 Not Found`状态。

tests/test\_blog.py

```py

@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete'
))
def test_login_required(client, path):
    response = client.post(path)
    assert 'http://localhost/auth/login'  == response.headers['Location']

def test_author_required(app, client, auth):
    with app.app_context():
        db = get_db()
        db.execute(
            'UPDATE post SET author_id = 2 WHERE id = 1'
        )
        db.commit()

    auth.login()

    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403

    assert b'href="/1/update"' not in client.get('/').data

@pytest.mark.parametrize('path', (
    ('/2/update'),
    ('/2/delete')
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404

```

`create`和`update`视图在`GET`请求时应该渲染并返回`200 OK`状态。当有效的数据通过`POST`请求提交时，`create`视图应该输入新的数据到数据库，`update`视图应该修改存在的数据。两个视图在遇到无效的数据提交时应该显示错误信息。

tests/test\_blog.py

```py

def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200

    client.post('/create', data={'title':'created','body':''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2

def test_update(app, client, auth):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title':'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'

@pytest.mark.parametrize('path', (
    '/create',
    '/1/update'
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required' in response.data

```

`delete`视图应该重新到index URL，并且数据库不应该存在该帖子。

tests/test\_blog.py

```py

def test_delete(app, client, auth):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers['Location'] == 'http://localhost/'

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None

```

## 运行测试

可以将一些额外的配置添加到项目的`setup.cfg`文件中，这些配置不是必需的，但可以使运行测试的覆盖范围更加冗长。

setup.cfg

```bash

[tool:pytest]
testpaths = tests

[coverage:run]
branch = True
source = 
    baby

```

要运行测试，请使用pytest命令。它将查找并运行我们编写的所有测试函数。

```bash

$ pytest
============================== test session starts ==============================
platform darwin -- Python 3.6.5, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
rootdir: /Users/durban/python/baby, inifile: setup.cfg, testpaths: tests
collected 24 items

tests/test_auth.py ........                                               [ 33%]
tests/test_blog.py ............                                           [ 83%]
tests/test_db.py ..                                                       [ 91%]
tests/test_factory.py ..                                                  [100%]

=========================== 24 passed in 1.83 seconds ===========================
(.env3)

```

如果任何测试失败，pytest将显示引发的错误。您可以运行pytest -v来获取每个测试函数的列表而不是点。

```bash

$ pytest -v
===================================== test session starts ======================================
platform darwin -- Python 3.6.5, pytest-4.4.0, py-1.8.0, pluggy-0.9.0 -- /Users/durban/python/baby/.env3/bin/python3
cachedir: .pytest_cache
rootdir: /Users/durban/python/baby, inifile: setup.cfg, testpaths: tests
collected 24 items

tests/test_auth.py::test_register PASSED                                                 [  4%]
tests/test_auth.py::test_register_validate_input[--Username is required] PASSED          [  8%]
tests/test_auth.py::test_register_validate_input[a--Password is required] PASSED         [ 12%]
tests/test_auth.py::test_register_validate_input[test-test-already registered] PASSED    [ 16%]
tests/test_auth.py::test_login PASSED                                                    [ 20%]
tests/test_auth.py::test_login_validate_input[a-test-Incorrect username.] PASSED         [ 25%]
tests/test_auth.py::test_login_validate_input[test-a-Incorrect password.] PASSED         [ 29%]
tests/test_auth.py::test_logout PASSED                                                   [ 33%]
tests/test_blog.py::test_index PASSED                                                    [ 37%]
tests/test_blog.py::test_login_required[/create] PASSED                                  [ 41%]
tests/test_blog.py::test_login_required[/1/update] PASSED                                [ 45%]
tests/test_blog.py::test_login_required[/1/delete] PASSED                                [ 50%]
tests/test_blog.py::test_author_required PASSED                                          [ 54%]
tests/test_blog.py::test_exists_required[/2/update] PASSED                               [ 58%]
tests/test_blog.py::test_exists_required[/2/delete] PASSED                               [ 62%]
tests/test_blog.py::test_create PASSED                                                   [ 66%]
tests/test_blog.py::test_update PASSED                                                   [ 70%]
tests/test_blog.py::test_create_update_validate[/create] PASSED                          [ 75%]
tests/test_blog.py::test_create_update_validate[/1/update] PASSED                        [ 79%]
tests/test_blog.py::test_delete PASSED                                                   [ 83%]
tests/test_db.py::test_get_close_db PASSED                                               [ 87%]
tests/test_db.py::test_init_db_command PASSED                                            [ 91%]
tests/test_factory.py::test_config PASSED                                                [ 95%]
tests/test_factory.py::test_baby PASSED                                                  [100%]

================================== 24 passed in 1.94 seconds ===================================
(.env3)

```

要测量测试的代码覆盖率，请使用coverage命令运行pytest而不是直接运行它。

```bash

coverage run -m pytest

```

您可以在终端中查看简单的覆盖率报告：

```bash

coverage report

```

```bash

$ coverage report
Name               Stmts   Miss Branch BrPart  Cover
----------------------------------------------------
baby/__init__.py      25      1      4      1    93%
baby/auth.py          54      0     22      0   100%
baby/blog.py          54      0     16      0   100%
baby/db.py            24      0      4      0   100%
----------------------------------------------------
TOTAL                157      1     46      1    99%
(.env3)

```

HTML报告允许您查看每个文件中包含的行：

```bash

coverage html

```

这会在`htmlcov`目录中生成文件。在浏览器中打开`htmlcov/index.html`以查看报告。

下一期继续 - [部署到生产](https://www.walkerfree.com/article/161)
