+++
date = '2025-07-24T10:40:59.444366+08:00'
draft = false
title = 'Python 入门基础知识 - 列表和元组'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

实例环境声明

# \_\*\_ coding: utf-8 -\*-

# version 2.7.13

**列表和元组**

列表是以方括号"[]"包围的数据集合，不同成员以','分隔，列表中可以包含任何数据类型，也可以包括另一个列表。

列表可以通过序号来访问其中的成员。

脚本中可以对序列进行排序，添加，删除等操作，该表列表中某个成员的值。

元组的特性跟列表的特性相似，元组是以圆括号'()'包围的数据集合。于列表不同的是，元组中的数据一旦确立就不能被改变。

元组可以使用在不希望被其他操作改变的场合。

Python提供了对列表和元组强大的支持。如下：

* list.append() # 追加成员
* list.count(x) # 计算列表中x出现的次数
* list.extend(l) # 向列表中追加一个列表
* list.index(x) # 获得参数x在列表中的位置
* list.insert(n, x) # 向列表中指定位置插入数据
* list.pop(n) # 删除列表中的成员
* list.remove() # 删除列表中的成员
* list.reverse() # 将列表中成员的顺序颠倒
* list.sort() # 将列表中的成员排序

除此之外，在Python中也可以使用类似于字符串的分片和索引操作列表。而对于元组，没有上述的操作，只能对其使用分片和索引的操作。

基本操作如下演示

```python
list = []
list.append(1)
list.append(2)
print(list)

print(list.count(2))

list.extend([1,2,3,4,5])
print(list)

print(list[5])
list.insert(2, 6)
print(list)

list.pop(2)
print(list)

list.remove(5)
print(list)

list.reverse()
print(list)

list.sort()
print(list)

tuple = (1,2,3,4)
print(tuple)

list.insert(4, tuple)
print(list)

print(list[4])
print(list[1:4])
print(tuple[3])
print(tuple[1:-1])  

```
