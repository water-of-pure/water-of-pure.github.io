+++
date = '2025-07-30T11:27:11.477088+08:00'
draft = false
title = 'python http web server 探索（七）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

前面的文章已经理顺了如何获取请求的数据

包括路由路径，request method，和一些参数

接下里要结合下前面的文章中介绍的，装饰器

通过使用装饰器我们来填充下路由创建的空白功能

先看下代码

```python

def route(url, **kwargs):
    def wrapper(func):
        url_map.append((url, func, kwargs))
        return func

    return wrapper
```

这个是比较基础的，但是能够实现最基础的功能

然后添加两个函数

```python

@route('/hello')
def hello():
    return 'hello'

@route('/world')
def world():
    return 'world'
```

最后看下整体的代码

```python

import asyncio, logging

url_map = []

def route(url, **kwargs):
    def wrapper(func):
        url_map.append((url, func, kwargs))
        return func

    return wrapper

@route('/hello')
def hello():
    return 'hello'

@route('/world')
def world():
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

async def handle(reader, writer):
    print(f'handle...')

    print(url_map)

    try:
        data = await reader.readline()
        method, path, proto = data.split()
        print(data)
        print(method)
        print(path)
        print(proto)

    except Exception as e:
        print(e)

    await handler(reader, writer)
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
```

运行下代码

```python

asyncio.run(run('0.0.0.0'))
```

访问http://127.0.0.1:8090看看输出的结果

```bash

[('/hello', <function hello at 0x10f80ea70>, {}), ('/world', <function world at 0x10fd53b90>, {})]
```

可以看到类似上面的输出，说明这个就装饰器就解决了一个痛点，就是需要自己去维护一个路由列表，这里一个函数就对应的一个路由，非常方便维护，此刻能够理解Flask为什么也适用此方式了，而且也理解了Flask的实现原理的一部分
