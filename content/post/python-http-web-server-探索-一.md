+++
date = '2025-07-30T11:04:07.245960+08:00'
draft = false
title = 'python http web server 探索（一）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

最近想着这么多的python web框架

但是也只是处于会用的阶段，如果不懂其中的原理（非理论），即不知道如何实现，似乎有点愧于接触web开发

看个小例子

```python

from http.server import HTTPServer, BaseHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8009)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
```

运行下，然后访问http://127.0.0.1:8009/，得到如下结果

```bash

$ python main.py
127.0.0.1 - - [22/Sep/2020 23:48:53] code 501, message Unsupported method ('GET')
127.0.0.1 - - [22/Sep/2020 23:48:53] "GET / HTTP/1.1" 501 -
127.0.0.1 - - [22/Sep/2020 23:48:54] code 501, message Unsupported method ('GET')
127.0.0.1 - - [22/Sep/2020 23:48:54] "GET /favicon.ico HTTP/1.1" 501 -
```

似乎有点眉头了，明天继续。