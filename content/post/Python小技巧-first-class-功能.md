+++
date = '2025-07-30T10:41:22.931827+08:00'
draft = false
title = 'Python小技巧 - first-class 功能'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

由于Python具有 fisrt-class 的功能，因此它们可用于模拟switch / case语句

先看下一个if逻辑判断函数

代码如下

```python

def if_func(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None
```

上面代码我们能很清晰的看清楚这个函数的具体功能

然后我们参考上面的代码逻辑新写一个

```python

def dict_func(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y
    }.get(operator, lambda: None)()
```

下面我们测试下两个函数的结果

```python

print(if_func('add', 1, 2))
print(dict_func('add', 1, 2))
print(if_func('mul', 3, 4))
print(dict_func('mul', 3, 4))
```

执行结果如下

```bash

3
3
12
12
```
