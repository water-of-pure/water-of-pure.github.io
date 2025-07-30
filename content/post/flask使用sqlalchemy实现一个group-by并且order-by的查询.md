+++
date = '2025-07-30T10:40:51.535045+08:00'
draft = false
title = 'flask使用sqlalchemy实现一个group by并且order by的查询'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask",
    "SQLAlchemy"
]
+++

比如我要将我的Tags表的title，按照使用次数最多的并进行降序排列，而且获取前20条Tag  
 如果是sql查询的话，如果下

```sql

select count(*) as total, title 
from tags 
where title <> '' 
group by title 
order by total DESC 
limit 0, 20;
```

用sqlalchemy的使用方式如下

```python

from sqlalchemy import func

Tag.query.with_entities(
    Tag.title, func.count(Tag.title).label('total')
).filter(Tag.title != '')\
    .group_by(Tag.title)\
    .order_by('total DESC')\
    .limit(20)\
    .all()
```

但是上面的使用方式在执行的时候会报如下错误

```bash

SAWarning: Can't resolve label reference 'total DESC'; converting to text() (this warning may be suppressed after 10 occurrences)
  util.ellipses_string(element.element))
```

解决方案的代码如下

```python

from sqlalchemy import func, desc

order_by_total = func.count(Tag.title).label('total')

Tag.query.with_entities(
    Tag.title, func.count(Tag.title).label('total')
).filter(Tag.title != '')\
    .group_by(Tag.title)\
    .order_by(desc(order_by_total))\
    .limit(20)\
    .all()
```

使用方式还是挺奇怪的
