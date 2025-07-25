+++
date = '2025-07-25T14:10:40.194839+08:00'
draft = false
title = 'Python 入门基础知识 - 正则表达式对象的属性和方法'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**正则表达式对象的属性和方法**

正则表达式对象提供了与re模块中函数类似的字符串操作方法。常用的正则表达式对象的属性和方法可以分为以下几种

**匹配和搜索**

正则表达式对象的match()方式用于从字符串开始处进行匹配，或者从指定位置进行匹配。要匹配的字符串必须位于开始，或者参数指定的位置才会匹配成功。

原型如下

> match(string[, pos[, endpos]])

参数含义如下

> string: 要进行匹配的字符串。
>
> pos: 可选参数，进行匹配的起始位置。
>
> endpos: 可选参数，进行匹配的结束位置。

如果匹配成功，match()返回一个MatchObject对象实例。与match()类型，search()方法用于对字符串进行查找，不同的是search()方法在整个

字符串中搜索。如果查找成功，search()将返回一个MatchObject对象实例。

原型如下

> search(string[, pos[, endpos]])

参数含义如下

> string: 要进行查找的字符串。
>
> pos: 可选参数，进行查找的起始位置。
>
> endpos: 可选参数，进行查找的结束位置。

正则表达式对象的findall()方法用于在字符串中查找所有符合正则表达式的字符串，并返回这些字符串的列表。如果在正则表达式中使用了组，则返回

一个元组。

原型如下

> findall(string[, pos[, endpos]])

参数含义跟search()方法中的相同

实例如下

```py
import re  # 导入模块
# 编译正则表达式，"who*ps"表示在'h'和'p'之间有任意个以字母'o'开头的单词，如'hp','hop','hoop'
r = re.compile('who*ps')

# 在字符串开始处匹配，没有返回值，表示匹配失败
print(r.match('Life can be whoops'))
# None

# 从字符串的第13个字符串开始匹配(字符串从0开始)，也就是从字母'w'开始，返回MatchObject对象实例
print(r.match('Life can be whoops', 12))
# <_sre.SRE_Match object at 0x10729f850>

# 在字符串中搜索'who*ps',返回MatchObject对象实例，表示字符串中含有'who*ps'
print(r.search('Life can be whoops'))
# <_sre.SRE_Match object at 0x10729f850>
#
# 重新编译，匹配字母'b'和字母'g'之间包含的一个字母以及一个空字符的情况
r = re.compile('b.\sw')

# 在字符串中搜索，此处匹配的是'be w'
print(r.search('Life can be whoops'))
# <_sre.SRE_Match object at 0x106edb850>

# 重新编译，匹配后边有一个空字符的任意包含两个或者三个字符的单词
r = re.compile('\\b\w..?\s')
# 使用findall()函数查找
print(r.findall('Life can be whoops'))
# ['can ', 'be ']  

```

**替换**

正则表达式对象的sub()和subn()方法用于对字符串的替换，原型如下

> sub(repl, string[, count = 0])
>
> subn(repl, string[, count = 0])

参数含义如下：

> repl: 要替换的内容。
>
> string: 进行内容替换的字符串。
>
> count: 可选参数，最大替换次数。

如下实例，将所有字母'b'开头的单词替换成'\*'

```py
import re
s = '''
Life can be whoops;
Life can be bad;
Life is mostly cheerful;
But sometimes is sad;
'''
r = re.compile('b\w*', re.I)  # 编译正则表达式，忽略大小写
print(r.sub('*', s))
# Life can * whoops;
# Life can * *;
# Life is mostly cheerful;
# * sometimes is sad;

print(r.sub('*', s, 2))  # 只在字符串中替换两次
# Life can * whoops;
# Life can * bad;
# Life is mostly cheerful;
# But sometimes is sad;

r = re.compile('b\w*')  # 重新编译，不区分大小写
# 使用subn()替换替换字符，它返回一个元组
s1 = r.subn('*', s)
print(s1)
# ('\nLife can * whoops;\nLife can * *;\nLife is mostly cheerful;\nBut sometimes is sad;\n', 3)

print(s1[0])
# Life can * whoops;
# Life can * *;
# Life is mostly cheerful;
# But sometimes is sad;

print(s1[1])
# 3

s2 = r.subn('*', s, 1)  # 只在字符串中替换一次
print(s2)
# ('\nLife can * whoops;\nLife can be bad;\nLife is mostly cheerful;\nBut sometimes is sad;\n', 1)

print(s2[0])
# Life can * whoops;
# Life can be bad;
# Life is mostly cheerful;
# But sometimes is sad;

print(s2[1])
# 1  

```

**分隔字符串**

正则表达式对象的split()方法用于对字符串进行分隔。原型如下:

> split(string[, maxsplit=0])

参数含义如下

> string: 要分割的字符串。
>
> maxsplit: 可选参数，最大分割次数。

实例演示如下

```py
import re
r = re.compile('\s')
s3 = r.split(s)
print(s3)
# ['', 'Life', 'can', 'be', 'whoops;', 'Life', 'can', 'be', 'bad;', 'Life', 'is', 'mostly', 'cheerful;', 'But', 'sometimes', 'is', 'sad;', '']

s4 = r.split(s, 2)  # 只分割2次
print(s4)
# ['', 'Life', 'can be whoops;\nLife can be bad;\nLife is mostly cheerful;\nBut sometimes is sad;\n']

r = re.compile('b\w*', re.I)  # 重新编译，匹配以字母'b'开头的字符串，忽略大小写
s4 = r.split(s)
print(s4)
# ['\nLife can ', ' whoops;\nLife can ', ' ', ';\nLife is mostly cheerful;\n', ' sometimes is sad;\n']

r = re.compile('e\w*', re.I)  # 重新编译，匹配以字母'e'开头的字符串，忽略大小写
s5 = r.split(s)
print(s5)
# ['\nLif', ' can b', ' whoops;\nLif', ' can b', ' bad;\nLif', ' is mostly ch', ';\nBut som', ' is sad;\n']  

```

实例环境说明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
