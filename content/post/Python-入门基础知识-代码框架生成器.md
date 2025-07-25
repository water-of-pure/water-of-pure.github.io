+++
date = '2025-07-25T15:54:54.724558+08:00'
draft = false
title = 'Python 入门基础知识 - 代码框架生成器'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**代码框架生成器**

编写代码要养成良好的习惯，为了使脚本更具可读性，往往需要添加注释，而且还应该在脚本头添加基本的说明，如作者、文件名、日期、

用途、版本说明。以及所需要使用的模块等信息。这样不仅便于保存脚本，而且也便于交流。

但是，如果每次编写代码写一个脚本就依次添加这样的信息，不免有些麻烦，下面代码简单生成了一个代码框架生成器

```py
# _*_ coding: utf-8 -*-
import os
import sys
import string
import datetime
py = '''# ------------------------------------------------------
# To:
# ------------------------------------------------------
# By:
# ------------------------------------------------------
'''

c = ''' * ------------------------------------------------------
 * To:
 * ------------------------------------------------------
 * By:
 * ------------------------------------------------------
'''

if os.path.isfile(sys.argv[1]):
    print('%s already exist!' % sys.argv[1])
    sys.exit()

file = open(sys.argv[1], 'w')  # 创建文件
today = datetime.date.today()  # 获取当前日期，并格式化为xxxx-xx-xx形式
date = today.strftime('%Y') + '-' + today.strftime('%m') + \
    '-' + today.strftime('%d')
filetypes = string.split(sys.argv[1], '.')  # 判断将创建的文件是什么类型以便对其分别处理
length = len(filetypes)
filetype = filetypes[length - 1]
if filetype == 'py':
    print('use python mode')
    file.writelines('# -*- coding: utf-8 -*-')
    file.write('\n')
    file.writelines('# File: ' + sys.argv[1])
    file.write('\n')
    file.write(py)
    file.write('# Date: ' + date)
    file.write('\n')
    file.write('# ------------------------------------------------------')
    file.write('\n')
elif filetype == 'c' or filetype == 'cpp':
    print('use c mode')
    file.writelines('/*')
    file.write('\n')
    file.writelines(
        ' * ------------------------------------------------------')
    file.write('\n')
    file.writelines(' * File: ' + sys.argv[1])
    file.write('\n')
    file.write(c)
    file.write(' * Date: ' + date)
    file.write('\n')
    file.write(' * ------------------------------------------------------')
    file.write('\n')
    file.write(' */ \n')
else:
    print('just create %s ' % sys.argv[1])

file.close()  

```

这样就可以随时运行，方便在目录中生成Python脚本或c/c++脚本

测试如下

```bash
python generate.py python.py
python generate.py c.c
```

实例环境声明

```bash
# _*_ coding: utf-8 -*-
# version 2.7.13  

```
