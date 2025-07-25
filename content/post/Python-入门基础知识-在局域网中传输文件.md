+++
date = '2025-07-25T15:55:14.855311+08:00'
draft = false
title = 'Python 入门基础知识 - 在局域网中传输文件'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

在局域网中传输文件

使用Python中的socket模块可以编写一个简单的传文件的脚本。传输文件也就是将文件内容依次发送出去。服务端代码实例如下

```py
# -*- coding: utf-8 -*-
import Tkinter
import threading
import socket
import os

class ListenThread(threading.Thread):  # 监听线程

    def __init__(self, edit, server):
        threading.Thread.__init__(self)
        self.edit = edit  # 保存窗口中的多行文本框
        self.server = server

    def run(self):  # 进入监听状态
        while 1:  # 使用while循环等待连接
            try:  # 捕获异常
                client, addr = self.server.accept()  # 等待连接
                self.edit.insert(Tkinter.END, '连接来自:%s:%d\n' %
                                 addr)  # 向文本框输出状态
                data = client.recv(1024)  # 接收数据
                print('recieve filename = ' + data)
                self.edit.insert(Tkinter.END, '收到的文件:%s\n' % data)  # 向文本框中输出数据
                file = os.open(data, os.O_WRONLY | os.O_CREAT |
                               os.O_EXCL)  # 创建文件
                while 1:
                    rdata = client.recv(1024)  # 接收数据
                    print('recieve data = ' + rdata)
                    if not rdata:
                        break

                    os.write(file, rdata)  # 将数据写入文件
                os.close(file)  # 关闭文件
                client.close()  # 关闭同客户端的连接
                self.edit.insert(Tkinter.END, '关闭客户端\n')  # 向文本框中输出状态
            except IndexError, value:
                self.edit.insert(Tkinter.END, value)
                self.edit.insert(Tkinter.END, '关闭连接\n')
                break  # 结束循环

class Control(threading.Thread):  # 控制线程

    def __init__(self, edit):
        threading.Thread.__init__(self)
        self.edit = edit  # 保留窗口中的多行文本框
        self.event = threading.Event()  # 创建Event对象
        self.event.clear()  # 清楚event标志

    def run(self):
        server = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)  # 创建socket连接
        server.bind(('', 1051))  # 绑定本地端口1051
        server.listen(1)  # 开始监听
        self.edit.insert(Tkinter.END, '正在等待连接\n')  # 向文本框中输出状态
        self.lt = ListenThread(self.edit, server)  # 创建监听线程对象
        self.lt.setDaemon(True)
        self.lt.start()  # 执行监听线程
        self.event.wait()  # 进入等待状态
        server.close()  # 关闭连接

    def stop(self):  # 结束控制线程
        self.event.set()  # 设置event标志

class Window:  # 主窗口

    def __init__(self, root):
        self.root = root
        self.butlisten = Tkinter.Button(
            root, text='开始监听', command=self.listen)  # 创建组件
        self.butlisten.place(x=20, y=15)
        self.butclose = Tkinter.Button(root, text='停止监听', command=self.close)
        self.butclose.place(x=120, y=15)
        self.edit = Tkinter.Text(root)
        self.edit.place(y=50)

    def listen(self):  # 处理按钮事件
        self.ctrl = Control(self.edit)  # 创建控制线程对象
        self.ctrl.setDaemon(True)
        self.ctrl.start()  # 执行控制线程

    def close(self):
        self.ctrl.stop()  # 结束控制线程

root = Tkinter.Tk()
window = Window(root)
root.mainloop()  

```

下面是客户端的代码，用户发送文件(脚本中没有处理字符编码，因此发送的文件路径和文件名不能包含中文)。客户端代码示例如下

```py
# -*- coding: utf-8 -*-
import Tkinter
import tkFileDialog
import socket
import os
import time

class Window:

    def __init__(self, root):  # 创建组件
        label1 = Tkinter.Label(root, text='IP')
        label2 = Tkinter.Label(root, text='Port')
        label3 = Tkinter.Label(root, text='文件')
        label1.place(x=5, y=5)
        label2.place(x=5, y=30)
        label3.place(x=5, y=55)

        self.entryIP = Tkinter.Entry(root)
        self.entryIP.insert(Tkinter.END, '127.0.0.1')
        self.entryPort = Tkinter.Entry(root)
        self.entryPort.insert(Tkinter.END, '1051')
        self.entryData = Tkinter.Entry(root)
        self.entryData.insert(Tkinter.END, 'Hello')

        self.Recv = Tkinter.Text(root)
        self.entryIP.place(x=40, y=5)
        self.entryPort.place(x=40, y=30)
        self.entryData.place(x=40, y=55)

        self.Recv.place(y=105)
        self.send = Tkinter.Button(root, text='发送数据', command=self.send)
        self.openfile = Tkinter.Button(root, text='浏览', command=self.open_file)
        self.send.place(x=40, y=80)
        self.openfile.place(x=170, y=55)

    def send(self):  # 按钮事件
        try:  # 异常处理
            ip = self.entryIP.get()  # 获取IP
            port = self.entryPort.get()  # 获取端口
            filename = self.entryData.get()  # 获取发送数据
            tt = filename.split('/')
            name = tt[len(tt) - 1]
            client = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象

            client.connect((ip, int(port)))  # 连接服务器
            print('filename: ' + name)
            client.send(name)  # 发送数据

            time.sleep(3)

            file = os.open(filename, os.O_RDONLY |
                           os.O_EXCL)  # 打开文件
            while 1:  # 发送文件
                data = os.read(file, 1024)
                if not data:
                    break
                print('filename data : ' + data)
                client.send(data)
            os.close(file)
            client.close()  # 关闭连接
        except IndexError, value:
            print(value)
            self.Recv.insert(Tkinter.END, '发送错误\n')

    def open_file(self):
        r = tkFileDialog.askopenfilename(
            title='Python Tkinter',
            filetypes=[('All Files', '*'), ('Python', '*.py *.pyw')])
        if r:
            self.entryData.delete(0, Tkinter.END)
            self.entryData.insert(Tkinter.END, r)

root = Tkinter.Tk()
window = Window(root)
root.mainloop()

```
