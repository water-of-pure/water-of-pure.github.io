+++
date = '2025-07-30T11:04:01.027235+08:00'
draft = false
title = 'Python asyncio协程 - 简单等待（一）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

asyncio协程 - 简单等待

语法如下

```python
coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)¶
```

官方文档简介如下

并发运行 *aws* 指定的 [可等待对象](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio-awaitables) 并阻塞线程直到满足 *return\_when* 指定的条件。

返回两个 Task/Future 集合: `(done, pending)`。

用法如下

```python
done, pending = await asyncio.wait(aws)
```

如指定 *timeout* (float 或 int 类型) 则它将被用于控制返回之前等待的最长秒数。

请注意此函数不会引发 [`asyncio.TimeoutError`](https://docs.python.org/zh-cn/3/library/asyncio-exceptions.html#asyncio.TimeoutError)。当超时发生时，未完成的 Future 或 Task 将在指定秒数后被返回。

*return\_when* 指定此函数应在何时返回。它必须为以下常数之一:

| 常数 | 描述 |
| --- | --- |
| `FIRST_COMPLETED` | 函数将在任意可等待对象结束或取消时返回。 |
| `FIRST_EXCEPTION` | 函数将在任意可等待对象因引发异常而结束时返回。当没有引发任何异常时它就相当于 `ALL_COMPLETED`。 |
| `ALL_COMPLETED` | 函数将在所有可等待对象结束或取消时返回。 |

与 [`wait_for()`](https://docs.python.org/zh-cn/3/library/asyncio-task.html#asyncio.wait_for) 不同，`wait()` 在超时发生时不会取消可等待对象。

注意

`wait()` 会自动将协程作为任务加入日程，以后将以 `(done, pending)` 集合形式返回显式创建的任务对象。因此以下代码并不会有预期的行为:

```python
import asyncio

async def num():
    return 42

async def main():

    coro = num()
    done, pending = await asyncio.wait({coro})

    if coro in done:
        # 这里将不会运行
        print(coro)

asyncio.run(main())
```

上面的代码将不会运行

如果将上面的代码修改为下面的代码

```python
import asyncio

async def num():
    return 42

async def main():

    coro = asyncio.create_task(num())
    done, pending = await asyncio.wait({coro})

    if coro in done:
        # 这里将不会运行
        print(coro)

asyncio.run(main())
```

上面的代码运行结果类似如下

```bash
$ python main.py
<Task finished coro=<num() done, defined at main.py:14> result=42>
```
