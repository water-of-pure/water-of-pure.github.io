+++
date = '2025-07-25T14:10:43.638243+08:00'
draft = false
title = 'Python 入门基础知识 - 正则表达式 - 使用组'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用组**

组允许将正则表达式分解成几个不同的组成部分。在完成匹配和搜索后，可以使用元组编号访问不同部分匹配的内容。

**组概述**

在正则表达式中以一对圆括号"()"来表示位于其中的内容属于一个组。

例如"(re)+"将匹配"rere","rerere"等多个"re"重复的情况。组在匹配由不同部分组成的一个整体时非常有用。

如电话号码由区号和号码组成，在正则表达式中可以使用两组来进行匹配：一组匹配区号，另外一组匹配后边的号码。

实例演示如下

```py
import re
s = 'Phone No. 010-9876543'
r = re.compile(r'(\d+)-(\d+)')
m = r.search(s)
print(m)
# <_sre.SRE_Match object at 0x1059838b0>

print(m.group(1))
# 010

print(m.group(2))
# 9876543

print(m.groups())
# ('010', '9876543')
```

在正则表达式中可以通过使用"(?P<组名>)"为组设置一个名字，通过使用如下所示模式，将第一个组的名字设置为"Area"，将第二组的名字设置为"No"。

```py
import re
s = 'Phone No. 010-9876543'
r = re.compile(r'(?P<Area>\d+)-(?P<No>\d+)')
m = r.search(s)
print(m.groups())
# ('010', '9876543')

print(m.group(1))
# 010

print(m.group(2))
# 9876543

print(m.groupdict())
# {'Area': '010', 'No': '9876543'}

print(m.group('Area'))
# 010

print(m.group('No'))
# 9876543  

```

**组的扩展语法**

除了在组中使用"?P<组名>"来命名组名以外，还可以使用以下集中以"?"开头的扩展语法

> (?iLmsux) 设置匹配标志，可以是i、L、m、s、u、x以及它们的组合。其含义与编译标志相同。
>
> (?:...) 表示此非一个组
>
> (?P=name) 表示在此之前的名为name的组
>
> (?#...) 表示注释
>
> (?=...) 用于正则表达式之后，表示如果"="后的内容在字符串中出现则匹配，但不返回"="后的内容
>
> (?!...) 用于正则表达式之后，表示如果"!"后的内容在字符串中不出现则匹配，但不返回"!"后的内容
>
> (?<=...) 用于正则表达式之前，与(?=...)含义相同
>
> (?<!...) 用于正则表达式之前，与(?!...)含义相同

实例演示如下

```py
import re
s = '''Life can be good;
Life can be bad;
Life is mostly cheerful;
But sometimes sad.
'''
r = re.compile(r'be(?=\sgood)')  # 编译正则表达式，只匹配其后单词为'good'的'be'
m = r.search(s)
print(m)
# <_sre.SRE_Match object at 0x10625e850>

print(m.span())  # 输出匹配到的单词在字符串的位置
# (9, 11)

print(r.findall(s))
# ['be']

r = re.compile('be')
print(r.findall(s))
# ['be', 'be']

r = re.compile(r'be(?!\sgood)')  # 重新编译，匹配之后的单词不为'good'的'be'
m = r.search(s)
print(m)
# <_sre.SRE_Match object at 0x1007c6238>

print(m.span())
# (27, 29)

r = re.compile(r'(?:can\s)be(\sgood)')  # 使用组来匹配'be good'
m = r.search(s)
print(m)
# <_sre.SRE_Match object at 0x1055b1648>

print(m.groups())
# (' good',)

print(m.group(1))
#  good # good前面是有空格的哦

r = re.compile(r'(?P<first>\w)(?P=first)')  # 使用组名重复，此处匹配具有两个重复字母的单词
print(r.findall(s))
# ['o', 'e']

r = re.compile(r'(?<=can\s)b\w*\b')  # 匹配以字母'b'开头位于'can'之后的单词
print(r.findall(s))
# ['be', 'be']

r = re.compile(r'(?<!can\s)b\w*\b')  # 匹配以字母'b'开头不位于'can'之后的单词
print(r.findall(s))
# ['bad']

r = re.compile(r'(?<!can\s)(?i)b\w*\b')  # 重新编译，忽略大小写
print(r.findall(s))
# ['bad', 'But']

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13

```
