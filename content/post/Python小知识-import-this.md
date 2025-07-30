+++
date = '2025-07-30T10:40:33.726152+08:00'
draft = false
title = 'Python小知识 - import this'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

最近发现一个很神奇的import使用方法

```python

import this
```

导入`this`之后会自动输出如下内容

```bash

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

具体的原因可以查看[这里](https://stackoverflow.com/questions/5855758/what-is-the-source-code-of-the-this-module-doing?__s=tjrh931s9dfh1ucarf2c)