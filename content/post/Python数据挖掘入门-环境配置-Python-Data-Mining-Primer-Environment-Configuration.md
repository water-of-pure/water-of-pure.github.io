+++
date = '2025-07-28T17:52:24.270207+08:00'
draft = false
title = 'Python数据挖掘入门-环境配置(Python Data Mining Primer - Environment Configuration)'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

1】创建虚拟环境

```bash
virtualenv -p /usr/local/Cellar/python/3.6.5/bin/python3 .env3
```

此处的python路径根据自己本地的环境来配置，如果本地安装的默认的就是python3的版本，可以直接创建虚拟环境，或者不创建虚拟环境也是可以的，只要保持本地的python版本是3以上的就好了。我这里的python版本是“Python 3.6.5”

提示：如果你没有安装virtualenv、python等基础的软件，请自行google安装，或者加群交流

安装完之后执行

```bash
source .env3/bin/activate
```

激活python3的运行环境

2】安装ipython

```bash
pip install ipython[all]
```

这里注意别安装错误了

```bash
pip install ipython
```

跟

```bash
pip install ipython[all]
```

是不一样的

3】运行notebook

```bash
jupyter notebook
```

运行后会自动打开一个页面，界面类似如下

![Image](https://cdn.xiaorongmao.com/up/129-1.png)

4】安装scikit-learn库

scikit-learn库是Pythonk开发的机器学习库，这个库包含大量的机器机器算法、数据集、工具和框架

```bash
pip install scikit-learn
```

好了，以上我们就搭建了数据挖掘需要的基本环境
