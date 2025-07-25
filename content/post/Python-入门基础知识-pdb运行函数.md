+++
date = '2025-07-25T15:09:53.009933+08:00'
draft = false
title = 'Python 入门基础知识 - pdb运行函数'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**pdb运行函数**

在Python中可以使用pdb模块的runcall函数来调试函数。其函数原型如下所示。

> runcall(function[, argument, ...])

其参数含义如下

> function: 函数名
>
> argument: 函数的参数

实例演示如下

```py
import pdb

def sum(*args):
    r = 0
    for arg in args:
        r = r + arg
    return r

pdb.runcall(sum, 1, 2, 3, 4)  

```

运行顺序可以参考如下

```bash
>>> import pdb # 导入pdb模块
>>>
>>>
>>> def sum(*args): #定义函数sum求所有参数之和
...     r = 0
...     for arg in args:
...         r = r + arg
...     return r
...
>>> pdb.runcall(sum, 1, 2, 3, 4) # 使用runcall调试函数sum
> <stdin>(2)sum()
(Pdb) print(r)
*** NameError: name 'r' is not defined
(Pdb) n # 进入调试状态，使用n命令，进行单步执行
> <stdin>(3)sum()
(Pdb) n # 使用n命令，进行单步执行
> <stdin>(4)sum()
(Pdb) print r 使用print打印变量r的值
0
(Pdb) print(r)
0
(Pdb) n
> <stdin>(3)sum()
(Pdb) n
> <stdin>(4)sum()
(Pdb) n
> <stdin>(3)sum()
(Pdb) print(r)
3
(Pdb) continue # 使用continue继续执行
10 # 函数返回结果  

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13

```
