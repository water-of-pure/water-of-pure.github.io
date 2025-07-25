+++
date = '2025-07-25T15:09:08.949292+08:00'
draft = false
title = 'Python 入门基础知识 - 类的继承'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**类的继承**

一个新类可以通过继承来获得已有类的方法以及属性等。通过继承而来的类也可以自己定义新的方法或者属性。

**通过创建继承类**

在类的定义中已经提到如何通过继承来获得一个新类。新类可以继承公类的公有属性和公有方法，但是不能继承

父类的私有属性和私有方法。

实例如下：

```py
class book:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = 0

    def __check(self, item):
        if item == '':
            return 0
        else:
            return 1

    def show(self):
        if self.__check(self.__author):
            print(self.__author)
        else:
            print('No Value')

        if self.__check(self.__name):
            print(self.__name)
        else:
            print('No Value')

    def setname(self, name):
        self.__name = name

    def __init__(self, author, name):
        self.__author = author
        self.__name = name

class student(book):
    __class = ''
    __grade = ''
    __sname = ''

    def showinfo(self):
        self.show()

b = student('John', 'A Great Book')
b.showinfo()
# John
# A Great Book  

```

如果在定义类的时候，试图使用父类的私有属性或者私有方法将会导致错误，如下：

```py
class student(book):

    def showall(self):
        if self.__check(self.__name):
            print(self.__name)
        else:
            print('No Value')

c = student('John', 'A Great Book')
# c.showall()
# 会遇到如下错误：
# AttributeError: student instance has no attribute '_student__check'  

```

多重继承

多重继承是指创建的类同时拥有几个类的属性和方法。多重继承与单重继承不同的是在类名后边的圆括号中包含多个父类名，

父类名以逗号隔开。通过多重继承创建一个新类的一般形式如下所示：

> class <新类名>(父类1，父类2，....，父类n):
>
>   <语句1>
>
>   <语句2>
>
>   ...
>
>   <语句n>

使用多重继承需要注意圆括号中父类名字的顺序。如果父类中有相同的方法名，而在类中使用时未指定父类名，Python解释器

将从左到右搜索。示例如下：

```py
class A:
    name = 'A'
    __num = 1
    def show(self):
        print(self.name)
        print(self.__num)
    def setnum(self, num):
        self.__num = num
class B:
    nameb = 'B'
    __numb = 2
    def show(self):
        print(self.nameb)
        print(self.__numb)
    def setname(self, name):
        self.nameb = name
class C(A, B):
    def showall(self):
        print(self.name)
        print(self.nameb)
c = C()
c.showall()
# A
# B

c.show()
# A
# 1

c.setnum(3)
c.show()
# A
# 3

c.setname('D')
c.showall()
# A
# D
```

如果需要在类C中使用类B的show方法，可以按如下实例操作：

```py
class C(A, B):

    def showall(self):
        print(self.name)
        print(self.nameb)

    show = B.show

c = C()
c.show()
# B
# 2  

```

实例环境如下

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
