+++
date = '2025-07-28T17:06:27.522972+08:00'
draft = false
title = 'Python 入门基础知识 - 多媒体编程 - 使用PyOpenGL绘制3D图形(五)'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**纹理映射**

在PyOpenGL中处理纹理贴图需要使用PIL模块，在下篇文章中讲解PIL模块详细的使用方法。实例代码如下，绘制了一个立方体，并对每一个面进行贴图，在代码中使用glutIdleFunc函数，设置了空闲时的场景绘制函数，创建了立方体旋转dd额动画。

```py

# _*_ coding: utf-8 -*-
# version 2.7.13

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from PIL import Image

class OpenGLWindow:
    # 初始化

    def __init__(self, width=640, height=480, title='PyOpenGL'):
        # 传递命令行参数
        glutInit(sys.argv)
        # 设置显示模式
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        # 设置窗口大小
        glutInitWindowSize(width, height)
        # 创建窗口
        self.window = glutCreateWindow(title)
        # 设置场景绘制函数
        glutDisplayFunc(self.Draw)
        # 设置空闲时场景绘制函数
        glutIdleFunc(self.Draw)
        # 调用OpenGL初始化函数
        self.InitGL(width, height)
        self.x = 0.2
        self.y = 0.2
        self.z = 0.2
    # 绘制场景

    def Draw(self):
        # 清除屏幕和深度缓存
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # 重置观察矩阵
        glLoadIdentity()
        # 移动位置
        glTranslatef(0.0, 0.0, -5.0)
        # 绕x轴旋转
        glRotate(self.x, 1.0, 0.0, 0.0)
        # 绕y轴旋转
        glRotate(self.y, 0.0, 1.0, 0.0)
        # 绕z轴旋转
        glRotate(self.z, 0.0, 0.0, 1.0)
        # 绘制立方体
        glBegin(GL_QUADS)
        # 对前面进行贴图
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, 1.0, 1.0)
        # 对后面进行贴图
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        # 对顶面进行贴图
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        # 对底面进行贴图
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        # 对右侧面进行贴图
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        # 对左侧面进行贴图
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        # 结束绘制
        glEnd()
        # 交换缓存
        glutSwapBuffers()
        # 旋转角度增加
        self.x = self.x + 0.2
        self.y = self.y + 0.2
        self.z = self.z + 0.2

    # OpenGL初始化函数
    def InitGL(self, width, height):
        # 载入纹理
        self.LoadTextures()
        # 允许纹理映射
        glEnable(GL_TEXTURE_2D)

        # 设置为黑色背景
        glClearColor(0.0, 0.0, 0.0, 0.0)
        # 设置深度缓存
        glClearDepth(1.0)
        # 设置深度测试类型
        glDepthFunc(GL_LESS)
        # 允许深度测试
        glEnable(GL_DEPTH_TEST)
        # 启动平滑阴影
        glShadeModel(GL_SMOOTH)
        # 设置观察矩阵
        glMatrixMode(GL_PROJECTION)
        # 重置观察矩阵
        glLoadIdentity()
        # 设置屏幕宽高比
        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)
        # 设置观察矩阵
        glMatrixMode(GL_MODELVIEW)

    def LoadTextures(self):  # 载入纹理图片
        # 打开图片
        image = Image.open('jonatan-pie-226805.jpg')
        # 图像宽度
        width = image.size[0]
        # 图像高度
        height = image.size[0]
        # 转换图像
        image = image.tobytes('raw', 'RGBX', 0, -1)
        # 创建纹理
        glBindTexture(GL_TEXTURE_2D, glGenTextures(1))
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)

        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    def MainLoop(self):
        # 进入消息循环
        glutMainLoop()

# 创建窗口
window = OpenGLWindow()
# 进入消息循环
window.MainLoop()

```

运行结果如下

![Image](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560389330/walkerfree/117-1.png)
