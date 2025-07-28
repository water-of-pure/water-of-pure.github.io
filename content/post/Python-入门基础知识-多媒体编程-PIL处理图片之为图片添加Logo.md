+++
date = '2025-07-28T17:48:31.024740+08:00'
draft = false
title = 'Python 入门基础知识 - 多媒体编程 - PIL处理图片之为图片添加Logo'
categories = [
    "技术",

]

tags = [
    "Python",
    "多媒体编程"
]
+++

**为图片添加Logo**

使用PIL为图片添加Logo，主要使用Image的paste函数。paste函数可以向图片中粘贴其他的图片。代码实例如下，使用PIL模块为图片批量添加Logo

```py
# _*_ coding: utf-8 -*-
# version 2.7.13
# osx

import os
from PIL import Image
import Tkinter
import tkFileDialog
import tkMessageBox

class Window:
    def __init__(self):
        self.root = root = Tkinter.Tk()
        self.Image = Tkinter.StringVar()
        self.status = Tkinter.StringVar()
        self.mstatus = Tkinter.IntVar()
        self.fstatus = Tkinter.IntVar()
        self.pstatus = Tkinter.IntVar()
        self.Image.set('bmp')
        self.mstatus.set(0)
        self.fstatus.set(0)
        self.pstatus.set(0)
        label = Tkinter.Label(root, text='Logo')
        label.place(x=5, y=5)
        self.entryLogo = Tkinter.Entry(root)
        self.entryLogo.place(x=55, y=5)

        self.buttonBrowserLogo = Tkinter.Button(
            root, text='浏览', command=self.BrowserLogo)
        self.buttonBrowserLogo.place(x=200, y=5)

        self.checkM = Tkinter.Checkbutton(root, text='批量转换',
                                          command=self.OnCheckM,
                                          variable=self.mstatus,
                                          onvalue=1,
                                          offvalue=0)
        self.checkM.place(x=5, y=30)
        label = Tkinter.Label(root, text='选择文件')
        label.place(x=5, y=55)
        self.entryFile = Tkinter.Entry(root)
        self.entryFile.place(x=55, y=55)
        self.buttonBrowserFile = Tkinter.Button(root, text='浏览',
                                                command=self.BrowserFile)
        self.buttonBrowserFile.place(x=200, y=55)
        label = Tkinter.Label(root, text='选择目录')
        label.place(x=5, y=80)
        self.entryDir = Tkinter.Entry(root, state=Tkinter.DISABLED)
        self.entryDir.place(x=55, y=80)
        self.buttonBrowserDir = Tkinter.Button(root, text='浏览',
                                               command=self.BrowserDir,
                                               state=Tkinter.DISABLED)
        self.buttonBrowserDir.place(x=200, y=80)
        self.checkF = Tkinter.Checkbutton(root, text='改变文件格式',
                                          command=self.OnCheckF,
                                          variable=self.fstatus,
                                          onvalue=1,
                                          offvalue=0)
        self.checkF.place(x=5, y=110)
        frame = Tkinter.Frame(root)
        frame.place(x=10, y=130)
        labelTo = Tkinter.Label(frame, text='格式')
        labelTo.pack(anchor='w')
        self.rBmp = Tkinter.Radiobutton(frame, variable=self.Image,
                                        value='bmp',
                                        text='BMP',
                                        state=Tkinter.DISABLED)
        self.rBmp.pack(anchor='w')
        self.rJpg = Tkinter.Radiobutton(frame, variable=self.Image,
                                        value='jpg',
                                        text='JPG',
                                        state=Tkinter.DISABLED)
        self.rJpg.pack(anchor='w')
        self.rGif = Tkinter.Radiobutton(frame, variable=self.Image,
                                        value='gif',
                                        text='GIF',
                                        state=Tkinter.DISABLED)
        self.rGif.pack(anchor='w')
        self.rPng = Tkinter.Radiobutton(frame, variable=self.Image,
                                        value='png',
                                        text='PNG',
                                        state=Tkinter.DISABLED)
        self.rPng.pack(anchor='w')

        pframe = Tkinter.Frame(root)
        pframe.place(x=70, y=130)

        labelPos = Tkinter.Label(pframe, text='位置')
        labelPos.pack(anchor='w')

        self.rLT = Tkinter.Radiobutton(
            pframe, variable=self.pstatus, value=0, text='左上角')
        self.rLT.pack(anchor='w')

        self.rRT = Tkinter.Radiobutton(
            pframe, variable=self.pstatus, value=1, text='右上角')
        self.rRT.pack(anchor='w')

        self.rLB = Tkinter.Radiobutton(
            pframe, variable=self.pstatus, value=2, text='左下角')
        self.rLB.pack(anchor='w')

        self.rRB = Tkinter.Radiobutton(
            pframe, variable=self.pstatus, value=3, text='左上角')
        self.rRB.pack(anchor='w')

        self.buttonAdd = Tkinter.Button(root, text='添加', command=self.Add)
        self.buttonAdd.place(x=180, y=175)

        self.labelStatus = Tkinter.Label(root, textvariable=self.status)
        self.labelStatus.place(x=150, y=205)

    def MainLoop(self):  # 进入消息循环
        self.root.minsize(250, 250)
        self.root.maxsize(250, 250)
        self.root.mainloop()

    def BrowserLogo(self):
        file = tkFileDialog.askopenfilename(title='Python Music Player', filetypes=[(
            'JPG', '*.jpg'), ('BMP', '*.bmp'), ('PNG', '*.png'), ('GIF', '*.gif')])
        if file:
            self.entryLogo.delete(0, Tkinter.END)
            self.entryLogo.insert(Tkinter.END, file)

    def BrowserDir(self):
        directory = tkFileDialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0, Tkinter.END)
            self.entryDir.insert(Tkinter.END, directory)

    def BrowserFile(self):
        file = tkFileDialog.askopenfilename(title='Python Music Player', filetypes=[(
            'JPG', '*.jpg'), ('BMP', '*.bmp'), ('PNG', '*.png'), ('GIF', '*.gif')])
        if file:
            self.entryFile.delete(0, Tkinter.END)
            self.entryFile.insert(Tkinter.END, file)

    def OnCheckM(self):  # 设置组件状态
        if not self.mstatus.get():
            self.entryDir.config(state=Tkinter.DISABLED)
            self.entryFile.config(state=Tkinter.NORMAL)
            self.buttonBrowserDir.config(state=Tkinter.DISABLED)
            self.buttonBrowserFile.config(state=Tkinter.NORMAL)
        else:
            self.entryDir.config(state=Tkinter.NORMAL)
            self.entryFile.config(state=Tkinter.DISABLED)
            self.buttonBrowserDir.config(state=Tkinter.NORMAL)
            self.buttonBrowserFile.config(state=Tkinter.DISABLED)

    def OnCheckF(self):  # 设置组件状态
        if not self.fstatus.get():
            self.rBmp.config(state=Tkinter.DISABLED)
            self.rJpg.config(state=Tkinter.DISABLED)
            self.rGif.config(state=Tkinter.DISABLED)
            self.rPng.config(state=Tkinter.DISABLED)
        else:
            self.rBmp.config(state=Tkinter.NORMAL)
            self.rJpg.config(state=Tkinter.NORMAL)
            self.rGif.config(state=Tkinter.NORMAL)
            self.rPng.config(state=Tkinter.NORMAL)

    def Add(self):
        n = 0
        if self.mstatus.get():
            path = self.entryDir.get()
            if path == '':
                tkMessageBox.showerror('Python Tkinter', '请输入路径')
                return

            filenames = os.listdir()
            if self.fstatus.get():
                f = self.Image.get()
                for filename in filenames:
                    if filename[-3:] in ('bmp', 'jpg', 'gif', 'png'):
                        self.addlogo(path + '/' + filename, f)
                    n = n + 1
            else:
                for filename in filenames:
                    if filename[-3:] in ('bmp', 'jpg', 'gif', 'png'):
                        self.addlogo(path + '/' + filename)
                    n = n + 1
        else:
            file = self.entryFile.get()
            if file == '':
                tkMessageBox.showerror('Python Tkinter', '请选择文件')
                return

            if self.fstatus.get():
                f = self.Image.get()
                self.addlogo(file, f)
                n = n + 1
            else:
                self.addlogo(file)
                n = n + 1

        self.status.set('成功添加%d图片' % n)

    def addlogo(self, file, format=None):
        logo = self.entryLogo.get()
        if logo == '':
            tkMessageBox.showerror('Python Tkinter', '请选择logo')

        im = Image.open(file)
        lo = Image.open(logo)
        imwidth, imheight = im.size
        lowidth, loheight = lo.size

        pos = self.pstatus.get()
        if pos == 0:
            left = 0
            top = 0
            right = lowidth
            bottom = loheight
        elif pos == 1:
            left = imwidth - lowidth
            top = 0
            right = imwidth
            bottom = loheight
        elif pos == 2:
            left = 0
            top = imheight - loheight
            right = lowidth
            bottom = imheight
        else:
            left = imwidth - lowidth
            top = imheight - loheight
            right = imwidth
            bottom = imheight

        im.paste(lo, (left, top, right, bottom))
        if format:
            im.save(file[:len(file)-4] + '_logo.' + format)
        else:
            im.save(file[:len(file)-4] + '_logo' + file[-4:])

window = Window()
window.MainLoop()  

```

运行后效果如下

![Image](https://cdn.xiaorongmao.com/up/121-1.png)
