+++
date = '2025-07-30T10:41:26.092204+08:00'
draft = false
title = 'Python小技巧 - Python内置 HTTP server'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

Python有个非常好用的功能，Python内置 HTTP server，对于预览网站非常有用，尤其是静态网站开发的时候

Python 3 以上版本使用方法如下

```bash

$ python3 -m http.server
```

类型如下的输出代表运行正常

```bash

Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

Python 2 版本使用方法如下

```bash

$ python -m SimpleHTTPServer 8000
```

类型如下的输出代表运行正常

```bash

Serving HTTP on 0.0.0.0 port 8000 ...
```

访问以上地址，打开的就是当前目录下的文件
