+++
date = '2025-07-28T17:05:48.678184+08:00'
draft = false
title = 'Python 入门基础知识 - 数据结构与算法 - 图'
categories = [
    "技术",

]

tags = [
    "Python",
    "数据结构"
]
+++

**图**

图也是非线性的数据结构，是由顶点和边组成的。如果图中的顶点是有序的，那么图是有方向的，称之为有向图，


否则，图是无方向的，称之为无向图。在图中，由顶点组成的序列称为路径。

图和树相比，少了树明显的层次结构。在Python中可以采用字典的方式来创建图，图中的每个元素是字典中的键，该元素所指向的图中其他元素则组成键的值。同树一样，对于图来说也可以对其进行遍历。除了遍历外，可以在图中搜索所有的从一个顶点到另一个定点的路径。图中的顶点可以看做是城市，路径可以看做是城市到城市之间的公路。因此，通过搜索所有的路径，可以找到一个顶点到另一个顶点的最短路径，即城市到城市间的最短路线。

如下代码所示，使用字典的方法构建了有向图，并搜索图中的路径。

```py
# _*_ coding: utf-8 -*-
# version 2.7.13

def searchGraph(graph, start, end):  # 搜索树
    results = []  # 路径列表
    generatePath(graph, [start], end, results)  # 生成路径
    results.sort(lambda x, y: cmp(len(x), len(y)))  # 按路径长短排序
    return results

def generatePath(graph, path, end, results):  # 生成路径
    state = path[-1]
    if state == end:
        results.append(path)
    else:
        for arc in graph[state]:
            if arc not in path:
                generatePath(graph, path + [arc], end, results)

if __name__ == '__main__':
    Graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['D', 'F'],
        'D': ['B', 'E', 'G'],
        'E': [],
        'F': ['D', 'G'],
        'G': ['E']
    }

    r = searchGraph(Graph, 'A', 'D')  # 搜索A到D的路径
    print('*******************************')
    print('         A TO D                ')
    print('*******************************')

    for i in r:
        print(i)

    r = searchGraph(Graph, 'A', 'E')  # 搜索A到E的路径
    print('*******************************')
    print('         A TO E                ')
    print('*******************************')

    for i in r:
        print(i)

    r = searchGraph(Graph, 'C', 'E')  # 搜索C到E的路径
    print('*******************************')
    print('         C TO E                ')
    print('*******************************')

    for i in r:
        print(i)  

```

运行的结果如下

```bash
*******************************
         A TO D
*******************************
['A', 'D']
['A', 'C', 'D']
['A', 'C', 'F', 'D']
*******************************
         A TO E
*******************************
['A', 'B', 'E']
['A', 'D', 'E']
['A', 'C', 'D', 'E']
['A', 'D', 'B', 'E']
['A', 'D', 'G', 'E']
['A', 'C', 'D', 'B', 'E']
['A', 'C', 'D', 'G', 'E']
['A', 'C', 'F', 'D', 'E']
['A', 'C', 'F', 'G', 'E']
['A', 'C', 'F', 'D', 'B', 'E']
['A', 'C', 'F', 'D', 'G', 'E']
*******************************
         C TO E
*******************************
['C', 'D', 'E']
['C', 'D', 'B', 'E']
['C', 'D', 'G', 'E']
['C', 'F', 'D', 'E']
['C', 'F', 'G', 'E']
['C', 'F', 'D', 'B', 'E']
['C', 'F', 'D', 'G', 'E']  

```
