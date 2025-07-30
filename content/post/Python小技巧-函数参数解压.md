+++
date = '2025-07-30T10:40:54.382971+08:00'
draft = false
title = 'Python小技巧 - 函数参数解压'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

函数参数解压

一个非常方便传递参数的功能

看下实例代码

```python

def my_func(a, b, c):
    print(a)
    print(b)
    print(c)
    print(a, b, c)

tuple_value = (1, 2, 3)
dict_value = {'a': 1, 'b': 2, 'c': 3}

my_func(*tuple_value)
my_func(*dict_value)
my_func(**dict_value)
```

运行后结果如下

```bash

1
2
3
1 2 3
a
b
c
a b c
1
2
3
1 2 3
```

当我们使用字典参数的时候，需要注意的是，字典中必须包含对应的参数key，而且键值个数必须跟参数相对应，键值的前后顺序可以不同

看下面错误的例子

```python

def my_func(a, b, c):
    print(a)
    print(b)
    print(c)
    print(a, b, c)

dict_wrong_1_value = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_wrong_2_value = {'a': 1, 'b': 2, 'd': 4}

my_func(**dict_wrong_1_value)
my_func(**dict_wrong_2_value)
```

运行后会得到如下的错误

```bash

Traceback (most recent call last):
  File "main.py", line 24, in <module>
    my_func(**dict_wrong_1_value)
TypeError: my_func() got an unexpected keyword argument 'd'
```