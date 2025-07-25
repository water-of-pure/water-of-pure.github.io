+++
date = '2025-07-25T15:09:59.609177+08:00'
draft = false
title = 'Python 入门基础知识 - pdb调试命令'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**pdb调试命令**

前几篇文章已经使用了部分pdb的调试命令与被调试的脚本进行交互。pdb中的调试命令可以完成单步执行、打印变量值、设置断点等功能。

pdb的部分调试命令如下

> 完整命令 | 简写命令 | 描述
>
> args | a | 打印当前函数的参数
>
> break | b | 设置断点
>
> clear | cl | 清楚断点
>
> condition | 无 | 设置条件断点
>
> continue | c或者cont | 继续运行，直到遇到断点或者脚本结束
>
> disable | 无 | 禁用断点
>
> help | h | 查看pdb帮助
>
> ignore | 无 | 忽略断点
>
> jump | j | 跳转到指定行数运行
>
> list | l | 列出脚本清单
>
> next | n | 执行下条语句，遇到函数不进行其内部
>
> p | p | 打印变量值，也可以用print
>
> quit | q | 退出pdb
>
> return | r 一直运行到函数返回
>
> tbreak | 无 | 设置临时断点，断点只中断一次
>
> step | s | 执行下一条语句，遇到函数进入其内部
>
> where | w | 查看所在的位置
>
> ! | 无 | 在pdb中执行语句

以下实例通过命令行启动pdb对脚本机型调试。如下所示

```bash
$ python -m pdb pdb_test.py
> /Users/durban/python/practise/pdb_test.py(4)<module>()
-> import math
(Pdb) list # 先停在这里，前边有"(Pdb)"提示符，输入list命令
  1     # _*_ coding: utf-8 -*- # list命令默认只列出前11行
  2     # version 2.7.13
  3     #
  4  -> import math
  5
  6
  7     def isprime(i):
  8         for t in range(2, int(math.sqrt(i)) + 1):
  9             if i % t == 0:
 10                 return 0
 11             return 1
(Pdb) n
> /Users/durban/python/practise/pdb_test.py(7)<module>()
-> def isprime(i):
(Pdb) l 14, 17 # 使用list命令列出14到17行的脚本内容
 14     print('打印100-110之间的素数有：')
 15
 16
 17     for i in range(100, 110):
(Pdb) b 14 # 使用b在第14行设置断点
Breakpoint 1 at /Users/durban/python/practise/pdb_test.py:14 # 返回断点编号1
(Pdb) b isprime # 在函数isprime上设置断点
Breakpoint 2 at /Users/durban/python/practise/pdb_test.py:7 # 返回断点编号2
(Pdb) c # 使用c命令运行脚本
> /Users/durban/python/practise/pdb_test.py(14)<module>() # 停在断点1处，即第14行
-> print('打印100-110之间的素数有：')
(Pdb) c # 使用c命令继续运行脚本
打印100-110之间的素数有： # 第14行脚本输出
> /Users/durban/python/practise/pdb_test.py(8)isprime() # 停在断点2处，即isprime函数处
-> for t in range(2, int(math.sqrt(i)) + 1):
(Pdb) b 17 # 在17行设置断点
Breakpoint 3 at /Users/durban/python/practise/pdb_test.py:17 # 返回断点编号3
(Pdb) disable 2 # 禁用断点2，即isprime函数处的断点
(Pdb) c # 继续运行脚本
> /Users/durban/python/practise/pdb_test.py(17)<module>() # 停在断点3处，即第15行
-> for i in range(100, 110):
(Pdb) print i # 使用print打印变量i的值
100
(Pdb) print(i)
100
(Pdb) c # 继续运行断点
101
> /Users/durban/python/practise/pdb_test.py(17)<module>() # 停在断点3处，即第17行
-> for i in range(100, 110):
(Pdb) p i # 使用p打印变量i的值
101
(Pdb) enable 2 # 恢复断点2，即isprime函数处的断点
(Pdb) c # 继续运行脚本
> /Users/durban/python/practise/pdb_test.py(8)isprime() # 停在断点2处，即isprime函数处的断点
-> for t in range(2, int(math.sqrt(i)) + 1):
(Pdb) n # 单步执行下一语句
> /Users/durban/python/practise/pdb_test.py(9)isprime()
-> if i % t == 0: # 停在下一语句处
(Pdb) p t # 使用p打印变量t的值
2
(Pdb) cl # 清楚所有断点，输入y确认
Clear all breaks? y
(Pdb) c # 继续运行脚本
103
105
107
109
The program finished and will be restarted # 脚本运行结束，回到开始处
> /Users/durban/python/practise/pdb_test.py(4)<module>()
-> import math
(Pdb) q # 使用q命令退出pdb  

```

pdb\_test.py文件代码如下：

```py
# _*_ coding: utf-8 -*-
# version 2.7.13
#
import math

def isprime(i):
    for t in range(2, int(math.sqrt(i)) + 1):
        if i % t == 0:
            return 0
        return 1

print('打印100-110之间的素数有：')

for i in range(100, 110):
    if isprime(i):
        print(i)

```

实例环境如下

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13

```
