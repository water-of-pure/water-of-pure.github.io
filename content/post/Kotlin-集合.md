+++
date = '2025-07-30T13:38:21.586732+08:00'
draft = false
title = 'Kotlin 集合'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1709200527/walkerfree/kotlin-mobile-application-programming-language-600nw-1466263208.webp'
categories = [
    "技术",

]

tags = [
    "Kotlin",

]
+++

Kotlin 集合

集合有以下常用的几个类型

**Array**

```Kotlin

val friuts = arrayOf<String>("apple", "banana", "juice")

val numbers = arrayOf<Number>(1, 2, 3, 4)
```

Array的相关功能

查看元素

```Kotlin

friuts[2]

numbers[3]
```

**Lists**

创建Lists

```Kotlin

val friuts = listOf("apple", "banana", "pear")
val numbers = listOf(1, 2, 3, 4)
```

查看大小

```Kotlin

friuts.size
```

查看元素

```Kotlin

friuts.get(2)
```

查看元素索引

```Kotlin

friuts.indexOf("apple")
```

查看所有元素

```Kotlin

for (friut in friuts) {
    println(friut)
}
```

要修改元素的话需要用mutableListOf创建元素

```Kotlin

val friuts = mutableListOf("apple", "banana", "pear")
```

添加元素

```Kotlin

fruits.add("juice")
```

更新元素

```Kotlin

friuts[1] = "juice1"
```

移除元素

```Kotlin

friuts.remove("juice")

friuts.removeAt(1)
```

包含元素

```Kotlin

friuts.contains("juice")

"juice" in friuts
```

**Sets**

创建Sets

```Kotlin

val friuts = mutableSetOf("apple", "banana", "pear")
```

查看大小

```Kotlin

friuts.size
```

添加元素

```Kotlin

fruits.add("juice")
```

包含元素

```Kotlin

friuts.contains("juice")
```

移除元素

```Kotlin

friuts.remove("juice")
```

**Map集合**

创建map

```Kotlin

val friuts = mutableMapOf(
    "apple" to 1,
    "banana" to 2,
    "juice" to 3
)
```

查看大小

```Kotlin

friuts.size
```

查看元素

```Kotlin

friuts["apple"]
```

移除元素

```Kotlin

friuts.remove("juice")
```

修改元素

```Kotlin

friuts["apple"] = 10
```

**Lists** 用于元素列表是大小可变，元素可变，而且有序的情况

**Sets** 用于元素不能重复，而且元素是无序的情况

**Map集合** 用于元素是键值对的情况
