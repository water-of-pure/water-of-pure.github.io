+++
date = '2025-07-28T17:06:49.917432+08:00'
draft = false
title = 'Python 入门基础知识 - 使用PIL处理图片'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用PIL处理图片**

PIL(Python Imaging Library)为Python提供了强大的图形处理能力，并支持多种图形文件格式。通过使用PIL模块，可以使用Python对图片进行处理。

**PIL的安装**

PIL是跨平台的，在Mac下可以使用PIL的强大功能。由于PIL不是Python自带的模块，因此需要用户自己安装。

执行下面的命令

```bash
pip install pillow
```

出现类型如下内容

```bash
Installing collected packages: pillow
Successfully installed pillow-5.0.0
```

代表已经安装成功

**PIL简介**

在PIL中提供了以下主要模块对图片进行处理

> Image: PIL的主要模块
>
> ImageChops: 图片计算模块
>
> ImageColor: 颜色模块
>
> ImageDraw: 绘图模块
>
> ImageEnchace: 图片效果模块
>
> ImageFile: 图片文件存取模块
>
> ImageFileIO: 图片流模块
>
> ImageFilter: 图片过滤模块
>
> ImageFont: 字形模块，用于绘图
>
> ImageGrab: 图片抓取模块
>
> ImageOps: 图片处理模块
>
> ImagePath: 路径队列模块
>
> ImagePalette: 图片调色板模块
>
> ImageSequence: 队列包装模块
>
> ImageStat: 图片属性模块
>
> ImageTk: 提供对Tkinter模块
>
> ImageWin: 提供对Windows的支持
>
> PSDraw: 提供对PostScript的支持

对于简单的图片处理一般仅需要使用Image模块，此处仅对Image模块中的主要函数进行简要的介绍，其他模块中的函数可以参考PIL的帮助文档。

1、打开图片

Image模块中主要的函数时open函数，其用于打开图片。函数原型如下

> open(file, mode)

参数含义如下

> fiile: 要打开的图片文件
>
> model: 可选参数，打开文件的方式

2、复制图片

open函数执行成功后返回一个Image对象，使用Imagem模块的copy方法可以复制图片，使用crop方法可以复制图片中的某一个区域，函数原型如下

> crop(box)

参数含义如下

> box: 一个由4个元素组成的元组，分别表示图片的左、上、右、下的位置。

3、粘贴图片

使用Image对象的paste方法可以向图片中粘贴图片、图像，paste方法有以下几种形式。

> paste(image, box)
>
> paste(color, box)
>
> paste(image, box)
>
> paste(image, box, mask)
>
> paste(color, box, mask)

参数含义如下

> image: 被粘贴到图片中的图片对象
>
> box: 所要粘贴的区域，同crop中的参数box
>
> color: 填充的颜色
>
> mask: 指定填充颜色透明度

4、调整图片大小

使用Image对象的resize方法可以重新调整图片的大小。函数原型如下

> resize(size, filter)

参数含义如下

> size: 图片调整后的大小，为由宽和高组成的元组
>
> filter: 可选参数，可以是NEAREST、BILINEAR、BICUBIC或者ANTIALIAS

5、旋转图片

使用Imaged对象的rotate方法可以选装图片。函数原型如下

> rotate(angle, filter, expand)

参数含义如下

> angle: 旋转的角度
>
> filter: 可选参数，同resize中的filter参数
>
> expand: 可选参数，如果为真，则增大图片，以容纳旋转后的图片，否则保持图片尺寸。

6、显示图片

使用Image对象的show方法可以显示图片。使用Image对象的save方法可以保存图像，函数原型如下

> save(outfile, format, options)

参数含义如下

> outfile: 所保存的文件名
>
> format: 可选参数，保存的文件格式。如果不给出，将根据保存的文件名的扩展名进行存储。
>
> options: 其他的操作参数

另外，Image对象还有size属性，其有宽和高组成的元组。Image对象的format属性为图片的格式。Image对象的mode属性为图片的模式。
