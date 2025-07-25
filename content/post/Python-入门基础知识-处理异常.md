+++
date = '2025-07-25T15:09:27.872919+08:00'
draft = false
title = 'Python 入门基础知识 - 处理异常'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**处理异常**

在except中可以捕获指定的异常。除此之外，except语句还可以捕获异常的附加数据。

Python中常用的内置异常如下

> AttributeError 调用不存在的方法引发的异常
>
> EOFError 遇到文件末尾引发的异常
>
> ImportError 导入模块出错引发的异常
>
> IndexError 列表越界引发的异常
>
> IOError I/O操作引发的异常，如打开文件出错等
>
> KeyError 使用字典中不存在的关键字引发的异常
>
> NameError 使用不存在的变量名引发的异常
>
> TabError 语句块缩进不正确引发的异常
>
> ValueError 搜索列表中不存在的值引发的异常
>
> ZeroDivisionError 除数为零引发的异常

except语句主要有以下几种用法。

```py
except:
except <异常名>:
except (异常名1,异常名2):
except <异常名>, <数据>:
except (异常名1,异常名2), <数据>:
```

以下实例使用except捕获异常

```py
l = [1, 2, 3]
```

```py
try:
    l[5]
except IndexError, Error:
    print Error
else:
    print('No Error')
```

以下代码运行后会输出如下

```bash
list index out of range
```

```py
try:
    l[5] / 0
except:
    print('Error')
else:
    print('No Error')
```

运行上段代码会输出如下内容

```bash
Error
```

```py
try:
    l[2] / 0
except (IndexError, ZeroDivisionError), value:
    print(value)
```

# 运行上段代码会得到如下输出

```bash
integer division or modulo by zero
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
