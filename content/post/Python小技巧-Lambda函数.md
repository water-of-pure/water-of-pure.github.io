+++
date = '2025-07-30T11:43:32.901084+08:00'
draft = false
title = 'Python小技巧 - Lambda函数'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "Lambda"
]
+++

Lambda函数

lambda创建函数

```python

add = lambda x, y: x + y
```

```python

print(add(2, 3))
```

普通方式创建函数

```python

def add(x, y):
    return x + y
```

```python

print(add(2, 3))
```

lambda匿名函数

```python

add_res = (lambda x, y: x + y)(2, 3)
print(add_res)
```
