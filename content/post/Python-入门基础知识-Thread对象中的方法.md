+++
date = '2025-07-25T15:10:06.484582+08:00'
draft = false
title = 'Python 入门基础知识 - Thread对象中的方法'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**Thread对象中的方法**

在上一篇文章中，仅使用了Thread对象中的start方法，重载了Thread对象的run方法。当线程被运行时，将运行run方法。

Thread对象具有以下的几种方法。

**1、join方法**

如果一个线程或者在函数的执行过程中调用另一个线程，并且待其完成操作后才能执行，那么在调用线程时可以使用被调用线程的join方法。

方法的原型如下

> join([timeout])

其参数函数如下。

> timeout: 可选参数，线程运行的最长时间。

实例演示如下

```py
import threading  # 导入threading模块
import time  # 导入time模块
class TestThread(threading.Thread):  # 通过继承Thread创建类
    def __init__(self, id):  # 初始化方法
        threading.Thread.__init__(self)  # 调用父类的初始化方法
        self.id = id
    def run(self):  # 重载run方法
        time.sleep(10)  # 使用time模块中的sleep方法让线程休眠10秒
        print('线程ID: %s' % self.id)
def testFunc():  # 定义线程
    t1.start()  # 运行线程
    for i in range(5):
        print(i)
t1 = TestThread(2)  # 生成TestThread对象
testFunc()  # 调用函数，运行线程
```

运行结果如下

```bash
0
1
2
3
4
线程ID: 2
```

从上面的结果看出，testFunc直接运行了，并没有等待线程完成

```py
def secondTestFunc():
    t2.start()
    t2.join()
    for i in range(5):
        print(i)
t2 = TestThread(3)
secondTestFunc()
```

运行结果如下

```bash
线程ID: 3
0
1
2
3
4
```

从上面的结果看出，secondTestFunc等待线程完成后，在执行

**2、isAlive方法**

当线程创建后，可以使用Thread对象的isAlive方法查看线程是否运行。

实例演示如下

```py
import threading
import time
class TestThread2(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        time.sleep(5)
        print('当前线程ID: %s' % self.id)
t3 = TestThread2(4)
def thirdTestFunc():
    t3.start()  # 运行线程
    print(t3.isAlive())  # 打印线程状态
thirdTestFunc()  # 调用函数
```

运行结果如下

```bash
True # 线程状态
当前线程ID: 4 # 线程输出
```

**3、线程名**

当线程创建后可以设置线程名来区分不同的线程，以便对线程进行控制。线程名可以在类的初始化函数中定义，也可以使用Thread

对象setName方法设置线程名。使用Thread对象的getName方法可以获得线程名。

实例演示如下

```py
import threading
class TestThread3(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self, name=threadName)
    def run(self):
        print(self.getName())
t1 = TestThread3('t1')
print(t1.getName())
```

运行后输出结果如下

```bash
t1
```

```py
t1.setName('T1')
print(t1.getName())
```

运行后输出结果如下

```bash
T1
```

```py
t2 = TestThread3('t2')
t2.start()
print(t2.getName())
t2.setName('T2')
print(t2.getName())
```

运行后输出如下

```bash
t2
t2
T2
```

**4、setDaemon方法**

在脚本运行过程中有一个线程，如果主线程又创建一个子线程，那么当主线程退出时，会检验子线程是否完成。如果子线程未完成，则

主线程会等待子线程完成后再退出。当需要主线程退出时，不管子线程是否完成都随主线程退出，则可以使用Thead对象的setDaemon

方法来设置。

代码示例如下

```py
# _*_ coding: utf-8 -*-
# version 2.7.13
import threading
import time

class TestThread(threading.Thread):

    def __init__(self, thread_name):
        threading.Thread.__init__(self, name=thread_name)

    def run(self):
        time.sleep(10)
        print(self.getName())

def func1():
    t1.start()
    print('func1 done')

def func2():
    t2.start()
    print('func2 done')

t1 = TestThread('线程T1')
t2 = TestThread('线程T2')
t2.setDaemon(True)
func1()
func2()  

```

运行后输出结果如下

```bash
func1 done
func2 done
线程T1
```

由于调用了线程t2的setDaemon方法，当主线程结束时，线程t2也跟着结束。因此t2还没有来得及打印自己的线程名，就结束了。

将脚本中的t2.setDaemon(True)删除后运行得到结果如下

```bash
func1 done
func2 done
线程T2
线程T1
```

修改后的脚本要等待所有子线程完成后才会退出，因此线程t1和t2都被执行完成。如果在交互式模式下运行改脚本，则不会有区别，

因为在交互模式下的主线程在退出Python时才终止。

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
