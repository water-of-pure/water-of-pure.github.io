+++
date = '2025-07-25T15:09:41.740690+08:00'
draft = false
title = 'Python 入门基础知识 - 自定义异常类'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

自定义异常类

在Python中可以通过继承Exception类来创建自己的异常类。异常类和其他的类并没有区别，一般仅有在

异常类中定义几个属性信息。

实例如下

```py
class CustomError(Exception):
    def __init__(self, data):  # 重载__init__方法
        self.data = data

    def __str__(self):  # 重载__str__方法
        return self.data

```

```bash
raise CustomError, 'Error'
```

异常输出如下

```bash
    raise CustomError, 'Error'
__main__.CustomError: Error
```

```bash
try:
    raise CustomError, 'Raise CustomError'
except CustomError, data:
    print(data)
else:
    print('No Error')
```

输出如下

```bash
Raise CustomError
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
