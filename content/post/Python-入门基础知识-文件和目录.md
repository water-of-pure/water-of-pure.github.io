+++
date = '2025-07-25T15:54:48.205270+08:00'
draft = false
title = 'Python 入门基础知识 - 文件和目录'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**文件和目录**

**文件目录常用函数**

在进行文件和目录操作的时候，一般会用到以下几种函数

1，获取当前路径

在Python中可以使用os.getcwd()函数获得当前目录的路径。其原型如下所示。

```bash
os.getcwd()
```

该函数不需要传入参数，他返回当前目录。需要说明的是，当前目录并不是指脚本所在的目录，而是所运行脚本的目录。

示例如下

```py
import os
print('current directory %s' % os.getcwd())
```

运行后结果输出如下

```bash
current directory /Users/durban/python/practise
```

2，获得目录中的内容

在Python中可以使用os.listdir()函数获得指定目录中的内容，其原型如下

> os.listdir(path)

其参数含义如下

> path: 要获得内容目录的路径

示例如下

```py
import os
print(os.listdir(os.getcwd()))
```

运行后输出如下

```bash
['base_phrase.py', 'base_practise.py', 'module', 'pdb_test.py', 'test.py', 'usemodule.py', 'usemodule.pyo']
```

3，创建目录

在Python中可以使用os.mkdir()函数创建目录，其原型如下所示

> os.mkdir(path)

其参数函数如下

> path 要创建目录的路径

示例如下

```py
import os
os.mkdir('/Users/durban/python/practise/temp')
```

4，删除目录

在Python中删除目录可以使用os.rmdir函数删除目录。其原型如下

> os.rmdir(path)

其参数含义如下

> path 要删除的目录的路径

示例如下

```py
import os
os.rmdir('/Users/durban/python/practise/temp')
```

需要注意的是，使用os.rmdir()删除目录的时候，目录必须为空，否则会报错

5，判断目录是否存在

在Python中可以使用os.path.isdir()函数判断某一路径是否是目录。

其原型如下

> os.path.isdir(path)

其参数含义如下

> path: 要进行判断的路径

示例如下

```py
import os
print(os.path.isdir('/Users/durban/python/practise/module')) # 一个存在的目录
```

运行结果如下

```bash
True
```

6，判断是否是文件

在Python中os.path.isfile()函数可以判断一个目录是否是文件，其函数原型如下

> os.path.isfile(path)

其参数含义如下

> path: 要进行判断的路径

示例如下

```py
import os
print(os.path.isfile('/Users/durban/python/practise/module'))  # 一个目录
```

结果输出如下

```bash
False
```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13
```
