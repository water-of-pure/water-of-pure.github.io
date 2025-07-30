+++
date = '2025-07-30T09:57:12.161769+08:00'
draft = false
title = "wrap_socket() got an unexpected keyword argument '_context'"
categories = [
    "技术",

]

tags = [
    "Python",

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

最近的项目gunicorn+flask+nginx

但是最近在使用过程中，通过urllib发起请求的时候，遇到了一个错误，错误如下

```bash

wrap_socket() got an unexpected keyword argument '_context'

```

不知道，不懂这是什么错误信息，于是google了一下

居然是eventlet的问题

可以追溯到这里

<https://github.com/eventlet/eventlet/issues/526>

看到最后，会发现“python 3.8+pyopenssl”，居然有人用这个方式说解决了。我懵了，我的是python 3.7你让我升级吗？开玩笑，我不想折腾了，我就要用3.7。然后在网上爬一会，会发现有人建议使用`gevent`

截止2019-12-27，解决方案是

将eventlet替换为gevent，加完之后，在使用的时候会提示这个错误哦

```bash

/var/www/baby/.env3_baby/lib/python3.7/site-packages/gunicorn/workers/ggevent.py:53: MonkeyPatchWarning: Monkey-patching ssl after ssl has already been imported may lead to errors, including RecursionError on Python 3.6. It may also silently lead to incorrect behaviour on Python 3.7. Please monkey-patch earlier. See https://github.com/gevent/gevent/issues/1016. Modules that had direct imports (NOT patched): ['pymongo.ssl_support (/var/www/baby/.env3_baby/lib/python3.7/site-packages/pymongo/ssl_support.py)', 'eventlet.green.ssl (/var/www/baby/.env3_baby/lib/python3.7/site-packages/eventlet/green/ssl.py)']. Subclasses (NOT patched): ["<class 'eventlet.green.ssl.GreenSSLContext'>"].
  monkey.patch_all()

```

但是后来我又测试了几次又没有问题了，看来不是必现的问题

不过看他提示的意思是代码入口处加上`monkey.patch_all()`，下次遇到可以试试。
