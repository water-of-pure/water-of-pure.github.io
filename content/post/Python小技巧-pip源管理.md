+++
date = '2025-07-30T10:41:04.584176+08:00'
draft = false
title = 'Python小技巧 - pip源管理'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

列出pip配置信息，命令如下

```bash

pip config list
```

正常情况下，pip的配置文件是放在下面这个文件中的(我的是mac)

```bash

~/.config/pip/pip.conf
```

但是一般去配置它，也不会自动生成，我的就是，当然也不需要你自己去创建，多麻烦

我们只要自己添加一个配置项就好了

在国内，安装pip源码的时候，最麻烦的就是要千里迢迢的去国外拉资源，这样很不方便，必将有铜墙铁壁，有时候不方便

pip国内的一些镜像推荐几个如下

> *阿里云 http://mirrors.aliyun.com/pypi/simple/*

> *中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/*

> *豆瓣(douban) http://pypi.douban.com/simple/*

> *清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/*

> *中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/*

若担心安全问题请使用HTTPS加密源

我们以豆瓣的pip源为例子

```bash

pip config set global.index-url http://pypi.douban.com/simple/
pip config set global.trusted-host pypi.douban.com # 信任pypi.douban.com这个域名下面源，主要是解决不支持https的如果你配置了https源的话，不需要这个配置项也是可以的
```

下次再次执行pip源安装的时候就会从http://pypi.douban.com/simple/下面拉取源代码了，如下

```bash

pip install --upgrade pip
Looking in indexes: http://pypi.douban.com/simple/
Collecting pip
  Downloading http://pypi.doubanio.com/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl (1.4MB)
     |████████████████████████████████| 1.4MB 2.3MB/s
Installing collected packages: pip
  Found existing installation: pip 19.3.1
    Uninstalling pip-19.3.1:
      Successfully uninstalled pip-19.3.1
Successfully installed pip-20.0.2
```
