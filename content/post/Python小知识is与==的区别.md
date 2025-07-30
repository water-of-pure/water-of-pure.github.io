+++
date = '2025-07-30T10:41:00.390292+08:00'
draft = false
title = 'Python小知识 - “is” 与 “==” 的区别'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

Python中 “`is`” 与 “`==`” 有什么区别

示例如下

```python

a = ['a', 'b', 'c']
b = a

print(a is b)
print(a == b)
```

运行结果如下

```bash

True
True
```

“is”与“==”结果是一致的

在看下面的示例

```python

a = ['a', 'b', 'c']
c = list(a)
print(a is c)
print(a == c)
```

运行结果如下

```bash

False
True
```

“is”与“==”结果是不一致的

"is" 如果两个变量指向同一个对象，则表达式的计算结果为True

"==" 如果变量引用的对象相等，则求值为True
