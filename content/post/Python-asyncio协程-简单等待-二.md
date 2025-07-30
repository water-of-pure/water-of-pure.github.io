+++
date = '2025-07-30T11:04:04.127384+08:00'
draft = false
title = 'Python asyncio协程 - 简单等待（二）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

asyncio协程 - 简单等待（二）

语法如下

```python

asyncio.as_completed(aws, *, loop=None, timeout=None)
```

官方文档解释

并发地运行 *aws* 集合中的 [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables)。 返回一个协程的迭代器。 所返回的每个协程可被等待以从剩余的可等待对象集合中获得最早的下一个结果。

如果在所有 Future 对象完成前发生超时则将引发 [`asyncio.TimeoutError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.TimeoutError)。

比如下面的示例

```python

for coro in as_completed(aws):
    earliest_result = await coro
    # ...
```

我们看一个完整的示例

```python

import asyncio
import time

async def delay_timer(delay):
    await asyncio.sleep(delay)
    print(f"delay for {delay} seconds")
    return delay

async def main():
    print(f"start at {time.strftime('%X')}")
    tasks = [delay_timer(i) for i in range(10)]
    for p in asyncio.as_completed(tasks):
        res = await p

    print(f"end at {time.strftime('%X')}")

asyncio.run(main())
```

运行结果如下

```bash

$ python main.py
start at 22:23:48
delay for 0 seconds
delay for 1 seconds
delay for 2 seconds
delay for 3 seconds
delay for 4 seconds
delay for 5 seconds
delay for 6 seconds
delay for 7 seconds
delay for 8 seconds
delay for 9 seconds
end at 22:23:57
```
