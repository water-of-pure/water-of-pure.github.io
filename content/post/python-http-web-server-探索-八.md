+++
date = '2025-07-30T11:27:14.190674+08:00'
draft = false
title = 'python http web server 探索（八）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

前面的文章已经分析了，路由如何创建。并且知道如何根据请求的数据获取路由参数

今天记录下，如何匹配路由，并根据路由来执行指定的函数方法

看下面代码

```python

import asyncio, logging

url_map = []

def route(url, **kwargs):
    def wrapper(func):
        url_map.append((url, func, kwargs))
        return func

    return wrapper

@route('/hello')
async def hello(reader, writer):
    await start_response(writer, status='200')

    writer.write(b"hello\r\n")

    return 'hello'

@route('/world')
async def world(reader, writer):
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
        method, path, proto = data.split()
        print(data)
        print(method)
        print(path)
        print(proto)

    except Exception as e:
        print(e)

    print('method = ', method)
    print('path = ', path)

    pattern = None
    handler_action = None
    extra = {}

    for url in url_map:
        pattern = url[0]
        handler_action = url[1]

        if len(url) > 2:
            extra = url[2]

        print('pattern = ', str.encode(pattern))
        print('path = ', path)
        if path == str.encode(pattern):
            found = True
            break

    if found:
        await handler_action(reader, writer)
    else:
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

运行上面代码，然后分别访问http://127.0.0.1:8090/hello和http://127.0.0.1:8090/world

可以在浏览器中看到，分别输出hello和world

主要的逻辑其实这部分

```python

for url in url_map:
    pattern = url[0]
    handler_action = url[1]

    if len(url) > 2:
        extra = url[2]

    print('pattern = ', str.encode(pattern))
    print('path = ', path)
    if path == str.encode(pattern):
        found = True
        break

if found:
    await handler_action(reader, writer)
else:
    await handler_404(reader, writer)
```

从目前来看目前小型web server已经成型，后面要进行封装下
