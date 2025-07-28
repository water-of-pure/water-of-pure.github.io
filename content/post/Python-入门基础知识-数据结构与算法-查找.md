+++
date = '2025-07-28T17:05:52.758040+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 查找'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**查找与排序**

查找和排序是最基本的算法。在很多脚本中都会用到查找和排序，在前边的文章中，多次使用Python的函数查找字符串中的子字符串。尽管Python提供了用户查找和排序的函数能够满足绝大多数需求，但还是有必要了解最基本的查找和排序算法。

**查找**

基本的查找方法有顺序查找、二分查找和分块查找。其中，顺序查找是最简单的查找方法，就是按数据排列的顺序依次查找，直到找到所查找的数据为止。二分查找是首先对要进行查找的数据进行排序，有按大小顺序排好的9个数字，如下图

![Image](https://cdn.xiaorongmao.com/up/108-1.png)

如果要查找数字5，首先与中间值10进行比较，5小于10，于是对序列的前半部分1~9进行查找。此时，中间值为5，恰好为要找的数字，查找结束。

分块查找是顺序查找和二分查找之间的一种查找方法。使用分块查找时首先对查找表建立一个索引表，再进行分块查找。建立索引表时，首先对查找表进行分块，要求"分块有序"，即块内关键字不一定有序，但分块之间有大小顺序。索引表是抽取各块中的最大关键字及起始位置构成的，如下图

![Image](https://cdn.xiaorongmao.com/up/108-2.png)

分块查找分两步进行，首先查找索引表，因为索引表是有序的，查找索引表时可以使用二分查找。查找完索引表以后，就确定了要查找的数据所在的分块，然后在改分块中进行顺序查找。

实例演示代码如下

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

def binary_search(l, key):  # 二分查找
    low = 0
    high = len(l) - 1
    i = 0
    while (low <= high):
        i = i + 1
        mid = (high + low) / 2
        if (l[mid] < key):
            low = mid + 1
        elif (l[mid] > key):
            high = mid - 1
        else:
            print('use %d time(s)' % i)
            return mid
    return -1

if __name__ == '__main__':
    l = [1, 5, 6, 9, 10, 51, 62, 65, 70]  # 构造列表
    print(binary_search(l, 5))  # 在列表中查找
    print(binary_search(l, 10))
    print(binary_search(l, 65))
    print(binary_search(l, 70))  

```

运行结果如下

```bash
use 2 time(s)
1
use 1 time(s)
4
use 3 time(s)
7
use 4 time(s)
8
```
