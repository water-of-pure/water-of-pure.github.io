+++
date = '2025-07-30T11:44:26.617752+08:00'
draft = false
title = 'fabric 2.5.0添加类似env配置文件，减少执行命令重复操作'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1575509665/gowhich/fabric1.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "Fabric"
]
+++

fabric 2.5.0可以通过添加类似env配置文件，从而达到减少执行命令的重复操作，比如减少每次执行任务的用户名和密码的输入

如果将用户名和密码写入fabric.py这种项目文件中，并提交到git仓库的话也是非常不安全的

但是根据用户来创建一个可自己访问和执行的文件就比较方便，尤其是在linux系统下，多个用户多一个操作系统都有权限的话，每个用户下面只要有个`~/.fabric.yaml`文件

便可以执行fabric的任务操作，从而避免了将重要密码暴漏给所有人，或者将自己的密码共享给所有人

创建配置文件

```bash

touch ~/.fabric.yaml
```

在配置文件中添加类似如下的配置信息

```ini

user: dpzhang
pwd: 123456
```

然后在`fabric.py`中添加任务

```python

# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-04 16:52:35
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-20 18:50:44

import getpass
from fabric import Connection, task

@task
def test(c):
    print(c.user)
    print(c.pwd)
```

命令行下执行

```bash

fab test
```

得到输出的结果如下

```bash

dpzhang
123456
```

如果将test方法修改如下

```python

# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-04 16:52:35
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-20 18:50:44

import getpass
from fabric import Connection, task

@task
def test(c):
    print(c.user)
    print(c.pwd)
    print(c.hosts.host)
```

同时修改`~/.fabric.yaml`，内容修改后如下

```ini

user: dpzhang
pwd: 123456
hosts:
    host: 127.0.0.1
```

再次运行

```bash

fab test
```

得到的输出结果如下

```bash

dpzhang
123456
127.0.0.1
```
