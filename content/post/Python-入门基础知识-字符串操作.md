+++
date = '2025-07-24T10:40:55.616309+08:00'
draft = false
title = 'Python 入门基础知识 - 字符串操作'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

实例环境声明

# \_\*\_ coding: utf-8 \_\*\_

# version 2.7.13

**字符串操作**

Python提供很多针对字符串操作的函数，也可以使用"+","\*"等运算符对字符串进行操作

string.capitalize() # 将字符串的第一个字符大写

```py
str = "qwe"
print(str.capitalize())
```

string.count() # 用于统计字符串里某个字符出现的次数

```py
str = "qwewww"
print(str.count('w', 0, len(str)))
```

string.find() # 检测字符串中是否包含子字符串，如果包含子字符串返回开始的索引值，否则返回-1

```py
str = "qwewww"
print(str.find('w', 2, len(str)))
```

string.isalnum() # 检测字符串是否由字母和数字组成

```py
str = "qweqwe123"
print(str.isalnum())	
```

string.isalpha() # 字符串中的所有字符是字母，并有至少一个字符

```py
str = "qweqwe"
print(str.isalpha())
```

string.isdigit() # 检测字符串是否只有数字组成

```py
str = "123456"
print(str.isdigit())
```

string.islower() # 检测字符串是否由小写字母组成

```py
str = "qqq@123"
print('string.islower = %s' % str.islower())
```

string.istitle() # 检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写

```py
str = "D123456"
print('string.istitle = %s' % str.istitle())
```

string.isupper() # 检测字符串中所有的字母是否都为大写

```py
str = "D123456"
print('string.isupper = %s' % str.isupper())
```

string.join() # 用于将序列中的元素以指定的字符连接生成一个新的字符串

```py
str = "D123456"
print('string.join = %s' % str.join([' a ',' b ',' c ']))
```

string.lower() # 转换字符串中所有大写字符为小写

```py
str = "D123456"
print('string.lower = %s' % str.lower())
```

string.split() # 指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个子字符串

```py
str = "D1 2 34 56"
print('string.split = %s' % str.split(' ', 2))
```

试着修改第二个参数试试

string.swapcase() # 用于对字符串的大小写字母进行转换

```py
str = "D1 2 34 56 b"
print('string.swapcase = %s' % str.swapcase())
```

string.title() # 返回"标题化"的字符串,就是说所有单词都是以大写开始

```py
str = "dcccc1 2 34 56 b"
print('string.title = %s' % str.title())
```

string.upper() # 将字符串中的小写字母转为大写字母

```py
str = "D1 2 34 56 b"
print('string.upper = %s' % str.upper())
```

len(string) # 返回对象（字符、列表、元组等）长度或项目个数

```py
str = "D1 2 34 56 b"
print('len(string) = %s' % len(str))
```

使用"+","\*"等运算符对字符串进行操作

```py
str = "gowhich "
print(str + ', where are you?')
print(str * 3)
```

看一个好玩的，下面这个会将字符串插入的---之中

```py
print("abc".join('---'))
>>> -abc-abc-
```

**索引和分片**

Python中字符串相当于一个不可变序列的列表。一旦声明一个字符串，则该字符串中的每个字符都有了自己的位置。在

Python中可以使用"[]"来访问字符串中指定位置上的字符，在Python中字符串中的字符的序号是从0开始，及string[0]

表示字符串string中的第一个字符。Python还允许以负数表示字符的序号，负数表示从字符串尾部开始计算，此时最后

一个字符的序号为-1。如下演示

```py
str = "abcdefg"
print("str[2] = %s" % str[2])
print("str[-2] = %s" % str[-2])
print("str[-0] = %s" % str[-0])
print("str[-1] = %s" % str[-1])
print("str[1:4] = %s" % str[1:4])	# 取从第2个字符到第5个字符，但是不包含第五个字符
print('str[1:1] = %s' % str[1:1])
print('str[2:4] = %s' % str[2:4])
print('str[1:-1] = %s' % str[1:-1])
print('str[0:-2] = %s' % str[0:-2])
print('str[:-2] = %s' % str[:-2]) 	# 跟str[0:-2]结果一致
```

**格式化字符串**

在Python中使用以"%"开头的字符,以在脚本中格式化字符串的内容

常见的格式化字符有以下几个

> %d - 十进制整数
>
> %c - 单个字符
>
> %o - 八进制整数
>
> %s - 字符串
>
> %x - 十六进制整数，其中的字母小写
>
> %X - 十六进制整数，其中的字母大写

# 实例如下

```py
print('So %s day!' % 'beautiful')
print('1 %c 1 %c %d' % ('+', '=', 2))
print('x = %x' % 0xA)
print('x = %X' % 0xa)
```

**字符串与数字相互装换**

字符串转换为整数可以使用string模块的string.atoi函数将字符串转换为整数，实例如下

```py
import string
print(string.atoi('10') + 4)		# 默认十进制
print(string.atoi('10', 8) + 4)		# 八进制
print(string.atoi('10', 16) + 4)	# 十六进制
```

**原始字符串**

原始字符串是Python中一类比较特殊的字符串，以大写字母R或r开始。在原始字符串中，"\"不在表示转移字符的含义。

原始字符串是为正则表达式设计的

```py
import os
print(os.listdir(r'/'))
```
