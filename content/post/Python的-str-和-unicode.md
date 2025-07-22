+++
date = '2025-07-22T18:31:22.600921+08:00'
draft = false
title = 'Python的 str 和 unicode'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

如果你不知道变量是啥类型的，可以像下面这样操作

```bash
>>> isinstance(u'中文', unicode)
True
>>> isinstance('中文', unicode)
False
>>> isinstance('中文', str)
True
>>> isinstance(u'中文', str)
False
str与unicode的转换很简单
```

简单原则：不要对str使用encode，不要对unicode使用decode

搞明白要处理的是str还是unicode, 使用对的处理方法(str.decode/unicode.encode)

不同编码转换,使用unicode作为中间编码

#s是code\_A的str

```py
s.decode('code_A').encode('code_B')
```

<http://wklken.me/posts/2013/08/31/python-extra-coding-intro.html>
