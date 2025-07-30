+++
date = '2025-07-30T09:57:26.930294+08:00'
draft = false
title = 'Python的List Comprehension(列表推导式)'
categories = [
    "技术",

]

tags = [
    "Python",
    "List"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

如何更高效的创建列表

Python提供了一个高效的列表推导式（List Comprehension）

语法如下

```python

values = [expression
        for value in collection
        if condition]
```

等价于

```python

vals = []
for value in collection:
	if condition:
		vals.append(expression)
```

举个简单的例子

```python

even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)
```

输出结果如下

```bash

[0, 4, 16, 36, 64]
```

列表推导式（List Comprehension）还有更多好用的方法，后面继续补充
