+++
date = '2025-07-22T18:31:45.479304+08:00'
draft = false
title = 'Python json.loads fails with `ValueError: Invalid control character at: line 1 column 33 (char 33)`'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

> Python json.loads fails with `ValueError: Invalid control character at: line 1 column 33 (char 33)`

这种问题的正确解决办法是

由原来的

```py
json.loads(s)
```

改为

```py
json.loads(s,strict=False)
```
