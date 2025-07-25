+++
date = '2025-07-25T14:10:27.254669+08:00'
draft = false
title = 'Python 入门基础知识 - re模块函数的应用 - 匹配和搜索'
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

**匹配和搜索**

re.match()函数用于在字符串中匹配正则表达式，如果匹配成功，则返回MatchObject对象实例。

re.search()函数用于在字符串中查找正则表达式，如果找到，则返回MatchObject对象实例。

re.findall()函数用于在字符串中查找所有符合正则表达式的字符串，并返回这些字符串的列表。

如果在正则表达式中使用了组，则返回一个元组。

re.match()和re.search()函数的作用基本一样。不同的是，re.match()函数只从字符串中第一个字符开始匹配。

而re.search()函数则搜索整个字符串。以上三个函数的原型如下

> re.match(pattern, string[, flags])
>
> re.search(pattern, string[, flags])
>
> re.findall(pattern, string[, flags])

其参数含义如下。

> pattern: 匹配模式。
>
> string: 要进行匹配的字符串。
>
> flags: 可选参数，进行匹配的标志。

参数flags可以是以下选项。

> re.I 忽略大小写。
>
> re.L 根据本地设置而更改\w、\W、\b、\B、\s、\S的匹配内容。
>
> re.M 多行匹配模式
>
> re.S 使'.'元字符匹配换行符。
>
> re.U 匹配Unicode字符。
>
> re.X 忽略pattern中的空格，并且可以使用"#"注释

上述的几个编译标志可以同时使用。同时使用几个编译标志时，需要使用"|"对并用的编译标志进行运算。

以下实例使用上述函数进行匹配和搜索。

```py
import re  # 导入re模块
s = 'Lift is good'  # 定义字符串
print(re.match('is', s))  # 在字符串中匹配"is"
> None # 输出为None

print(re.search('is', s))  # 在字符串中搜索"is"
> <_sre.SRE_Match object at 0x102b2e850> # 返回一个MatchObject对象，并返回

print(re.match('l.*', s))  # 匹配任何以字母'l'开头的字符串
> None # 表示未找到

print(re.match('l.*', s, re.I))  # 此处设置忽略大小写
> <_sre.SRE_Match object at 0x103312850> # 返回MatchObject对象，表示找到。

print(re.findall('[a-z]{3}', s))  # 查找所有3个字母的字符串
> ['ift', 'goo']

print(re.findall('[a-z]{1,3}', s))  # 查找所有由1到3个字母组成的字符串
> ['ift', 'is', 'goo', 'd']
```
