+++
date = '2025-07-25T14:10:50.561153+08:00'
draft = false
title = 'Python 入门基础知识 - 使用正则表达式处理文件'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用正则表达式处理文件**

正则表达式是处理文本文件的强有力的工具。

下面演示一个获取Python文件中所有函数跟变量的实例

在Python脚本中，函数定义是以"def"开头，因此处理函数的过程相当简单。为了代码简洁，此处假设脚本编写规范"def"后跟一个空格，

然后是函数名，接着就是函数。没有考虑使用多个空格的情况。

而Python脚本中的变量不好处理，因为变量一般不需要事先声明，而是直接赋值，因此脚本中首先处理了变量直接赋值的情况。

通过匹配单词后接"="的情况查找变量名。同样，为了代码简洁，仅考虑比较规范整洁的代码写法，变量名与"="之间有一空格。

另外，还有一类变量是在for循环语句中直接使用的，因此脚本中又特别处理了for循环的情况。为了使代码简洁，脚本并没有

处理变量名重复的情况。整个脚本的代码如下所示。

```py
# _*_ coding: utf-8 -*-
# File: test.py
import re
import sys

def deal_with_func(s):
    r = re.compile(r'''
        (?<=def\s)  # 前边必须含有def且def后跟一个空格
        \w+         # 匹配函数名
        \(.*?\)     # 匹配参数
        (?=:)       # 后边必须跟一个:
        ''', re.X)  # 设置编译选项，忽略模式中的注释
    return r.findall(s)

def deal_with_var(s):
    vars = []      # 定义一个列表，因为这里分两种情况处理
    r = re.compile(r'''
        \b         # 匹配单词开始
        \w+        # 匹配变量名
        (?=\s=)    # 处理未给变量赋值的情况
        ''', re.X)
    vars.extend(r.findall(s))

    r = re.compile(r'''
        (?<=for\s)    # 处理变量位于for语句中的情况
        \w+           # 匹配变量名
        \s            # 匹配空格
        (?=in)        # 匹配in
        ''', re.X)    # 设置编译选项，忽略模式中的注释

    vars.extend(r.findall(s))

    return vars

# 判断命令行是否有输入，没有则要求输入
if len(sys.argv) == 1:
    sour = raw_input('请输出要处理的文件路径:')
else:
    sour = sys.argv[1]

file = open(sour)
s = file.readlines()
file.close()
print('**********************************')
print('%s 中的函数有：' % sour)
print('**********************************')
i = 0
for line in s:
    i = i + 1
    function = deal_with_func(line)
    if len(function) == 1:
        print('Line: %i \t %s' % (i, function[0]))

i = 0
for line in s:
    i = i + 1
    var = deal_with_var(line)
    if var and len(var) == 1:
        print('Line: %i \t %s' % (i, var[0]))  

```

比如运行此脚本后输入：test.py

得到的结果如下：

```bash
请输出要处理的文件路径:test.py
**********************************
base_practise.py 中的函数有：
**********************************
Line: 20 	 deal_with_func(s)
Line: 30 	 deal_with_var(s)
Line: 21 	 r
Line: 31 	 vars
Line: 32 	 r
Line: 39 	 r
Line: 53 	 sour
Line: 55 	 sour
Line: 57 	 file
Line: 58 	 s
Line: 63 	 i
Line: 64 	 line
Line: 65 	 i
Line: 66 	 function
Line: 70 	 i
Line: 71 	 line
Line: 72 	 i
Line: 73 	 var
```
