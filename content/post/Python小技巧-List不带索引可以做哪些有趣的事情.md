+++
date = '2025-07-30T11:03:22.640455+08:00'
draft = false
title = 'Python小技巧 - List不带索引可以做哪些有趣的事情'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "List"
]
+++

List不带索引可以做很多有趣的事情，比如下面的代码

**清空List列表**

```python
list_1 = [1, 2, 3, 4]
a = list_1
del list_1[:]
print(list_1)
print(a)
```

运行后输出结果如下

```bash
$ python main.py
[]
[]
```

**替换所有元素**

```python
list_1 = [1, 2, 3, 4]
a = list_1
list_1[:] = ['a', 'b', 'c']
print(list_1)
print(a)
print(a is list_1)
```

运行后输出结果如下

```bash
$ python main.py
['a', 'b', 'c']
['a', 'b', 'c']
True
```

**List复制**

```python
list_1 = [1, 2, 3, 4]
a = list_1[:]
print(list_1)
print(a)
print(a is list_1)
```

运行后输出结果如下

```bash
$ python main.py
[1, 2, 3, 4]
[1, 2, 3, 4]
False
```
