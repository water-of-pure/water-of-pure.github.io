+++
date = '2025-07-25T15:09:16.778747+08:00'
draft = false
title = 'Python 入门基础知识 - 重载'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**重载**

重载允许通过继承而创建的类重新定义父类的方法。不仅可以重载方法，而且还可以重载运算符，例如"+"、"\*"等，

以适用自创建的类。

**方法重载**

通过继承而创建的类，其父类的方法不一定能满足类的需求。新类实际上只是修改部分功能，为了避免命名函数的麻烦，可以使用方法重载来解决。

或者，新类需要重新初始化，此时就可以重载\_\_init\_\_方法来实现。

方法的重载实际上就是在类中使用def关键字重载父类的方法。如果重载父类中的方法，但又需要在类中先使用父类的该方法，可以使用父类加"."加方法名的形式调用。

例如重载"\_\_init\_\_"方法时，而父类也需要使用\_\_init\_\_方法，则可以在\_\_init\_\_前加上父类名来调用该方法。

如下实例演示

```py
class human:
    __age = 0
    __sex = ''
    __height = ''
    __weight = ''
    name = ''

    def __init__(self, age, sex, height, weight):
        self.__age = age
        self.__sex = sex
        self.__height = height
        self.__weight = weight

    def setname(self, name):
        self.name = name

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.__sex)
        print(self.__height)
        print(self.__weight)

class student(human):
    __classes = ''
    __grade = ''
    __num = 0

    def __init__(self, classes, grade, num, age, sex, height, weight):
        self.__classes = classes
        self.__grade = grade
        self.__num = num
        human.__init__(self, age, sex, height, weight)

    def show(self):
        human.show(self)
        print(self.__classes)
        print(self.__grade)
        print(self.__num)

a = student('小学', '大班', '20171128', 12, '男', 140, 40)
a.setname('John')
a.show()

```

输出结果如下

```bash
# John
# 12
# 男
# 140
# 40
# 小学
# 大班
# 20171128
```

**运算符重载**

在Python中运算符重载不需要像在C++中那样使用operator关键字。由于在Python中，运算符都有其相对应的函数。在类中，运算符对应类的专有方法。因此运算符的重载

实际上是对运算符对应的专有方法的重载。

部分运算符和类的专有方法对应表如下：

> 运算符|专有方法
>
> + | \_\_add\_\_
>
> - | \_\_sub\_\_
>
> \* | \_\_mul\_\_
>
> / | \_\_div\_\_
>
> % | \_\_mod\_\_
>
> \*\* | \_\_pow\_\_

实例演示如下

```py
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

l = ListExample(1, 2, 3, 4, 5)
l.show()
# [1, 2, 3, 4, 5]
l + 5
l.show()
# [6, 7, 8, 9, 10]
l - 3
l.show()
# [3, 4, 5, 6, 7]
l * 3
l.show()
# [9, 12, 15, 18, 21]
l / 3
l.show()
# [3, 4, 5, 6, 7]
l % 3
l.show()
# [0, 1, 2, 0, 1]
l ** 3
l.show()
# [0, 1, 8, 0, 1]
print(len(l))
# 5
b = ListExample(2, 3, 4, 5, 6, 7, 8)
b.show()
# [2, 3, 4, 5, 6, 7, 8]
b - 5
b.show()
# [-3, -2, -1, 0, 1, 2, 3]  

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
