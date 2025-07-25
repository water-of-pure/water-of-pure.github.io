+++
date = '2025-07-25T14:10:59.642614+08:00'
draft = false
title = 'Python 入门基础知识 - 类的属性和方法'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**类的属性和方法**

每一个类都有自己的属性和方法。属性和方法是面向对象程序设计所独有的概念。属性是类所封装的数据，而方法则是类对数据进行的操作。

**类的属性**

在上一篇文章中简单的定义和使用了类的属性。类的属性实际上是类内部的变量。上一篇文章的例子使用了类的属性，确切的说，称作类的

公有属性。在上篇文章中在类的外部设置了其属性的值，在某些情况下可能不希望在类的外部多其属性进行操作，此时就可以使用类的私有

属性。

数据保护是面向对象程序设计所特有的，在面向过程的程序设计中并没有数据保护的概念。在Python中与C++不同，在类的内部声明一个私有

成员不需要使用private关键字。在Python中，是通过类中属性的命名形式来表示类属性是公有还是私有的。类中的私有属性是不能在类的外部

进行操作的，这种方式起到了对属性的保护作用。

在Python中，如果类中的属性是以两条下划线开始的话，则该属性为类的私有属性，不能在类的外部被使用或者访问。

下面为一个私有属性的命名方式

> \_\_private\_attre # 以双下划线开始

如果在类内部的方法中使用类的私有属性，则应该以如下的方式调用：

> self.\_\_private\_attre # 应该在私有属性名钱加上"self."

实例如下：

```py
class book:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = ''

a = book()
# a.__author # 调用属性 __author
# 会跑出如下异常信息
# AttributeError: book instance has no attribute '__author'

print(a.price)
# 0

a.price = 20
print(a.price)
# 20

# print(a.__name)
# 报错内容如下：
# AttributeError: book instance has no attribute '__name'

# print(a.__page)
# 报错内容如下：
# AttributeError: book instance has no attribute '__page'  

```

可以看到，在类的定义的时候，凡是两条下划线开始的属性不能在类的外部访问，当然也不能修改。如果要修改类的私有属性值或者获取其值，

可以通过使用提供的方法来完成。

**类的方法**

类的方法实际上就是类内部使用def关键字定义的函数。定义类的方法与定义一个函数基本相同，在类的方法中同样也要使用缩进。

**1、定义类的方法**

在类的内部使用def关键字可以为类定义一个方法。与函数定义不同的是，类的方法必须包含函数"self"，且"self"必须为第一个参数。

实例如下：

```py
class book:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = ''

    def show(self):
        print(self.__author)
        print(self.__name)

    def setname(self, name):
        self.__name = name

a = book()
a.show()
a.setname('John')
a.show()  # 这里会输出"John"  

```

与类的属性相同，类的方法也可以是类私有的，类的私有方法不能在类的外部调用。和类的私有属性命名相同，类的私有方法名也要

以两条下划线开始。类的私有方法只能在类的内部调用，而不能在类的外部调用。另外，在类的内部调用其私有方法，要使用"self.私有方法名"的形式。实例代码如下

```py
class book:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = ''

    def __check(self, item):
        if item == '':
            return 0
        else:
            return 1

    def show(self):
        if self.__check(self.__author):
            print(self.__author)
        else:
            print('No value')

        if self.__check(self.__name):
            print(self.__name)
        else:
            print('No value')

    def setname(self, name):
        self.__name = name

a = book()
a.show()
a.setname('John')
a.show()
# a.__check() # 调用类的私有方法，结果出错
# 报错内容如下；
# AttributeError: book instance has no attribute '__check'  

```

**2、类的专有方法**

在Python中有一类似以两条下划线开始并且以两条下划线结束的类的方法，称之为类的专有方法。专有方法是针对类的特殊操作。

例如，在类实例化时将调用\_\_init\_\_方法。部分类的专有方法如下：

> \_\_init\_\_ 构造函数，生成对象时调用
>
> \_\_del\_\_ 析构函数，释放对象时调用
>
> \_\_add\_\_ 加运算
>
> \_\_mul\_\_ 乘运算
>
> \_\_cmp\_\_ 比较运算
>
> \_\_repr\_\_ 打印、转换
>
> \_\_setitem\_\_ 按照索引赋值
>
> \_\_getitem\_\_ 按照索引获取值
>
> \_\_len\_\_ 获得长度
>
> \_\_call\_\_ 函数调用

实例演示如下：

```py
class book:
    __author = ''
    __name = ''
    __page = 0
    price = 0
    __press = ''

    def __check(self, item):
        if item == '':
            return 0
        else:
            return 1

    def show(self):
        if self.__check(self.__author):
            print(self.__author)
        else:
            print('No value')

        if self.__check(self.__name):
            print(self.__name)
        else:
            print('No value')

    def setname(self, name):
        self.__name = name

    def __init__(self, author, name):
        self.__author = author
        self.__name = name

a = book('John', 'I like this book')
a.show()
# John
# I like this book
a.setname('About John')
a.show()
# John
# About John  

```

实例环境声明：

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
