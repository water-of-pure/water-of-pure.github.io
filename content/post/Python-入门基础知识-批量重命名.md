+++
date = '2025-07-25T15:54:51.302933+08:00'
draft = false
title = 'Python 入门基础知识 - 批量重命名'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**批量重命名**

在日常工作中经常会遇到这样的情况，需要将某个文件夹下的文件按照一定的规律重新命名。如果手完成的话，

需要耗费大量的时间，而且容易出错。在学习Python以后，完全可以写一个脚本完成这样的工作。

示例如下

```py
import os
prefix = 'Python'  # prefix 为重命名后的文件起始字符
length = 2  # length为除去prefix以后，文件名要达到的长度
base = 1  # 文件名的其实函数
format = 'mdb'  # 文件名的后缀

'''函数padLeft将文件名补全到指定长度
str 为要补全的字符
num 为要达到的长度
padstr 为达到长度所需要添加的字符
'''

def padLeft(str, num, padstr):
    stringLen = len(str)
    n = num - stringLen
    if n > 0:
        str = padstr * n + str

    return str

# 为了避免用户误操作，这里先提示用户
print('the files in "%s" will be renamed' % os.getcwd())
input = raw_input('press y to continue\n')
if input != 'y':
    exit()

filenames = os.listdir(os.curdir)  # 获取当前目录中的内容
# 从基数减1，为了使i = i + 1在第一次执行时等于基数
i = base - 1
for filename in filenames:
    i = i + 1
    # 判断当前路径是否为文件，并且不是"rename.py"
    if filename != 'base_practise.py' and os.path.isfile(filename):
        name = str(i)
        name = padLeft(name, length, '0')
        t = filename.split('.')
        m = len(t)
        if format == '':  # 如果未指定文件类型，则更改当前目录中所有文件
            os.rename(filename, prefix + name + '.' + t[m - 1])
        else:  # 否则只修改指定类型的文件
            if t[m - 1] == format:
                os.rename(filename, prefix + name + '.' + str(t[m - 1]))
            else:
                i = i - 1  # 保证i连续
    else:
        i = i - 1  

```

可以自己运行下，创建个xxx.mdb的文件

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
