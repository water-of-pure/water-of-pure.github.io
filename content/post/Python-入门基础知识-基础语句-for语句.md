+++
date = '2025-07-24T10:41:15.906471+08:00'
draft = false
title = 'Python 入门基础知识 - 基础语句 - for语句'
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

**for 语句**

for 语句是Python中的循环控制语句。for语句可以使用循环遍历某一个对象，它还具有一个附带的else块。附带的else块是可选的，

主要用于处理for语句中包含的break语句。如果for循环未被break终止，则会执行else块中语句。for语句中的break语句，可以在

需要的时候终止for循环。在for语句中还可以使用continue语句。continue语句语句可以逃过位于其后的语句，开始下一轮循环。

for语句的格式如下：

```py
for <> in <对象集合>:
	if <条件>:
		break
	if <条件>:
		continue
	<其他语句>	
else:
	<语句>
```

完整的例子如下

```py
for i in [1,2,3,4,5,6,7,8]:
	if i == 6:
		break;
	if i == 2:
		continue
	print i
else:
	print 'all'  

```

for语句中的对象集合可以是列表、字典以及元组等。也可以通过range()函数产生一个整数列表，已完成计数循环。

range()函数原型如下

> range([start], stop[, step])
>
> start 可选参数， 起始数
>
> stop 终止数，如果range只要一个参数x,则range产生一个从0至x-1的整数列表。
>
> step 可选参数，步长

完整例子如下

```py
for i in range(1, 5 + 1):
	print i
```

以下实例遍历一个字典

```py
people = { 'apple': 6, 'orange': 3, 'banana': 4 }
for name in people:
	print name, people[name]
```

for循环中，除了循环的对象是元组以外，循环的目标也可以是元组，可以在循环的过程中对元组进行赋值等操作。

```py
t = ( ('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h'))
for i in t:
	print i
for (x, y) in t:
	print x, y
```

# 来一个比较复杂的实例，求解50至100之间的全部素数

```py
import math	# 导入math模块，以使用求平方根的函数
for i in range(50, 100 + 1):	# 遍历50到100
	for t in range(2, int(math.sqrt(i)) + 1): # 从2到i的平方根， 此处使用int转为整数
		if i % t == 0:	# 判断i是否能被2到i的平方根整除，能则终止，即i不是素数
			break;
	else:
		print i # 如果循环没有被break终止，即i为素数，打印i
```
