+++
date = '2025-07-30T10:40:26.921838+08:00'
draft = false
title = 'Python小知识 - asyncio使用记录（1）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

asyncio是什么，如何使用

官方介绍如下，熟读

> asyncio is a library to write concurrent code using the async/await syntax.
>
> asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
>
> asyncio is often a perfect fit for IO-bound and high-level structured network code.
>
> asyncio provides a set of high-level APIs to:
>
> * run Python coroutines concurrently and have full control over their execution;
> * perform network IO and IPC;
> * control subprocesses;
> * distribute tasks via queues;
> * synchronize concurrent code;
>
> Additionally, there are low-level APIs for library and framework developers to:
>
> * create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc;
> * implement efficient protocols using transports;
> * bridge callback-based libraries and code with async/await syntax.

简单的看下如何使用，建议使用 Python 3.7+

```python

import asyncio

async def main():
    print("Print ..... 1")
    await asyncio.sleep(10)
    print("Print ..... 2")

asyncio.run(main())
```

运行下之后，可以发现，“Print ..... 1”输出之后要过10秒才会输出“Print ..... 2”

这个不是并发的吗，为什么，用起来却不是并发的

其实上面的代码只是展示了如何用asyncio的async/await语法

看下如何实现并发的操作

实现之前先看下我么要做的功能

```python

import time
import asyncio

async def start_run(delay, name):
    await asyncio.sleep(delay)
    print('%s start run' % name)

async def main():
    print(f"started at {time.strftime('%X')}")

    await start_run(2, 'dog')
    await start_run(3, 'cat')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

运行后输出结果如下

```bash

started at 20:15:09
dog start run
cat start run
finished at 20:15:14
```

这里我们知道要如何运行了，下面我们来实现下如何并发

```python

import time
import asyncio

async def start_run(delay, name):
    await asyncio.sleep(delay)
    print('%s start run' % name)

async def main():
    dog_run = asyncio.create_task(start_run(2, 'dog'))
    cat_run = asyncio.create_task(start_run(3, 'cat'))

    print(f"started at {time.strftime('%X')}")

    await dog_run
    await cat_run

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

运行后输出结果如下

```bash

started at 20:19:18
dog start run
cat start run
finished at 20:19:23
```

提示：暂时别像下面这样操作

```python

import time
import asyncio

async def start_run(delay, name):
    await asyncio.sleep(delay)
    print('%s start run' % name)

async def main():
    print(f"started at {time.strftime('%X')}")

    await asyncio.create_task(start_run(2, 'dog'))
    await asyncio.create_task(start_run(3, 'cat'))

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
```

我实验了下，不会有效果，待查
