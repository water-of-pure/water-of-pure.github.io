+++
date = '2025-07-28T17:05:16.345815+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 栈'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**栈**

栈可以看做插入和删除在同一个位置上进行的表，一般是栈顶。栈的基本操作是进栈和出栈，栈可以看作是一个容器。

如下图，

![Image](https://cdn.xiaorongmao.com/up/102-1.png)

先入栈的在容器底部，后入栈的在容器顶部。在出栈的时候，后入栈的先出，而先入栈的后出，因此栈有一个特性叫做

后进先出

在Python中，仍然可以使用列表来存储堆栈数据。通过创建堆栈类，来实现对堆栈进行操作的方法。如，进栈PUSH

方法、出栈POP方法，编写检查栈是都为满栈，或者是否为空栈的方法等。

如下示例代码

```py
# _*_ coding: utf-8 -*-
# version 2.7.13
class TestStack:

    def __init__(self, size=20):
        self.stack = []
        self.size = size
        self.top = -1

    def setSize(self, size):
        self.size = size

    def push(self, element):
        if self.is_full():
            raise 'TestStack OverFlow'
        else:
            self.stack.append(element)
            self.top = self.top + 1

    def pop(self):
        if self.is_empty():
            raise 'TestStack Empty'
        else:
            element = self.stack[-1]
            self.top = self.top - 1
            del self.stack[-1]
            return element

    def Top(self):
        return self.top

    def empty(self):
        self.stack = []
        self.top = -1

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.size - 1:
            return True
        else:
            return False

if __name__ == '__main__':
    stack = TestStack()
    for i in range(10):
        stack.push(i)

    print('%d' % stack.Top())

    for i in range(10):
        print(stack.pop())

    stack.empty()
    for i in range(21):
        stack.push(i)  

```
