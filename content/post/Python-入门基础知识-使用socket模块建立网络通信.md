+++
date = '2025-07-25T15:55:07.488900+08:00'
draft = false
title = 'Python 入门基础知识 - 使用socket模块建立网络通信'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用socket模块建立网络通信**

使用Python中的socket模块提供的socket对象的方法，可以在计算机与计算机之间建立连接。一般来说，使用socket创建的通信

应有服务端和客户端，服务端首先建立一个socket，并等待客户端的连接。

客户端建立与服务端的socket连接，当连接成功后，客户端和服务端就可以使用socket进行通信。

**socket模块简介**

使用socket模块时，应首先使用socket()函数，创建一个socket对象。然后就可以使用socket对象的方法创建连接。

socket()函数原型如下

> socket(family, type, proto)

参数含义如下：

> family: 地址系列，可选参数。默认为AF\_INET，也可以是AF\_INET6或AF\_UNIX。
>
> type: socket类型，可选参数。默认为SOCK\_STREAM
>
> proto: 协议类型，可选参数。

创建好socket对象后，可以使用socket对象的bind方法绑定IP地址和端口。

bind方法的原型如下所示。

> bind(address)

其参数函数如下

> address: 由IP地址和端口组成的元组，例如"('127.0.0.1', 1051)"。如果IP地址为空，则表示本机。

使用socket对象的listen方法可以监听所有socket对象创建的连接。

其函数原型如下

> listen(backlog)

其参数含义如下

> backlog: 指定连接队列数，最小值为1，最大值由所使用的操作系统决定，一般情况下为5。

使用socket对象的connect和connect\_ex都可以连接到服务端，不同的是将返回一个错误，代替引发一个异常。

> connect(address)
>
> connect\_ex(address)

其参数含义如下

> address: 由IP地址和端口组成的元组。

使用socket对象的accept方法可以接收来自客户端的数据。accept方法将返回一个新的socket对象和客户端的地址。

使用socket对象的recv和recvfrom方法都可以从socket对象获取数据，不同的是recvfrom方法将返回所接收的字符串和地址，

而recv方法仅返回字符串，其原型分别如下

> recv(bufsize, flags)
>
> recvfrom(bufsize, flags)

其参数含义如下

> bufsize: 指定接收缓冲区的大小
>
> flags: 接收标志，可选参数。

使用socket对象的send和sendall方法都可以向已经连接的socket发送数据，不同的是sendall将一直发送完全的数据，

其原型分别如下

> send(string, flags)
>
> sendall(string, flags)

其参数含义如下

> string: 所发送的数据
>
> flags: 发送标志，可选参数

使用socket对象的sendto方法可以向一个未连接的socket发送数据，

其参数原型如下

> sendto(string, flags, address)

其参数含义如下

> string: 所发送的数据
>
> flags: 发送标志，可选参数
>
> address: 由IP地址和端口组成的元组

使用socket对象的makefile方法可以将socket关联到文件对象上，

其原型如下

> makefile(mode, bufsize)

参数含义如下

> mode: 文件模式，可选参数
>
> bufsize: 缓冲区大小，可选参数

当完后通信后，应使用socket对象的close方法关闭网络连接。

下一篇文章我们演示下如何建立服务器
