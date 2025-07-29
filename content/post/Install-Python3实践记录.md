+++
date = '2025-07-29T10:55:54.982580+08:00'
draft = false
title = 'Install Python3实践记录'
categories = [
    "技术",

]

tags = [
    "Python3",

]
+++

2019年了，在使用python2的时候，偶尔会发现python2将被deprecated，将被弃用了。那么为了能够使用新的包，跟着大众的步伐，安装python3是个不可以少的环节了。下面记录下我的安装以及使用python3的一些记录。

服务器: centos 7 当前python版本: 2.7.5

## 下载安装包

go to webpage <https://www.python.org/downloads/release/python-374/>

```bash

wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz 

```

## 简单安装

使用超级用户身份登录，比如 root，然后参考下面的方式安装python3

```bash

tar zxvf Python-3.7.4
cd Python-3.7.4
./configure
make && make install

```

---

### 遇到的问题一

> Traceback (most recent call last):
>
> File "/root/Python-3.7.4/Lib/runpy.py", line 193, in \_run\_module\_as\_main
>
> ```bash
> 
> "__main__", mod_spec)
>
> ```
>
> File "/root/Python-3.7.4/Lib/runpy.py", line 85, in \_run\_code
>
> ```bash
> 
> exec(code, run_globals)
>
> ```
>
> File "/root/Python-3.7.4/Lib/ensurepip/**main**.py", line 5, in
>
> ```bash
> 
> sys.exit(ensurepip._main())
>
> ```
>
> File "/root/Python-3.7.4/Lib/ensurepip/**init**.py", line 204, in \_main
>
> ```bash
> 
> default_pip=args.default_pip,
>
> ```
>
> File "/root/Python-3.7.4/Lib/ensurepip/**init**.py", line 117, in \_bootstrap
>
> ```bash
> 
> return _run_pip(args + [p[0] for p in _PROJECTS], additional_paths)
>
> ```
>
> File "/root/Python-3.7.4/Lib/ensurepip/**init**.py", line 27, in \_run\_pip
>
> ```bash
> 
> import pip._internal
>
> ```
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/**init**.py", line 40, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/cli/autocompletion.py", line 8, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/cli/main\_parser.py", line 12, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/commands/**init**.py", line 6, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/commands/completion.py", line 6, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/cli/base\_command.py", line 20, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/download.py", line 37, in
>
> File "/tmp/tmpo8g\_7brw/pip-19.0.3-py2.py3-none-any.whl/pip/\_internal/utils/glibc.py", line 3, in
>
> File "/root/Python-3.7.4/Lib/ctypes/**init**.py", line 7, in
>
> ```bash
> 
> from _ctypes import Union, Structure, Array
>
> ```
>
> ModuleNotFoundError: No module named '\_ctypes'
>
> make: \*\*\* [install] 错误 1

### 解决方法

```bash

yum update
yum install libffi-devel
```
