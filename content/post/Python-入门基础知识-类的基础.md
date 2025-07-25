+++
date = '2025-07-25T14:10:56.972764+08:00'
draft = false
title = 'Python 入门基础知识 - 类的基础'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**类的基础**

由于Python面向对象程序设计的良好支持，在Python中定义和使用类并不复杂。类的定义和使用与函数的定义和使用有很多相似的地方。

**类的定义**

在Python中类的定义与函数的定义类似，不同的是，类的定义使用关键字"class"。与函数定义相同。在定义类的时候也要使用缩进以

表示缩进的语句属于该类。一般的类的定义形式如下所示：

> class <类名>:
>
>   <语句1>
>
>   <语句2>
>
>   ...
>
>   <语句3>

与函数定义一样，在使用类之前必须先定义类。类的定义一般放在脚本的头部。在Python中也可以在if语句的分之中或者函数定义中定义类。

以下实例定义一个human类，并定义了相关属性。

```py
class human:
    age = 0
    sex = ''
    height = ''
    weight = ''
    name = ''  

```

类还可以通过继承的形式获得。通过类继承来定义类的基本形式如下所示。

> class <类名>(父类名):
>
>   <语句1>
>
>   <语句2>
>
>   ...
>
>   <语句3>

其中园括号中的父类名就是要继承的类。关于继承将在后面的文章介绍，此处给出一个简单的实例，实例如下：

```py
class student(human):
    school = ''
    number = ''
    garde = ''  

```

上述通过human继承而来的student类具有human类的属性，并且又为student类定义了其他的属性。

类定义后就产生了一个名字空间，与函数类似。在类内部使用的属性，相当于函数的变量名，还可以在类的外部继续使用。

类的内部与函数的内部一样，相当于一个局部作用域。不同类的内部也可以使用相同的属性名。

**类的使用**

类在定义后必须先实例化才能使用。类的实例化与函数调用类似，只要使用类名加圆括号的形式就可以实例化一个类。类

实例话以后会生成一个对象。一个类可以实例化多个对象，对象与对象之间并不相互影响。类实例化以后可以使用其属性和

方法等。以下实例首先定义一个book类，然后将其实例化。

```py
class book:
    author = ''
    name = ''
    pages = 0
    price = 0
    press = ''

a = book()
print(a)
# <__main__.book instance at 0x10769fef0>

print(a.author)
print(a.pages)
print(a.price)
a.author = 'John'
a.pages = 300
a.price = 25
print(a.author)
print(a.pages)
print(a.price)
#  # 空字符串
# 0
# 0
# John
# 300
# 25

b = book()
print(b)
# <__main__.book instance at 0x105c7de18>

print(b.author)
print(b.price)
b.author = 'Json'
b.price = 10
print(b.author)
print(b.price)
print(a.price)  # a对象的price属性并没有改变
print(a.author)  # a对象的author属性也没有改变
print(b.pages)  # 访问b对象的pages属性
print(a.pages)  # 访问a对象的pages属性
#  # 空字符串
# 0
# Json
# 10
# 25
# John
# 0
# 300  

```

上述例子只定义了类的属性，并在类实例化以后重新设置其属性，从上例可以看出类的实例化相当于调用一个函数，这个函数就是类。

函数返回一个类的实例对象，返回后的对象就具有了类所定义的属性。上述例子生成了两个book实例对象，可以看到，设置其中一个

对象的属性，并不影响另一个对象的属性。

在Python中需要注意的是，虽然类首先需要实例化，然后才能使用其属性。而实际上当创建一个类以后就可以通过类名访问其属性。

如果直接使用类名修改器属性，那么将影响已经实例化的对象。

```py
class A:
    name = 'A'
    num = 2

print(A.name)
print(A.num)
# A
# 2

a = A()
print(a.name)
# A

b = A()  # 生成b对象
print(b.name)  # 查看b的name属性
# A

A.name = 'B'  # 使用类名修改name属性

print(a.name)  # a对象的name属性被修改
print(b.name)  # b对象的name属性被修改  

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
