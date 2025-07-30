+++
date = '2025-07-30T09:56:41.851209+08:00'
draft = false
title = 'Python正则表达式'
categories = [
    "技术",

]

tags = [
    "Python",
    "正则"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

### 知识点一：正则表达式使用方式

```bash

>>> import re
>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group()
'def'
>>> m.group(0)
'def'

```

`(?<=abc)def` ，并不是从`a`开始搜索，而是从`d`往回看的

```bash

>>> m = re.search('(?<=-)\w+', 'email-address')
>>> m.group(0)
'address'
>>>

```

这个例子搜索一个跟随在连字符(-)后的单词

具体的正则使用方式可以参考官网：https://docs.python.org/zh-cn/3/library/re.html

### 知识点二：正则表达式对象

将正则表达式的样式编译为一个正则表达式对象，可以让程序更加高效

```py

prog = re.compile(pattern)
results = prog.match(string)

```

等价于

```py

result = re.match(pattern, string)

```

### 知识点三：search() vs. match()

re.search()检查字符串的任意位置，re.match()检查字符串开头

```bash

>>> re.match("c", "abcded") # no match
>>> re.search("c", "abcdef") # match
<re.Match object; span=(2, 3), match='c'>
>>>

```

在`search()`中，可以使用`^`作为开始来限制匹配到字符串的首位

```bash

>>> re.match("c", "abcdef") # no match
>>> re.search("^c", "abcdef") # no match
>>> re.search("^a", "abcdef") # match
<re.Match object; span=(0, 1), match='a'>
>>>
```
