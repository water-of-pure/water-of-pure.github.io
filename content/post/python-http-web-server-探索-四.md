+++
date = '2025-07-30T11:27:01.480712+08:00'
draft = false
title = 'python http web server 探索（四）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

针对于昨天的简单web server的构造

今天需要实现一个简单的文本输出

既然能够运行起来一个web server，那么距离实现一个简单的文本输出也不远了

代码如下

```python

import asyncio, logging

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

    await handler(reader, writer)
    await writer.drain()
    await asyncio.sleep(0.001)
    writer.close()

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

运行后访问http://127.0.0.1:8090

我们用curl测试下，得到的结果如下

```bash
$ curl -v http://127.0.0.1:8090
*   Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8090 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:8090
> User-Agent: curl/7.64.1
> Accept: */*
>
* HTTP 1.0, assume close after body
< HTTP/1.0 200 NA
< Content-Type: text/html; charset=utf-8
<
hello
* Closing connection 0
```

一个小的server终于运行起来了，后面会加以完善
