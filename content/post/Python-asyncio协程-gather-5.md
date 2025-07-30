+++
date = '2025-07-30T11:03:49.502723+08:00'
draft = false
title = 'Python asyncio协程 - gather(5)'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

在Python 3的协程中，官方针对gather的使用有几个特性的说明，先说第六点的特性

## 如果 aws 序列中的任一 Task 或 Future 对象 被取消，它将被当作引发了 CancelledError 一样处理 -- 在此情况下 gather() 调用 不会 被取消。这是为了防止一个已提交的 Task/Future 被取消导致其他 Tasks/Future 也被取消。

前面的几篇文章分别记录了gather的五个特性，基本上都在说gather中的方法执行的时候被取消会发生什么异常，这个是最后的一个特性

下面先记录下一个简单的例子来说明问题

```python
import asyncio

async def div(x, y):
    if x == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(1)
        print(f"{x} / {y} = {x/y}")
        return x / y

async def main():
    task1 = asyncio.create_task(div(0, 2))
    task2 = asyncio.create_task(div(1, 2))
    task3 = asyncio.create_task(div(3, 4))

    t = asyncio.gather(task1, task2, task3, return_exceptions=True)

    task1.cancel()

    print(await t)

asyncio.run(main())
```

运行结果如下

```bash
$ python main.py
1 / 2 = 0.5
3 / 4 = 0.75
[CancelledError(), 0.5, 0.75]
```
