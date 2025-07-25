+++
date = '2025-07-25T14:10:30.944277+08:00'
draft = false
title = 'Python 入门基础知识 - re模块函数的应用 - 替换函数'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**re模块函数的应用**

Python中的re模块提供了对正则表达式的支持。虽然Python中有一个string模块用来对字符串进行处理，但是string模块只能进行简单的操作。

而使用re模块可以完成对复杂字符串的操作。它提供了一下几类对字符串进行操作的函数。

**替换函数**

re.sub()函数用于替换字符串中符合正则表达式的内容，它返回替换后的字符串。

re.subn()函数与re.sub()函数相同，只不过re.subn()函数返回一个元组。

其函数原型分别如下。

> re.sub(pattern, repl, string[, count])
>
> re.subn(pattern, repl, string[, count])

参数含义如下

> pattern: 正则表达式。
>
> repl: 要替换成的内容。
>
> string: 进行内容替换的字符串
>
> count: 可选参数，最大替换次数。

实例演示如下

```py
import re  # 导入re模块
s = 'Life is good'  # 定义字符串
print(re.sub('good', 'awesome', s))  # 用'awesome'替换为'good'
# Life is awesome
print(re.sub('good|is', 'awesome', s))  # 用'awesome'替换为'good'或'is'
# Life awesome awesome
print(re.sub('good|is', 'awesome', s, 1))  # 用'awesome'替换为'good'或'is'，但只替换一次
# Life awesome good
r = re.subn('good|is', 'awesome', s, 1)  # 用'awesome'替换为'good'或'is'，但只替换一次
print(r)
# ('Life awesome good', 1)
print(r[0])
# Life awesome good
r = re.subn('good|is', 'awesome', s)  # 用'awesome'替换为'good'或'is'
print(r)
# ('Life awesome awesome', 2)
print(r[0])
# Life awesome awesome
print(r[1])
# 2
```

**分隔字符串函数**

re.split()函数用于分隔字符串，它返回分割后的字符串列表。

其函数原型如下。

> re.split(pattern, string[, maxsplit = 0])

参数含义如下

> pattern: 正则表达式模式。
>
> string: 要分割的字符串。
>
> maxsplit: 可选参数，最大分割次数。

实例演示如下

```py
import re
s = 'List can be awesome'
print(re.split(' ', s))
# ['List', 'can', 'be', 'awesome']
print(re.split('b', s))
# ['List can ', 'e awesome']
```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13
```
