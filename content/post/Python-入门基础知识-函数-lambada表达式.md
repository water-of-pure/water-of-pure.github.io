+++
date = '2025-07-25T14:09:52.538254+08:00'
draft = false
title = 'Python 入门基础知识 - 函数 - lambada表达式'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**lambada表达式**

lambada表达式是Python中一类比较特殊的声明函数的方式。

使用它可以声明一个匿名函数，所谓匿名函数是指所声明的函数没有函数名称，lambda表达式就是一个简答的函数。

使用lambda表示是就是一个简单的函数。使用lambda声明的函数返回一个值，在调用函数的使用直接使用lambda表达式的返回值。

lambda声明函数的一般形式如下：

lambda 参数列表:表达式

以下实例使用lambda定义了一个函数，并调用一个函数。

```py
def func(a=lambda x: x * x - x, b=0):
    return a(b)

print(func(b=3))  

```

lambda适用于定义小型函数。与def声明函数的不同，使用lambda声明的函数，在函数中仅包含单一的参数表达式，而不能包含其他的语句。

在lambda中也可以调用其他的函数。如下：

```py
def func1(a):
    a()

def show():
    print 'lambda'

def shown(n):
    print 'lambda ' * n

def returnargs(x):
    return x

func1(lambda: show())
func(a=lambda x: shown(x), b=2)
print(func(a=lambda x: returnargs(x) * x, b=2))  

```

不能在lambda中使用print函数

> func1(lambda s: print(s))
>
>     func1(lambda: print 'x')
>
>                       ^
>
> SyntaxError: invalid syntax

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
