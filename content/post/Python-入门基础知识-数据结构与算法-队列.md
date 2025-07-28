+++
date = '2025-07-28T17:05:32.556151+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 队列'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**队列**

队列和栈类似 

但不同的是，队列的出队操作是队首元素进行的删除操作，因而对于队列而言，先入队的元素将先出队。因此队

的特性可以称为先进先出（FIFO）。

和堆栈类似，在Python中同样可以使用列表来构建一个队列，并完成对队列的操作。如下实例

```py
# _*_ coding: utf-8 -*-
# version 2.7.13
class TestQueue:

    def __init__(self, size=20):  # 创建队列
        self.queue = []  # 队列
        self.size = size  # 队列大小
        self.end = -1  # 队列尾

    def setSize(self, size):  # 设置队列大小
        self.size = size

    def In(self, element):  # 入队
        if self.end < self.size - 1:
            self.queue.append(element)
            self.end = self.end + 1
        else:
            raise 'TestQueue Full'  # 如果队列满，则引发异常

    def Out(self):  # 出队
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end - 1
            return element
        else:
            raise 'TestQueue Empty'

    def End(self):
        return self.end

    def Empty(self):  # 清空队列
        self.queue = []
        self.end = -1

if __name__ == '__main__':
    queue = TestQueue()
    for i in range(10):
        queue.In(i)

    print(queue.End())

    for i in range(10):
        print(queue.Out())

    for i in range(20):
        queue.In(i)

    print(queue.Empty())

    for i in range(20):
        print(queue.Out())  

```

运行结果如下

```bash
9
0
1
2
3
4
5
6
7
8
9
None
Traceback (most recent call last):
  File "base_phrase.py", line 64, in <module>
    print(queue.Out())
  File "base_phrase.py", line 38, in Out
    raise 'TestQueue Empty'
TypeError: exceptions must be old-style classes or derived from BaseException, not str
```
