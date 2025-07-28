+++
date = '2025-07-28T17:05:09.038268+08:00'
draft = false
title = 'Python 入门基础知识 - Python处理XML实例-简单的RSS阅读器'
categories = [
    "技术",

]

tags = [
    "Python",
    "XML"
]
+++

**Python处理XML实例-简单的RSS阅读器**

RSS(Really Simple Syndication)是一种描述和同步网站内容的格式。RSS是基于XML的。使用Python可以做一个

简单的RSS阅读器。RSS有其自己的标准，可以通过阅读其标准编写一个脚本来处理网站的RSS。但鉴于XML的良好

可读性和良好的结构，只要找到一个简单的RSS文件，完全可以写出一个简答的RSS阅读器。以Python官网提供的

RSS为例，访问地址如下：<https://www.python.org/jobs/feed/rss/>

可以看到每一条主要的消息处于"item"元素之间。在"item"元素中依次包含"title"、"link"、"description"、

"guid"元素。其中"title"元素包含了消息的标题，"description"元素包含了消息的简要描述，"link"元素包含

了消息的具体访问地址。Python官网的RSS文件非常直观，通过查看RSS文件内容即可了解其结构。

下面通过如下代码实例演示如何获取标题和"link"访问地址

```py
# _*_ coding: utf-8 -*-
import Tkinter
import urllib
import xml.parsers.expat

class ParserXML:

    def __init__(self, edit):
        self.parser = xml.parsers.expat.ParserCreate()  # 生成XMLParser
        self.parser.StartElementHandler = self.start  # 起始标记处理方法
        self.parser.EndElementHandler = self.end  # 结束标记处理方法
        self.parser.CharacterDataHandler = self.data  # 字符数据处理方法

        self.title = False
        self.link = False
        self.edit = edit

    def start(self, name, attrs):
        if name == 'title':
            self.title = True
        elif name == 'link':
            self.link = True
        else:
            pass

    def end(self, name):
        if name == 'title':
            self.title = False
        elif name == 'link':
            self.link = False
        else:
            pass

    def data(self, data):
        if self.title:
            self.edit.insert(Tkinter.END, '******************************\n')
            self.edit.insert(Tkinter.END, 'Title: ')
            self.edit.insert(Tkinter.END, data + '\n')
        elif self.link:
            self.edit.insert(Tkinter.END, 'Link: ')
            self.edit.insert(Tkinter.END, data + '\n')
        else:
            pass

    def feed(self, data):
        self.parser.Parse(data, 0)

class Window:

    def __init__(self, root):
        self.root = root
        self.get = Tkinter.Button(root, text='获取RSS', command=self.get)
        self.get.place(x=280, y=15)
        self.frame = Tkinter.Frame(root, bd=2)
        self.scrollbar = Tkinter.Scrollbar(self.frame)
        self.edit = Tkinter.Text(self.frame,
                                 yscrollcommand=self.scrollbar.set,
                                 width=96,
                                 height=32)
        self.scrollbar.config(command=self.edit.yview)
        self.edit.pack(side=Tkinter.LEFT)
        self.scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        self.frame.place(y=50)

    def get(self):
        url = 'https://www.python.org/jobs/feed/rss/'
        page = urllib.urlopen(url)
        data = page.read()
        parser = ParserXML(self.edit)
        parser.feed(data)

root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.maxsize(600, 480)
root.mainloop()  

```

运行后，生成的结果如下

![Image](https://cdn.xiaorongmao.com/up/article-100.png)
