+++
date = '2025-07-25T15:55:22.846204+08:00'
draft = false
title = 'Python 入门基础知识 - 访问FTP'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**访问FTP**

Python中的ftplib模块提供了用于访问FTP的函数。使用ftplib模块可以在Python脚本中访问FTP，完后

上传、下载文件等

**1、ftplib模块简介**

使用ftplib模块中的FTP类，可以创建一个FTP连接对象。其原型如下

> FTP(host, user, passwd, acct)

参数含义如下

> host: 要连接的FTP服务器，可选参数
>
> user: 登录FTP服务器所使用的用户名，可选参数
>
> passwd: 登录FTP服务器所使用的密码，可选参数
>
> acct: 可选参数，默认为空

当创建一个FTP连接对象后，可以使用set\_debuglevel方法设置调试级别。其原型如下

> set\_debuglevel(level)

参数含义如下

> level: 调试级别，默认的调试级别为0

如果在创建FTP连接对象时未使用HOST参数，则可以使用FTP对象的connect方法，其原型如下

> connect(host, port)

其参数含义如下

> host: 要连接的FTP服务器
>
> port: FTP服务器的端口，可选参数

如果在创建FTP对象时未使用用户名和密码，则可以使用FTP对象的login对象使用用户名和密码

登录到FTP服务器。其原型如下

> login(user, passwd, acct)

其参数含义如下

> host: 要连接的FTP服务器，可选参数
>
> user: 登录FTP服务器所使用的用户名，可选参数
>
> passwd: 登录FTP服务器所使用的密码，可选参数

使用FTP对象的getwelcome方法可以获得FTP服务器的欢迎信息。使用FTP对象的abort方法可以中断文件传输。

使用FTP对象的sendcmd和voidcmd方法可以向FTP服务器发送命令。不同的是voidcmd没有返回值。其原型如下

> sendcmd(command)
>
> voidcmd(command)

其参数含义如下

> command: 向服务器发送的命令字符串

使用FTP对象的retrbinary和retrlines方法可以从FTP服务器下载文件。不同的是retrbinary方法使用二进制

形式传输文件，而retrlines方法使用ASCII形式传输文件。其函数原型如下

> retrbinary(command, callback, maxblocksize, rest)
>
> retrlines(command, callback)

retrbinary参数含义如下

> command: 传输命令，由"RETR+文件名"组成（之间有空格）
>
> callback: 传输回调函数
>
> maxblocksize: 设置每次传输的最大字节数，可选参数
>
> rest: 设置文件续传位置，可选参数

retrlines参数含义如下

> command: 传输命令
>
> callback: 传输回调函数

使用FTP对象的storbinary和storlines方法可以向FTP服务器上传文件。不同的是

storbinary方法使用二进制形式传输文件，而storlines方法使用ASCII形式传输文件。

其函数原型分别如下

> storbinary(command, file, blocksize)
>
> storlines(command, file)

storbinary参数含义如下

> command: 传输命令，由"STOR+文件名"组成（之间有空格）
>
> file: 本地文件句柄
>
> blocksize: 设置每次读取文件最大字节数，可选参数

storlines参数含义如下

> command: 传输命令
>
> file: 本地文件句柄

使用FTP对象的set\_pasv方法可以设置传输模式。其函数原型如下

> set\_pasv(boolean)

参数含义如下

> boolean: 如果为True，则为被动模式，如果未False，则为主动模式

使用FTP对象的dir方法可以获取当前目录中的内容列表。使用FTP对象的rename方法可以修改FTP

服务器中的文件名。其原型如下：

> rename(fromname, toname)

其参数含义如下

> fromname: 原来文件名
>
> toname: 重命名后的文件名

使用FTP对象的delete方法可以从FTP服务器上删除文件。其原型如下

> delete(filename)

其参数含义如下

> filename: 要删除的文件名

使用FTP对象的cwd方法可以改变当前目录。其原型如下：

> cwd(pathname)

参数含义如下

> pathname: 要进入目录的路径

使用FTP对象的mkd方法可以获得当前目录。使用FTP对象的rmd方法可以删除FTP服务器上的目录。其函数原型如下

> rmd(dirname)

参数含义如下

> dirname: 要删除的目录

使用FTP对象的size方法可以获得文件的大小。其函数原型如下

> size(filename)

其参数含义如下

> filename: 文件名

使用FTP对象的quit和close方法可以关闭同FTP服务器的连接。

**2、使用Python访问FTP**

Python的ftplib模块提供了完整的用于FTP协议的函数、方法，使用ftplib模块可以制作一个简单的

类似于Windows自带的FTP客户端。

代码示例演示如下

```py
# _*_ coding: utf-8 -*-
import string
from ftplib import FTP

bufsize = 1024

def get(filename):
    command = 'RETR ' + filename
    ftp.retrbinary(command, open(filename, 'wb').write, bufsize)
    print('下载成功')

def put(filename):
    command = 'STOR ' + filename
    filehandler = open(filename, 'rb')
    ftp.storbinary(command, filehandler, bufsize)
    filehandler.close()
    print('上传成功')

def pwd():
    print(ftp.cwd())

def size(filename):
    print(ftp.size(filename))

def help():
    print('''
    ==================================
              Simple Python FTP  
    ==================================
    cd              进入文件夹
    delete          删除文件
    dir             获取当前文件列表
    get             下载文件
    help            帮助
    mkdir           创建文件夹
    put             上传文件
    pwd             获取当前目录
    rename          重命名文件
    rmdir           删除文件夹
    size            获取文件大小

    ''')

server = raw_input('请输入FTP服务器地址:')
ftp = FTP(server)
username = raw_input('请输入用户名:')
passwd = raw_input('请输入密码:')
ftp.login(username, passwd)
print(ftp.getwelcome())
actions = {
    'dir': ftp.dir,
    'pwd': pwd,
    'cd': ftp.cwd,
    'get': get,
    'put': put,
    'help': help,
    'rmdir': ftp.rmd,
    'mkdir': ftp.mkd,
    'delete': ftp.delete,
    'size': size,
    'rename': ftp.rename
}

while True:
    print('pyftp>')
    cmds = raw_input()
    cmd = string.split(cmds)

    try:
        if len(cmd) == 1:
            if string.lower(cmd[0]) == 'quit':
                break
            else:
                actions[string.lower(cmd[0])]()
        elif len(cmd) == 2:
            actions[string.lower(cmd[0])](cmd[1])
        elif len(cmd) == 3:
            actions[string.lower(cmd[0])](cmd[1], cmd[2])
        else:
            print('输入错误')
    except:
        print('命令出错')
ftp.quit()  

```

实例环境声明

```bash
# version 2.7.13  

```
