+++
date = '2025-07-25T14:10:46.843888+08:00'
draft = false
title = 'Python 入门基础知识 - 正则表达式 - Match对象'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**Match对象**

Match对象实例是有正则表达式对象的match()，以及search()方法在匹配成功后返回的。Match对象有以下常用的方法和属性，

用于对匹配成功的正则表达式进行处理。

**使用Match对象处理组**

group(),groups()和groupdict()方法都是处理在正则表达式中使用"()"分组的情况。不同的是，group的返回值为字符串，

当传递多个参数时其返回值为元组。groups()的返回值为元组。groupdict()的返回值为字典。

原型分别如下

> group([group1, ...])
>
> groups([default])
>
> groupdict([default])

对于group()而言，其参数为分组的编号。如果向group()传递多个参数，则其返回各个参数所对应的字符串组成的元组。对于groups()和

groupdict()一般不需要向其传递参数。

示例演示如下：

```py
import re
s = '''Life can be dreams,
Life can be great thoughts;
Life can mean a person,
Sitting in a count.'''
r = re.compile('\\b(?P<first>\w+)a(\w+)\\b')  # 编译正则表达式，匹配所有包含字母'a'的单词
m = r.search(s)  # c从头开始搜索，search()返回搜索到的第一个单词
print(m)
# <_sre.SRE_Match object at 0x100af58b0>

print(m.groupdict())
# {'first': 'c'}

print(m.groups())
# ('c', 'n')

m = r.search(s, 9)  # 从第十个字符开始搜索
print(m.group())
# dreams

print(m.group(1))
# dre

print(m.group(2))
# ms

print(m.group(1, 2))
# ('dre', 'ms')

print(m.groupdict())
# {'first': 'dre'}

print(m.groups())
# ('dre', 'ms')
```

**使用Match对象处理索引**

start()、end()以及span()方法返回所匹配的子字符串的索引。

原型如下

> start([groupid=0])
>
> end([groupid=0])
>
> span([groupid=0])

参数含义

> groupid: 为可选参数，即分组编号。

如果不传递参数，则返回整个字符串的索引。

start()方法返回子字符串或者组的起始位置索引。

end()方法返回子字符串或者组的结束位置索引。

而span()方法则以元组的形式返回以上两者。

使用方法如下

```py
import re
s = '''Life can be dreams,
Life can be great thoughts;
Life can mean a person,
Sitting in a court.'''
r = re.compile('\\b(?P<first>\w+)a(\w+)\\b')  # 编译正则表达式匹配含有字母"a"的单词
m = r.search(s, 9)  # 从第十个字符开始搜索
print(m.start())  # 输出匹配到的子字符串的起始位置
# 12

print(m.start(1))  # 输出第一组的起始位置
# 12

print(m.start(2))  # 输出第二组的起始位置
# 16

print(m.end(1))  # 输出第一组的子字符串结束位置
# 15

print(m.end())  # 输出子字符串的结束位置
# 18

print(m.span())  # 输出子字符串的开始和结束的位置
# (12, 18)

print(m.span(2))  # 输出第二组子字符串的开始和结束的位置
# (16, 18)
```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
