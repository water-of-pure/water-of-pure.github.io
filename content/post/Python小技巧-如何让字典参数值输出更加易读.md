+++
date = '2025-07-30T10:40:39.928583+08:00'
draft = false
title = 'Python小技巧 - 如何让字典参数值输出更加易读'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

标准的字典字符串的输出是比较难易读的，这个说的是什么意思

下面看个代码例子

```python

mapping_1 = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(mapping_1)
```

执行后代码输出结果如下

```bash

{'a': 23, 'b': 42, 'c': 12648430}
```

但是我们换个输出方式，会让字段输出比较人性化

“ json”模块可以做的更好：

看下面这个代码例子

```python

import json

mapping_1 = {'a': 23, 'b': 42, 'c': 0xc0ffee}

print(json.dumps(mapping_1, indent=4, sort_keys=True))
```

运行后输出结果如下

```python

$ python main.py
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
```

是不是这个方式的输出更加友好一些
