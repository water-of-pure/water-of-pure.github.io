+++
date = '2025-07-30T11:28:38.143307+08:00'
draft = false
title = 'Python小知识 - classmethod、staticmethod和正常方法的区别'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

`classmethod`、`staticmethod`和正常方法的区别是什么

简单的创建一个类

```python

class TestClass(object):
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(self):
        return 'class method called', self

    @staticmethod
    def staticmethod(self):
        return 'static method called', self
```

接下来实例化类，实现如下

```python

test = TestClass()
print(test.method())
print(test.classmethod())
print(test.staticmethod())
```

运行后输出的结果如下

```bash

('instance method called', <__main__.TestClass object at 0x10fe64e50>)
('class method called', <class '__main__.TestClass'>)
Traceback (most recent call last):
  File "/Users/durban/python/practise/main.py", line 31, in <module>
    print(test.staticmethod())
TypeError: staticmethod() missing 1 required positional argument: 'self'
```

`staticmethod`这个方法因为加了`@staticmethod`修饰符导致第一个参数self并不是类自身，而是作为一个参数需要传入

看下面的调用方式

```python

test = TestClass()
print(test.method())
print(test.classmethod())
print(test.staticmethod(1))
```

运行后输出的结果如下

```bash

('instance method called', <__main__.TestClass object at 0x105e72e50>)
('class method called', <class '__main__.TestClass'>)
('static method called', 1)
```

再看个调用方式

```python

print(TestClass.classmethod())
print(TestClass.staticmethod(1))
print(TestClass.method())
```

运行后得到的结果类似如下

```bash

('class method called', <class '__main__.TestClass'>)
('static method called', 1)
Traceback (most recent call last):
  File "/Users/durban/python/practise/main.py", line 30, in <module>
    print(TestClass.method())
TypeError: method() missing 1 required positional argument: 'self'
```

将上面的调用方式调整如下

```python

print(TestClass.classmethod())
print(TestClass.staticmethod(1))
print(TestClass.method(1))
```

运行后得到的结果类似如下

```bash

('class method called', <class '__main__.TestClass'>)
('static method called', 1)
('instance method called', 1)
```

奇怪的是`method`可以被正常的调用了
