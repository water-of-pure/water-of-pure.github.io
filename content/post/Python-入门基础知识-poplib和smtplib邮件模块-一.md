+++
date = '2025-07-25T15:55:26.913930+08:00'
draft = false
title = 'Python 入门基础知识 - poplib和smtplib邮件模块(一)'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用poplib和smtplib模块收到邮件**

Python中的poplib模块和smtplib模块提供了对POP3协议和SMTP协议的支持。使用POP3协议可以登录E-mail

收取邮件，使用SMTP协议可以发送邮件。

本篇博文先介绍下如何收取邮件

**收取邮件**

一般的邮箱服务器都提供了POP3收取邮件的方式，Outlook等E-mail客户端就是使用POP3协议收取邮箱中的邮件。

使用Python的poplib模块可以实现一个简单的收取邮件的客户端。

**1、poplib模块简介**

使用poplib模块中的POP3类可以创建一个POP3对象实例。其原型如下

> POP3(host, port)

参数含义如下

> host: POP3邮件服务器
>
> port: 服务器端口，可选参数，默认为110

当创建一个POP3对象实例后可以使用其user方法向POP3服务器发送用户名。其原型如下

> user(username)

参数含义如下

> username: 登录服务器的用户名

使用POP3对象的pass\_方法可以向POP3服务器发送密码。其原型如下

> pass\_(password)

参数含义如下

> password: 登录服务器密码

当登录服务器后可以使用POP3对象的getwelcome方法获取服务器的欢迎信息。使用POP3对象的set\_debuglevel方法

可以设置调试级别。其原型如下

> set\_debuglevel(level)

参数含义如下

> level: 调试级别

使用POP3对象的stat可以获取邮箱的状态，如邮件数、邮箱大小等。使用POP3对象的list方法可以获得邮件的内容列表。

其原型如下

> list(which)

参数含义如下

> which: 可选参数，如果指定，则仅列出指定的邮件内容。

使用POP3对象的retr方法可以获取指定的邮件。其原型如下

> retr(which)

参数含义如下

> which: 指定要获取的邮件

使用POP3对象的dele方法可以删除指定额邮件。其原型如下

> dele(which)

参数含义如下

> which: 指定要删除的邮件

使用POP3对象的top方法可以删除指定的邮件。其原型如下

> top(which, howmuch)

参数含义如下

> which: 指定获取的邮件
>
> howmuch: 指定获取的行数

使用POP3对象的rset方法可以清除收件箱中的删除标记。使用POP3对象的noop方法可以保持同服务器的连接。

使用POP3对象的quit方法可以断开同服务器的连接。

**2、使用Python收取E-mail**

使用Python检查E-mail首先应该知道自己所使用的E-mail的POP3服务器地址和端口。对于网易163邮箱，其POP3

服务器的地址为pop.163.com，端口为默认值110。对于网易126的邮箱，其POP3服务器地址为pop.126.com，端口

为默认值110。使用其他的E-mail可以查看网站帮助，获取POP3服务器的地址和端口。

代码示例演示如下

```py
# _*_ coding: utf-8 -*-
import poplib
import re
import Tkinter

class Window:

    def __init__(self, root):
        label1 = Tkinter.Label(root, text='POP3:')
        label2 = Tkinter.Label(root, text='Port:')
        label3 = Tkinter.Label(root, text='用户名:')
        label4 = Tkinter.Label(root, text='密码:')
        label1.place(x=5, y=5)
        label2.place(x=5, y=30)
        label3.place(x=5, y=55)
        label4.place(x=5, y=80)

        self.entryPOP = Tkinter.Entry(root)
        self.entryPort = Tkinter.Entry(root)
        self.entryUser = Tkinter.Entry(root)
        self.entryPass = Tkinter.Entry(root, show='*')
        self.entryPort.insert(Tkinter.END, '110')
        self.entryPOP.place(x=50, y=5)
        self.entryPort.place(x=50, y=30)
        self.entryUser.place(x=50, y=55)
        self.entryPass.place(x=50, y=80)
        self.get = Tkinter.Button(root, text="收取邮件", command=self.get)
        self.get.place(x=60, y=120)
        self.text = Tkinter.Text(root)
        self.text.place(y=150)

    def get(self):  # 按钮事件
        try:
            host = self.entryPOP.get()  # 获取服务器地址
            port = self.entryPort.get()  # 获取主机端口
            user = self.entryUser.get()  # 获取用户名
            passwd = self.entryPass.get()  # 获取密码

            // pop = poplib.POP3(host, port)  # 创建POP3实例
            pop = poplib.POP3_SSL(host)  # 创建POP3实例
            pop.user(user)  # 登录服务器
            pop.pass_(passwd)

            stat = pop.stat()  # 获取状态
            self.text.insert(  # 输出状态
                Tkinter.END, 'Status: %d message(s), %d bytes\n' % stat)

            rx_headers = re.compile(r"(From|To|Subject)")  # 编译正则表达式
            for n in range(stat[0]):
                response, lines, bytes = pop.top(n + 1, 10)
                self.text.insert(Tkinter.END, "-" * 30 + '\n')
                self.text.insert(Tkinter.END, '\n'.join(
                    filter(rx_headers.match, lines)))  # 输出匹配到的内容
                self.text.insert(Tkinter.END, "-" * 30 + '\n')
        except IndexError, value:
            print(value)
            self.text.insert(Tkinter.END, '接受错误\n')

root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()  

```
