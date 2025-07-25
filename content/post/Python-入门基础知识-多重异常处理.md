+++
date = '2025-07-25T15:09:32.198606+08:00'
draft = false
title = 'Python 入门基础知识 - 多重异常处理'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**多重异常处理**

在Python中可以在try语句中嵌套另外一个try语句。由于Python将try放在堆栈中，一旦引发异常，Python将匹配

最近的except语句。如果except能够处理异常，则外围的try语句将不再不会捕获异常。如果except忽略该异常，

则异常将被外围try语句捕获。

代码实例如下：

```py
l = [1, 2]  # 定义一个列表  

```

```py
try:  # 嵌套try语句
    try:
        l[5]
    except:  # 捕获所有异常
        print('Error1')  # 打印Error1
except:  # 捕获所有异常
    print('Error2')  # 打印Error2
else:
    print('No Error')
```

输出结果如下

```bash
Error1
No Error
```

```py
try:
    try:
        l[1] / 0
    except IndexError:
        print('Error1')
except:
    print('Error2')
else:
    print('No Error')
```

输出结果如下

```bash
Error2
```

```py
try:
    try:
        l[1] / 's'
    except IndexError:
        print('Error1')
except ZeroDivisionError:
    print('Error2')
else:
    print('No Error')  

```

运行代码后会遇到如下错误

```bash
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13
```
