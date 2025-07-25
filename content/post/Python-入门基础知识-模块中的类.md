+++
date = '2025-07-25T15:09:20.072564+08:00'
draft = false
title = 'Python 入门基础知识 - 模块中的类'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**模块中的类**

类与函数一样，也可以写到模块中。在其他脚本中可以通过导入模块名使用定义的类。

模块中类的使用方式与模块中的函数类似。实际上可以将模块中的类当做函数一样使用。将上一篇文章中定义的LiseExample类整理后保存到ListExample中。

如下所示 :

```py
# _*_ coding: utf-8 -*-
# Filename : ListExample.py

class ListExample:
    __list = []

    def __init__(self, *args):
        self.__list = []
        for arg in args:
            self.__list.append(arg)

    def __add__(self, n):
        for i in range(0, len(self.__list)):
            self.__list[i] = self.__list[i] + n

    def __sub__(self, n):
        for i in range(0, len(self.__list)):
            self.__list[i] = self.__list[i] - n

    def __mul__(self, n):
        for i in range(0, len(self.__list)):
            self.__list[i] = self.__list[i] * n

    def __div__(self, n):
        for i in range(0, len(self.__list)):
            self.__list[i] = self.__list[i] / n

    def __mod__(self, n):
        for i in range(0, len(self.__list)):
            self.__list[i] = self.__list[i] % n

    def __pow__(self, n):
        for i in range(0, len(self.__list)):
            self.__list[i] = self.__list[i] ** n

    def __len__(self):
        return len(self.__list)

    def show(self):
        print(self.__list)

```

然后在编写一个UseListExample.py的脚本，使用ListExample.py中的ListExample类。实例代码如下

```py
# _*_ coding: utf-8 -*-
# 
# Filename: UseListExample.py

import ListExample

l = ListExample.ListExample(1, 2, 3, 4, 5)
l.show()

l + 10
l.show()

l * 2
l.show()

print(len(l))

l ** 3
l.show()

```

结果输出如下

```bash
# [1, 2, 3, 4, 5]
# [11, 12, 13, 14, 15]
# [22, 24, 26, 28, 30]
# 5
# [10648, 13824, 17576, 21952, 27000]
```
