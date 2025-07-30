+++
date = '2025-07-30T10:40:24.009000+08:00'
draft = false
title = 'Python小知识 - 什么是Namedtuples，如何使用Namedtuples'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "Namedtuples"
]
+++

什么是Namedtuples，如何使用Namedtuples

Namedtuples是一个轻量的并且很容易创建的对象类型

Namedtuples的实例可以像对象实例一样使用

Namedtuples跟struct很像

Namedtuples是不可变的

Namedtuples类型被添加在Python 2.6 和 Python 3.0

下面看个例子

```python

from math import sqrt

p1 = (1, 2)
p2 = (2, 3)

line_length = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print(line_length)
```

如果使用Namedtuples，上面代码的可读性将会稍微有些改善

下面看代码

```python

from math import sqrt
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(1, 2)
p2 = Point(2, 3)

line_length = sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

print(line_length)
```

Namedtuples也兼容了第一个例子中的使用方式，代码如下

```python

from math import sqrt
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(1, 2)
p2 = Point(2, 3)

line_length = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print(line_length)
```

`Point = namedtuple('Point', ['x', 'y'])`

这段代码也可以用下面的方式来声明

`Point = namedtuple('Point', ('x y'))`

用个例子来说明下

```python

from math import sqrt
from collections import namedtuple

Point = namedtuple('Point', ('x y'))

p1 = Point(1, 2)
p2 = Point(2, 3)

line_length = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

print(line_length)
```

再来看下，Namedtuples是如何不可变的

示例如下

```python

from collections import namedtuple

Point = namedtuple('Point', ('x y'))

p = Point(1, 2)

p.x = 3
```

运行结果报错如下

```bash

Traceback (most recent call last):
  File "main.py", line 95, in <module>
    p.x = 3
AttributeError: can't set attribute
```

参考文章：[地址](https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python)
