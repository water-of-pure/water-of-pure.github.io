+++
date = '2025-07-30T11:26:55.643604+08:00'
draft = false
title = 'Python小知识 - 装饰器'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "装饰器"
]
+++

装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。

比如我们有个函数，如下

```python

def do_get():
    """
    docstring
    """
    print('do get')
```

有个需求，需要给这个函数增加一个日志，记录这个函数的执行日志，于是在代码中添加日志代码如下

```python

def do_get():
    print('do get')
    logging.info('go get logging')
```

但是如果我们要给类似的函数都加上函数的执行日志，会造成大面积的修改，如果一两个函数还是可以的

但是如果有很多的函数需要添加，就需要大量的工作，这个是不可取的

所以需要一个专门来处理日志的函数

```python

import logging

def do_logging(func):
    logging.warning(f"{func.__name__} is running")
    func()

def do_get():
    print("do get")

do_logging(do_get)
```

但是这样的话，需要每次将一个函数作为参数传递给do\_logging函数，也不是非常理想

于是我想到了装饰器

```python

import logging

def do_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning(f"{func.__name__} is running")
        return func(*args, **kwargs)

    return wrapper

def do_get():
    print('do get')

do_get = do_logging(do_get)

do_get()
```

这里do\_logging就是一个装饰器

`'@符号'`是装饰器的语法糖，在定义函数的时候使用，避免再一次赋值操作，使用方式如下

```python

import logging

def do_logging(func):
    def wrapper(*args, **kwargs):
        logging.warning(f"{func.__name__} is running")
        return func(*args, **kwargs)

    return wrapper

@do_logging
def do_get():
    print('do get')

do_get()
```

使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了

```python

import logging
from functools import wraps

def do_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.warning(f"{func.__name__} is running")
        func(*args, **kwargs)

    return wrapper

@do_logging
def do_get():
    print('do get')

do_get()
```
