+++
date = '2025-07-25T14:09:55.798688+08:00'
draft = false
title = 'Python 入门基础知识 - 模块'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**模块**

Python中的模块实际上就是包含函数或者类的Python脚本。它是以.py为后缀，也就是Python脚本的后缀名。

用作模块的Python脚本与其他的脚本并没有什么区别。

在Python中通过导入模块，然后使用模块中提供的函数或者数据。

1，模块导入

在Python中可以使用以下两种方法导入模块或者模块中的函数

> import: 模块名
>
> import: 模块名 as 新名字
>
> from: 模块名 import 函数名

其中使用import是将整个模块导入，而使用from则是将模块中的某一个函数或者名字导入，而不是整个模块。

使用import和from导入模块还有一个不同之处：使用import导入模块时，要使用模块中的函数，则必须以

模块名加"."然后是函数名的形式调用函数；而使用from导入模块时，则可以直接使用模块中的函数名调用函数。

如下：

```py
import string  # 使用import导入string模块
print(string.capitalize('use modules'))  # 使用string模块中的capitalize函数
```

```py
capitalize('use modules')  # 直接使用capitalize名字调用函数，函数会调用失败
```

报错如下

> NameError: name 'capitalize' is not defined

```bash
from math import sqrt  # 使用from导入math模块中的sqrt函数
print(sqrt(9))  # 直接使用sqrt名字调用函数
```

```bash
print(math.sqrt(9)) # 错误的调用方式
```

会报错如下

> NameError: name 'math' is not defined

当需要使用模块中的函数时，使用from导入模块要方便的多，不用在调用函数时使用模块名。如果需要使用模块中的所有函数，

则可以在from中使用"\*"通配符，表示导入模块中的函数。

如下：

```py
from string import capitalize  # 仅从string模块中导入capitalize
print(capitalize('use modules'))
```

```py
print(split('use modules')) # 调用string模块中的split函数时会出错
```

会报错如下：

> NameError: name 'split' is not defined

```py
from string import *  # 重新从string模块中导入所有函数
print(split('use modules'))  # 重新调用split函数
```

在Python中还可以通过使用内置函数reload重新载入模块。reload可以在模块被修改的情况下不必关闭Python而重新载入模块。

在使用它重载模块时，该模块必须已经事先被导入。

2，编写模块

编写模块很简单，以下实例，在模块中包含一个函数，这个函数值打印"我是一个模块"。将该模块保存为testmodule.py。代码如下：

```py
# -*- coding:utf-8 -*-
def show():
    print('我是一个模块')
```

编写一个调用函数show的脚本，将其保存为usemodule.py。代码如下：

```py
# -*- coding:utf-8 -*-
import testmodule
testmodule.show()
```

脚本运行后输出如下

```bash
我是一个模块
```

除了在模块中声明函数，还可以声明变量。

模块中的变量同样可以在其他脚本中使用。

在testmodule.py的模块中添加一个变量，如下

```py
name = 'testmodule.py'
```

在usemodule.py中添加如下代码

```py
# -*- coding:utf-8 -*-
import testmodule
testmodule.show()

print(testmodule.name)

testmodule.name = 'usemodule.py'
print(testmodule.name)

```

脚本运行后输出如下

```bash
我是一个模块
testmodule.py
usemodule.py
```
