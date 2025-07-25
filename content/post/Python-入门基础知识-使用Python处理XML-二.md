+++
date = '2025-07-25T15:55:42.396611+08:00'
draft = false
title = 'Python 入门基础知识 - 使用Python处理XML（二）'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用xml.sax处理XML的简介**

与xml.parsers.expat模块不同，xml.sax模块将分析器和处理器分离了。使用

xml.sax模块时，可以使用make\_parser函数创建分析器，它返回一个XMLParser

对象。然后使用XMLReader对象的setContentHandler设置XMLReader对象的

ContentHandler。在脚本中通过继承ContentHandler类，重载相应的处理方法，

即可对XML文档进行处理。如果需要对DTD进行处理，可以使用XMLReader对象的

setDTDHandler方法。使用setDTDHandler方法设置XMLReader对象的DTDHandler

句柄。

xml.sax的分析器在分析XML文档时，在XML文档开始时将调用ContentHandler的startDocument方法，在XML文档结束时将调用ContentHandler的endHandler方法。其函数原型分别如下

> startElement(name, attrs)
>
> endElement(name)

参数含义如下

> name: 元素名
>
> attrs: 元素属性

如果在XML文档中使用了命名空间，将调用startElementNS方法和endElementNS方法。原型分别如下

> startElementNS(name, qname, attrs)
>
> endElementNS(name, qname)

参数含义如下

> name: 由URI和本地名组成的元组
>
> qname: 元素名
>
> attrs: 元素属性

当xml.sax的分析器遇到字符数据时，将调用ContentHandler的characters方法。原型如下

> characters(content)

参数含义如下

> content: 字符数据内容

当xml.sax的分析器遇到XML处理指令时，将调用ContentHandler的processingInstruction方法。原型如下

> processingInstruction(target, data)

参数含义如下

> target: 指令名称
>
> data: 指令数据

当xml.sax的分析器处理DTD时，将调用DTDHandler中的方法。在DTDHandler中主要提供了用于处理声明的notationDecl方法和用于处理分析实体声明unparsedEntityDecl方法。原型如下

> notationDecl(name, publicId, systemId)
>
> upparsedEntityDecl(name, publicId, systemId, ndata)
