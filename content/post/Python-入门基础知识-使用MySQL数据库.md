+++
date = '2025-07-25T15:54:57.975641+08:00'
draft = false
title = 'Python 入门基础知识 - 使用MySQL数据库'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**使用MySQL数据库**

MySQL是一个小巧的多用户、多线程SQL数据库服务器。MySQL是一个客户机/服务器结构的实现，它由一个服务器守护进程和客户程序组成。

MySQL提供了对SQL语句的支持。在Python中可以使用MySQLdb模块链接到MySQL，对于MySQL数据库进行操作。

**1、安装MySQL**

这个环节，可以自行去官网下载进行安装，不会的可以群里交流

安装好MySQL后可以使用其附带的命令行工具创建数据库。创建好数据库后，就可以使用MySQL模块，在Python中连接到数据，对记录进行操作。

**2、安装MySQLdb**

在Python中使用MySQL的数据库需要安装MySQLdb模块。

由于我的是在mac下，我一般都是用命令行安装，可以参考如下命令

pip install MySQL-python

**3、在Python中使用MySQL数据库**

使用MySQLdb连接到MySQL数据库，首先使用MySQLdb模块的connect方法链接到MySQL守护进程。connect方法将返回一个数据库链接。使用数据库

链接的cursor方法可以获得当前数据库的游标。然后就可以使用游标的Execute方法执行SQL语句，完成对数据库的操作。

同样，当完成操作应调用close方法关闭游标和数据连接。

示例如下

```py
import MySQLdb  # 导入MySQLdb模块
db = MySQLdb.connect(
    host='localhost',  # 连接到数据库，服务器为本机
    user='root',  # 用户名为root
    passwd='123456',  # 密码为123456
    db='test')  # 数据库名为test
cur = db.cursor()  # 获得数据库游标
cur.execute(
    'insert into people \
    (name, age, sex) \
    values \
    (\'Durban - 1\', 21, \'Female\')')  # 执行SQL语句，添加记录
cur.execute(
    'insert into people \
    (name, age, sex) \
    values \
    (\'Durban - 2\', 20, \'Male\')')  # 执行SQL语句，添加记录
r = cur.execute('delete from people where age = 20')  # 执行SQL语句，删除记录
db.commit()  # 提交事务
r = cur.execute('select * from people')  # 执行SQL语句，获得记录
r = cur.fetchall()  # 获取数据
print(r)  # 输出数据
cur.close()
db.close()
```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
