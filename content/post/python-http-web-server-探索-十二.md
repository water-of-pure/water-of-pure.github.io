+++
date = '2025-07-30T11:28:33.880371+08:00'
draft = false
title = 'python http web server 探索（十二）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

作为一个简单的http web server

response应该提供一个公共的方法，方便调用的函数能够根据具体的情况做具体的内容类型调用

我这里目前简单的做了一个文本的操作

代码如下

```python

# _*_coding:utf-8_*_

class HttpResponse(object):
    def __init__(self, writer):
        self.writer = writer

    def text(self, text):
        self.writer.write(str.encode(text))

```

在使用的时候，我们只返回一个response给调用函数，然后在调用函数中调用text方法就可以了

```python

import asyncio, logging
from http_request import HttpRequest
from http_response import HttpResponse

url_map = []

def route(url, **kwargs):
    def wrapper(func):
        url_map.append((url, func, kwargs))
        return func

    return wrapper

@route('/hello')
async def hello(request, response):
    response.text("hello")

@route('/world')
async def world(request, response):
    response.text("world")

async def response_before(writer,
                          content_type="text/html; charset=utf-8",
                          status="200",
                          headers=None):
    writer.write(str.encode(f"HTTP/1.0 {status} NA\r\n"))
    writer.write(b"Content-Type: ")
    writer.write(str.encode(content_type))

    if not headers:
        writer.write(b"\r\n\r\n")
        return

    writer.write(b"\r\n")
    if isinstance(headers, bytes) or isinstance(headers, str):
        await writer.write(str.encode(headers))
    else:
        for k, v in headers.items():
            writer.write(str.encode(k))
            writer.write(b": ")
            writer.write(str.encode(v))
            writer.write(b"\r\n")
    writer.write(b"\r\n")

async def response_404(reader, writer):
    await response_before(writer, status='404')

async def handle(reader, writer):
    method = ''
    path = ''
    found = False

    try:
        data = await reader.readline()
    except Exception as e:
        print(e)

    request = HttpRequest(reader, data)

    if request:
        pattern = None
        response_action = None
        extra = {}

        for url in url_map:
            pattern = url[0]
            response_action = url[1]

            if len(url) > 2:
                extra = url[2]

            if request.path == str.encode(pattern):
                found = True
                break

        response = HttpResponse(writer)
        if found:
            await response_before(writer, status='200')
            await response_action(request, response)
        else:
            await response_404(reader, writer)
    else:
        await response_404(reader, writer)

    await writer.drain()
    writer.close()
    await writer.wait_closed()

def serve(loop, host, port):
    loop.create_task(asyncio.start_server(handle, host, port))
    loop.run_forever()

def run(host, port=8090):
    loop = asyncio.get_event_loop()
    serve(loop, host, port)
    print('run ....')
    loop.close()

def runner(host, port):
    print('running')
    asyncio.run(run('0.0.0.0'))

runner('127.0.0.1', 8090)
```

然后启动下项目

运行后分别访问`http://127.0.0.1/hello`和`http://127.0.0.1/world`

均能看到输出`hello`和`word`
