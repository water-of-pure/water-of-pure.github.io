+++
date = '2025-07-25T15:10:12.806515+08:00'
draft = false
title = 'Python 入门基础知识 -使用条件变量保持线程同步'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用条件变量保持线程同步**

Python的Condition对象提供了对复杂线程同步的支持。使用Condition对象可以在某些事件触发后才处理数据。

Condition对象除了具有acquire方法和release方法以外，还有wait方法、notify方法、notifyAll方法等用于

条件处理。

实例代码演示如下

```py
# _*_ coding: utf-8 _*_
import threading

class Producer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global x
        con.acquire()
        if x == 100000:
            con.wait()
            pass
        else:
            for i in range(100000):
                x = x + 1
            con.notify()
        print(x)
        con.release()

class Consumer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global x
        con.acquire()
        if x == 0:
            con.wait()
            pass
        else:
            for i in range(100000):
                x = x - 1
            con.notify()
        print(x)
        con.release()

con = threading.Condition()
x = 0
p = Producer('Producer')
c = Consumer('Consumer')
p.start()
p.join()
c.start()
c.join()  

```

运行后输出结果如下

```bash
100000
0
```
