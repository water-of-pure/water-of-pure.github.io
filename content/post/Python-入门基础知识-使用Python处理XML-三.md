+++
date = '2025-07-25T15:55:46.043401+08:00'
draft = false
title = 'Python 入门基础知识 - 使用Python处理XML（三）'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用xml.dom处理XML的简介**

DOM(Document Object Model)，即文档对象模型，使用树式结构创建XML文档。Python的xml.dom模块提供了DOM

接口，可以将XML文档转为树结构。Python提供了基本的DOM分析系统minidom模块和复杂的DOM分析系统pulldom

模块。minidom模块适用于较小的XML文档，因为它将整个文档读到内存中。而pulldom模块则适用于较大的XML文档，

因为它不将整个XML文档读入内存。

Python的xml.dom中的接口较多，其常用的有Element对象中的如下几种方法

> getElementByTagName(): 用于获取标记的分支
>
> getElementBtTagNameNS(): 用于获取标记的分支(使用了命名空间的情况)
>
> getAttribute(): 用于获取属性值
>
> getAttributeNode(): 用于获取属性节点
>
> getAttributeNS(): 用于获取属性值(使用了命令空间的情况)
>
> getAttributeNodeNS(): 用于获取属性节点(使用了命令空间的情况)
>
> removeAttribute(): 用于移除属性
>
> removeAttributeNode(): 用于移除属性节点
>
> removeAttributeNS(): 用于移除属性节点(使用了命令空间的情况)
>
> setAttribute(): 用于设置属性
>
> setAttributeNS(): 用于设置属性(使用了命令空间的情况)
>
> setAttributeNode(): 用于设置属性节点
>
> setAttributeNodeNS(): 用于设置属性节点(使用了命令空间的情况)

使用minidom时应首先使用parse，或parseString方法获取XML数据。当获取XML数据后就可以使用xml.dom中的

方法对XML文档进行处理。
