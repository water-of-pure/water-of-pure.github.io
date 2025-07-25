+++
date = '2025-07-25T14:10:05.620851+08:00'
draft = false
title = 'Python 入门基础知识 - 模块独立运行-__name__属性及dir()函数'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**模块独立运行-\_\_name\_\_属性**

每个Python脚本在运行时都有一个\_\_name\_\_属性（name前后均是两条下划线）。在脚本中通过

对\_\_name\_\_属性值的判断，可以让脚本在作为导入模块和独立运行时都可以正确运行。在Python

中如果脚本作为模块被导入，则其\_\_name\_\_属性被设置为模块名。如果脚本独立运行，则其\_\_name\_\_属性

被设置为"\_\_main\_\_"。因此可以通过\_\_name\_\_属性来判断脚本的运行状态。

如下所示脚本，既可以自己运行，也可以作为模块被其他脚本导入。

```py
# file：testmodule2.py
def show():
    print 'I am a module!'
if __name__ == '__main__':
    show()
    print 'I am not a module!'
```

建立脚本usemodule2.py，内容如下：

```py
_*_ coding: utf-8 -*-
import testmodule2

testmodule2.show()
print('my __name__ is %s' % __name__)  

```

运行usemodule2.py，输出内容如下：

```bash
I am a module!
my __name__ is __main__  

```

运行testmodule2.py，输出内容如下：

```bash
I am a module!
I am not a module!  

```

**dir()函数**

如果需要获得导入模块中的所有定义的名字、函数等，可以使用内置函数dir()来获得模块所定义的名字的列表。

如下所示代码获得sys模块中的名字。

```py
import sys
print(dir(sys))  

```

输出的内容如下

> ['\_\_displayhook\_\_', '\_\_doc\_\_', '\_\_excepthook\_\_', '\_\_name\_\_', '\_\_package\_\_', '\_\_stderr\_\_', '\_\_stdin\_\_', '\_\_stdout\_\_', '\_clear\_type\_cache', '\_current\_frames', '\_getframe', '\_mercurial', 'api\_version', 'argv', 'builtin\_module\_names', 'byteorder', 'call\_tracing', 'callstats', 'copyright', 'displayhook', 'dont\_write\_bytecode', 'exc\_clear', 'exc\_info', 'exc\_type', 'excepthook', 'exec\_prefix', 'executable', 'exit', 'flags', 'float\_info', 'float\_repr\_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'long\_info', 'maxint', 'maxsize', 'maxunicode', 'meta\_path', 'modules', 'path', 'path\_hooks', 'path\_importer\_cache', 'platform', 'prefix', 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version\_info', 'warnoptions']

dir()函数的原型如下所示。

> dir([object])
>
> 其参数含义如下。
>
> -object 可选参数，要列举的模块名。

如果不向dir()函数传递参数，那么dir()函数将返回当前脚本的所有名字列表，如下所示。

```py
a = [1, 3, 6]
b = 'Python'
print(dir())  

```

输出后的内容如下：

> ['\_\_builtins\_\_', '\_\_doc\_\_', '\_\_file\_\_', '\_\_name\_\_', '\_\_package\_\_', 'a', 'b', 'show', 'sys']

在加入一个函数后，输出试试

```py
def func():
    print 'Python'
print(dir())
```

输出后结果类似如下

> ['\_\_builtins\_\_', '\_\_doc\_\_', '\_\_file\_\_', '\_\_name\_\_', '\_\_package\_\_', 'a', 'b', 'func', 'show', 'sys']
