+++
date = '2025-07-25T15:10:02.757415+08:00'
draft = false
title = 'Python 入门基础知识 - 多线程编程'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**多线程编程**

进程是操作系统中应用程序的执行实例，而线程是进程内部的一个执行单元。当系统创建一个进程后，也就创建了一个主线程。每个进程至少有一个线程，

也可以有多个线程。在程序中使用多线程可以实现并行处理，充分利用CPU。Python提供了对多线程的支持。在Python中可以方便的使用多线程进行编程。

**线程基础**

Python提供了thread、threading模块对多线程编程的支持。threading模块是对thread模块的封装。多数情况下使用threading模块来进行多线程编程。

**创建编程**

在Python中可以通过使用thread模块中的函数，或者通过继承threading类来创建线程。编程创建后还可以对其进行操作。

**1，使用thread模块创建线程**

thread模块提供了start\_new\_thread函数，用以创建线程。start\_new\_thread函数成功创建线程后将返回线程标识。其函数原型如下所示。

其函数含义如下。

> function: 在线程中执行的函数名
>
> args: 元组形式的函数列表
>
> kwargs: 可选参数，以字典的形式指定参数

实例演示如下

```py
import thread  # 导入thread函数
import time

def run(n):  # 定义run函数
    for i in range(n):
        print(i)

print(thread.start_new_thread(run, (4,)))  # 使用start_new_thread函数创建线程
print(thread.start_new_thread(run, (2,)))  # 使用start_new_thread函数创建线程
print(thread.start_new_thread(run, (), {'n': 4}))  # 使用字典向函数传递参数

time.sleep(10)  # 防止主线程先于子线程结束而报错  

```

运行代码后输出如下

```bash
123145544208384 # 返回线程的标识
0 # 此处为run函数的输出
1
2
3
0
1
123145548414976 # 返回线程的标识
0 # 此处为run函数的输出
1
123145544208384 # 返回线程的标识
```

可以看到以上输入 每次执行后都会有不同的顺序输出

**2，使用threading模块创建线程**

通过继承threading模块中的Thread创建新类，重载run方法后，可以通过start方法创建线程。线程创建后将运行run方法。

代码演示如下

```py
import threading

class TestThread(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print('I am ' + str(self.num))

t1 = TestThread(1)
t2 = TestThread(2)
t3 = TestThread(3)
t1.start()
t2.start()
t3.start()  

```

运行代码后输出如下

```bash
I am 1
I am 2
I am 3
```

除了通过继承threading.Thread创建类以外，还可以通过使用threading.Thread直接在线程中创建函数。

实例演示如下

```py
import threading  # 导入threading模块

def run(x, y):  # 定义run函数
    for i in range(x, y):
        print(i)

t1 = threading.Thread(target=run, args=(15, 20))  # 直接使用Thread附加函数，args为函数参数
t1.start()  # 运行线程
# 运行结果如下
# 15
# 16
# 17
# 18

t2 = threading.Thread(target=run, args=(7, 11))  # 直接使用Thread附加函数，args为函数参数
t2.start()  # 运行线程
# 运行结果如下
# 7
# 8
# 9
# 10  

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
