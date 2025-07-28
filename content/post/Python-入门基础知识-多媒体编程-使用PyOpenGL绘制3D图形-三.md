+++
date = '2025-07-28T17:06:20.504032+08:00'
draft = false
title = 'Python 入门基础知识 - 多媒体编程 - 使用PyOpenGL绘制3D图形(三)'
categories = [
    "技术",

]

tags = [
    "Python",
    "PyOpenGL"
]
+++

绘制2D图形

在PyOpenGL中绘制图形时应以glBegin函数开始，当绘制完成后应调用glEnd函数。glBegin函数原型如下所示。

glBegin(mode)

参数含义如下

mode: 绘制的图形

其中可以选择的图形有以下几种。

GL\_POINTS: 绘制点

GL\_LINES: 绘制直线

GL\_LINES\_STRIP: 绘制连续直线，不封闭

GL\_LINE\_LOOP: 绘制连续直线，封闭

GL\_TRIANGLES: 绘制三角形

GL\_TRIANGLES\_STRIP: 绘制三角形串

GL\_TRIANGLES\_FAN: 绘制三角扇形

GL\_QUADS: 绘制四边形

GL\_QUADS\_STRIP: 绘制四边形串

GL\_POLYGON: 绘制多边形

由于在PyOpenGL中没有提供直接绘制圆形的函数，因此可以使用多边形来模拟绘制圆形，如下代码演示绘制了几种简单的2D图形

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math

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
        # 调用OpenGL初始化函数
        self.InitGL(width, height)

    # 绘制场景
    def Draw(self):
        # 清除屏幕和深度缓存
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # 重置观察矩阵
        glLoadIdentity()
        # 移动位置
        glTranslatef(-2.0, 2.0, -6.0)
        # 绘制直线
        glBegin(GL_LINES)
        # 直线第一点坐标
        glVertex3f(0.0, 0.0, 0.0)
        # 直线第二点坐标
        glVertex3f(2.0, 0.0, 0.0)
        # 结束绘制
        glEnd()
        # 移动位置
        glTranslatef(3.0, 0.0, 0.0)
        # 通过绘制多边形来模拟圆形
        glBegin(GL_POLYGON)
        i = 0
        while(i <= 3.14 * 2):
            x = 0.5 * math.cos(i)
            y = 0.5 * math.sin(i)
            glVertex3f(x, y, 0.0)
            i = i + 0.01

        glEnd()
        # 移动位置
        glTranslatef(-2.0, -3.0, 0.0)
        # 绘制三角形
        glBegin(GL_POLYGON)
        glVertex3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glEnd()

        # 移动位置
        glTranslatef(2.5, 0.0, 0.0)
        # 绘制四边形
        glBegin(GL_QUADS)
        glVertex3f(-1.0, 1.0, 0.0)
        glVertex3f(1.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)
        glEnd()
        # 交换缓存
        glutSwapBuffers()

    # 绘制文字函数
    def DrawText(self, string):
        # 循环处理字符串
        for c in string:
            # 输出文字
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(c))

    # OpenGL初始化函数
    def InitGL(self, width, height):
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

    def MainLoop(self):
        # 进入消息循环
        glutMainLoop()

# 创建窗口
window = OpenGLWindow()
# 进入消息循环
window.MainLoop()  

```


