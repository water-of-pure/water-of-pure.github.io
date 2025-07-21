+++
date = '2025-07-21T18:16:09.788734+08:00'
draft = false
title = 'react-native 学习（一）'
categories = [
    "技术",

]

tags = [
    "ReactNative",

]
+++

react-native的安装

首先确定自己是否安装了Node，如果没有安装Node的话，就需要安装node了，因为是依赖node的。

安装推荐方式：nvm

nvm是node的一个多版本管理器，方便管理node的版本安装和更新，本人觉得超级好用，推荐之。

nvm的安装很简单，去github上了解一下就好了，这里给个链接：<https://github.com/creationix/nvm>

安装完就可以安装node了，使用nvm安装node很简单

```bash
nvm install v4.2.1
```

就这么简单

安装完node，还要设定一下，不然一会安装完react-native后启动了，还是会找不到node

```bash
nvm alias default v4.2.1
```

这样的话v4.2.1版本的node就加入到你的Path中了，每次启动都会默认存在的。

安装react-native

```bash
node install react-native -g
brew install watchman
brew instal flow //建议安装上比较好，不然watchman出问题怎么办，备用
```

就是这样，可以了，等待安装结束吧

**================**

**brew 没有咋办？自己去安装哇，这么好用的工具都不知道:<http://brew.sh/>**

**================**

生成一个react-native项目吧

```bash
react-native init GowhichProject
```

如何查看项目呢，需要用到xcode，没有的话，自己先安装吧，安装完再继续看吧。这里假如你已经安装好了。

用xcode打开GowhichProject/ios/目录下的.xcodeproj为后缀的文件，运行一下模拟器试试吧。

=====

以上步骤没看懂？好吧，给自己一个连接吧

英文：

<https://facebook.github.io/react-native/docs/getting-started.html#content>

中文：

<http://wiki.jikexueyuan.com/project/react-native/GettingStarted.html>
