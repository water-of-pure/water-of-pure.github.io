+++
date = '2025-07-30T11:03:32.276577+08:00'
draft = false
title = 'Python asyncio协程 - gather(2)'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

在Python 3的协程中，官方针对gather的使用有几个特性的说明，先说第二点的特性

## 如果所有可等待对象都成功完成，结果将是一个由所有返回值聚合而成的列表。结果值的顺序与 aws 中可等待对象的顺序一致。

我们看一个例子理解下

```python
import asyncio

async def fac(name, num):
    total = 1
    for i in range(2, num + 1):
        await asyncio.sleep(1)
        total *= i

    return total

async def main():
    gather_res = await asyncio.gather(fac('xiao wang', 2), fac('xiao li', 3),
                                      fac('xiao zhang', 4))

    print(gather_res)

asyncio.run(main())
```

ok，运行后得出的结果如下

```bash
$ python main.py
[2, 6, 24]
```

从输出的结果中可以看出，这个是一个列表，而且是一个有序的列表，正好跟我们传值的顺序一致

下面换个调用顺序测试下

代码如下

```python
import asyncio

async def fac(name, num):
    total = 1
    for i in range(2, num + 1):
        await asyncio.sleep(1)
        total *= i

    return total

async def main():
    gather_res = await asyncio.gather(fac('xiao wang', 4), fac('xiao li', 3),
                                      fac('xiao zhang', 2))

    print(gather_res)

asyncio.run(main())
```

运行后的结果如下

```bash
$ python main.py
[24, 6, 2]
```
