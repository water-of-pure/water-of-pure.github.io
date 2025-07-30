+++
date = '2025-07-30T10:40:18.086037+08:00'
draft = false
title = '什么是迭代器，什么是生成器（generator）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "迭代器",
    "生成器"
]
+++

## 迭代器

迭代器是Python中最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历位置的对象。

迭代器对象从集合的第一个元素开始访问，知道所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：`iter()`和`next()`

字符串、列表或元祖对象都可用于创建迭代器

举个例子

```python

list = ['a', 'b', 'c']
list_iter = iter(list)  # 创建迭代器
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
```

迭代器可以使用常规的for语句进行遍历

举个例子

```python

list = ['a', 'b', 'c']
list_iter = iter(list)  # 创建迭代器
for i in list_iter:
    print(i)
```

### 如何创建迭代器

举个例子

```python

import sys

class IncrementNumber(object):
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

num = IncrementNumber()
num_iter = iter(num)
for n in num:
    if n > 100:
        sys.exit()
    else:
        print(n)
```

把一个类作为一个迭代器使用，需要在类中实现两个方法`__iter__()`和`__next__()`

`__iter__()`方法返回一个特殊的迭代器对象，这个迭代器对象实现了\_\_next\_\_方法并通过`StopIteration`异常标识迭代的完成

`__next__()`方法会返回下一个迭代器对象

`StopInteration`异常用于标识迭代的完成，防止出现无限循环的情况，

在`__next__()`方法中我们可以设置在完成指定循环次数后触发`StopIntertion`异常来结束迭代

举个例子

```python

import sys

class IncrementNumber(object):
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num > 50:
            raise StopIteration

        num = self.num
        self.num += 1
        return num

num = IncrementNumber()
num_iter = iter(num)
for n in num:
    if n > 100:
        sys.exit()
    else:
        print(n)
```

### 生成器

生成器是一个返回迭代器的函数

在调用生成器运行的过程中，每次遇到`yield`的时候函数会暂停继续执行并保存当前所有的运行信息，返回`yield`的值，

并在下一次执行`next()`的时候从当前位置继续运行

调用一个生成器函数，返回的是一个迭代器对象

```python

import sys

# 生成器函数
def getNum():
    yield 1
    yield 2
    yield 3

# num 是一个迭代器，由生成器返回生成
num = getNum()

while True:
    try:
        print(next(num))
    except StopIteration:
        sys.exit()
```
