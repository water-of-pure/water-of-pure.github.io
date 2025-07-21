+++
date = '2025-07-21T18:17:12.795234+08:00'
draft = false
title = 'Package name does not correspond to the file path - IntelliJ 解决方案'
categories = [
    "技术",

]

tags = [
    "IntelliJ",

]
+++

在使用IntelliJ做java测试的时候，我不希望我会用到多么完善的框架，因为就只是类似一个工厂方法模式的测试，

直接就创建了java文件，代码里面使用了package这样的方法，结果运行的时候，发现我的sdk没有配置，于是开始配置，

配置完之后发现一个问题，文件中package的地方都提示一个红色波浪线在下面，并且提示的信息类似是这样的

Package name does not correspond to the file path

怎么办？

多次尝试后，答案有了出路。

> 右键点击src->New->Package->输入Package的名称，我这里是qeeniao.com

然后把其他加了package qeeniao.com;的代码拖到这个目录下面就好了。
