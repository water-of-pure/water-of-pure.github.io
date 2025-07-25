+++
date = '2025-07-25T15:09:24.820012+08:00'
draft = false
title = 'Python 入门基础知识 - 异常与调试'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**异常与调试**

异常通常是脚本在运行过程中引发的错误。如果在脚本中未包含有关异常处理的代码，那么脚本将终止运行。

在Python中可以为脚本添加异常处理，以应对可能出现的错误，从而使脚本更'健壮'。

**捕获异常**

在脚本运行的过程中常见的异常有除零、下标越界等。在Python中可以捕获这些异常，并编写相关异常的处理语句。

**使用try语句**

在Python中可以使用try语句来处理异常。和Python中其他语句一样，try语句也要使用缩进结构。try语句也有

一个可选的else语句块。一般的try语句形式如下所示。

```py
try:
  <语句> # 要进行捕捉的语句
except <异常名1>: # 要进行处理的语句
  <语句> # 对异常进行处理的语句
except <异常名2>: # 要进行处理的异常
  <语句> # 对异常进行处理的语句
else:
  <语句> # 如果异常未捕获，则执行该语句
```

执行过程如下

```bash
                                   |--- 引发异常1 ---> 异常1处理语句 ---
                                   |                                |
                                   |                                |
开始 ---> 其他语句 ---> try语句块|--- 未引发异常 ---> else语句块 ---> 其他语句 --->结束
                                   |                                |
                                   |                                |
                                   |--- 引发异常2 ---> 异常2处理语句 ---
```

try语句还有还有一种不包含except和else语句的特殊形式。其形式如下所示

```py
try:
  <语句>
finally:
  <语句>
```

不管try语句块中是否发生异常，都将执行finally语句块。

实例演示如下：

```py
l = [1, 2, 3]
print(l[5])
```

会遇到如下错误

```bash
IndexError: list index out of range
```

```py
try:
    print(l[5])
except:
    print('Error')
else:
    print('No Error')
```

运行上面的代码会输出如下内容

```bash
Error
```

```py
try:
    print(l[2])
except:
    print('Error')
else:
    print('No Error')
```

运行上面的代码会输出如下内容

```bash
3
No Error
```

```py
try:
    l[2] / 0
except IndexError:
    print('Error')
else:
    print('No Error')
```

上面这段代码运行后会遇到如下错误

```bash
ZeroDivisionError: integer division or modulo by zero
```

```py
try:
    l[2] / 0
except IndexError:
    print('IndexError')
except ZeroDivisionError:
    print('ZeroDivisionError')
else:
    print('No Error')
```

运行后会输出如下结果

```bash
ZeroDivisionError
```

```py
try:
    print(l[2])
finally:
    print('A')
```

会输出如下

```bash
3
A
```

```py
try:
    print(l[5])
finally:
    print('A')
```

会抛出异常并输出'A'

```bash
IndexError: list index out of range
A
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
#
# Python 2.7.13  

```
