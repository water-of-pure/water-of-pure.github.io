+++
date = '2025-07-30T10:40:45.322807+08:00'
draft = false
title = 'Python 3 小知识 - asyncio writable'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

在asyncio 中什么是 writable

在asyncio 中 writable 一般指的是 writable object

如果一个对象在await语句中使用，那么TA就是 writable object ，叫做可等待对象

在许多 asyncio API中，许多都被设计为 writable object

writable object 分为三种主要类型：**Coroutines、Tasks和Futures**

### Coroutines

Coroutines 属于 writable object，因此可以在其他Coroutines中被等待:

比如如下代码

```python

import asyncio

async def num():
    return 50

async def main():
    print(num())

    print(await num())

asyncio.run(main())
```

执行后的结果如下

```bash

$ python main.py
main.py:29: RuntimeWarning: coroutine 'num' was never awaited
  num()
RuntimeWarning: Enable tracemalloc to get the object allocation traceback
50
```

### Tasks

Tasks 被用来设置日程以便 并发 执行Coroutines

当一个Coroutines通过 asyncio.create\_task() 等函数被打包为一个 任务，该Coroutines将自动排入日程准备立即运行:

下面看如下实例代码

```python

import asyncio

async def num():
    return 50

async def main():

    task = asyncio.create_task(num())

    print(await task)

asyncio.run(main())
```

执行后的结果如下

```bash

$ python main.py
50
```

### Futures

Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。

当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。

在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。

通常情况下 没有必要 在应用层级的代码中创建 Future 对象。

Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:
