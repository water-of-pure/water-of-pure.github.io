+++
date = '2025-07-25T15:54:39.936476+08:00'
draft = false
title = 'Python 入门基础知识 - 微线程 - Stackless Python'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**微线程 - Stackless Python**

Stackless Python是Python的一个增强版本。Stackless Python修改了Python的代码，提供了对微线程的支持。

微线程是轻量级的线程，与前边所讲的线程相比，微线程在多个线程间切换所需的时间更多，占用资源也更少。

**Stackless Python概述**

Stackless Python不是必需的，它只是Python的一个修改版本，对多线程编程更友好的支持。如果在对线程应用有较高的的要求时

可以考虑使用Stackless Python来完成。

**1.Stackless Python 安装**

在安装Stackless Python之前应该先安装Python，根据所安装的Python版本到Stackless Python的官网

<http://stackless.com>下载相应的版本。

安装完后可以在Python的交换式环境中输入如下代码

```py
import stackless
```

如果没有错误产生，则表示Stackless Python已经安装好了。若出现错误，则可能是Stackless Python与当前的Python版本不兼容，

可以考虑使用其他版本的Python

**2. stackless模块中的tasklet对象**

Stackless Python提供了stackless内置模块。stackless模块中的tasklet对象完成了与创建线程类似的功能。

使用tasklet对象可以像创建线程运行函数那样来运行函数。

示例代码如下

```py
# _*_ coding: utf-8 _*_
import stackless
def show():
    print('Stackless Python')
st = stackless.tasklet(show)() # 调用tasklet添加函数，第2个括号为函数参数
st.run() # 调用run方法，执行函数
st = stackless.tasklet(show)() # 重新生成st
print(st.alive) # 查看其状态
st.kill() # 调用kill方法结束线程
print(st.alive) # 查看其状态
print(stackless.tasklet(show)()) # 直接调用tasklet
print(stackless.tasklet(show)())
stackless.run() # 调用run方法
```

运行后输出结果如下

```bash
Stackless Python
True
False
<_stackless.tasklet object at 0x1007e76e0>
<_stackless.tasklet object at 0x1007e7b40>
Stackless Python
Stackless Python
```

**3.stackless模块中的schedule对象**

stackless模块中的schedule对象可以控制任务的执行顺序。当有多个任务时，可以使用schedule对象使其依次执行。

示例代码如下

```py
# _*_ coding: utf-8 _*_
import stackless
def show():
    stackless.schedule()
    print(1)
    stackless.schedule()
    print(2)
stackless.tasklet(show)()  # 调用tasklet,生成任务列表
stackless.tasklet(show)()
stackless.run()  # 执行任务
```

运行后输出结果如下

```bash
1
1
2
2
```

**4.stackless模块中的channel对象**

使用stackless模块中的channel对象可以在不同的人之间进行通信，这和线程间的通信类似。使用channel对象的

send方法可以发送数据。使用channel对象的receive方法可以接收数据。

```py
# _*_ coding: utf-8 _*_
import stackless
def send():
    chn.send('Stackless Python')
    print('I send: Stackless Python')
def rec():
    print('I receive: %s ' % chn.receive())
chn = stackless.channel()
stackless.tasklet(send)()
stackless.tasklet(rec)()
stackless.run()
```

运行结果如下

```bash
I receive: Stackless Python
I send: Stackless Python
```

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
