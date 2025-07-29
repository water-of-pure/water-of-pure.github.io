+++
date = '2025-07-29T10:56:11.650591+08:00'
draft = false
title = 'python升级后，如何给virtualenv里的python进行升级'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

> 如题：virtualenv的python版本是3.6.4，现在装了3.7.4，如何将virtualenv里的版本也更新到3.7.4呢？如果是3.6，那么这种跨大版本的又该如何升级到3.7呢？

这个问题我是这样解决的，其实如果python2的话我觉得是没有必要进行升级，因为使用包可能面临着必须要重新安装的情况，如果溶蚀python3的话就好解决了，从理论上上讲，同一个版本的迭代应该不会有太大的区别，除非改动太大了，这个情况的话，建议重新建立一个virtualenv比较妥当一些。

前提我本地是有一个.env3的虚拟环境的，而且现在里面的python版本指向的是一个3.6的版本

```bash

 '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/Python' -> '/Users/durban/python/.env3/.Python'
```

现在我进行了覆盖式的操作

```bash

virtualenv -p /usr/local/Cellar/python/3.7.4/bin/python3 .env3
```

然后报错了，错误如下

```bash

unning virtualenv with interpreter /usr/local/Cellar/python/3.7.4/bin/python3
Already using interpreter /usr/local/opt/python/bin/python3.7
Using base prefix '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/durban/python/.env3/bin/python3.7
Not overwriting existing python script /Users/durban/python/.env3/bin/python (you must use /Users/durban/python/.env3/bin/python3.7)
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 420, in copyfile
    os.symlink(os.path.realpath(src), dest)
FileExistsError: [Errno 17] File exists: '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/Python' -> '/Users/durban/python/.env3/.Python'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 2632, in <module>
    main()
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 870, in main
    symlink=options.symlink,
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 1156, in create_environment
    install_python(home_dir, lib_dir, inc_dir, bin_dir, site_packages=site_packages, clear=clear, symlink=symlink)
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 1629, in install_python
    copyfile(os.path.join(prefix, "Python"), virtual_lib, symlink)
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 423, in copyfile
    copy_file_or_folder(src, dest, symlink)
  File "/usr/local/lib/python3.7/site-packages/virtualenv.py", line 403, in copy_file_or_folder
    shutil.copy2(src, dest)
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/shutil.py", line 266, in copy2
    copyfile(src, dst, follow_symlinks=follow_symlinks)
  File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/shutil.py", line 121, in copyfile
    with open(dst, 'wb') as fdst:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/durban/python/.env3/.Python'
```

从错误可以看出来问题在哪里，原因是因为.env3里面已经存在了一个/Users/durban/python/.env3/.Python

看下指向了哪里

```bash

$ ll .env3/.Python
lrwxr-xr-x  1 durban  staff    78B  5  7  2018 .env3/.Python -> /usr/local/Cellar/python/3.6.5/Frameworks/Python.framework/Versions/3.6/Python
```

那试着删除下吧

```bash

$ rm .env3/.Python
```

删除后在执行下看看

```bash

$ virtualenv -p /usr/local/Cellar/python/3.7.4/bin/python3 .env3
Running virtualenv with interpreter /usr/local/Cellar/python/3.7.4/bin/python3
Already using interpreter /usr/local/opt/python/bin/python3.7
Using base prefix '/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/durban/python/.env3/bin/python3.7
Not overwriting existing python script /Users/durban/python/.env3/bin/python (you must use /Users/durban/python/.env3/bin/python3.7)
Installing setuptools, pip, wheel...
done.
Overwriting /Users/durban/python/.env3/bin/activate with new content
Overwriting /Users/durban/python/.env3/bin/activate.fish with new content
Overwriting /Users/durban/python/.env3/bin/activate.csh with new content
Overwriting /Users/durban/python/.env3/bin/activate_this.py with new content
```

居然初始化成功了，从结果上来看应该是没有删除我们已经安装的包的。