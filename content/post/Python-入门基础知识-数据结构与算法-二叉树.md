+++
date = '2025-07-28T17:05:39.708776+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 二叉树'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**二叉树**

二叉树是一类比较特殊的数，在二叉树中每个节点最多只有两个儿子，分为左和右

相对于树而言，二叉树的构建和使用都要简单的多，而且任何一棵树，都可以通过变换转换成一颗二叉树。

在Python中，二叉树的构建和树一样，可以使用列表或者类的方式。由于二叉树中的节点具有确定的儿子数，

因此，使用类的方式要更为简便。代理实例演示如下

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

class BTree:  # 二叉树节点

    def __init__(self, value):  # 初始化函数
        self.left = None  # 左儿子
        self.data = value  # 节点值
        self.right = None  # 右儿子

    def insertLeft(self, value):  # 向左子树中插入节点
        self.left = BTree(value)
        return self.left

    def insertRight(self, value):  # 向右子树中插入节点
        self.right = BTree(value)
        return self.right

    def show(self):  # 输出节点数据
        print(self.data)

if __name__ == "__main__":
    Root = BTree('Root')
    A = Root.insertLeft('A')
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = Root.insertRight('B')
    E = B.insertRight('E')
    Root.show()
    Root.left.show()
    Root.right.show()
    A = Root.left
    A.left.show()
    Root.left.right.show()  

```

运行后输出结果如下

```bash
Root
A
B
C
D  

```

当创建好一颗二叉树后，可以按照一定的顺序对树中所有的元素进行遍历。按照先左后右，树的遍历方法有3种：

先序遍历、中序遍历、后序遍历。其中，先序遍历的次序是：如果二叉树不为空，则访问根节点，然后访问左子树，

最后访问右子树；否则，程序退出。中序遍历的次序是：如果二叉树不为空，则先访问左子树，然后范文根节点，

最后访问右子树；否则，程序退出。后序遍历的次序依次是：如果二叉树不为空，则先访问左子树，然后访问右子树，

最后访问根节点。

遍历的方式我们下篇文章继续概述。
