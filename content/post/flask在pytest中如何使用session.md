+++
date = '2025-07-30T09:56:47.985866+08:00'
draft = false
title = 'flask在pytest中如何使用session'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

先看代码

```py

class AuthActions(object):

    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test', code='1111'):
        with self._client.session_transaction() as session:
            session['captcha_key'] = '1111'

        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password,
                  'verification-code': code}
        )

    def logout(self):
        return self._client.get('/auth/logout')

```

这里为什么会提到session，因为我们正常使用的过程中，在登录或者注册的逻辑中会遇到session记录验证码，然后用户用户进行登录或者注册提交表单时的验证，但是这个逻辑在pytest中会遇到一些问题，因为要伪造一个类似于session的情况来测试类似登录或者注册的逻辑中使用session的情况。

这个问题在flask的官网也有介绍如何在测试环境中使用session，可以参考

> https://flask.palletsprojects.com/en/1.1.x/testing/#accessing-and-modifying-sessions

> https://flask.palletsprojects.com/en/1.1.x/api/#flask.testing.FlaskClient.session\_transaction

都有对应的说明但是具体没有实例的话时没有办法具体了解其使用场景的

不过今天在进行测试单元改写的时候发现原来可以这样使用 特此记录下方便日查找

上段代码是自我在conftest.py中的代码

使用的时候可以像下面这样调用

```py

@pytest.fixture
def auth(client):
    return AuthActions(client)

```

然后在测试函数中可以直接这样写

```py

def test_login(client, auth):
    # ... 省略 
    response = auth.login()

    # ... 省略

```

当然还要自己定义一个叫做client的fixture
