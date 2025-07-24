+++
date = '2025-07-24T10:41:12.266794+08:00'
draft = false
title = 'Python 入门基础知识 - 基础语句 - if语句'
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

**if 语句**

if 语句是基本的条件测试语句，用来判断可能遇到的不同情况，并针对不同的情况进行操作。

```py
if <条件>:		# 当条件为真时，执行缩进的语句，当条件为假时判断elif的条件
	<语句>		# 要用缩进来表示语句处于if语句之中
elif <条件>:		# 当条件为真时，执行缩进的语句，当条件为假时执行else
	<语句>		# 要用缩进来表示语句处于elif语句之中
else:			# 当前边的所有的条件都为假时，则执行下面的缩进语句
	<语句>		# 要用缩进来表示语句处于else语句之中
```

在条件语句中主要使用如下比较运算符

```py
a == b		# a 与 b是否相等，是则返回真，否则返回假
a != b 		# a 与 b是否不相等，是则返回真，否则返回假
a > b 		# a 是否大于 b，是则返回真，否则返回假
a < b 		# a 是否小于 b，是则返回真，否则返回假
a >= b 		# a 是否大于等于 b，是则返回真，否则返回假
a <= b 		# a 是否小于等于 b，是则返回真，否则返回假
```

以上比较运算符，可以用户数字、字符串、列表、元组、以及字典等。除了上述的比较运算符以外，

在条件中也可以使用逻辑运算，以及一些其他的语句。

下面做些实例演示

```py
a = 1
b = 2
if a == b:
	print 'true'
else:
	print 'false'

if a < b:
	print 'true'
else:
	print 'false'

m = 'hi'
n = 'hello'

if m == n:
	print 'true'
else:
	print 'false'

if m < n:
	print 'true'
elif m > n:
	print 'false'
else:
	print m,n

l1 = [1,2]
l2 = [3,4]

if l1 == l2:
	print 'true'
else:
	print 'false'

if l1 <= l2:
	print 'true'

if not 1:
	print 'true'
else:
	print 'false'  

```

if语句中可以嵌套其他的if语句，被包含的if语句要用缩进来表示自己所包含的语句。

这是Python独特的语法，而不像其他语言使用一对大括号'{}'来表示一个语句块，这样可以使

脚本看起来更清晰，但是编程过程中容易被忽略缩进，而导致程序语法错误，或者导致结果出错。

在编写Python脚本是最好使用具有自动缩进功能的编辑器，保证程序正确缩进，减少敲击键盘的次数。

if语句嵌套结果如下

```py
if <条件>:
	if <条件>:
		<语句>
	else:
		<语句>
elif <条件>:
	if <条件>:
		<语句>
	else:
		<语句>
else:
	<语句>  

```
