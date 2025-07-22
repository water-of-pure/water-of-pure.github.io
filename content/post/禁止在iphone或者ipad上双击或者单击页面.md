+++
date = '2025-07-22T18:31:52.654730+08:00'
draft = false
title = '禁止在iphone或者ipad上双击或者单击页面'
categories = [
    "技术",

]

tags = [
    "JavaScript",

]
+++

先看一段代码

```js
$('.advertise-main .advertise-cover').bind('touchend', function(event){
   event.preventDefault();
});  

```

能明白这个是用来啥的不！

阻止safari 再iphone或者ipad上不能点击页面，禁止再iphone或者ipad上双击页面

参考：<http://appcropolis.com/blog/howto/implementing-doubletap-on-iphones-and-ipads//>
