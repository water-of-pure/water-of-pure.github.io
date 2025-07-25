+++
date = '2025-07-25T15:09:45.069762+08:00'
draft = false
title = 'Python 入门基础知识 - 使用pdb调试Python脚本'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用pdb调试Python脚本**

在Python中脚本的语法错误可以被Python解释器发现，但是脚本逻辑上的错误，或者其他的一些变量使用错误却不容易被发现。

如果脚本运行后没有获得预想的结果，则需要对脚本进行调试。pdb模块是Python自带的调试模块。使用该模块可以为脚本设置

断点、单步执行、查看变量值等。pdb模块可以以命令行参数的形式启动，也可以通过import将其导入使用。

通过import导入pdb模块后，就可以使用pdb模块的函数对脚本进行调试。常用的pdb模块的函数可以分为以下几类。

**运行语句**

在Python中可以使用pdb模块的run函数来调试语句块。其参数原型如下所示。

> run(statement[, globals[, locals]])

其参数如下。

> statement: 要调试的语句块，以字符串的形式
>
> globals: 可选参数，设置statement运行的全局环境变量
>
> locals: 可选参数，设置statement运行的局部环境变量

以下实例使用run函数调试语句块。

```py
import pdb
pdb.run('''
for i in range(0, 3):
    i = i ** 2
    print(i)
''')
```

运行后得到如下

```bash
> <string>(2)<module>()
(Pdb) n # "(Pdb)"为调试命令提示符，表示可以输入调试命令
> <string>(3)<module>()
(Pdb) n # 执行下一行
> <string>(4)<module>()
(Pdb) n
0
> <string>(2)<module>()
(Pdb) n
> <string>(3)<module>()
(Pdb) n
> <string>(4)<module>()
(Pdb) n
1
> <string>(2)<module>()
(Pdb) print(i) # print打印变量i值
1
(Pdb) continue # 继续运行程序
4
```

实力环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
