+++
date = '2025-07-30T09:57:08.661259+08:00'
draft = false
title = '如何在Flask扩展开发的过程中加入异常日志'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

之前开发了一个扩展叫做[flask\_dxcaptcha](https://github.com/durban89/flask_dxcaptcha)

最近在使用他的过程中发现了一个问题，发现异常的时候直接导致使用的他的程序奔溃了，异常让人崩溃，但是不能给使用者带来崩溃，于是做了修复，加了下日志处理逻辑。

但是如果自己再定义一个好像显得有些麻烦，毕竟定义一套虽说可以更加责任化（就是出了问题知道是自己扩展的问题），但是既然是Flask扩展，应该跟使用Flask框架结合下会更好，于是决定先暂时这样处理吧，添加的代码如下

```py

from flask import current_app

try:
    ......
except Exception as e:
    current_app.logger.exception(str(e))
    ......

```

测试如下

```py

from flask import current_app

try:
	raise Exception('测试异常')
    ......
except Exception as e:
    current_app.logger.exception(str(e))
    ......

```

于是得到的异常结果如下

```bash

[2019-12-27 10:51:12,653] ERROR in captchaclient: 测试异常
Traceback (most recent call last):
  File "/Users/durban/python/baby/.env3_baby/lib/python3.7/site-packages/flask_dxcaptcha/captchaclient.py", line 57, in checkToken
    raise Exception('测试异常')
Exception: 测试异常
```
