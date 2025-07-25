+++
date = '2025-07-25T15:09:49.891904+08:00'
draft = false
title = 'Python 入门基础知识 - pdb运行表达式'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**pdb运行表达式**

在Python中可以使用pdb模块的runeval函数来调试表达式。其参数原型如下所示。

> runeval(expression[, globals[, locals]])

其参数如下。

> statement: 要调试的表达式，以字符串的形式
>
> globals: 可选参数，设置statement运行的全局环境变量
>
> locals: 可选参数，设置statement运行的局部环境变量

以下实例如下

```py
import pdb # 导入pdb模块
l = [1,2,3] # 定义一个列表
pdb.runeval('n = l[1]') # 使用runeval调试表达式l[1]
```

运行后结果如下

```bash
> <string>(1)<module>()
(Pdb) n # 进入调试状态，使用n命令，单步执行
--Return--
> <string>(1)<module>()->2
(Pdb) n # 使用n命令，单步执行
```

```py
pdb.runeval('3+5*6/2')  # 使用runeval调试表达式3+5*6/2
```

运行后结果如下

```bash
> <string>(1)<module>()
(Pdb) n # 进入调试状态，使用n命令，单步执行
--Return--
> <string>(1)<module>()->18
(Pdb) n # 使用n命令，单步执行
```

实例声明如下

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13
```
