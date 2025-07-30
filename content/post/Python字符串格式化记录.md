+++
date = '2025-07-30T09:56:39.059458+08:00'
draft = false
title = 'Python字符串格式化记录'
categories = [
    "技术",

]

tags = [
    "Python",

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

之前学习Python只是在一些书籍或者是文章中学习，而且是一遍实践一遍学，这样的话，会很容易忽略一些细节的，导致你发现不了Python的强大

最近在看Python的官方文档，看到“字符串格式化”，发现这个格式化使用可以非常灵活

我这里使用的是Python 4.7.4

下面记录下格式化具体可以如何使用，方便日后查找，格式化用起来还是很方便的

* **第一种格式化使用方式 - 按位置访问参数**

```bash

>>> '{0},{1},{2}'.format(1,2,3)
'1,2,3'
>>> '{},{},{}'.format(1,2,3)
'1,2,3'
>>> '{2},{1},{0}'.format(1,2,3)
'3,2,1'
>>> '{2},{1},{0}'.format(*('123'))  # 解包参数序列
'3,2,1'
>>> '{0},{1},{0}'.format('123','45') # 参数的索引可以重复
'123,45,123'

```

* **第二种格式化使用方式 - 按名称访问参数**

```bash

>>> '坐标：{lat},{lon}'.format(lat='37.24N',lon='-155.8W')
'坐标：37.24N,-155.8W'
>>> coord = {'lat':'37.24N','lon':'-155.8W'}
>>> '坐标：{lat},{lon}'.format(**coord)
'坐标：37.24N,-155.8W'
>>>

```

* **第三种格式化使用方式 - 按参数访问参数**

```bash

>>> c = 5-3j
>>> '复数{0}是有实数{0.real}和虚数{0.imag}组成'.format(c)
'复数(5-3j)是有实数5.0和虚数-3.0组成'
>>> class Point():
...     def __init__(self, x, y):
...             self.x, self.y = x, y
...     def __str__(self):
...             return 'Point({self.x}, {self.y})'.format(self=self)
...
>>> str(Point(4, 5))
'Point(4, 5)'

```

* **第四种格式化使用方式 - 按参数的项访问参数**

```bash

>>> point = (3, 5)
>>> 'X: {0[0]}, Y: {0[1]}'.format(point)
'X: 3, Y: 5'

```

* **第五种格式化使用方式 - 替代`%s`和`%r`**

```bash

>>> 'repr() show qoutes:{!r}, str() do not:{!s}'.format("test1","test2")
"repr() show qoutes:'test1', str() do not:test2"

```

*这里的区别就是引号的区别*，test1加了引号，test2没有加引号

* **第六种格式化使用方式 - 对齐文本以及指定宽度**

```bash

>>> '{:<60}'.format('left aligned，length - 60')
'left aligned，length - 60                                    '
>>> '{:>60}'.format('right aligned，length - 60')
'                                   right aligned，length - 60'
>>> '{:^60}'.format('center aligned，length - 60')
'                 center aligned，length - 60                 '
>>> '{:*^60}'.format('center aligned，length - 60')
'*****************center aligned，length - 60*****************'

```

* **第七种格式化使用方式 - 替代 %+f, %-f 和 % f 以及指定正负号**

```bash

>>> '{:+f};{:-f}'.format(3.14, -3.14)
'+3.140000;-3.140000'
>>> '{: f};{: f}'.format(3.14, -3.14)
' 3.140000;-3.140000'
>>> '{: f};{: f}'.format(+3.14, -3.14)
' 3.140000;-3.140000'
>>> '{:-f};{:-f}'.format(3.14, -3.14)
'3.140000;-3.140000'
>>> '{:f};{:f}'.format(3.14, -3.14)
'3.140000;-3.140000'

```

* **第八种格式化使用方式 - 替代 %x 和 %o 以及转换基于不同进位制的值**

```bash

>>> 'int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}'.format(42)
'int: 42; hex: 2a; oct: 52; bin: 101010'
>>> 'int: {0:#d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}'.format(42)
'int: 42; hex: 0x2a; oct: 0o52; bin: 0b101010'
>>>

```

*binary 二进制 octal 八进制 hexadecimal 十六进制 decimal 十进制*

* **第九种格式化使用方式 - 使用逗号作为千位分隔符**

```bash

>>> '{:,}'.format(123456789)
'123,456,789'

```

* **第十种格式化使用方式 - 使用特定类型的专属格式化**

```bash

>>> import datetime
>>> d = datetime.datetime(2010, 11, 28, 11, 54, 20)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-11-28 11:54:20'

```

* **第十一种格式化使用方式 - 嵌套参数以及更复杂的示例**

```bash

>>> for align, text in zip('<^>',['left','center','right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>> octets = [192, 168, 0, 1] # 16进制
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
>>> width = 5
>>> for num in range(5, 12):
...     for base in 'dXob':
...             print('{0:{width}{base}}'.format(num, width=width, base=base), end=' ')
...     print()
...
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011

```

其实我比较喜欢最后一种格式，其实也是应用中应该被经常用到的使用方式
