+++
date = '2025-07-30T11:43:35.974822+08:00'
draft = false
title = 'Python 3.9.0 小知识 - PEP 585：标准多项集中的类型标注泛型'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

PEP 585：标准多项集中的类型标注泛型

字面上有点难理解，我也是懵圈中

看了下官网的解释：https://www.python.org/dev/peps/pep-0585/

大概了解下来我用实例演示下

从Python 3.7到Python 3.8之前我们可以这样创建函数了

比如我要获取一个List的长度

```bash

$ python
Python 3.8.6 (default, Oct  8 2020, 14:06:32)
[Clang 12.0.0 (clang-1200.0.32.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import typing
>>> def get_value_length(l: typing.List[str]) -> int:
...     return len(l)
...
>>> get_value_length([1,2,4])
3
```

但是如果我要像下面这样创建是不行的

```bash

$ python
Python 3.8.6 (default, Oct  8 2020, 14:06:32)
[Clang 12.0.0 (clang-1200.0.32.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def get_value_length(l: List[str]) -> int:
...     return len(l)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'List' is not defined
```

或者

```bash

>>> def get_value_length(l: list[str]) -> int:
...     return len(l)
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not subscriptable
```

但是现在在Python 3.9中这个事情就变的简单了

```bash

$ /usr/local/Cellar/[email protected]/3.9.0/bin/python3
Python 3.9.0 (default, Oct  6 2020, 04:17:54)
[Clang 12.0.0 (clang-1200.0.32.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> def get_value_length(l: list[str]) -> int:
...     return len(l)
...
>>> get_value_length([1,2,3])
3
>>> get_value_length(['1','2','3'])
3
```

这里我只演示了list

其实还有很多类似这样的，如下

* tuple # typing.Tuple
* list # typing.List
* dict # typing.Dict
* set # typing.Set
* frozenset # typing.FrozenSet
* type # typing.Type
* collections.deque
* collections.defaultdict
* collections.OrderedDict
* collections.Counter
* collections.ChainMap
* collections.abc.Awaitable
* collections.abc.Coroutine
* collections.abc.AsyncIterable
* collections.abc.AsyncIterator
* collections.abc.AsyncGenerator
* collections.abc.Iterable
* collections.abc.Iterator
* collections.abc.Generator
* collections.abc.Reversible
* collections.abc.Container
* collections.abc.Collection
* collections.abc.Callable
* collections.abc.Set # typing.AbstractSet
* collections.abc.MutableSet
* collections.abc.Mapping
* collections.abc.MutableMapping
* collections.abc.Sequence
* collections.abc.MutableSequence
* collections.abc.ByteString
* collections.abc.MappingView
* collections.abc.KeysView
* collections.abc.ItemsView
* collections.abc.ValuesView
* contextlib.AbstractContextManager # typing.ContextManager
* contextlib.AbstractAsyncContextManager # typing.AsyncContextManager
* re.Pattern # typing.Pattern, typing.re.Pattern
* re.Match # typing.Match, typing.re.Match

不过对于我来说也许我也就用到下面几个

* tuple # typing.Tuple
* list # typing.List
* dict # typing.Dict
* set # typing.Set
* frozenset # typing.FrozenSet
* type # typing.Type

完全个人理解，仅供参考
