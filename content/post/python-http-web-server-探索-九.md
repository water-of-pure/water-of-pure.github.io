+++
date = '2025-07-30T11:27:17.045001+08:00'
draft = false
title = 'python http web server 探索（九）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

如何封装

关于web server的封装，这点首先我自己是没有想好的

不过能够清楚的知道

Requet部分、Response部分、Header部分应该是可以被先封装下的

Request部分主要用来处理请求过来的信息，至少包括路由、请求参数、请求方法等

Response部分主要是用来处理回应信息，至少要包括回应的文本信息，后面可以对接第三方的库

Header部分也是可以被封装的，至少基本的Header部分中的ContentType等类似的值可以封装下

具体的后面介绍