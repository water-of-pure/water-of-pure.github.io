+++
date = '2025-07-30T11:03:08.234397+08:00'
draft = false
title = 'Python小技巧 - Python 类型注释'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "注释",
]
+++

Python 类型注释

Python 3.5+ 开始支持 类型注释 ，以后也可以写一些静态类型的代码了

具体如何使用，看下面的代码

```python

def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y

def multi(x: int, y: int) -> int:
    return x * y

def div(x: int, y: int) -> int:
    return x / y

def splice(x: str, y: str) -> str:
    return x + ' ' + y
```

调用上面的函数试试

```python

print(add(1, 2))
print(sub(4, 3))
print(multi(2, 3))
print(div(10, 5))
print(splice('hello', 'world'))
print(add('1', '2'))
```

运行后得到的结果如下

```bash

$ python main.py
3
1
6
2.0
hello world
12
```

从上面的结果可以看出，虽然在代码编写的时候是可以加类型注释的，但是在运行的时候并没有提示异常的错误信息

关于这个问题我找到了答案可以点击[这里](https://stackoverflow.com/questions/43976861/python-3-type-check-not-works-with-use-typing-module)进行详细了解

另外推荐一个[mypy](http://mypy-lang.org/)
