+++
date = '2025-07-30T11:25:07.300870+08:00'
draft = false
title = 'python http web server 探索（二）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

web server的实现最基础逻辑的几点思考

request：接收请求

response：返回结果

path：如何解决路由的问题

还有BaseHTTPRequestHandler这个最基础的类，我们应该如何解决，为什么很少见到有人使用这个简答的Handler

如果自己做的话，如何做一个Handler