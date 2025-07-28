+++
date = '2025-07-28T17:39:02.283435+08:00'
draft = false
title = 'Python 入门基础知识 - 多媒体编程 - PIL处理图片之转换图片格式'
categories = [
    "技术",

]

tags = [
    "Python",
    "多媒体编程"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

转换图片格式

使用PIL转换图片格式，主要是使用PIL的Image模块。首先使用Image.open函数打开文件，然后将文件保存成所需要的格式即可。Image可以根据文件的扩展名自动选择文件保存的格式，因此不需要设置文件格式。如下所示的代码演示，使用Image模块进行批量图片文件格式转换。

```py

# _*_ coding: utf-8 -*-
# version 2.7.13

import os
from PIL import Image
import Tkinter
import tkFileDialog
import tkMessageBox

class Window:

    def __init__(self):
        self.root = root = Tkinter.Tk()
        label = Tkinter.Label(root, text='选择目录')
        label.place(x=5, y=5)
        self.entry = Tkinter.Entry(root)
        self.entry.place(x=55, y=5)
        self.buttonBrowser = Tkinter.Button(
            root, text='浏览', command=self.Browser)
        self.buttonBrowser.place(x=200, y=5)
        frameF = Tkinter.Frame(root)
        frameF.place(x=5, y=30)
        frameT = Tkinter.Frame(root)
        frameT.place(x=100, y=30)
        self.fImage = Tkinter.StringVar()
        self.tImage = Tkinter.StringVar()
        self.status = Tkinter.StringVar()
        self.fImage.set('.bmp')
        self.tImage.set('.bmp')
        labelFrom = Tkinter.Label(frameF, text='From')
        labelFrom.pack(anchor='w')
        labelTo = Tkinter.Label(frameT, text='To')
        labelTo.pack(anchor='w')
        frBmp = Tkinter.Radiobutton(
            frameF, variable=self.fImage, value='.bmp', text='BMP')
        frBmp.pack(anchor='w')

        frJpg = Tkinter.Radiobutton(
            frameF, variable=self.fImage, value='.jpg', text='JPG')
        frJpg.pack(anchor='w')

        frGif = Tkinter.Radiobutton(
            frameF, variable=self.fImage, value='.gif', text='GIF')
        frGif.pack(anchor='w')

        frPng = Tkinter.Radiobutton(
            frameF, variable=self.fImage, value='.png', text='PNG')
        frPng.pack(anchor='w')

        trBmp = Tkinter.Radiobutton(
            frameT, variable=self.tImage, value='.bmp', text='BMP')
        trBmp.pack(anchor='w')

        trJpg = Tkinter.Radiobutton(
            frameT, variable=self.tImage, value='.jpg', text='JPG')
        trJpg.pack(anchor='w')

        trGif = Tkinter.Radiobutton(
            frameT, variable=self.tImage, value='.gif', text='GIF')
        trGif.pack(anchor='w')

        trPng = Tkinter.Radiobutton(
            frameT, variable=self.tImage, value='.png', text='PNG')
        trPng.pack(anchor='w')

        self.buttonConv = Tkinter.Button(root, text='转换', command=self.Conv)
        self.buttonConv.place(x=100, y=150)
        self.labelStatus = Tkinter.Label(root, textvariable=self.status)
        self.labelStatus.place(x=50, y=175)

    def MainLoop(self):
        self.root.minsize(250, 200)
        self.root.maxsize(250, 200)
        self.root.mainloop()

    def Browser(self):
        directory = tkFileDialog.askdirectory(title='Python')
        if directory:
            self.entry.delete(0, Tkinter.END)
            self.entry.insert(Tkinter.END, directory)

    def Conv(self):
        n = 0
        t = self.tImage.get()
        f = self.fImage.get()
        path = self.entry.get()
        if path == '':
            tkMessageBox.showerror('Python Tkinter', '请输入路径')
            return

        filenames = os.listdir(path)
        os.mkdir(path + '/' + t[-3:])
        for filename in filenames:
            if filename[-4:] == f:
                Image.open(path + '/' + filename)\
                    .save(path + '/' + t[-3:] + '/' + filename[:-4] + t)
                n = n + 1

        self.status.set('成功转换%d张图片' % n)

window = Window()
window.MainLoop()

```

运行效果如下

![Image](https://cdn.xiaorongmao.com/up/119-1.png)
