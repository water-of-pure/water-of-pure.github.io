+++
date = '2025-07-30T10:39:40.891148+08:00'
draft = false
title = 'Python小技巧 - 如何根据字典中的值来排序字典'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

很多情况下，我们需要的数据是按照一定顺序的，通常情况下顺序都是按照键或者是键值来排序

按照字典的值来排序的话，记录集中方式供参考

举个例子

原始字典值为

```python

dict1 = {'x1': 4, 'x2': 5, 'x3': 6, 'x4': 7, 'x5': 3}
```

### 第一种按照值来排序的方式

```python

dict2 = sorted(dict1.items(), key=lambda x: x[1])
print(dict2)
```

输出结果如下

```python

[('x5', 3), ('x1', 4), ('x2', 5), ('x3', 6), ('x4', 7)]
```

### 第二种按照值来排序的方式

```python

dict3 = sorted(dict1.items(), key=operator.itemgetter(1))
print(dict3)
```

输出结果如下

```python

[('x5', 3), ('x1', 4), ('x2', 5), ('x3', 6), ('x4', 7)]
```