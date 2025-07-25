+++
date = '2025-07-25T15:10:09.618914+08:00'
draft = false
title = 'Python 入门基础知识 - 线程同步'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**线程同步**

如果多个线程共同对某个数据修改，则可能会出现不可预料的结果。为了保证数据被正确修改，需要对多个线程进行同步。

**简单的线程同步**

使用Thead对象的Lock和RLock可以实现简单的线程同步。Lock对象和RLock对象都具有acquire方法和release方法。对于如果

需要每次只有一个线程操作的 数据，可以将操作过程放在acquire方法和release方法之间。

实例演示如下

```py
# _*_ coding: utf-8 -*-
# version 2.7.13
#
import threading  # 导入threading模块
import time  # 导入time模块

class TestThread(threading.Thread):  # 通过继承创建类

    def __init__(self, thread_name):  # 初始化方法
        threading.Thread.__init__(self, name=thread_name)  # 调用父类的初始化方法

    def run(self):  # 重载run方法
        global x  # 使用global表明x为全局变量
        lock.acquire()  # 调用lock的acquire方法
        for i in range(3):
            x = x + 1

        time.sleep(5)  # 让线程休眠5秒
        print(x)
        lock.release()  # 调用lock的release方法

lock = threading.RLock()  # 生成RLock对象
t1 = []  # 定义列表
for i in range(10):
    t = TestThread('线程 %s' % str(i))  # 类实例化
    t1.append(t)  # 将类对象添加到列表中

x = 0
for i in t1:
    i.start()  

```

执行后输出结果如下

```bash
3
6
9
12
15
18
21
24
27
30
```

将上面脚本中的"lock.acquire()"、"lock.release()"和"threading.RLock()"删除后运行脚本。得到如下结果

```bash
30
30
30
30
30
30
30
30
30
30
```

修改后的脚本输出都是30也就是x的终值。由于x是全局变量，在每个线程对x进行操作后就"休眠"了。在线程休眠的时候，Python

解释器已经执行了其他的线程，而使x值增加。当所有线程"休眠"结束后，i的值已被所有线程修改变成了30，因此输出30。

而在使用Lock对象的脚本中，对全局变量x的操作放在acquire方法和release方法之间。Python解释器每次仅允许一个线程对x

进行操作。只有当该线程操作完成后，并且结束休眠以后才开始下一个线程，所以使用Lock对象的脚本输出是依次递增的。

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13
```
