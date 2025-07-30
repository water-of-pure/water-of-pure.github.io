+++
date = '2025-07-30T11:03:39.981683+08:00'
draft = false
title = 'Python asyncio协程 - gather(4)'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

在Python 3的协程中，官方针对gather的使用有几个特性的说明，先说第五点的特性

## 如果 gather() 被取消，所有被提交 (尚未完成) 的可等待对象也会 被取消。

前面的几篇文章分别记录了gather的四个特性，为了下面的记录能够比较好的理解，请先回顾

下面先记录下一个简单的例子来说明问题

```python

import asyncio

async def fac(x, y):
    if x == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(5)
        print(f"{x} / {y} = {x/y}")
        return x / y

async def main():
    t = asyncio.gather(fac(0, 2), fac(1, 2), fac(3, 4))
    await asyncio.sleep(1)
    t.cancel()
    await t

asyncio.run(main())
```

运行后得到的结果如下

```bash
$ python main.py
1 / 2 = 0.5
3 / 4 = 0.75
Traceback (most recent call last):
  File "main.py", line 29, in <module>
    asyncio.run(main())
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/runners.py", line 43, in run
    return loop.run_until_complete(main)
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 579, in run_until_complete
    return future.result()
  File "main.py", line 26, in main
    await t
  File "main.py", line 15, in fac
    raise ZeroDivisionError
ZeroDivisionError
```

似乎看不出什么效果

我们将gather的代码修改如下，将sleeo的时间增加到5秒

```python
import asyncio

async def fac(x, y):
    if x == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(5)
        print(f"{x} / {y} = {x/y}")
        return x / y

async def main():
    t = asyncio.gather(fac(0, 2), fac(1, 2), fac(3, 4))
    await asyncio.sleep(1)
    t.cancel()
    await t

asyncio.run(main())
```

运行后得到的结果如下

```bash
$ python main.py
Traceback (most recent call last):
  File "main.py", line 30, in <module>
    asyncio.run(main())
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/runners.py", line 43, in run
    return loop.run_until_complete(main)
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 579, in run_until_complete
    return future.result()
  File "main.py", line 27, in main
    await t
  File "main.py", line 16, in fac
    raise ZeroDivisionError
ZeroDivisionError
```

从这里可以很清楚的了解这一特性

只要有一个是异常的后面的尚未执行的也会被取消
