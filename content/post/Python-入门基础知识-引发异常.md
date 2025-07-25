+++
date = '2025-07-25T15:09:35.107402+08:00'
draft = false
title = 'Python 入门基础知识 - 引发异常'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**引发异常**

除了内置的异常意外，在Python中还可以通过使用raise语句引发异常。在类中也可以使用raise引发异常，

并向异常传递数据。使用raise可以定义新的错误类型，以适应脚本的需要。例如对用户输入数据的长度有要求，

则可以使用raise引发异常，以确保数据输入符合要求。

**使用raise引发异常**

使用raise引发异常十分简单，有以下几种形式

> raise 异常
>
> raise 异常名, 附加数据
>
> raise 类名

以下实例使用try语句捕获由raise引发的异常。

```py
raise BaseException
```

会得到如下异常输出

```bash
    raise BaseException
BaseException
```

```py
try:
    raise BaseException, 'Raise an BaseException'
except BaseException, data:
    print(data)
else:
    print('No Error')
```

会得到如下输出

```bash
Raise an BaseException
```

```py
def fun(n):
    if n == 0:
        raise BaseException, 'n in Zero'
    else:
        print(n)
try:
    fun(0)
except BaseException, data:
    print(data)
```

会得到如下输出

```bash
n in Zero
```

```py
class A:
    def show(self):
        print('A')
try:
    raise A
except A:
    print('Error')
else:
    print('No Error')
```

会得到如下输出

```bash
Error
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
