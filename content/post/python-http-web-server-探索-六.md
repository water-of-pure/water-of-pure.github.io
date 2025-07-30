+++
date = '2025-07-30T11:27:08.394992+08:00'
draft = false
title = 'python http web server 探索（六）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

前面很多做了一部分铺垫

今天想着如何解析出路由信息，method信息等

下面看个实现的代码

```python

async def handle(reader, writer):
    print(f'handle...')

    try:
        data = await reader.readline()

        print(data)
    except Exception as e:
        print(e)

    await handler(reader, writer)
    await writer.drain()

    writer.close()
    await writer.wait_closed()
```

运行之后，输出下data结果如下

```bash

b'GET / HTTP/1.1\r\n'
```

从上面的字符串可以看到是一个字符串，用空格分割的，这样的话我们就能拿到method方法，route路径

修改后的代码如下

```python

async def handle(reader, writer):
    print(f'handle...')

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
```

运行后会看到类似如下的输出内容

```bash

b'GET / HTTP/1.1\r\n'
b'GET'
b'/'
b'HTTP/1.1'
```