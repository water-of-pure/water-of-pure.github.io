+++
date = '2025-07-30T10:40:57.365183+08:00'
draft = false
title = 'Python小知识 - Python中的函数的几个特点'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

Python中的函数可以作为一个参数传递给另外一个函数，同时可以作为另外一个函数的返回值，同时可以复制给一个变量并且存储里面的数据结构

比如下面的代码示例

```python

def my_func(x, y):
    return x + y

funcs = [my_func]
print(funcs[0])
print(funcs[0](1, 2))
```

运行后得到的结果如下

```bash

$ python main.py
<function my_func at 0x10d46bc20>
3
```