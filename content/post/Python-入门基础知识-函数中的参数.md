+++
date = '2025-07-25T14:09:36.241092+08:00'
draft = false
title = 'Python 入门基础知识 - 函数中的参数'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**函数中的参数**

在Python中，函数的参数可以有多钟形式。例如某些函数，在其调用时需要向其传递参数，但在使用时，可以不向

其传递参数，依然可以正常调用。在Python中还可以声明一个具有任意个参数的函数。

**函数中的参数 - 参数默认值**

在Python中声明函数时，可以预先声明一个默认的参数值。当调用具有参数值的函数时，可以不向函数传递参数，

而使用声明函数时设置的默认值。

举例如下：

```py
def cube(x=5):
    return x ** 3
print(cube())
print(cube(2))
```

如果一个函数具有多个参数，而且这些参数都具有默认值，在调用函数的时候，传递参数是按照声明函数时参数的

顺序依次传递的。如果在调用的时候仅使用","表示向函数的最后一个参数传递值，会引发错误。如下：

```py
def cube2(x=1, y=2, z=3):
    return (x + y - z) ** 3
# print(cube2( 3, 3 ))      # 这里会正常运行
# print(cube2( , , 3 ))     # 这里会抛出异常
```

异常内容类似如下

>     print(cube2( , , 3 ))
>
>                   ^
>
> SyntaxError: invalid syntax

如果需要向指定的参数传递值可以使用如下方式重新定义函数

```py
def cube3(x=None, y=None, z=None):
    if x is None:
        x = 1
    if y is None:
        y = 2
    if z is None:
        z = 3
    return (x + y - z) ** 3
print(cube3())
print(cube3(None, None, 5))
```

除了使用上面的方法，还可以使用下面的方法，向指定的参数传递值

**函数中的参数 - 参数传递**

在Python中参数值的传递是按照声明函数时参数的顺序进行传递的。

而实际上Python还提供了另外一个传递参数的方法---按照参数名传递值的方法。

以参数名传递参数时类似于设置参数的默认值。使用按参数名传递参数的方式调用函数时，要在函数名后的圆括号里为函数的所有参数赋值。

赋值的顺序不必按照函数声明时的参数顺序。如下

```py
def fun(x, y, z):
    return x + y - z
print(fun(1, 2, 3))
print(fun(z=1, x=2, y=3))
```

在Python中，调用函数可以同时使用按顺序传递参数，以及按参数名传递参数的方式。

但是，要注意按顺序传递参数要位于按参数名传递的参数之前，而且不能有重复的情况。

如下

```py
def fun1(x, y, z):
    return x + y + z
print(fun1(1, z=2, y=3))
```

```py
print(fun1(z = 1, y= 2, 3))   # 错误的方式！按顺序传递的参数不能位于按参数名传递的参数之后
```

这里会报如下错误

>     print(fun1(z = 1, y= 2, 3))
>
> SyntaxError: non-keyword arg after keyword arg

```py
print(fun1(1, z = 2, x = 3))  # 错误的方式！参数重复，1已经传递给x,后面又将3传递给x
```

这里会报错如下

>     print(fun1(1, z = 2, x = 3))
>
> TypeError: fun1() got multiple values for keyword argument 'x'

在具有默认参数值的函数中，使用按参数名向函数中参数传递的方法非常方便。

如果使用按照参数名向函数传递参数的方法，不必在函数的声明时将参数的默认值设置为None,

可以省去函数中的判断语句。为了让函数更具通用性，下面的实例依然将参数的默认值设置为None。

```py
def cube4(x=None, y=None, z=None):
    if x is None:
        x = 1
    if y is None:
        y = 2
    if z is None:
        z = 3
    return (x + y - z) ** 3
print(cube4(z=4))
print(cube4(x=2, z=5))
```

**函数中的参数 - 可变长参数**

在Python中，函数可以具有任个参数，而不必将所有参数定义。使用可变参数的函数，将其所有参数保存在一个元组里，

在函数中可以使用for循环来处理。声明一个可变长参数的函数只需已"\*"开头定义一个参数即可。

代码如下

```py
def my_list_append(*list):
    newList = []
    for i in list:
        newList.extend(i)
    return newList

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print(my_list_append(a, b))
print(my_list_append(a, b, c))  

```

**函数中的参数 - 参数引用**

在Python中可以在参数中使用可变对象，如列表等，来达到改变参数值的目的。如下

```py
def reset_value1(x):
    x = x ** 2

def reset_value2(x):
    x[0] = x[0] ** 2

a = 2
b = [2]
reset_value1(a)  # 这里的改变是不会成功的
print(a)
reset_value2(b)  # 这里的改变成功的
print(b)  

```

以上实例环境声明

# \_\*\_ coding: utf-8 -\*-

# version 2.7.13
