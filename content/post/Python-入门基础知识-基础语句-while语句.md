+++
date = '2025-07-24T10:41:20.981358+08:00'
draft = false
title = 'Python 入门基础知识 - 基础语句 - while语句'
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

**while 语句**

while语句跟for语句是一样的循环控制语句。与for循环不同的是，while语句中只有在测试条件为假时才会停止。

在while的语句块中一定要包含改变条件的语句，以保证循环能够结束，避免死循环的出现。

while语句包含与if语句相同的条件测试语句，如果条件为假，则终止循环。while语句也有一个可选的else语句块。

与for循环中的else语句块一样，当while循环不是由break语句终止的话，则会执行else语句块中的语句。continue

也可以用于while循环中，其作用同if语句中的continue相同，都是跳过continue后的语句，进入下一个循环。

while的一般形式如下所示。

```py
while <条件>:
	if <条件>:
		<语句>
	if <条件>:
		<语句>
	<语句>
else:
	<语句>  

```

while的使用比较简单。但是也是最容易出现问题，如果条件为真会导致死循环，因此在使用while循环时应仔细检查

while语句的条件测试，避免出现死循环。

如下实例

```py
x = 1
while x <= 5:
	print x
	x = x + 1
```

使用while遍历一个列表

```py
list = ['a', 'b', 'c', 'd', 'e', 'f', 'h']
len = len(list)
while len != 0:
	print list[-len]
	len = len - 1
```
