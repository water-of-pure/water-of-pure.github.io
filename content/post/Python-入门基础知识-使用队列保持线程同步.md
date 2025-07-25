+++
date = '2025-07-25T15:10:16.114820+08:00'
draft = false
title = 'Python 入门基础知识 - 使用队列保持线程同步'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用队列保持线程同步**

Python中的Queue对象也提供了对线程同步的支持。使用Queue对象可以实现多生产者和多消费者形成的先进先出的队列。

每个生产者将数据依次存入队列，而每个消费者则依次从队列中取出数据。

实例演示如下

```py
# _*_ coding: utf-8 _*_

import threading
import Queue

class Producer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global queue
        queue.put(self.getName())
        print('%s, put %s to queue' % (self.getName(), self.getName()))

class Consumer(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global queue
        print('%s, get %s from queue' % (self.getName(), self.getName()))

queue = Queue.Queue()
plist = []
clist = []

for i in range(10):
    p = Producer('Producer ' + str(i))
    plist.append(p)

for i in range(10):
    c = Consumer('Consumer ' + str(i))
    clist.append(c)

for i in plist:
    i.start()
    i.join()

for i in clist:
    i.start()
    i.join()

```

运行结果如下

```bash
Producer 0, put Producer 0 to queue
Producer 1, put Producer 1 to queue
Producer 2, put Producer 2 to queue
Producer 3, put Producer 3 to queue
Producer 4, put Producer 4 to queue
Producer 5, put Producer 5 to queue
Producer 6, put Producer 6 to queue
Producer 7, put Producer 7 to queue
Producer 8, put Producer 8 to queue
Producer 9, put Producer 9 to queue
Consumer 0, get Consumer 0 from queue
Consumer 1, get Consumer 1 from queue
Consumer 2, get Consumer 2 from queue
Consumer 3, get Consumer 3 from queue
Consumer 4, get Consumer 4 from queue
Consumer 5, get Consumer 5 from queue
Consumer 6, get Consumer 6 from queue
Consumer 7, get Consumer 7 from queue
Consumer 8, get Consumer 8 from queue
Consumer 9, get Consumer 9 from queue
```
