+++
date = '2025-07-25T14:10:34.813618+08:00'
draft = false
title = 'Python 入门基础知识 - 正则表达式对象'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**正则表达式对象**

使用re.compile()函数将正则表达式编译生成正则表达式对象实例后，可以使用正则表达式对象实例提供的属性和方法对字符串进行处理。

**以"\"开头的元字符**

除了基本的元字符以外还有一类似"\"开头的元字符。以"\"开头的元字符主要表示某一类型的集合，比如数字的集合、字母的集合等。

常用的以"\"开头的元字符如下

> \b 匹配单词头或者单词尾
>
> \B 与\b词义相反
>
> \d 匹配任何数字
>
> \D 匹配任何非数字
>
> \s 匹配任何空白字符
>
> \S 匹配任何非空白字符
>
> \w 匹配任何字母、数字、以及下划线
>
> \W 匹配任何非字母、数字、以及下划线

”\“开头的元字符也可以与其他的元字符配合使用。例如"\d\*"可以匹配任何由数字组成的字符串。

其中"\d"相当于[0-9]，"\w"相当于[z-aA-Z0-9]。下面演示使用元字符"\"开头的的实例

```py
import re
s = 'Python can run on Window'

print(re.findall('\\bo.+?\\b', s))  # 查找首字母为"o"的单词
# ['on']

print(re.findall('\\Bo.+?', s))  # 查找含字母"o"的单词，但"o"不是单词的首字母
# ['on', 'ow']

print(re.findall('\so.+?', s))  # 使用空白字符来匹配首字母为"o"的单词
# [' on']

print(re.findall('\\b\w.+?\\b', s))  # 查找字符串中的所有单词
# ['Python', 'can', 'run', 'on', 'Window']

print(re.findall('\d.\d', 'Python 2.7.13'))  # 匹配x.x的数字形式
# ['2.7']

print(re.findall('\D+', 'Python 2.7.13'))  # 查找不含数字的字符
# ['Python ', '.', '.']

print(re.split('\s', s))  # 使用空白字符分隔字符串
# ['Python', 'can', 'run', 'on', 'Window']

print(re.split('\s', s, 1))  # 使用空白字符份跟字符串，只分隔一次
# ['Python', 'can run on Window']

print(re.findall('\d\w+?', 'asd3asd'))  # 查找以数字开始的字符
```

在上面的实例中，使用的是'\\bo.+?\\b'来匹配首字母为"o"的单词，而不是直接使用'\\b\o.+\\b'或者'\\b\o.\*\\b'来匹配。

如果使用'\\b\o.+\\b'或者'\\b\o.\*\\b'，则输出如下

```py
print(re.findall('\\b\o.+\\b', s))
# ['on Window']

print(re.findall('\\b\o.*\\b', s))
# ['on Window']
```

可以看到，本来预想的是"on"后有一个空格，应该只匹配到"on"，然而最终结果连后面的"Window"也匹配了。这是因为"+","\*"等元字符为"贪婪"模式的元字符，

他们尽可能匹配更多的字符。为了避免"+","\*"等元字符过多的匹配，可以在其之后使用"非贪婪"模式的"?"，或者使用"{}"指定匹配的次数。

**编译正则表达式**

re模块中包含一个re.compile()函数，可以使用re.compile()函数将正则表达式编译生成一个RegexObject实例。

然后通过生成的RegexObject对象实例对字符串进行操作，如查找、替换等。re.compile()的函数原型如下所示：

> compile(pattern[, flags])

参数含义如下

> pattern: 正则表达式的匹配模式
>
> flags: 可选参数，编译标志

实例如下：

```py
import re

print(re.compile('a*b', re.I | re.X))  # 编译正则表达式，忽略大小写和模式中的空格
# <_sre.SRE_Pattern object at 0x10185bdd8>

r = re.compile('''
    \b  # 匹配单词开始
    A?  # 以A或者AA开头
    \d  # 匹配一个数字
    \w* # 匹配任意字符
        # 一个空行
    \b  # 匹配单词结束
''', re.X)
print(r)
# <_sre.SRE_Pattern object at 0x7fe5a5d00330>
```

**使用原始字符串**

原始字符串在以前文章中提到过，原始字符串是为正则表达式设计的，以提高正则表达式的可读性，减少"\"在正则表达式中的数目。

由于在正则表达式中也要使用以"\"开头的字符以表示某些特殊的含义，而在字符串中，转义字符也是以"\"开头，这就导致了冲突。

例如在正则表达式中，"\b"表示匹配一个单词的开始或结束，而在字符串中，"\b"则表示退格。如果在正则表达式中使用"\b"，则

应该写成"\\b"。

在re.compile()中使用"\b"的正确写法如下：

```py
re.compile('\\ba.?')
```

如果使用原始字符串的话，正确的写法如下：

```py
re.compile(r'\ba.?') 
```

如果要在正则表达式中匹配一个以"\"开头的字符串，比如"\word"，则首先要将"\"转义，以避免元字符"\w"，应将其写成"\\word"。

而"\\word"作为一个包含有两个"\"的字符串，又需要两个"\"将其转义，因此正确的写法如下:

```py
re.compile('\\\\word') 
```

而如果使用原始字符串，则正确的写法如下：

```py
re.compile(r'\\word')
```
