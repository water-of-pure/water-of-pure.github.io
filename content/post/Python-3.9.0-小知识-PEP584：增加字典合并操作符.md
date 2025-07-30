+++
date = '2025-07-30T11:43:01.665833+08:00'
draft = false
title = 'Python 3.9.0 小知识 - PEP584：增加字典合并操作符'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

PEP584：增加字典合并操作符

内置字典类增加合并（ | ）与更新（ |= ）操作符

就是增加了合并操作符和更新操作符，简单应用下

```python

>>> d = {'spam': 1, 'eggs': 2, 'cheese': 3}
>>> e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
>>> d | e
{'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
>>> e | d
{'aardvark': 'Ethel', 'spam': 1, 'eggs': 2, 'cheese': 3}
```

```python

>>> d |= e
>>> d
{'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'}
```

文章参考：[链接1](https://zhuanlan.zhihu.com/p/111228843)
