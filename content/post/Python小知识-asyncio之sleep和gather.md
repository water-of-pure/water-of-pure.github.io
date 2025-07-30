+++
date = '2025-07-30T10:40:48.665616+08:00'
draft = false
title = 'Python小知识 - asyncio之sleep和gather'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

asyncio 之 Sleep 阻塞休眠

coroutine asyncio.sleep(delay, result=None, \*, loop=None)

阻塞指定的描述

如果指定了 result，则当协程完成时将其返回给调用者。

sleep() 总是会挂起当前任务，以允许其他任务运行。

Deprecated since version 3.8, will be removed in version 3.10: loop 形参。

以下协程示例运行 5 秒，每秒显示一次当前日期:

```python

import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break

        await asyncio.sleep(1)

asyncio.run(display_date())
```

运行结果类似如下

```bash

$ python main.py
2020-08-13 22:26:19.414429
2020-08-13 22:26:20.417651
2020-08-13 22:26:21.418705
2020-08-13 22:26:22.420557
2020-08-13 22:26:23.421803
```

asyncio 之 Gather 并发运行任务

awaitable asyncio.gather(\*aws, loop=None, return\_exceptions=False)¶

并发 运行 aws 序列中的 可等待对象。

如果 aws 中的某个可等待对象为协程，它将自动作为一个任务加入日程。

如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。

如果 return\_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。

如果 return\_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。

如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。

如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一样处理 -- 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。

Deprecated since version 3.8, will be removed in version 3.10: loop 形参。

简单应用实例

```python

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compure factorial({i})")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    await asyncio.gather(factorial("X", 2), factorial("Y", 3),
                         factorial("Z", 4))

asyncio.run(main())
```

运行结果类似如下

```bash

$ python main.py
Task X: Compure factorial(2)
Task Y: Compure factorial(2)
Task Z: Compure factorial(2)
Task X: factorial(2) = 2
Task Y: Compure factorial(3)
Task Z: Compure factorial(3)
Task Y: factorial(3) = 6
Task Z: Compure factorial(4)
Task Z: factorial(4) = 24
```
