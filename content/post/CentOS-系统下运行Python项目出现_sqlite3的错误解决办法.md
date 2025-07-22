+++
date = '2025-07-22T18:31:39.001843+08:00'
draft = false
title = 'CentOS 系统下运行Python项目出现_sqlite3的错误解决办法'
categories = [
    "技术",

]

tags = [
    "CentOS",
    "Linux"
]
+++

先来看下这个错误提示：

```bash
Failed to load application: No module named _sqlite3
```

还是第一次见，唉，玩的少呗。

经过资料的查找是因为少了一个叫做\_sqlite3.so文件。这个在Centos系统中默认的python2.6是有的：存放的路径如下

```bash
/usr/lib64/python2.6/lib-dynload/_sqlite3.so
```

如果你的不在这里的话，可以使用如下命令查找一下：

```bash
find / -name _sqlite3.so
```

既然知道了原因我们就分析一下处理方法好了。

我呢就直接把python2.6下面的这个文件\_sqlite3.so直接复制到了python2.7对应的lib-dynload目录下了。

再次运行项目后是没有任何错误的。

不过你也可以自己去安装一下这个扩展，不过我觉得还是稍微费点时间，就没做了。
