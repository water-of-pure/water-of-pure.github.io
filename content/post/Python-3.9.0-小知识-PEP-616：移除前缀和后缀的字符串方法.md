+++
date = '2025-07-30T11:43:46.026961+08:00'
draft = false
title = 'Python 3.9.0 小知识 - PEP 616：移除前缀和后缀的字符串方法'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

Python 3.9.0 新增内置方法：移除前缀和后缀的字符串方法

详情可以点击[这里](https://www.python.org/dev/peps/pep-0616/)查看

这里简单做下记录

从详情中我们可以看到其具体实现

```python

def removeprefix(self: str, prefix: str, /) -> str:
    if self.startswith(prefix):
        return self[len(prefix):]
    else:
        return self[:]

def removesuffix(self: str, suffix: str, /) -> str:
    # suffix='' should not call self[:-0].
    if suffix and self.endswith(suffix):
        return self[:-len(suffix)]
    else:
        return self[:]
```

同时列举了几个例子

第一个列子

```python

if test_func_name.startswith("test_"):
    print(test_func_name[5:])
else:
    print(test_func_name)
```

这里例子如果在Python 3.9.0的话，可以改善为下面的方式

```python

print(test_func_name.removeprefix("test_"))
```

第二个例子

```python

if funcname.startswith("context."):
    self.funcname = funcname.replace("context.", "")
    self.contextfunc = True
else:
    self.funcname = funcname
    self.contextfunc = False
```

如果使用Python 3.9.0的话，可以改善为下面的方式

```python

if funcname.startswith("context."):
    self.funcname = funcname.removeprefix("context.")
    self.contextfunc = True
else:
    self.funcname = funcname
    self.contextfunc = False
```

进一步可以改善为

```python

self.contextfunc = funcname.startswith("context.")
self.funcname = funcname.removeprefix("context.")
```

第三个例子

```python

def strip_quotes(text):
    if text.startswith('"'):
        text = text[1:]
    if text.endswith('"'):
        text = text[:-1]
    return text
```

如果使用Python 3.9.0的话，可以改善为下面的方式

```python

def strip_quotes(text):
    return text.removeprefix('"').removesuffix('"')
```

第四个列子

```python

if name.endswith(('Mixin', 'Tests')):
    return name[:-5]
elif name.endswith('Test'):
    return name[:-4]
else:
    return name
```

如果使用Python 3.9.0的话，可以改善为下面的方式

```python

return (name.removesuffix('Mixin')
            .removesuffix('Tests')
            .removesuffix('Test'))
```
