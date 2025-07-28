+++
date = '2025-07-28T17:05:42.936442+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 二叉树遍历'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**二叉树遍历**

按照先左后右，树的遍历方法有3种：

先序遍历、中序遍历、后序遍历。其中，先序遍历的次序是：如果二叉树不为空，则访问根节点，然后访问左子树，最后访问右子树；否则，程序退出。中序遍历的次序是：如果二叉树不为空，则先访问左子树，然后范文根节点，最后访问右子树；否则，程序退出。后序遍历的次序依次是：如果二叉树不为空，则先访问左子树，然后访问右子树，最后访问根节点。

代码实例演示如下

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

def preorder(node):  # 先序遍历
    if node.data:
        node.show()
        if node.left:
            preorder(node.left)

        if node.right:
            preorder(node.right)

def inorder(node):  # 中序遍历
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()

        if node.right:
            inorder(node.right)

def postorder(node):
    if node.data:
        if node.left:
            postorder(node.left)
        if node.right:
            postorder(node.right)

        node.show()

if __name__ == "__main__":
    Root = BTree('Root')
    A = Root.insertLeft('A')
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = Root.insertRight('B')
    E = B.insertRight('E')

    print('*********************************')
    print('Binary Tree Pre Order')
    print('*********************************')
    preorder(Root)

    print('*********************************')
    print('Binary Tree In Order')
    print('*********************************')
    inorder(Root)

    print('*********************************')
    print('Binary Tree Post Order')
    print('*********************************')
    postorder(Root)  

```

**运行后结果如下**

```bash
*********************************
Binary Tree Pre Order
*********************************
Root
A
C
D
F
G
B
E
*********************************
Binary Tree In Order
*********************************
C
A
F
D
G
Root
B
E
*********************************
Binary Tree Post Order
*********************************
C
F
G
D
A
E
B
Root
```
