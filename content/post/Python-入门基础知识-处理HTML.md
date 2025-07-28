+++
date = '2025-07-25T15:55:36.263007+08:00'
draft = false
title = 'Python 入门基础知识 - 处理HTML'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**![Image](https://cdn.xiaorongmao.com/up/fw658.png)**

**处理HTML**

在Python中可以使用HTMLParser模块处理HTML，获取页面中感兴趣的内容

HTMLParser模块提供了对HTML标记处理的方法。如果有些内容不能使用HTMLParser

处理，还可以自己编写正则表达式进行匹配

**1、HTMLParser模块简介**

在使用HTMLParser模块处理HTML时，首先应继承HTMLParser模块中的HTMLParser

类，然后重载相关的处理方法。使用HTMLParser对象的feed方法可以向HTMLParser传递数据。

其原型如下

> feed(data)

参数含义

> data: 传递的数据

当向HTMLParser对象传递数据后，就开始对数据进行处理。使用HTMLParser对象的close

方法，可以强制处理feed方法存在缓冲区的数据。使用HTMLParser对象的reset方法

可以重新设置对象实例，进行新一轮的数据处理。使用HTMLParser对象的getpos方法

可以获得当前处理的行号和偏移位置。

在使用HTMLParser处理HTML的过程中，遇到某些标记或者数据就会调用相应的方法。一般

情况下，在脚本中需要重载这些方法，已完成对HTML的处理。当HTMLParser每次遇到一个

起始标记时，会调用handle\_starttag方法。原型如下

> handle\_starttag(tag, attrs)

参数含义

> tag: HTMLParser遇到的标记
>
> attrs: 标记的属性

当HTMLParser遇到类似于<br />的标记时，将调用handle\_startendtag方法。原型如下

> handle\_startendtag(tag, attrs)

参数含义

> tag: HTMLParser遇到的标记
>
> attrs: 标记的属性

当HTMLParser遇到结束标记时，会调用handle\_endtag。其原型如下

> handle\_endtag(tag)

参数含义

> tag: HTMLParser遇到的结束标记。

使用HTMLParser的handle\_data方法可以处理标记间的数据。原型如下

> handle\_data(data)

参数含义

> data: 标记间的数据

当HTMLParser遇到HTML中的注释时，将调用handle\_comment方法。原型如下

> handle\_comment(data)

参数含义如下

> data: 注释内容

除了HTMLParser模块中的HTMLParser类以外，在htmllib模块中也提供了一个简单的HTMLParser

类。其提供了处理超链接和图片的方法。htmllib模块中HTMLParser类处理超链接

的方法如下

> anchor\_bgn(href, name, type)
>
> anchor\_end()

参数如下

> href: href属性
>
> name: name属性
>
> type: type属性

htmllib模块中HTMLParser类处理图片的方法原型如下

> handle\_image(source, alt, ismap, align, width, height)

参数含义

> source: source属性
>
> alt: alt属性
>
> ismap: ismap属性
>
> align: align属性
>
> width: width属性
>
> height: height属性

**2、获取页面图片地址**

在Python的HTMLParser模块中提供了处理标记的方法，由于在网页中图片都是以'<img>'标记

嵌入到网页中的，因此要获取页面中图片的地址只要处理'<img>'标记即可。如下代码实例

重载了HTMLParser类的handle\_starttag方法，对'<img>'标记进行处理分别获得GIF和JPG

图片的地址。

```py
# _*_ coding: utf-8 -*-
import Tkinter
import urllib
import HTMLParser

class ImageHTMLParser(HTMLParser.HTMLParser):

    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.gifs = []
        self.jpgs = []

    def handle_starttag(self, tags, attrs):
        if tags == 'img':
            for attr in attrs:
                for t in attr:
                    if 'gif' in t:
                        self.gifs.append(t)
                    elif 'jpg' in t:
                        self.jpgs.append(t)
                    else:
                        pass

    def get_gifs(self):
        return self.gifs

    def get_jpgs(self):
        return self.jpgs

class Window:

    def __init__(self, root):
        self.root = root
        self.label = Tkinter.Label(root, text='输入URL:')
        self.label.place(x=5, y=15)
        self.entryUrl = Tkinter.Entry(root, width=30)
        self.entryUrl.place(x=65, y=15)
        self.get = Tkinter.Button(root, text='获取图片', command=self.get)
        self.get.place(x=280, y=15)

        self.edit = Tkinter.Text(root, width=470, height=600)
        self.edit.place(y=50)

    def get(self):
        try:
            url = self.entryUrl.get()
            page = urllib.urlopen(url)
            data = page.read()
            parser = ImageHTMLParser()
            parser.feed(data)
            self.edit.insert(Tkinter.END, '============GIF=========\n')
            gifs = parser.get_gifs()
            for gif in gifs:
                self.edit.insert(Tkinter.END, gif + '\n')

            self.edit.insert(Tkinter.END, '========================\n')
            self.edit.insert(Tkinter.END, '============JPG=========\n')
            jpgs = parser.get_jpgs()
            for jpg in jpgs:
                self.edit.insert(Tkinter.END, jpg + '\n')

            self.edit.insert(Tkinter.END, '========================\n')
            page.close()
        except IndexError, value:
            print(value)

root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()  

```

运行脚本后，在文本框中输入网址，单击'获取图片'按钮，将对网址进行处理，获取网页

中的图片地址。由于很多网站使用的HTML不是标准的语法格式，因此，使用HTMLParser

处理时，并不一定能够获得所有的图片。
