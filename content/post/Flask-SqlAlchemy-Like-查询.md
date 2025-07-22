+++
date = '2025-07-22T18:31:27.567711+08:00'
draft = false
title = 'Flask SqlAlchemy Like 查询'
categories = [
    "技术",

]

tags = [
    "Flask",
    "SqlAlchemy"
]
+++

SQLAlchemy 如何进行 mysql的Like查询呢？

```py
Article.query.join(Category).filter(Article.title.like("%%s%", name), Article.is_deleted == 0).order_by(Article.id.desc())
```
