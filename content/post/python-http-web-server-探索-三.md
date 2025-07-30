+++
date = '2025-07-30T11:26:58.578018+08:00'
draft = false
title = 'python http web server 探索（三）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

最近思考如何更进一步了web server

前面有一篇文章解释如何使用http.server创建一个web server，这样的话就会不支持asyncio，或者需要自己再封装一个

经过资料的查询，发现一个start\_server的方法

```bash

coroutine asyncio.start_server(client_connected_cb, host=None, port=None, *, loop=None, limit=None, family=socket.AF_UNSPEC, flags=socket.AI_PASSIVE, sock=None, backlog=100, ssl=None, reuse_address=None, reuse_port=None, ssl_handshake_timeout=None, start_serving=True)
```

本意是指启动一个socket服务器

下面看下如何简单的使用

```python

import asyncio

async def handle(reader, writer):
    print(f'handle...')
    await asyncio.sleep(1)
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

运行后访问http://127.0.0.1:8090/

在终端会得到如下输出

```bash

$ python main.py

handle...
handle...
handle...
handle...
handle...
handle...
```

可以说能够得到正常的运行了