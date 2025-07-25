+++
date = '2025-07-25T15:10:19.686368+08:00'
draft = false
title = 'Python 入门基础知识 - 线程间通信'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**线程间通信**

Python提供了Event对象用于线程间的相互通信。实际上线程同步在一定程度上已经实现线程间的通信。线程同步是每次仅有一个线程

对共享数据进行操作，其他线程则等待。而Event对象是由线程设置的信号标志，如果信号标志为真，则其他线程等待直到信号解除。

**Event对象的方法**

Event对象实现了简单的线程通信机制，它提供了设置信号、清除信号、等待等用于实现线程间的通信。

*1.设置信号*

使用Event对象的set()方法可以设置Event对象内部的信号标志为真。Event对象提供了isSet()方法来判断其内部信号标志的状态。

当使用Event对象的set()方法后，isSet()方法返回真。

*2.清除信号*

使用Event对象的clear()方法可以清除Event对象内部的信号标志，即将其设置为假。当使用Event对象的clear()方法后，isSet()方法

返回假。

*3.等待*

Event对象wait的wait方法只有在其内部信号为真时才会很快的执行完成并返回。当Event对象的内部信号标志为假时，则wait方法一直

等到为真时才返回。另外还可以向wait方法传递参数，以设定最长等待时间。

使用Event对象实现线程间通信

配合使用Event对象的几种方法可以实现进程间的简单通信。

实例演示如下

```py
# _*_ coding: utf-8 _*_
import threading

class TestThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global event  # 使用全局Event对象
        if event.isSet():  # 判断Event对象内部信号标志
            event.clear()  # 若已设置标志则清除
            event.wait()  # 调用wait方法
            print(self.getName())
        else:
            print(self.getName())
            event.set()  # 设置Event对象内部信号标志

event = threading.Event()  # 生成Event对象
event.set()  # 设置Event对象内部信号标志

t1 = []
for i in range(10):
    t = TestThread('线程：' + str(i))
    t1.append(t)

for i in t1:
    i.start()

```

运行脚本后结果输出如下，每次运行后结果会不一样

```bash
线程：1
线程：2
线程：0
线程：4
线程：5
线程：3
线程：8
线程：7
线程：6
线程：9
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
