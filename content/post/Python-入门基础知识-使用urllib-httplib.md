+++
date = '2025-07-25T15:55:18.985143+08:00'
draft = false
title = 'Python 入门基础知识 - 使用urllib、httplib'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用urllib、httplib**

Python提供的socket的模块主要用户底层网络协议，对于常用的HTTP协议和FTP协议可以使用Python中的

httplib和ftplib进行访问

**1、使用Python访问网站**

网站都是基于HTTP协议的，使用Python中的urllib和httplib都可以访问网站。其中urllib主要用于处理

URL，使用urllib操作URL可以使用和打开本地文件一样的操作。而httplib则实现了对HTTP协议的封装。

**1、urllib模块简介**

使用Python中的urllib模块可以对URL进行处理。使用urllib模块中的urlopen函数可以打开一个URL。

原型如下

> urlopen(url, data, proxies)

参数含义如下

> url: 要进行操作的URL地址
>
> data: 向URL传递的数据，可选参数
>
> proxies: 使用的代理地址，可选参数
>
> urlopen将返回一个类似于file的对象，可以像操作文件一样使用read、readline、close等方法对URL
>
> 进行操作。

使用urllib模块中的urlretrieve可以将URL保存为本地文件。

原型如下

> urlretrieve(url, filename, reporthook, data)

参数含义如下

> url: 要保存的URL地址
>
> filename: 指定保存的文件名，可选参数
>
> reporthook: 回调函数，可选参数
>
> data: 发送的数据，一般用于POST，可选参数

使用urllib模块中的urlencode可以对URL进行编码

原型如下

> urlencode(query, doseq)

参数含义如下

> query: 由要进行编码的变量和变量值组成的字典
>
> doseq: 可选参数，若为True，则将为元组的值分别编码成"变量=值"的形式

使用urllib模块中的quote和quote\_plus可以替换字符串中的特殊字符，使其符合URL所要求使用的字符

原型如下

> quote(string, safe)
>
> quote\_plus(string, safe)

参数含义如下

> string: 要进行替换的字符串
>
> safe: 可选参数，指定不需要替换的的字符，默认为"/"

使用urllib模块中的unquote和unquote\_plus可以将quote和quote\_plus替换后的字符还原

原型如下

> unquote(string)
>
> unquote\_plus(string)

参数含义如下

> string: 要进行还原的字符串

**2、httplib简介**

在Python的httplib模块中提供了HTTPConnection对象和HTTPResponse对象。

当创建一个HTTPConnection对象后，可以使用request方法向服务器发送请求

原型如下

> request(method, url, body, headers)

参数含义如下

> method: 发送的操作，一般为"GET"或"POST"
>
> url: 进行操作的URL
>
> body: 发送的数据
>
> headers: 发送的HTTP头

当想服务器发送请求后，可以使用HTTPConnection对象的getresponse方法返回一个HTTPResponse对象。使用

HTTPConnection对象的close方法可以关闭同服务器的连接。除了使用request方法外，还可以依次使用如下所示方法

向服务器发送请求。

> putrequest(request, selector, skip\_host, skip\_accept\_encoding)
>
> putheader(header, argument, ...)
>
> endheaders()
>
> send(data)

putrequest的参数含义如下

> request: 所发送的操作
>
> seletor: 进行操作的URL
>
> skip\_host: 可选参数，若为真，禁止自动发送"HOST:"
>
> skip\_accept\_encoding: 可选参数，若为真，禁止自动发送"Accept-Encoding:headers"

putheader的参数含义如下

> header: 发送的HTTP头
>
> argument: 发送的参数

send的参数函数如下

> data: 发送的数据

urllib模块中的HTTPResponse对象主要用于处理服务器对所发送请求的响应，使用HTTPResponse对象的read方法

可以获得服务器响应主体。使用HTTPResponse对象的getheader可以获得服务器响应的HTTP头

原型如下

> getheader(name, default)

参数含义如下

> name: 指定HTTP头名
>
> default: 可选参数，如果指定的name不存在，则获取default指定的HTTP头。

HTTPResponse对象还具有version、status和reason等属性，用于查看HTTP协议的版本、状态等。

**3、使用Python访问网站**

使用Python的urllib模块可以创建一个简单的访问网站的脚本，获取指定的页面。如果使用GUI库中显示HTML的

组件，还可以制作一个简单的Python Web浏览器，使用httplib模块也可以访问网站，但此过程比urllib模块要复杂。

httplib模块可以用于需要用户名和密码认证的网站，而urllib模块只能简单的访问、下载页面内容。

实例演示如下

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

import Tkinter
import urllib

class Window:

    def __init__(self, root):
        self.root = root
        self.entryUrl = Tkinter.Entry(root, width=40)  # 创建组件
        self.entryUrl.place(x=5, y=15)
        self.get = Tkinter.Button(root, text='下载页面', command=self.get)
        self.get.place(x=340, y=15)
        self.edit = Tkinter.Text(root)
        self.edit.place(y=50)

    def get(self):
        url = self.entryUrl.get()  # 获取URL
        page = urllib.urlopen(url)  # 打开URL
        data = page.read()  # 读取URL内容
        self.edit.insert(Tkinter.END, data)  # 将内容输出到文本框
        page.close()

root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()

```
