+++
date = '2025-07-16T15:25:48+08:00'
draft = false
title = 'Git在clone的时候忘记了submodule怎么办'
categories = [
	"技术"
]

tags = [
	"Git"
]
+++

我有一个git仓库，这个仓库有子仓库

我在clone代码的时候，没有对子模块进行clone，直接执行了clone操作

比如
```bash
git clone xxx .
```

执行完发现子模块下面没有文件，这是有问题的 

可以执行命令

```bash
git submodule update --init --recursive
```

