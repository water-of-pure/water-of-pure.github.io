+++
date = '2025-07-30T10:40:13.609289+08:00'
draft = false
title = 'Fabric 并发方式执行项目部署命令'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "Fabric"
]
+++

最近做运维工作，遇到项目部署的问题，不过通过python库fabric也是可以解决问题的

而且还是很方便，大概的方式如下

强调下，这里使用的是fabric 2这个版本

原理也是简单就是，fabric提供了`ThreadingGroup`这个类，网上很少有人用吧，google很久才找到

先看下以前的并行的方式，是如何执行项目部署命令的

代码如下

```python

import getpass
from fabric import Connection, task
from invoke import Responder

hosts = [
    # service online machine
    '127.0.0.1',  # web1
    '127.0.0.2',  # web2
    '127.0.0.3',  # web3
]

user = input('Input username:')
auth_pass = getpass.getpass('Input password:')
sudo_pass = Responder(
    pattern=r'\[sudo\] password',
    response=auth_pass + '\n',
)

@task
def deploy_series(c):
    for host in hosts:
        conn = Connection('%s@%s' % (user, host),
                          connect_kwargs={'password': auth_pass})
        command = 'ls -al /'
        res = conn.run(command, pty=True, watchers=[sudo_pass])
        print(res)
```

示例代码简单的执行了`ls -al /`命令

上面的方式就是一台跟着一台机器的进行命令的执行，总的时间是没台机器执行完的时间总和，着实有点慢，影响代码上线的效率

下面看下并行的方式，并发的方式是如何运行的

代码如下

```python

import getpass
from fabric import Connection, task
from invoke import Responder
from fabric import SerialGroup, ThreadingGroup
from fabric.exceptions import GroupException

hosts = [
    # service online machine
    '127.0.0.1',  # web1
    '127.0.0.2',  # web2
    '127.0.0.3',  # web3
]

user = input('Input username:')
auth_pass = getpass.getpass('Input password:')
sudo_pass = Responder(
    pattern=r'\[sudo\] password',
    response=auth_pass + '\n',
)

@task
def deploy_parallel(c):
    g = ThreadingGroup(*hosts,
                       user=user,
                       connect_kwargs={'password': auth_pass})
    try:
        command = 'ls -al /'
        res = g.run(command, pty=True, watchers=[sudo_pass])
        print(res)
    except GroupException as e:
        for c, r in e.result.items():
            print(c)
            print(r)
```

同样的也只是执行命令而已

但是执行的顺序是并发的方式，总的执行时间是执行时间最长的那台机器的时间，很大程度提高了上线代码的执行效率。
