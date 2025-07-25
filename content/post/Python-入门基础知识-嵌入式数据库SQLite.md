+++
date = '2025-07-25T15:55:01.028758+08:00'
draft = false
title = 'Python 入门基础知识 - 嵌入式数据库SQLite'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**嵌入式数据库SQLite**

SQLite是一款轻型的嵌入式数据库，相对于其他的庞大数据库软件，SQLite显得十分小巧。

使用SQLite不需要要像MySQL的守护进程。SQLite可以满足一般的数据库应用，Python也提供了对SQLite的支持。

**1、SQLite的安装**

我使用的是Mac电脑，里面有个比较方便的工具brew，可以自己安装brew，然后执行

brew install sqlite3

安装SQLite完成

**2、创建数据库**

sqlite3 python

命令行参数"python"表示创建一个名为"python"的数据库。运行后将出现如下提示

SQLite version 3.21.0 2017-10-24 18:55:49

Enter ".help" for usage hints.

sqlite> CREATE TABLE people (name VARCHAR(30), age INT, sex CHAR(1)); # 创建名为'people'的表

sqlite> INSERT INTO people VALUES ('Durban-1', 20, 'M'); # 插入内容

sqlite> INSERT INTO people VALUES ('Durban-2', 20, 'F'); # 插入内容

sqlite> SELECT \* FROM people; # 查看表'people'的数据内容

Durban-1|20|M

Durban-2|20|F

sqlite>

**3、Python中使用SQLite**

完成对数据库的操作后可以使用.exit命令退出命令行，此时就可以在Python中使用所创建的'python'数据库了。在Python中

使用SQLite数据库和使用MySQL数据库的过程类似。首先需要导入sqlite3模块，由于SQLite不需要服务器，因此直接使用connect

方法直接打开数据库即可。connect方法返回一个数据库连接对象，使用其cursor方法可以获得一个游标，然后就可以对记录进行操作。

在完成操作后，应使用close方法关闭游标和数据库连接。

实例演示如下

```py
# _*_ coding: utf-8 -*-
import sqlite3
con = sqlite3.connect('python')
cur = con.cursor()
cur.execute(
    'insert into people (name, age, sex) values (\'Durban-3\', 23, \'F\')')
r = cur.execute('delete from people where age = 20')
con.commit()
cur.execute('select * from people')
s = cur.fetchall()
print(s)
cur.close()
con.close()  

```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
