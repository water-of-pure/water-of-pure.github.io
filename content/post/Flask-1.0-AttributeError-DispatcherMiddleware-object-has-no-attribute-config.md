+++
date = '2025-07-29T10:56:26.292211+08:00'
draft = false
title = "Flask 1.0 - AttributeError: 'DispatcherMiddleware' object has no attribute 'config'"
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

Flask 1.0使用过程中遇到“AttributeError: 'DispatcherMiddleware' object has no attribute 'config'”，官方的文档暂时还没更新，这里经过资料搜集，暂时有了一个可使用的解决方案。

最近在偷偷的自学Flask，一边看文档，一边实践，发现了一些小问题。

官方文档在“绑定应用”的章节实例代码如下

```python

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from frontend_app import application as frontend
from backend_app import application as backend

application = DispatcherMiddleware(frontend, {
    '/backend': backend
})
```

但是在经过测试后运行报错了

```bash

Server initialized for eventlet.
Traceback (most recent call last):
  File "wsgi.py", line 12, in <module>
    socketio.run(application, debug=True)
  File "/Users/durban/python/baby/.env3_baby/lib/python3.7/site-packages/flask_socketio/__init__.py", line 498, in run
    server_name = app.config['SERVER_NAME']
AttributeError: 'DispatcherMiddleware' object has no attribute 'config'
```

可以看出错误的问题属性没有了

> <https://stackoverflow.com/questions/36219842/flask-app-wrapped-with-dispatchermiddleware-no-longer-has-test-client>

于是在这里找到了答案

最后的实例使用方法如下

```python

from baby_backend import application as backend
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/backend': backend
})
```

这里的baby\_backend是个package
