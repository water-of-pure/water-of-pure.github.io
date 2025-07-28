+++
date = '2025-07-28T17:05:57.935999+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 排序'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**排序**

排序相对于查找来说要复杂的多，排序的方法也较多，有冒泡排序、希尔排序、二叉树排序和快速排序等，其中二叉树排序是比较有意思的一种排序方法，而且也便于操作。二叉树排序的过程主要是二叉树的建立和遍历的过程。例如有一组数据"3,5,7,20,44,2,15,30"，则二叉树的建立过程如下

1、首先将第一个数据3放如根节点

2、将数据5与节点中的数据3比较，由于5大于3，则将5放入3的右子树中

3、将数据7与根节点中的数据3比较，由于7大于3，则将7放入3的右子树中，由于2已经有右子树5，将7与5比较，因为7大于5，则将7放入5的有子树中。

4、将数据20与根节点3进行比较，由于20大于3，则将7放入3的右子树中，重复比较，最终将20放入7的右子树中

5，将数据44与树中的节点值进行比较，最终将其放入20的右子树中

6、将数据2与根节点3比较，由于2小于3，则将2放入3的左子树中

7、同样的对数据15和30进行处理，最终形成如下图的树

![Image](https://cdn.xiaorongmao.com/up/109-1.png)

当树创建好后，对树进行中序遍历后的结果就是对数据从小到大的排序。如果要从大到小进行排序，则可以先从右子树开始进行中序遍历。

实例代码演示如下，采用二叉树排序的方式对数据进行排序

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

class BTree:  # 二叉树节点

    def __init__(self, value):  # 初始化函数
        self.left = None  # 左子树
        self.data = value  # 节点值
        self.right = None  # 右子树

    def insertLeft(self, value):  # 向左子树插入节点
        self.left = BTree(value)
        return self.left

    def insertRight(self, value):  # 向右子树插入节点
        self.right = BTree(value)
        return self.right

    def show(self):  # 输出节点数据
        print(self.data)

def inorder(node):
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()

        if node.right:
            inorder(node.right)

def rinorder(node):
    if node.data:
        if node.right:
            rinorder(node.right)
        node.show()

        if node.left:
            rinorder(node.left)

def insert(node, value):
    if value > node.data:
        if node.right:
            insert(node.right, value)
        else:
            node.insertRight(value)

    else:
        if node.left:
            insert(node.left, value)
        else:
            node.insertLeft(value)

if __name__ == '__main__':
    l = [3, 5, 7, 20, 44, 2, 15, 30]
    Root = BTree(l[0])
    node = Root

    for i in range(1, len(l)):
        insert(Root, l[i])

    print('********************************')
    print('            从小到大             ')
    print('********************************')
    inorder(Root)

    print('********************************')
    print('            从大到小             ')
    print('********************************')
    rinorder(Root)  

```

运行结果如下

```bash
********************************
            从小到大
********************************
2
3
5
7
15
20
30
44
********************************
            从大到小
********************************
44
30
20
15
7
5
3
2
```
