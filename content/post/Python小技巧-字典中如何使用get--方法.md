+++
date = '2025-07-30T10:40:29.757225+08:00'
draft = false
title = 'Python小技巧 - 字典中如何使用get()方法'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "字典"
]
+++

字典类型在很多编程语言中都是常用的类型

js中

```javascript

let dict_obj = {
  a: 1,
};
```

如何获取其中的键值

```javascript

console.log(dict_obj["a"] || "");
console.log(dict_obj["b"] || "no value");
```

执行后得到结果如下

```bash

1
no value
```

那么在python中如何实现类似功能

先创建一个字典

```python

name_for_age = {30: "xiaowang", 28: "xiaoli", 32: "xiaozhang"}

def get_age(age):
    return "%d is %s" % (age, name_for_age.get(age, 'no person'))

print(get_age(30))
print(get_age(32))
print(get_age(18))
```

执行后结果如下

```bash

30 is xiaowang
32 is xiaozhang
18 is no person
```

这里用到了get()方法，一个非常方便的取值器
