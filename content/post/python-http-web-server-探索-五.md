+++
date = '2025-07-30T11:27:04.314292+08:00'
draft = false
title = 'python http web server 探索（五）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

前面的文章我做了一个简单的小例子

从小例子中可以看出，已经能够在server运行起来之后，访问的时候，可以简单的返回内容到浏览器了

接下来要做的就是如何接收请求，然后根据请求来处理不同的逻辑

首先看下如何解析一个GET请求的参数

代码如下

```python

def parse_query_args(s):
    res = {}
    if s:
        pairs = s.split('&')
        for p in pairs:
            vals = [x for x in p.split("=", 1)]
            res[vals[0]] = vals[1]

    return res
```

代码很简单

比如，如果接收一个参数类似“foo=1&bar=2”

简单写个测试的代码

```python
print(parse_query_args("foo=1&bar=2"))
```

运行后得到如下输出

```bash
{'foo': '1', 'bar': '2'}
```

这个就是我们想要的结果了，当然这个是一个简单的测试，还有很多应用场景需要测试
