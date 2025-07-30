+++
date = '2025-07-30T11:03:28.424749+08:00'
draft = false
title = 'Python asyncio协程 - gather(1)'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "AsyncIO"
]
+++

在Python 3的协程中，官方针对gather的使用有几个特性的说明，先说第一点的特性

并发执行aws参数指定的 可等待（awaitable）对象序列。

## 如果 aws 中的某个可等待对象为协程，它将自动作为一个任务加入日程。

可以理解为 如果 aws 序列中的某个 awaitable 对象 是一个 协程,则自动将这个 协程 封装为 Task对象进行处理

看下面的代码

```python
import asyncio

async def fac(name, number):
    num = 1

    for i in range(2, number + 1):
        print(f"Task {name}: Compute fac({i})")
        await asyncio.sleep(1)
        num *= i

    print(f"Task {name}: fac({number}) = {num}")

async def main():
    await asyncio.gather(fac("xiao wang", 2), fac("xiao li", 3),
                         fac("xiao zhang", 4))

asyncio.run(main())
```

运行下看下结果

```bash
$ python main.py
Task xiao wang: Compute fac(2)
Task xiao li: Compute fac(2)
Task xiao zhang: Compute fac(2)
Task xiao wang: fac(2) = 2
Task xiao li: Compute fac(3)
Task xiao zhang: Compute fac(3)
Task xiao li: fac(3) = 6
Task xiao zhang: Compute fac(4)
Task xiao zhang: fac(4) = 24
```

再来对比下下面的代码

```python
import asyncio

async def fac(name, number):
    num = 1

    for i in range(2, number + 1):
        print(f"Task {name}: Compute fac({i})")
        await asyncio.sleep(1)
        num *= i

    print(f"Task {name}: fac({number}) = {num}")

async def main():
    task1 = asyncio.create_task(fac("xiao wang", 2))
    task2 = asyncio.create_task(fac("xiao li", 3))
    task3 = asyncio.create_task(fac("xiao zhang", 4))

    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
```

运行看下效果

```bash
$ python main.py
Task xiao wang: Compute fac(2)
Task xiao li: Compute fac(2)
Task xiao zhang: Compute fac(2)
Task xiao wang: fac(2) = 2
Task xiao li: Compute fac(3)
Task xiao zhang: Compute fac(3)
Task xiao li: fac(3) = 6
Task xiao zhang: Compute fac(4)
Task xiao zhang: fac(4) = 24
```

这样应该可以理解为自动封装为一个task对象来处理了。
