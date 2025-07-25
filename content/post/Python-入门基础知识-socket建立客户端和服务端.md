+++
date = '2025-07-25T15:55:10.820412+08:00'
draft = false
title = 'Python 入门基础知识 - socket建立客户端和服务端'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**socket建立客户端和服务端**

**1，建立服务端**

使用socket模块建立一个简单的服务端。首先应创建一个socket对象，使用socket对象的bind方法绑定IP地址和端口。

然后使用socket对象的listen方法监听socket连接。最后进入循环等待客户端的连接。代码如下

```py
# -*- coding: utf-8 -*-
import Tkinter
import threading
import socket

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
                self.edit.insert(Tkinter.END, '收到的数据:%s\n' % data)  # 向文本框中输出数据
                client.send('I GOT: %s' % data)  # 发送数据
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

在上面的代码中，由于使用while循环监听连接，为了避免图形界面下假死的状态，将while循环放在一个线程里执行，

但Python中没有提供结束线程的函数或者方法，为了随时终止监听，在脚本中创建了一个控制线程。通过控制线程执行

监听线程，然后控制线程进如等待状态。当event被设置后，在控制线程中将关闭socket连接，监听也就停止了。由于

监听线程已经进入监听状态，在控制线程中关闭socket连接将导致异常，所有在监听线程中使用try捕获异常，结束循环。

**2，建立客户端**

客户端的创建相对简单，只要连接指定的IP和端口地址，然后想服务器发送数据即可，代码如下

```py
# -*- coding: utf-8 -*-
import Tkinter
import socket

class Window:

    def __init__(self, root):  # 创建组件
        label1 = Tkinter.Label(root, text='IP')
        label2 = Tkinter.Label(root, text='Port')
        label3 = Tkinter.Label(root, text='Data')
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
        self.send.place(x=40, y=80)

    def send(self):  # 按钮事件
        try:  # 异常处理
            ip = self.entryIP.get()  # 获取IP
            port = self.entryPort.get()  # 获取端口
            data = self.entryData.get()  # 获取发送数据
            client = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象

            client.connect((ip, int(port)))  # 连接服务器
            client.send(data)  # 发送数据
            rdata = client.recv(1024)  # 接收数据
            self.Recv.insert(Tkinter.END, "Server: " + rdata + '\n')  # 输出接收的数据
            client.close()  # 关闭连接
        except IndexError, value:
            print(value)
            self.Recv.insert(Tkinter.END, '发送错误\n')

root = Tkinter.Tk()
window = Window(root)
root.mainloop()  

```

服务端点击"开始监听"后，启动客户端，点击"发送数据"，这样客户端就能跟服务端进行通信了。

对于新手来说这里又用到Tkinter，这个GUI的模块，请关注后面的GUI模块的相关分享
