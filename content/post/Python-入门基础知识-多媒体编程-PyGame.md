+++
date = '2025-07-28T17:06:30.941784+08:00'
draft = false
title = 'Python 入门基础知识 - 多媒体编程 - PyGame'
categories = [
    "技术",

]

tags = [
    "Python",
    "PyGame"
]
+++

**PyGame**

PyGame是用来编写游戏的Python模块。PyGame是基于SDL的，SDL(Simple DirectMedia Layer)是一个跨平台的多媒体开发包，SDL专门为游戏h额多媒体设计。使用PyGame可以创建使用SDL库创建的游戏和多媒体程序。

**如何安装PyGame**

具体的安装细节，读者可以到这里查找<https://www.pygame.org/wiki/GettingStarted#Pygame> Installation

我这里使用的是mac，我就介绍下在mac下的安装过程

执行如下命令

```bash
pip install pygame
```

如果出现如下类似内容

```bash
Installing collected packages: pygame
Successfully installed pygame-1.9.3
```

说明就是安装成功了

**PyGame简单的使用介绍**

下面演示实例，简单的创建一个游戏窗口

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13

import pygame
import sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True:  # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()  

```

运行结果如下

![Image](https://cdn.xiaorongmao.com/up/118-1.png)
