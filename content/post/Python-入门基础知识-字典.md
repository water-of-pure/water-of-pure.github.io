+++
date = '2025-07-24T10:41:02.847280+08:00'
draft = false
title = 'Python 入门基础知识 - 字典'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

实例环境配置

# \_\*\_ coding: utf-8 -\*-

# version 2.7.13

**字典**

字典是Python中比较特殊的一类数据类型，以大括号"{}"包围的数据集合。

字典与列表的最大不同在于字典是无序的，在字典中是通过键来访问成员的。

字典也是可变的，可以包含任何其他类型，字典中的成员位置只是象征性的，

并不能通过其位置来访问该成员。

字典中的成员是以"键:值"的形式来声明的。

常用的字典操作如下：

> dic.clear # 清空字典
>
> dic.copy() # 复制字典
>
> dic.get(k) # 获得键k的值
>
> dic.has\_key(k) # 是否包括键k
>
> dic.items() # 获得由键和值组成的列表
>
> dic.keys() # 获得键的列表
>
> dic.pop(k) # 删除键k
>
> dic.update() # 更新成员
>
> dic.values() # 获得值的列表

实例走起，如下：

```python
dic = { 'apple': 2, 'orange': 3}
print(dic)

print(dic.copy())

dic['banana'] = 5
print(dic)

print(dic.items())

print(dic.pop('apple', 3))
print(dic.pop('apple', 3))		# 3 代表默认没有键值的默认值
print(dic)

print(dic.keys())

print(dic.values())

print(dic.update({ 'banana': 10 }))
print(dic)

print(dic.update({ 'apple': 4 }))		# 如果没有对应键值，则添加
print(dic)

print(dic['orange'])

print(dic.clear())
print(dic)  

```
