+++
date = '2025-07-30T10:41:19.736746+08:00'
draft = false
title = 'Python小技巧 - timeit计算代码片段的耗时'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

timeit提供了一种简单的方法来计算一小段 Python 代码的耗时

比如下面的代码段

```python

import timeit

print(timeit.timeit('"_".join(str(n) for n in range(1000))', number=10000))
```

执行结果如下

```bash

5.119179364
```

或者

```bash

3.155041132
```

但是每次执行的时间都不太一样

再比如下面的代码片段

```python

import timeit

print(timeit.timeit('"_".join([str(n) for n in range(100)])', number=10000))
```

执行结果如下

```bash

0.370741945
```

或者

```bash

0.395660464
```

再比如下面的代码片段

```python

import timeit

print(timeit.timeit('"_".join(map(str, range(100)))', number=10000))
```

执行结果如下

```python

0.370741945
```

或者

```python

0.395660464
```