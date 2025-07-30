+++
date = '2025-07-30T09:57:15.008858+08:00'
draft = false
title = 'Python 3.8 安装细节记录'
categories = [
    "技术",

]

tags = [
    "Python",

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

### 为了防止安装virtualenv时`sudo /usr/local/bin/pip install virtualenv`遇到如下错误

```bash

ModuleNotFoundError: No module named '_ctypes'
```

在CentOS 7下执行下面命令

```bash

sudo yum install libffi-devel -y
```

然后源码安装

```bash

cd Python-3.8.0
sudo make && sudo make install
```

### 为了防止安装mysql时遇到如下错误

```bash

OSError: mysql_config not found
```

在Centos 7下执行下面命令

```bash

sudo yum install mysql-devel -y
```

然后源码安装

```bash

cd Python-3.8.0
sudo make && sudo make install
```
