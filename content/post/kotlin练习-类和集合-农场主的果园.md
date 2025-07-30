+++
date = '2025-07-30T13:38:30.589977+08:00'
draft = false
title = 'kotlin练习 - 类和集合(农场主的果园)'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1709200527/walkerfree/kotlin-mobile-application-programming-language-600nw-1466263208.webp'
categories = [
    "技术",

]

tags = [
    "Kotlin",

]
+++

在软件开发领域，技术的更新迭代速度日新月异。作为一名程序员，不断学习新技术、新语言是必不可少的。而在这个快速发展的时代，Kotlin作为一门现代化、功能丰富的编程语言，正在迅速崭露头角并受到越来越多开发者的青睐。 Kotlin不仅是一种与Java完全兼容的语言，还具备了许多Java所不具备的特性，如空安全、函数式编程支持、扩展函数等。这些特性使得Kotlin在Android开发、服务器端编程、Web开发等领域都有着广泛的应用前景。因此，掌握Kotlin不仅可以让你更高效地开发应用，还能提升你在职场中的竞争力。

- 学习永无止境，最近我在学习kotlin

农场种了很多水果，苹果，梨，橘子，香蕉

* 苹果的英文名字叫做Apple
* 梨的英文名字叫做Pear
* 橘子的英文名字叫做Orange
* 香蕉的英文名字叫做Banana

农场主为了售卖水果，给每个水果进行了定价

* 苹果的价格是15元一斤
* 梨的价格是16元一斤
* 橘子的价格是18元一斤
* 香蕉的价格是20元一斤

```java

data class Fruit (
    val title: String,
    val description: String? = null,
    val eatTime: String,
    val price: Int
)
```

有一天农场主发现一个苹果熟了，于是取下来一个苹果

```java

fun main() {
    val apple = Fruit(
        title = "Apple",
        description = "A Red Apple",
        eatTime = "Evening",
        price = 15
    )

    println(apple)
}
```

```java

Fruit(title=Apple, description=A Red Apple, eatTime=Evening, price=15)
```

农场主决定晚上吃这个苹果，不过农场主希望上午和下午也能吃到水果

```java

enum class Time {
    MORNING,
    AFTERNOON,
    EVENING
}

data class Fruit(
    val title: String,
    val description: String? = null,
    val eatTime: Time,
    val price: Int
)

fun main() {
    val apple = Fruit(
        title = "Apple",
        description = "A Red Apple",
        eatTime = Time.EVENING,
        price = 15
    )

    println(apple)
}
```

```java

Fruit(title=Apple, description=A Red Apple, eatTime=EVENING, price=15)
```

没过多久农场主发现除了苹果熟了，梨、橘子、香蕉也熟了，于是找来一个箱子，将这几个水果全放了进去

```java

fun main() {
    val apple = Fruit(
        title = "Apple",
        description = "A Red Apple",
        eatTime = Time.EVENING,
        price = 15
    )

    val  pear = Fruit(
        title = "Pear",
        description = "A Small Pear",
        eatTime = Time.MORNING,
        price = 16
    )

    val orange = Fruit(
        title = "Orange",
        description = "A Big Orange",
        eatTime = Time.EVENING,
        price = 18
    )

    val banana = Fruit(
        title = "Banana",
        description = "A Yellow Banana",
        eatTime = Time.AFTERNOON,
        price = 20
    )

    val fruits = mutableListOf(apple, pear, orange, banana)

    println(fruits)
}
```

```bash

[Fruit(title=Apple, description=A Red Apple, eatTime=EVENING, price=15), Fruit(title=Pear, description=A Small Pear, eatTime=EVENING, price=16), Fruit(title=Orange, description=A Big Orange, eatTime=EVENING, price=18), Fruit(title=Banana, description=A Yellow Banana, eatTime=AFTERNOON, price=20)]
```

有一天农场主想吃价格18元的水果

```java

val priceFruit = fruits.filter {
    it.price == 18
}

println(priceFruit)
```

```java

[Fruit(title=Orange, description=A Big Orange, eatTime=EVENING, price=18)]
```

有一天农场主想要吃下午安排吃的水果

```java

val groupByFruits = fruits.groupBy { it.eatTime }

println(groupByFruits[Time.AFTERNOON])
```

```bash

[Fruit(title=Banana, description=A Yellow Banana, eatTime=AFTERNOON, price=20)]
```

一天周日，农场主的小孙子来到他家里，发现箱子里面好多的水果，就问哪些水果比较贵，哪些水果比较便宜  
 于是拿了一个苹果去问农场主爷爷

```java

val Fruit.priceOfFruit: String
    get() = if (this.price > 17) {
        "expensive"
    } else {
        "cheap"
    }

println(fruits[0].priceOfFruit)
```

```bash

cheap
```

希望本记录能够成为你学习Kotlin的良师益友，陪伴你在编程之路上不断前行，实现自己的编程梦想。愿你在学习Kotlin的旅程中收获知识、收获成长、收获快乐！
