+++
date = '2025-07-30T11:03:35.532581+08:00'
draft = false
title = 'Python asyncio协程 - gather(3)'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

在Python 3的协程中，官方针对gather的使用有几个特性的说明，先说第三点的特性

## 如果 return\_exceptions 为 False (默认)，所引发的首个异常会立即传播给等待 gather() 的任务。aws 序列中的其他可等待对象 不会被取消 并将继续运行。

先简单的看个例子

```python
import asyncio

async def fac(x, y):
    if x == 0:
        raise ZeroDivisionError
    else:
        print(f"{x}/{y}={x/y}")
        return x / y

async def main():
    res = await asyncio.gather(fac(1, 2), fac(2, 3), fac(0, 2))

    print(res)

asyncio.run(main())
```

运行后结果如下

```bash
$ python main.py
1/2=0.5
2/3=0.6666666666666666
Traceback (most recent call last):
  File "main.py", line 28, in <module>
    asyncio.run(main())
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/runners.py", line 43, in run
    return loop.run_until_complete(main)
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/asyncio/base_events.py", line 579, in run_until_complete
    return future.result()
  File "main.py", line 23, in main
    res = await asyncio.gather(fac(1, 2), fac(2, 3), fac(0, 2))
  File "main.py", line 16, in fac
    raise ZeroDivisionError
ZeroDivisionError
```

如果我们将return\_exceptions换个参数加上再试下

代码如下

```python
import asyncio

async def fac(x, y):
    if x == 0:
        raise ZeroDivisionError
    else:
        print(f"{x}/{y}={x/y}")
        return x / y

async def main():
    res = await asyncio.gather(fac(1, 2),
                               fac(2, 3),
                               fac(0, 2),
                               return_exceptions=True)

    print(res)

asyncio.run(main())
```

运行后结果如下

```bash
$ python main.py
1/2=0.5
2/3=0.6666666666666666
[0.5, 0.6666666666666666, ZeroDivisionError()]
```

上面的代码例子就是要说的第四点特性

## 如果 return\_exceptions 为 True，异常会和成功的结果一样处理，并聚合至结果列表。
