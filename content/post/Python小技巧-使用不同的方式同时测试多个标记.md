+++
date = '2025-07-30T09:57:45.085360+08:00'
draft = false
title = 'Python小技巧 - 使用不同的方式同时测试多个标记'
categories = [
    "技术",

]

tags = [
    "Python",

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
+++

如何使用不同的方式同时测试多个标记

比如我有个需求如下

代码逻辑是这样的

```python

x, y, z = 1, 0, 1
if x == 1 or y == 1 or z == 1:
    print('passed')
```

可以修改为如下方式，实现同时测试多个标记，不需要分开写，比较方便

```python

if 1 in (x, y, z):
    print('passed')
```

再比如我有这个需求，只判断true 或者 false

```python

if a or b or c:
    print('passed')
```

可以修改为下面的方式，实现同时测试多个标记

```python

if any((a, b, c)):
    print('passed')
```

---

每天积累一点，技术成熟一点
