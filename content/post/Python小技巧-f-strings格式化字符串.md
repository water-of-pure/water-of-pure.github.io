+++
date = '2025-07-30T11:03:18.640559+08:00'
draft = false
title = 'Python小技巧 - f-strings格式化字符串'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

Python 3.8 中 f-strings 添加了一个"="，让f-strings使用起来更加方便

比如下面的代码

```python

from datetime import date

user = 'durban'
member_since = date(1988, 1, 2)
print(f'{user=} {member_since=}')
```

运行后输出结果如下

```bash

user='durban' member_since=datetime.date(1988, 1, 2)
```

再比如下面的代码实例

```python

from datetime import date

user = 'durban'
member_since = date(1988, 1, 2)

delta = date.today() - member_since

print(f'{user=!s} {delta.days=:,d}')
```

运行后输出结果如下

```bash

user=durban delta.days=11,937
```

再比如下面的代码实例

```python

from math import cos, radians

theta = 45
print(f'{theta=} {cos(radians(theta))=:.3f}')
```

运行后结果如下

```bash
theta=45 cos(radians(theta))=0.707
```
