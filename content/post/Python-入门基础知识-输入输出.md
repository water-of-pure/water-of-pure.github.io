+++
date = '2025-07-22T18:32:00.824864+08:00'
draft = false
title = 'Python 入门基础知识 - 输入输出'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

实例环境声明

```bash
# -*- coding:utf-8 -*-
# python 的基本输入输出
# version 2.7.13
```

```py
name = raw_input("输入你的姓名:")
print(name)
```

运行脚本会得到如下

```py
输入你的姓名:duban
durban
```

raw\_input 返回的输入的字符串，这里应该是会把所有的输入当做字符串来处理并返回

如果想转换成对应的类型，需要使用对应的类型转换函数

1. # int 将字符串转为整数
2. # float 将字符串或整数转换为浮点型
3. # str 将数字转换为字符串
4. # chr 将ASCII值转换为ASCII字符
5. # hex 将整数转换为十六进制的字符串
6. # long 将字符串转换为长整型
7. # oct 将整数转换为八进制的字符串
8. # ord 将ASCII字符转换为ASCII值

```py
print(int(name))
```

这里的转换只能是 数字字符串 如果是 字母 汉字之类的是会报错的 如下

```bash
ValueError: invalid literal for int() with base 10: 'durban'
```

```py
print(float(name))
```

这里的转换只能是 数字字符串 如果是 字母 汉字之类的是会报错的

比如 输入 durban

会出现如下错误

```bash
ValueError: could not convert string to float: durban
```

print(str(name))

由于raw\_input本身返回的就是个字符串 这里总是会正常输出

```py
print(chr(int(name)))
```

chr 需要一个整数作为参数 否则会报错

```bash
ValueError: invalid literal for int() with base 10: 'durban'
```

如果输入 123 则会正常输出

```py
print(hex(int(name)))
```

hex 需要的参数也是个整数 如果给到的参数没有做整数转换 会报出如下错误

```bash
TypeError: hex() argument can't be converted to hex
```

```py
print(long(name))
```

这里要将输入装维长整型，首先我们数如的字符串必须是长整型的 否则会报错

```bash
ValueError: invalid literal for long() with base 10: 'durban'
```

如果输入 123L 或者 123l

则会正常输出

```py
print(oct(int(name)))
```

# 需要的参数也是个整数 如果给到的参数没有做整数转换 会报出如下错误

```bash
TypeError: oct() argument can't be converted to oct
```

```py
print(ord(chr(int(name))))
```

ord 这个比较特殊 需要配合chr来进行配合使用 否则会报出如下的错误

```bash
TypeError: ord() expected a character, but string of length 6 found
```
