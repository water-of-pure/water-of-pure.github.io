+++
date = '2025-07-25T15:54:44.658599+08:00'
draft = false
title = 'Python 入门基础知识 - 使用微线程'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用微线程**

使用Stackless Python的内置模块stackless可以完成多线程编程，使用起来更加方便。

实力代码如下

```py
# _*_ coding: utf-8 -*-
import stackless
import Queue

def Producer(i):
    global queue
    queue.put(i)
    print('Producer %s add %s' % (i, i))

def Consumer(i):
    global queue
    i = queue.get()
    print('Consumer %s add %s' % (i, i))

queue = Queue.Queue()

for i in range(10):
    stackless.tasklet(Producer)(i)

for i in range(10):
    stackless.tasklet(Consumer)(i)

stackless.run()
```

运行脚本后输出结果如下所示

```bash
Producer 0 add 0
Producer 1 add 1
Producer 2 add 2
Producer 3 add 3
Producer 4 add 4
Producer 5 add 5
Producer 6 add 6
Producer 7 add 7
Producer 8 add 8
Producer 9 add 9
Consumer 0 add 0
Consumer 1 add 1
Consumer 2 add 2
Consumer 3 add 3
Consumer 4 add 4
Consumer 5 add 5
Consumer 6 add 6
Consumer 7 add 7
Consumer 8 add 8
Consumer 9 add 9
```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13

```
