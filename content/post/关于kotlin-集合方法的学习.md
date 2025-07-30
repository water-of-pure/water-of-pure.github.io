+++
date = '2025-07-30T13:38:26.879142+08:00'
draft = false
title = '关于kotlin 集合方法的学习'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1709200527/walkerfree/kotlin-mobile-application-programming-language-600nw-1466263208.webp'
categories = [
    "技术",

]

tags = [
    "Kotlin",

]
+++

在软件开发领域，技术的更新迭代速度日新月异。作为一名程序员，不断学习新技术、新语言是必不可少的。而在这个快速发展的时代，Kotlin作为一门现代化、功能丰富的编程语言，正在迅速崭露头角并受到越来越多开发者的青睐。

Kotlin不仅是一种与Java完全兼容的语言，还具备了许多Java所不具备的特性，如空安全、函数式编程支持、扩展函数等。这些特性使得Kotlin在Android开发、服务器端编程、Web开发等领域都有着广泛的应用前景。因此，掌握Kotlin不仅可以让你更高效地开发应用，还能提升你在职场中的竞争力。

- 学习永无止境，最近我在学习kotlin

学习之前创建一个Friuts的类

```java

class Friut(
    val name: String,
    val price: Double
)

val friuts = listOf(
    Friut(
    	name = "apple",
        price = 1.0
    ),
    Friut(
    	name = "juice",
        price = 1.5
    ),
    Friut(
    	name = "pear",
        price = 2.5
    ),
    Friut(
    	name = "watermelon",
        price = 2.0
    ),
    Friut(
    	name = "banana",
        price = 3.0
    ),
)
```

**forEach**

```java

fun main() {
    friuts.forEach {
        println("Menu item: ${it}")
    }
}
```

```java

fun main() {
    friuts.forEach {
        println("Menu item: ${it.name}")
    }
}
```

**map**

```java

fun main() { 
    val fullFriuts = friuts.map {
        "${it.name} - $${it.price}"
    }

    fullFriuts.forEach {
        println("${it}")
    }
}
```

上面的例子将一个集合转换为另一个集合，另一个集合可以按照自己定义的格式来组合字符串

**filter**

```java

fun main() {
    val fullFriuts = friuts.filter {
        it.name == "apple"
    }

    fullFriuts.forEach {
        println("${it.name} - $${it.price}")
    }
}
```

上面的例子将一个集合转换为一个集合的子集合

**groupBy**

```java

fun main() {
    val fullFriuts = friuts.groupBy {
        it.price % 2 == 0.0
    }

    println("price % 2 != 0.0:")

    (fullFriuts[false] ?: listOf()).forEach {
        println("${it.name} - $${it.price}")
    }

    println("price % 2 == 0.0:")

    (fullFriuts[true] ?: listOf()).forEach {
        println("${it.name} - $${it.price}")
    }
}
```

上面的例子将一个集合根据条件进行了分组，分成了两个集合

**fold**

```java

fun main() {
    val fullFriuts = friuts.fold(0.0) { total, cookie ->
        total + cookie.price
    }

    println("Total price: ${fullFriuts}")
}
```

上面的例子将一个集合的price字段进行累加，计算出所有的price的和

```java

fun main() {
    val fullFriuts = friuts.fold("") { total, cookie ->
        total + " " + cookie.name
    }

    println("all friuts: ${fullFriuts}")
}
```

上面的例子将一个集合的name字段进行拼接，拼接出所有的name

**sortedBy**

```java

fun main() {
    val fullFriuts = friuts.sortedBy { 
        it.name
    }

    fullFriuts.forEach {
    	println("${it.name}") 
    }
}
```

上面的例子将一个集合按照name字段进行排序，生成一个新的集合

希望本记录能够成为你学习Kotlin的良师益友，陪伴你在编程之路上不断前行，实现自己的编程梦想。愿你在学习Kotlin的旅程中收获知识、收获成长、收获快乐！
