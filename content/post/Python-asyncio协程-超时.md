+++
date = '2025-07-30T11:03:58.705816+08:00'
draft = false
title = 'Python asyncio协程 - 超时'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

先回忆下之前关于asyncio的学习（基本忘的差不多了）

1、gather（集合，感觉类似于collect的意思），实际上是用来并发运行任务的

2、writable object（可等待对象）

3、Task（任务）

4、sleep（休眠）

好了，上面的几个特性，我觉得是在asyncio中用的比较多的

下面看下超时和屏蔽取消的特性

先看下屏蔽取消

### 屏蔽取消

这个屏蔽取消主要是针对gather里面的特性，因为在使用gather的时候，会遇到一个情况就是取消并发任务中的某个任务，这个时候就需要用到取消的动作，

既然有取消，就会有屏蔽取消的情况，这个功能果然与矛盾相关

看下如何屏蔽取消，首先是语法

```python
awaitable asyncio.shield(aw, * , loop=None)
```

然后在使用的时候，像下面这样调用

```python
await asyncio.shield(some_func())
```

下面看个简单的实例

```python
import asyncio

async def div(x, y):
    if x == 0:
        raise ZeroDivisionError
    else:
        await asyncio.sleep(2)
        print(f"{x} / {y} = {x/y}")
        return x / y

async def main():
    task1 = asyncio.shield(div(1, 2))
    task2 = asyncio.create_task(div(2, 3))
    task3 = asyncio.create_task(div(3, 4))
    res = asyncio.gather(task1, task2, task3, return_exceptions=True)

    task1.cancel()
    task2.cancel()
    print(await res)

asyncio.run(main())
```

运行后得到的结果如下

```bash
$ python main.py
1 / 2 = 0.5
3 / 4 = 0.75
[CancelledError(), CancelledError(), 0.75]
```

### 超时（Timeouts）

```python
coroutine asyncio.wait_for(aw, timeout, *, loop=None)
```

超时使用的情况也是比较多的

先看下官方的解释

> 等待 aw 可等待对象 完成，指定 timeout 秒数后超时。
>
> 如果 aw 是一个协程，它将自动作为任务加入日程。
>
> timeout 可以为 None，也可以为 float 或 int 型数值表示的等待秒数。如果 timeout 为 None，则等待直到完成。
>
> 如果发生超时，任务将取消并引发 asyncio.TimeoutError.
>
> 要避免任务 取消，可以加上 shield()。
>
> 函数将等待直到目标对象确实被取消，所以总等待时间可能超过 timeout 指定的秒数。
>
> 如果等待被取消，则 aw 指定的对象也会被取消。

*Deprecated since version 3.8, will be removed in version 3.10: loop 形参。*

下面看个简单的例子

```python
import asyncio

async def sleep(sleep_time):
    await asyncio.sleep(sleep_time)
    print(f'after {sleep_time} , sleep over')

async def main():

    try:
        await asyncio.wait_for(sleep(3600), 1.0)
    except asyncio.TimeoutError as timeout:
        print('timeout!')

asyncio.run(main())
```

运行后得到的结果如下

```bash
$ python main.py
timeout!
```

使用方法也比较简单

我能想到的可能的场景

比如，数据库SQL查询的时候
