+++
date = '2025-07-30T09:56:44.850627+08:00'
draft = false
title = 'fabric2.x使用指南'
categories = [
    "技术",

]

tags = [
    "Python",
    "Fabric"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1575509665/gowhich/fabric1.jpg"
+++

之前在看flask1.0的文档，里面学到了一个自动部署的工具fabric，但是里面介绍的是1.0系列的使用指南，但是我安装的时候版本已经更新了，已经是fabric2.x了，so，没办法，直接使用fabric2.x的版本吧，但是文档是fabric1.0的版本确实挺难受，毕竟很多功能要靠自己去摸索，然后再一点一点的实现，刚开始也是一头雾水，没有思路，今天回过头一看其实很简单的，主要是远程连接这块，不在区分本地和远程连接了，fabric1.x版本的时候会有个`local`的方法，使用起来一目了然，就知道具体这个是本地的还是远程。然后有小伙伴说了，就使用这个版本不行吗，我说不行，具体可以去fabric官网看下升级的必要性说明，其他不多说了，下面看下我说如何使用fabric2.x实现具体细节的

代码如下

```py

# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-04 16:52:35
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-04 18:41:59

import getpass
from fabric import Connection, task

@task
def pack(c):
    # 这里的c参数我理解为是Connection连接的本地 然后根据setup.py进行项目打包
    c.run('python setup.py release sdist --format=gztar')

@task
def deploy(c):
    # 输入服务器的登录用户名
    user = raw_input('Input login user name: ')
    # 输入服务器的登录地址
    host = raw_input('Input login host: ')
    # 输入服务器的项目目录地址
    root = raw_input('Input project root path：')
    # 输入服务器的登录密码
    user_pass = getpass.getpass('Input login user pass：')
    # 获取包的全名称
    result = c.run('python setup.py --fullname', hide=True)
    dist = result.stdout.strip()
    filename = '%s.tar.gz' % dist

    # 获取包的名称 - 这个名称可以根据自己的需求来自定义，这里主要是为了下面supervisor启动时使用
    result = c.run('python setup.py --name', hide=True)
    name = result.stdout.strip()

    # 远端服务器连接创建
    remote = Connection('%s@%s' % (user, host),
                        connect_kwargs={"password": user_pass})
    # 上传文件到远端服务器
    remote.put('./dist/%s' %
               filename, remote='%s' % root)

    # 在远端服务器上执行下面命令 - 这个会默认输出你在远端服务器展示的信息
    result = remote.run('cd %s &&\
     source .env/bin/activate &&\
        ls -al && type python &&\
         pip install %s &&\
         supervisorctl restart walkerfree' % (root, filename))
```

使用方式如下

```bash

fab pack deploy
```

这个命令其实也可以分布执行

```bash

fab pack
fab deploy
```

我上面的代码也可以将两个函数合并到一起在执行，分开的话主要是看起来思路比较清晰
