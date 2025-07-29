+++
date = '2025-07-29T10:56:35.427206+08:00'
draft = false
title = 'Python3如何捕获异常并输出异常错误信息'
categories = [
    "技术",

]

tags = [
    "Python3",

]
+++

最近在Python3环境中使用Flask，写代码的过程中，遇到一个捕获异常的代码

```py

try:
    open('xxx')
except OSError, e:
    print(e)

```

代码类似如上，其实就是需要捕获一个文件打开的异常，但是我想要获取这个异常的详细信息，但是在Python3下面运行报出了语法异常

```bash

SyntaxError: invalid syntax

```

但是代码改为下面的形式就会发现，异常能够正常捕获，并能够输出正常的异常详细信息

```py

try:
    open('xxx')
except OSError as e:
    print(e)

```

就可以正常捕获到详细的输出

```bash

[Errno 2] No such file or directory: 'xxx'

```

查了下文档原来

```bash

Exception, e

```

是在Python 2.x的版本中使用

```bash

Exception as e

```

是在Python 3.x的版本中使用

其他获取异常详细信息的方式

1、 sys.exc\_info() 和 sys.last\_traceback

sys.last\_traceback 包含的内容与 sys.exc\_info() 相同，但它主要用于调试，并不总是被定义

sys.exc\_info() 会返回一个3值元表，其中包含调用该命令时捕获的异常。 这个元表的内容为 (type, value, traceback) ，其中：

* type 从获取到的异常中得到类型名称，它是BaseException 的子类；
* value 是捕获到的异常实例；
* traceback 是一个 traceback 对象。

示例如下

```py

import sys
try:
    open('xxx')
except OSError as e:
    t,v,tb = sys.exc_info()
    print(t,v)

```

关于sys.last\_traceback，这里有其具体的使用方式 https://www.programcreek.com/python/example/3893/sys.last\_traceback

2、使用 traceback trackback 模块用来精确模仿 python3 解析器的 stack trace 行为。在程序中应该尽量使用这个模块。 traceback.print\_exc() 可以直接打印当前的异常。

```py

import traceback
try:
    open('xxx')
except OSError as e:
    traceback.print_exc()

```

traceback.print\_tb() 用来打印上面提到的 trackback 对象。

```py

import sys,traceback
try:
    open('xxx')
except OSError as e:
    t,v,tb = sys.exc_info()
    traceback.print_tb(tb)

```

traceback.print\_exception() 可以直接打印 sys.exc\_info() 提供的元表。

```py

import sys,traceback
try:
    open('xxx')
except OSError as e:
    traceback.print_exception(*sys.exc_info())

```

具体文档可以参考这里： https://docs.python.org/3/library/traceback.html?highlight=print\_tb#module-traceback
