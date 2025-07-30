+++
date = '2025-07-30T09:57:20.824544+08:00'
draft = false
title = '如何使用fabric 2.x使用并行方式和串行方式远程自动化运维部署'
categories = [
    "技术",

]

tags = [
    "Python",
    "Fabric"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1575509665/gowhich/fabric1.jpg"
+++

之前一篇文章介绍如何使用fabric进行远程自动化部署

[fabric2.x使用指南](https://www.walkerfree.com/article/183)

脚本如下

```python

import getpass
from fabric import Connection, task
from invoke import Responder

hosts = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']

user = raw_input('Input username: ')
project = raw_input('Input project dirname: ')
auth_pass = getpass.getpass('Input auth pass: ')

# 需要sudo权限的时候需要
sudo_pass = Responder(
        pattern=r'\[sudo\] password',
        response=auth_pass + '\n',
)

@task
def deploy(c):
    for h in hosts:
        conn = Connection('%s@%s' % (user, h), connect_kwargs={'password': auth_pass})
        command = 'ls -al'
        # sudo 权限可用下面的命令
        # conn.run(command, pty=True, watchers=[sudo_pass])
        # 非sudo权限可用下面的命令 - 这里使用非sudo权限
        conn.run(command)
```

串行方式如下

```python

import getpass
from fabric import Connection, task, SerialGroup
from invoke import Responder

hosts = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']

user = raw_input('Input username: ')
project = raw_input('Input project dirname: ')
auth_pass = getpass.getpass('Input auth pass: ')

# 需要sudo权限的时候需要
sudo_pass = Responder(
        pattern=r'\[sudo\] password',
        response=auth_pass + '\n',
)

@task
def deploy(c):
    g = SerialGroup(*hosts, user=user, connect_kwargs={'password': auth_pass})
    command = 'ls -al'
    # sudo 权限可用下面的命令
    # conn.run(command, pty=True, watchers=[sudo_pass])
    # 非sudo权限可用下面的命令 - 这里使用非sudo权限
    conn.run(command)
```

并行方式如下

```py

import getpass
from fabric import Connection, task, SerialGroup
from invoke import Responder

hosts = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4']

user = raw_input('Input username: ')
project = raw_input('Input project dirname: ')
auth_pass = getpass.getpass('Input auth pass: ')

# 需要sudo权限的时候需要
sudo_pass = Responder(
        pattern=r'\[sudo\] password',
        response=auth_pass + '\n',
)

@task
def deploy(c):
    g = ThreadingGroup(*hosts, user=user, connect_kwargs={'password': auth_pass})
    command = 'ls -al'
    # sudo 权限可用下面的命令
    # conn.run(command, pty=True, watchers=[sudo_pass])
    # 非sudo权限可用下面的命令 - 这里使用非sudo权限
    conn.run(command)
```

节省掉了for循环的操作 但是增加了排查问题的难度

这里举例如何处理异常

```python

import socket, paramiko.ssh_exception
from fabric import SerialGroup, exceptions, runners
from fabric import task
from fabric.exceptions import GroupException

@task
def run(c):
    g = SerialGroup('localhost')
    try:
        res = g.run('hostname')
        # print(res)
    except GroupException as e:
        for c, r in e.result.items():
            print("{}".format(c.host))
            print(c)
            print(r)
            if isinstance(r, runners.Result):
                print(" SUCCESS, " + r.stdout.strip())
            elif isinstance(r, socket.gaierror):
                print("NetWork Error")
            elif isinstance(r, paramiko.ssh_exception.AuthenticationException):
                print("Auth failed")
            else:
                print('Other Error')
```

基础知识汇总

Fabric 提供了一个 fabric.group.Group 基类，并由其派生出两个子类，区别是：

* SerialGroup(\*hosts, \*\*kwargs)：按串行方式执行操作
* ThreadingGroup(\*hosts, \*\*kwargs)：按并发方式执行操作

参考资料：

https://cloud.tencent.com/developer/article/1590930
