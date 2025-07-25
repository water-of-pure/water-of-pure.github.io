+++
date = '2025-07-25T15:09:38.684677+08:00'
draft = false
title = 'Python 入门基础知识 - assert - 简化的raise语句'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**assert - 简化的raise语句**

在Python中使用assert语句同样可以引发异常。但与raise语句不同，assert语句是在条件测试为假时，

才引发异常。assert语句的一般形式如下：

```py
assert <条件测试>, <异常附件数据> # 其中异常附加数据是可选的
```

实例如下

```py
l = []
```

```py
assert len(l) # 如果列表为空，则使用assert引发异常
```

异常抛出如下

```bash
    assert len(l)
AssertionError
```

```py
assert len(l), 'Error'
```

异常输出如下

```bash
    assert len(l), 'Error'
AssertionError: Error
```

```py
try:
    assert len(l), 'Error'
except:
    print('Error')
else:
    print('No Error')  

```

输出如下

```bash
Error
```

```py
l.append(1)  # 向列表中添加成员
assert len(l)  # 此时列表不为空，assert将不会引发异常
```

从上面的实例可以看出，assert相当于raise语句和if语句联合使用。

例如如下assert语句

```py
assert len(l)
```

可以改写如下

```py
if __debug__:
    if len(1):
        raise AssertionError, <附加数据>
```

需要注意的是，assert语句一般用于开发时对程序条件的验证。只有当内置\_\_debug\_\_为True时，assert语句才有效。

当Python脚本为-O选项编译成字节码文件时，assert语句将被移除。

实例环境声明

```bash
# _*_ coding: utf-8 _*_
# Python 2.7.13  

```
