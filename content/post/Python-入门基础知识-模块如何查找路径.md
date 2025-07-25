+++
date = '2025-07-25T14:09:59.114596+08:00'
draft = false
title = 'Python 入门基础知识 - 模块如何查找路径'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**模块如何查找路径**

编写好的模块的只有被Python找到才能被导入，上一篇文章中编写的模块以及调用模块的脚本位于同一个目录中。

如果在该目录中建立一个module目录，并且把testmodule.py移到module目录中，再次运行usermodule.py,会得到类似如下提示

```bash
Traceback (most recent call last):
  File "usemodule.py", line 2, in <module>
    import testmodule
ImportError: No module named testmodule
```

脚本运行出错，Python解释器没有找到testmodule模块。在导入模块时，Python解释器首先在当前目录中

查找导入的模块。如果未找到模块，Python解释器会从sys模块中的path变量指定的目录查找导入模块。

如果在以上所有目录中均未找到导入的模块，则会报错。

下面使用sys.path输出Python的模块查找路径

```py
import sys
print(sys.path)
```

会得到类似如下的输出

```bash
['/Users/durban/python/practise',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
'/usr/local/lib/python2.7/site-packages',
'/usr/local/Cellar/protobuf/3.2.0/libexec/lib/python2.7/site-packages']  

```

在脚本中可以向sys.path加入模块查找路径。如下

```py
import os
import sys
modulepath = os.getcwd() + '/module'
sys.path.append(modulepath)
print(sys.path)
import testmodule
testmodule.show()
print(testmodule.name)
testmodule.name = 'usemodule.py'
print(testmodule.name)  

```

会得到类似如下输出

```bash
['/Users/durban/python/practise',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
'/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
'/usr/local/lib/python2.7/site-packages',
'/usr/local/Cellar/protobuf/3.2.0/libexec/lib/python2.7/site-packages',
'/Users/durban/python/practise/module']
我是一个模块
testmodule.py
usemodule.py  

```

从输出可以看到，当前路径也被添加到了sys.path路径列表中，这说明Python其实是按照sys.path中的路径来查找模块的。

之所以首先在当前目录查找，是因为Python解释器在运行脚本的时候将当前目录添加到sys.path路径列表中了。
