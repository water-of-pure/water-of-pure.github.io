+++
date = '2025-07-24T10:41:05.911745+08:00'
draft = false
title = 'Python 入门基础知识 - 文件操作'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

实例环境配置

# \_\*\_ coding: utf-8 -\*-

# version 2.7.13

文件

文件也可以看做是Python中的数据类型。当使用Python的内置函数opne打开一个文件时，

返回一个文件对象。其原型如下所示：

> open(filename, mode, bufsize)
>
> filename: 要打开的文件名
>
> model: 可选参数，文件打开模式
>
> bufsize: 可选参数，缓冲区大小

其中mode可以是'r'表示以读方式打开文件，'w'表示以写的方式打开文件，'b'表示以二进制方式打开文件。

常用的操作如下：

> file.read() # 将整个文件读入字符串中
>
> file.readline() # 读入文件中的一行到字符串中
>
> file.readlines() # 将整个文件按行读取列表中
>
> file.write() # 向文件中写入字符串
>
> file.writelines() # 向文件中写一个列表
>
> file.close() # 关闭打开的文件

下面做些实例演示，这里我使用当前目录的测试文件test.txt,文件内容的话，可以根据情况自己来定

```py
# 以写的方式打开文件，如果文件不存在则创建
file = open('./test.txt', 'w')
# 执行完下面的命令，字符串就应该写入到文件中了，可以自己打开确认下。
file.write('python\n')
# 创建一个列表
testList = []
for i in range(10):
	s = str(i) + '\n'
	testList.append(s)
# 将列表写入文件
file.writelines(testList)
# 关闭文件
file.close()
# 以读方式打开文件
file = open('./test.txt', 'r')
# 读取整个文件
s = file.read()
# 输出字符串内容
print(s)
# 关闭文件，为了使用readlines读取文件。
# 如果不关闭文件，读取的内容为空。
# 因为文件内容已经被读入到变量s中了。
file = open('./test.txt', 'r')
# 将文件读入到列表中
l = file.readlines()
print(l)
file.close()
```

这里的区别可以自己体验下
