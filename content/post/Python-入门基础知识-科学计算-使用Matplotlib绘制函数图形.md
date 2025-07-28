+++
date = '2025-07-28T17:06:09.601047+08:00'
draft = false
title = 'Python 入门基础知识 - 科学计算 - 使用Matplotlib绘制函数图形'
categories = [
    "技术",

]

tags = [
    "Python",
    "Matplotlib"
]
+++

**使用Matplotlib绘制函数图形**

Matplotlib是绘制2D图形的Python的一种模块，它依赖于NumPy和Tkinter。Matplotlib中大部分函数都和MATLAB中的函数名相同，熟悉MATLAB的学者可以很快地掌握Matplotlib。Matplotlib可以绘制多种形式的图形包括普通的线图、直方图、饼图、散点图以及误差线图等。

**1、安装Matplotlib**

执行如下命令【unix linux系统】

```bash
pip install matplotlib
```

**2、使用Matplotlib绘制图形**

使用Matplotlib绘制图形主要使用其plot函数，plot函数和MATLAB中的plot函数用法相同。Matplotlib还包含了一些用于设置x、y轴标签文本以及图形标题的函数，如下所示

> xlabel 设置x轴标签
>
> ylabel 设置y轴标签
>
> title 设置绘图标题
>
> text 在指定坐标处输出文字
>
> figtext 在绘制的图形上添加文字

另外，Matplotlib还支持一部分Text排版命令，可以较好的显示数学公式。如下代码所示，在Python交互式命令行中使用Matplotlib绘制图形。

绘制正弦曲线

```bash
>>> import matplotlib.pyplot as plt
>>> from pylab import *
>>> t = arange(0.0, 2.0, 0.05)
>>> s = sin(2*pi*t)
>>> plot(t, s)
[<matplotlib.lines.Line2D object at 0x10b0abd10>]
>>> plt.show()
```


绘制余弦图形

```bash
>>> import matplotlib.pyplot as plt
>>> from pylab import *
>>> figure(2)
<matplotlib.figure.Figure object at 0x10de7f350>
>>> t = arange(0.0, 2.0, 0.05)
>>> s = cos(2*pi*t)
>>> plot(t, s)
[<matplotlib.lines.Line2D object at 0x111050d10>]
>>> plt.show()
```


同时绘制正弦曲线和余弦曲线

```bash
>>> import matplotlib.pyplot as plt
>>> from pylab import *
>>> t = arange(0.0, 2.0, 0.05)
>>> s = cos(2*pi*t)
>>> plot(t, s, linestyle='-', marker='o')
[<matplotlib.lines.Line2D object at 0x108fc4a50>]
>>> s = sin(2*pi*t)
>>> plot(t, s, linestyle='-', marker='+')
[<matplotlib.lines.Line2D object at 0x108fc4890>]
>>> xlabel('X')
<matplotlib.text.Text object at 0x109eba150>
>>> ylabel('Y')
<matplotlib.text.Text object at 0x109eae110>
>>> title('sin(x) and sin(y)')
<matplotlib.text.Text object at 0x108fa9bd0>
>>> plt.show()
```


绘制函数y = 10 / (1 + x \*\* 2)

```bash
>>> import matplotlib.pyplot as plt
>>> from pylab import *
>>> x = arange(-5, 5, 0.1)
>>> y = 10 / (1 + x ** 2)
>>> plot(x, y)
[<matplotlib.lines.Line2D object at 0x11191f590>]
>>> xlabel('X')
<matplotlib.text.Text object at 0x112648490>
>>> ylabel('Y')
<matplotlib.text.Text object at 0x112693090>
>>> plt.show()
```


实例演示环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
