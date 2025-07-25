+++
date = '2025-07-25T15:55:29.531921+08:00'
draft = false
title = 'Python 入门基础知识 - poplib和smtplib邮件模块（二）'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**发送邮件**

发送邮件一般使用的是SMTP协议，使用Python的smtplib模块可以登录SMTP协议发送邮件。使用SMTP协议发送邮件，

首先要登录SMTP服务器

**1、smtplib模块简介**

使用smtplib模块的SMTP类可以创建一个SMTP对象实例。其原型如下

> SMPT(host, port, local\_hostname)

其参数含义如下

> host: 连接的服务器名，可选参数
>
> port: 服务器端口，可选参数
>
> local\_hostname: 本地主机名，可选参数

如果在创建SMTP对象时没有指定host和port，可以使用SMTP对象的connect方法连接到服务器。其原型如下

> connect(host, port)

其参数含义如下

> host: 连接的服务器名，可选参数
>
> port: 服务器端口，可选参数

使用SMTP对象的set\_debuglevel方法可以设置调试级别。其原型如下

> set\_debuglevel(level)

其参数含义如下

> level: 调试级别

使用SMTP对象的docmd方法可以向SMTP服务器发送命令，其原型如下

> docmd(cmd, argstring)

其参数含义如下

> cmd: 向SMTP服务器发送的命令
>
> argstring: 命令参数，可选参数

使用SMTP对象的sendmail方法可以发送邮件。其原型如下

> sendmail(from\_addr, to\_addr, msg, mail\_options, rcpt\_options)

参数含义如下

> from\_addr: 发送者邮件地址
>
> to\_addr: 接收者邮件地址
>
> msg: 邮件内容
>
> mail\_options: 邮件ESMTP操作，可选参数
>
> rcpt\_options: RCPT操作，可选参数

使用SMTP对象的quit方法可以断开同服务器的连接

**2、使用smtplib发送邮件**

和Python收取邮件一样，使用Python发送邮件，也可以找到所使用的SMTP服务器的地址和端口。对于网易163的邮箱，其SMTP

服务器的地址为smtp.163.com,端口默认值为25。对于网易126的邮箱，其SMTP服务器的地址为smtp.126.com，

端口默认值为25。

代码示例演示如下

```py
# _*_ coding: utf-8 -*-
import smtplib
import Tkinter

class Window:
    """docstring for Window"""

    def __init__(self, root):
        label1 = Tkinter.Label(root, text='SMTP')
        label2 = Tkinter.Label(root, text='Port')
        label3 = Tkinter.Label(root, text='用户名')
        label4 = Tkinter.Label(root, text='密码')
        label5 = Tkinter.Label(root, text='收件人')
        label6 = Tkinter.Label(root, text='主题')
        label7 = Tkinter.Label(root, text='发件人')

        label1.place(x=5, y=5)
        label2.place(x=5, y=30)
        label3.place(x=5, y=55)
        label4.place(x=5, y=80)
        label5.place(x=5, y=105)
        label6.place(x=5, y=130)
        label7.place(x=5, y=155)

        self.entryPOP = Tkinter.Entry(root)
        self.entryPort = Tkinter.Entry(root)
        self.entryUser = Tkinter.Entry(root)
        self.entryPass = Tkinter.Entry(root)
        self.entryTo = Tkinter.Entry(root)
        self.entrySub = Tkinter.Entry(root)
        self.entryFrom = Tkinter.Entry(root)

        self.entryPort.insert(Tkinter.END, '25')

        self.entryPOP.place(x=50, y=5)
        self.entryPort.place(x=50, y=30)
        self.entryUser.place(x=50, y=55)
        self.entryPass.place(x=50, y=80)
        self.entryTo.place(x=50, y=105)
        self.entrySub.place(x=50, y=130)
        self.entryFrom.place(x=50, y=155)

        self.get = Tkinter.Button(root, text='发送邮件', command=self.get)
        self.get.place(x=60, y=180)
        self.text = Tkinter.Text(root)
        self.text.place(y=200)

    def get(self):
        try:
            host = self.entryPOP.get()
            port = self.entryPort.get()
            user = self.entryUser.get()
            pw = self.entryPass.get()
            from_addr = self.entryFrom.get()
            to_addr = self.entryTo.get()
            subject = self.entrySub.get()
            text = self.text.get(1.0, Tkinter.END)  # 获取邮件内容
            msg = ("From: %s\nTo: %s\nSubject: %s\n\n" %
                   (from_addr, to_addr, subject))
            msg = msg + text

            smtp = smtplib.SMTP(host, port)
            smtp.set_debuglevel(1)
            smtp.login(user, pw)
            smtp.sendmail(from_addr, to_addr, msg)
            smtp.quit()
        except IndexError, value:
            print(value)
            self.text.insert(Tkinter.END, '发送错误\n')

root = Tkinter.Tk()
window = Window(root)
root.minsize(600, 480)
root.mainloop()  

```
