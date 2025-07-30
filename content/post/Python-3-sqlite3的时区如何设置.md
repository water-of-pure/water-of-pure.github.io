+++
date = '2025-07-30T09:57:01.938475+08:00'
draft = false
title = 'Python 3 - sqlite3的时区如何设置'
categories = [
    "技术",

]

tags = [
    "Python",
    "SQLite"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

在使用Python的sqlite3库的时候，我第一次遇到时区不知道怎么设置的情况

比如下面这个表

```sql

CREATE TABLE post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    the_date VARCHAR(32) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES user (id)
);

```

插入记录的时候created和updated被默认赋值一个时间戳

比如我当前的时间是`2019-12-26 17:36:44`，时区是8

那么插入后的结果值是`2019-12-26 09:36:44`，了解程序的都知道这个是UTC时区为0的时间

那么知识点就来了，在使用sqlite3时，当插入表的数据中，`created`和`updated`字段是`TIMESTAMP`类型并且默认值为`CURRENT_TIMESTAMP`时，其值是一个UTC时区为0的时间。

另外一个知识点，如何将此时间转换为我们当前时区需要的值

```py

import datetime
import time

the_date = '2019-12-26 09:36:44'

t = time.strptime(the_date, "%Y-%m-%d %H:%M:%S")
timestamp = int(time.mktime(t))
dt = datetime.datetime.fromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)
dt8 = dt.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
date = dt8.strftime("%Y-%m-%d %H:%M:%S")
print(date)

```

Output:

```bash

>>> print(date)
2019-12-26 17:36:44

```

封装下，得到如下函数

```py

import datetime
import time

the_date = '2019-12-26 09:36:44'

def date_to_timezone_date(date, timezone):
    t = time.strptime(the_date, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(t))
    dt = datetime.datetime.fromtimestamp(timestamp).replace(tzinfo=datetime.timezone.utc)
    dt8 = dt.astimezone(datetime.timezone(datetime.timedelta(hours=timezone)))
    date = dt8.strftime("%Y-%m-%d %H:%M:%S")

    return date

```

后期在将数据查出来之后就可以直接进行转换了，想转任何一个时区都可以。

最终的解决方案是，sqlite3的时区可以不用设置，也是可以拿到准确时间的
