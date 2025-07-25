+++
date = '2025-07-25T15:55:40.065273+08:00'
draft = false
title = 'Python 入门基础知识 - 使用Python处理XML（一）'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用Python处理XML**

在Python中提供了许多标准模块用于处理XML文档。例如使用Expat分析器的xml.parsers.expat模块，

使用SAX分析器的xml.sax模块，使用DOM的xml.dom模块。其中xml.parsers.expat和xml.sax模块与

HTMLParser类似，都是基于事件的方式对XML文档进行分析。

**本篇文章简单了解下使用xml.parsers.expat处理XML**

在Python中使用xml.parsers.expat处理XML时，应首先使用其ParserCreate创建一个XMLParser实例

对象。其原型如下

> ParserCreate(encoding, namespace\_separator)

参数含义如下

> encoding: XML文档的编码，可选参数
>
> namespace\_separator: XML文档的命令空间，可选参数

当创建XMLParser对象后需要使用Parse或者ParseFile方法向其传递要处理的XML数据或XML文档。其原型如下

> Parse(data, isfinal)

参数含义如下

> data: 要进行处理的XML数据
>
> isfinal: 当最后一次调用该方法时，isfinal应为True，可选参数

> ParseFile(file)

参数含义如下

> file: 打开的文件对象

在使用XMLParser处理XML的过程中，当遇到相应的事件时，XMLParser会调用相应的事件处理方法。在使用

XMLParser时可以通过继承创建新类，重载需要处理的方法，也可以直接使用XMLParser，自己编写函数，将

其赋值给XMLParser的处理方法。当XMLParser遇到XML文档声明时，会调用XmlDeclHandler方法，其原型如下

> XmlDeclHandler(version, encoding, standalone)

其参数如下

> version: XML规范的版本
>
> encoding: XML文档的编码
>
> standalone: XML文档的standalone属性值

当XMLParser遇到文档类型定义开始时，将调用StartDoctypeDeclHandler方法，当结束时将调用EndDoctypeDeclHandler

方法。其原型如下

> StartDoctypeDeclHandler(doctypeName, systemId, publicId, has\_internal\_subset)

参数含义如下

> doctypeName: DID名称
>
> systemId: 系统标识
>
> publicId: 公共标识
>
> has\_internal\_subset: 如果XML文档包含DTD，则has\_internal\_subset为真

EndDoctypeDeclHandler()

当XMLParser遇到DTD中元素声明时，将调用ElementDeclHandler方法。其原型如下

> ElementDeclHandler(name, model)

参数含义如下

> name: 元素名
>
> model: 元素内容模型

当XMLParer遇到DTD中元素属性声明时，将调用AttlistDeclHandler方法，其原型如下

> AttlistDeclHandler(elname, attname, type, default, required)

参数含义如下

> elname: 元素名
>
> attname: 属性名
>
> type: 元素数据类型
>
> default: 属性默认值
>
> required: 如果属性为必须的，则required为真。

当XMLParser遇到元素开始标记时，将调用StartElementHandler方法，当遇到结束标记是，将调用EndElementHandler

方法，原型如下

> StartElementHandler(name, attributes)

参数含义如下

> name: 元素名
>
> attributes: 元素属性

> EndElementHandler(name)

参数含义如下

> name: 元素名

当XMLParser遇到XML处理指令时，将调用ProcessingInstructionHandler方法，其原型如下

> ProcessingInstructionHandler(target, data)

参数含义如下

> target: 指令名称
>
> name: 指令数据

当XMLParser遇到字符数据时，将调用CharacterDataHandler方法，原型如下

> CharacterDataHandler(data)

参数含义如下

> data: 字符数据

当XMLParser遇到XML文档中的注释时，将调用CommentHandler方法，原型如下

> CommentHandler(data)

参数含义如下

> data: 注释内容

当XMLParser遇到CDATA开始时，将调用StartCdataSectionHandler方法，当遇到CDATA结束时

将调用EndCdataSectionHandler方法。
