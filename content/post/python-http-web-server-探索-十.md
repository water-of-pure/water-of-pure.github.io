+++
date = '2025-07-30T11:27:20.246015+08:00'
draft = false
title = 'python http web server 探索（十）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

web server中的HttpRequest实现

这个花了点时间想做的完善一些

但是就目前的情况来说，先简单的实现基础的功能就好

代码实现如下

```python

class HttpRequest(object):
    def __init__(self, reader, data):
        self.reader = reader

        method, path, proto = data.split()

        self.method = method
        self.path = path
        self.query = self.parse_query_string(proto)

    def parse_query_string(self, data):
        return {}
```

然后调用的方式如下

```python

import asyncio, logging
from http_request import HttpRequest

url_map = []

def route(url, **kwargs):
    def wrapper(func):
        url_map.append((url, func, kwargs))
        return func

    return wrapper

@route('/hello')
async def hello(request, writer):

    print(request.method)
    print(request.path)

    await start_response(writer, status='200')

    writer.write(b"hello\r\n")

    return 'hello'

@route('/world')
async def world(request, writer):
    print(f"request.method = {request.method}")
    print(f"request.path = {request.path}")

    await start_response(writer, status='200')

    writer.write(b"world\r\n")

    return 'world'

async def start_response(writer,
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

async def handler(reader, writer):

    # await start_response(writer, status='404')
    await start_response(writer, status='200')

    writer.write(b"hello\r\n")

async def handler_404(reader, writer):
    await start_response(writer, status='404')

async def handle(reader, writer):
    print(f'handle...')

    print(url_map)

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
        handler_action = None
        extra = {}

        for url in url_map:
            pattern = url[0]
            handler_action = url[1]

            if len(url) > 2:
                extra = url[2]

            if request.path == str.encode(pattern):
                found = True
                break

        if found:
            await handler_action(request, writer)
        else:
            print('here 1')
            await handler_404(reader, writer)
    else:
        print('here 2')
        await handler_404(reader, writer)

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

asyncio.run(run('0.0.0.0'))
```

其实主要的实现逻辑在这个函数里面

```python

async def handle(reader, writer):
```

让我明白的是，request其实在整个请求中，我觉得是一个解析器，就是将所有的请求信息，解析出来然后提供给调用函数去调用，那么其实把所有需要的信息都塞给http类就好了，这样的话可以给调用函数提供更多的可用信息。