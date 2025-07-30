+++
date = '2025-07-30T10:40:36.992033+08:00'
draft = false
title = 'Python小技巧 - Fabric并发执行远程主机操作'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "Fabric"
]
+++

fabric中如何实现并发执行远程主机任务

比如我有多台远程主机，想要通过并行的方式在没太主机上执行同样的命令

如果按照fabric提供的`ThreadingGroup`的话，可能会遇到一个问题就是，每个主机在执行命令的时候，遇到问题，比如链接失败的话可能会导致所有的链接都失败，再比如我要判断每台机器的部署项目的目录是否存在，这个时候的话，每个远程主机执行的时候需要执行不同的逻辑，我采用另外一个方式，就是`multiprocessing`的方式

首先看下`multiprocessing的并发如何实现`

第一种是`Process`

实现方式如下

```python

from multiprocessing import Pool, Process
import time

def host_run(host):
    print('执行 %s' % host)
    time.sleep(10)
    print('结束 %s' % host)

hosts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Process方式创建进程
print('创建Process')
for h in hosts:
    p = Process(target=host_run, args=(h + ' - process', ))
    p.start()
print('Process执行结束')
```

运行结果如下

```bash

创建Process
执行 1 - process
执行 2 - process
执行 3 - process
执行 4 - process
执行 5 - process
执行 6 - process
执行 7 - process
执行 8 - process
Process执行结束
执行 9 - process
执行 10 - process
结束 1 - process
结束 2 - process
结束 3 - process
结束 4 - process
结束 5 - process
结束 6 - process
结束 7 - process
结束 8 - process
结束 9 - process
结束 10 - process
```

第二种是`Pool`

实现方式如下

```python

from multiprocessing import Pool, Process
import time

def host_run(host):
    print('执行 %s' % host)
    time.sleep(10)
    print('结束 %s' % host)

hosts = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Pool方式创建大量子进程
print('创建Pool')
pool = Pool(len(hosts))
for h in hosts:
    pool.apply_async(host_run, args=(h + 'pool', ))
print('等待Pool执行')
pool.close()
pool.join()
```

运行结果如下

```bash

创建Pool
等待Pool执行
执行 1 - pool
执行 2 - pool
执行 3 - pool
执行 4 - pool
执行 5 - pool
执行 6 - pool
执行 7 - pool
执行 8 - pool
执行 9 - pool
执行 10 - pool
结束 2 - pool
结束 3 - pool
结束 1 - pool
结束 4 - pool
结束 5 - pool
结束 6 - pool
结束 7 - pool
结束 8 - pool
结束 9 - pool
结束 10 - pool
```

到这里，两种方式我们都实现了并发的方式执行代码逻辑

下面回到主体，整合到fabric中，要如何实现

实现代码如下

```python

import socket, paramiko.ssh_exception
from fabric import SerialGroup, exceptions, runners, Connection
from fabric import task
from fabric.exceptions import GroupException
from multiprocessing import Process

hosts = ['localhost', 'localhost', 'localhost', 'localhost']

def host_run(host):
    c = Connection(host)
    res = c.run('ls -ahl')
    print(res)

@task
def asyncrun(c):
    for h in hosts:
        p = Process(target=host_run, args=(h, ))
        p.start()
```

运行结果如下

```bash

$ fab asyncrun
Process Process-1:
Traceback (most recent call last):
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 267, in _bootstrap
    self.run()
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/durban/python/practise/fabfile.py", line 34, in host_run
    res = c.run('ls -ahl')
  File "<decorator-gen-3>", line 2, in run
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 29, in opens
    self.open()
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 634, in open
    self.client.connect(**kwargs)
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/paramiko/client.py", line 368, in connect
Process Process-3:
Process Process-4:
Process Process-2:
Traceback (most recent call last):
Traceback (most recent call last):
Traceback (most recent call last):
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 267, in _bootstrap
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 267, in _bootstrap
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 267, in _bootstrap
    self.run()
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 114, in run
    self.run()
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/durban/python/practise/fabfile.py", line 34, in host_run
    self._target(*self._args, **self._kwargs)
  File "/Users/durban/python/practise/fabfile.py", line 34, in host_run
    res = c.run('ls -ahl')
  File "<decorator-gen-3>", line 2, in run
    self.run()
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 29, in opens
  File "/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/lib/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/durban/python/practise/fabfile.py", line 34, in host_run
    res = c.run('ls -ahl')
    res = c.run('ls -ahl')
  File "<decorator-gen-3>", line 2, in run
  File "<decorator-gen-3>", line 2, in run
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 29, in opens
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 29, in opens
    raise NoValidConnectionsError(errors)
NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 127.0.0.1 or ::1
    self.open()
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 634, in open
    self.client.connect(**kwargs)
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/paramiko/client.py", line 368, in connect
    self.open()
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 634, in open
    self.client.connect(**kwargs)
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/paramiko/client.py", line 368, in connect
    self.open()
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/fabric/connection.py", line 634, in open
    self.client.connect(**kwargs)
  File "/Users/durban/python/.env_2.7.16/lib/python2.7/site-packages/paramiko/client.py", line 368, in connect
    raise NoValidConnectionsError(errors)
    raise NoValidConnectionsError(errors)
NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 127.0.0.1 or ::1
NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 127.0.0.1 or ::1
    raise NoValidConnectionsError(errors)
NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 127.0.0.1 or ::1
```

我这里是报了错误，但是从错误信息可以看出，每个host都并发的执行了，不然错误应该不会交叉输出的

后面会记录一个完整版的fabric，能过链接正式生产环境的脚本实践实例。
