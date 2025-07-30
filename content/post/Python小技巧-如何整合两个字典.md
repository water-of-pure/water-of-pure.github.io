+++
date = '2025-07-30T10:40:20.643839+08:00'
draft = false
title = 'Python小技巧 - 如何整合两个字典'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "字典"
]
+++

在Python 3.5+中 如何合并两个字典

举个例子

```python

a_dict = {'x': 1, 'y': 2, 'z': 3}
b_dict = {'m': 1, 'p': 2, 'q': 3}
c_dict = {**a_dict, **b_dict}
print(c_dict)
```

输出的结果如下

```bash

{'x': 1, 'y': 2, 'z': 3, 'm': 1, 'p': 2, 'q': 3}
```

在Python2版本中可以使用如下的方式

举个例子

```python

a_dict = {'x': 1, 'y': 2, 'z': 3}
b_dict = {'m': 1, 'p': 2, 'q': 3}
c_dict = dict(**a_dict, **b_dict)
print(c_dict)
```

输出的结果如下

```bash

{'x': 1, 'y': 2, 'z': 3, 'm': 1, 'p': 2, 'q': 3}
```

在这些示例中，Python合并字典键按照表达式中列出的顺序，覆盖从左到右重复。

在Python3.5+中

举个例子

```python

a_dict = {'x': 1, 'y': 2, 'z': 3}
b_dict = {'z': 1, 'p': 2, 'q': 3}
c_dict = dict(**a_dict, **b_dict)
print(c_dict)
```

输出的结果如下

```bash

{'x': 1, 'y': 2, 'z': 1, 'p': 2, 'q': 3}
```
