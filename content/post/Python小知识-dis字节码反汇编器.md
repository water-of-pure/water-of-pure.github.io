+++
date = '2025-07-30T11:28:42.130152+08:00'
draft = false
title = 'Python小知识 - dis字节码反汇编器'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

dis字节码反汇编器

这里主要是通过dis类的dis方法

```bash

dis.dis(x=None, *, file=None, depth=None)
```

官方解释如下：

反汇编 *x* 对象。 *x* 可以表示模块、类、方法、函数、生成器、异步生成器、协程、代码对象、源代码字符串或原始字节码的字节序列。对于模块，它会反汇编所有功能。对于一个类，它反汇编所有方法（包括类和静态方法）。对于代码对象或原始字节码序列，它每字节码指令打印一行。它还递归地反汇编嵌套代码对象（推导式代码，生成器表达式和嵌套函数，以及用于构建嵌套类的代码）。在被反汇编之前，首先使用 [`compile()`](https://docs.python.org/zh-cn/3/library/functions.html#compile) 内置函数将字符串编译为代码对象。如果未提供任何对象，则此函数会反汇编最后一次回溯。

下面看个实例方法

```python

import dis

def greet(name):
    return 'Hello,' + name + '!'

dis.dis(greet)
```

运行后得到的结果如下

```bash

 15           0 LOAD_CONST               1 ('Hello,')
              2 LOAD_FAST                0 (name)
              4 BINARY_ADD
              6 LOAD_CONST               2 ('!')
              8 BINARY_ADD
             10 RETURN_VALUE
```
