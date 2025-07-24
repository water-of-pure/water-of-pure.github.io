+++
date = '2025-07-24T10:40:51.175163+08:00'
draft = false
title = 'Python 入门基础知识 - 字符串'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

实例环境声明

# -\*- coding: utf-8 -\*-

# version 2.7.13

字符串

Python的字符串用于表示和存储文本，字符串通常由单引号['...']，双引号["..."]或者三引号['''...''',"""..."""]包围。

其中三引号包围的字符串可以由多行组成。

字符串中可以包括数字，字母以及一些控制字符，如换行符、制表符，如

```py
str1 = 'qwe'
print(str1)
str2 = 'qwe123'
print(str2)
str3 = "qwe123"
print(str3)
str4 = 'a = 1 + 2 + 3 ^ 4 * 5'
print(str4)
str5 = 'it can\'t'
print(str5)
str6 = "it can't"
print(str6)
```

如果需要在字符串中包含控制字符或者表示特殊字符，需要使用转移字符。如：

```py
t = 'Hi,\tWhere are you?'
print(t)
t = 'Hi,\nWhere are you?'
print(t)
t = 'Hi,\rWhere are you?'
print(t)
t = 'Hi,\\nWhere are you?'
print(t)
```
