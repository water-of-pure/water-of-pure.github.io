+++
date = '2025-07-28T17:06:24.609245+08:00'
draft = false
title = 'Python 入门基础知识 - 多媒体编程 - 使用PyOpenGL绘制3D图形(四)'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

绘制3D图形

在PyOpenGL中绘制3D图形时和绘制2D图形类似，通过设置Z坐标，可以设置图形所在的空间位置。代码实例演示如下，绘制了一个立方体

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

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
        glTranslatef(1.5, 0.0, -7.0)
        # 绕x、y、z轴旋转45度
        glRotate(45, 1.0, 1.0, 1.0)
        # 绘制立方体
        glBegin(GL_QUADS)
        # 设置颜色为红色
        glColor3f(1.0, 0.0, 0.0)
        # 绘制立体的顶面
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        # 设置颜色为绿色
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(1.0, -1.0, -1.0)
        # 设置颜色为蓝色
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)

        # 设置颜色为红色
        glColor3f(1.0, 0.0, 0.0)
        # 绘制立体的顶面
        glVertex3f(1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, -1.0)
        # 设置颜色为绿色
        glColor3f(0.0, 1.0, 0.0)
        glVertex3f(-1.0, 1.0, 1.0)
        glVertex3f(-1.0, 1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        # 设置颜色为蓝色
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(1.0, 1.0, -1.0)
        glVertex3f(1.0, 1.0, 1.0)
        glVertex3f(1.0, -1.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)

        # 结束绘制
        glEnd()
        # 交换缓存
        glutSwapBuffers()

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


