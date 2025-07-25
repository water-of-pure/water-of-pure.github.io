+++
date = '2025-07-25T15:09:56.379394+08:00'
draft = false
title = 'Python 入门基础知识 - pdb设置硬断点'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**设置硬断点**

在Python中可以使用pdb模块的set\_trace函数在脚本中设置硬断点。set\_trace函数一般在".py"脚本中使用。

其函数原型如下所示：

> set\_trace()

实例演示如下：

```py
import pdb  # 导入pdb模块
pdb.set_trace()  # 使用set_trace函数设置硬断点
for i in range(1, 10):
    i = i * 5
    print(i)
```

运行脚本后如下所示

```bash
> /Users/durban/python/practise/test.py(12)<module>()
-> for i in range(1, 10):
(Pdb) list
  7  	# 其函数原型如下所示：
  8  	# set_trace()
  9  	import pdb  # 导入pdb模块
 10
 11  	pdb.set_trace()  # 使用set_trace函数设置硬断点
 12  ->	for i in range(1, 10):
 13  	    i = i * 5
 14  	    print(i)
 15
 16  	# 运行脚本后如下所示
[EOF]
(Pdb) n
> /Users/durban/python/practise/test.py(13)<module>()
-> i = i * 5
(Pdb) list
  8  	# set_trace()
  9  	import pdb  # 导入pdb模块
 10
 11  	pdb.set_trace()  # 使用set_trace函数设置硬断点
 12  	for i in range(1, 10):
 13  ->	    i = i * 5
 14  	    print(i)
 15
 16  	# 运行脚本后如下所示
[EOF]
(Pdb) continue
5
10
15
20
25
30
35
40
45  

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
