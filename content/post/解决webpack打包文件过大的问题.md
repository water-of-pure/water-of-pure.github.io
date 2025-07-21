+++
date = '2025-07-21T18:04:33.810568+08:00'
draft = false
title = '解决webpack打包文件过大的问题'
categories = [
    "技术",

]

tags = [
    "Webpack",

]
+++

经过自己的多次波折，终于找到了一个可以解决的webpack打包过大的问题。

首先说明一下我的打包文件为什么会很大，主要原因是里面的第三方库用的多了，打包的时候就会把依赖的文件打包到一起，当然会很大了。

解决的办法是使用

webpack的externals，记录一个例子

```json
externals: {
    'moment': true,
    'jquery':'jQuery',
    'bootstrap':true,
    'fancybox':true,
    'co':true,
    '_':'lodash',
    'async':true,
    'datetimepicker':true,
    'selectpicker':true,
    'sweetalert':true,
    'highcharts':'Highcharts',
    'director':'Router'
},
```

当然了这些库不用打包处理，但是在html文件中还是需要自己去引用的，不然我也不会知道你要运行的库文件在那里。

看我的

```html
<script src="https://cdn.bootcss.com/jquery/2.1.4/jquery.min.js"></script>
<script src="https://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
<script src="https://cdn.bootcss.com/fancybox/2.1.5/jquery.fancybox.min.js"></script>
<script src="http://apps.bdimg.com/libs/moment/2.8.3/moment-with-locales.min.js"></script>
<script src="https://cdn.bootcss.com/co/4.1.0/index.min.js"></script>
<script src="https://cdn.bootcss.com/lodash.js/3.10.1/lodash.min.js"></script>
<script src="https://cdn.bootcss.com/async/1.4.2/async.min.js"></script>
<script src="https://cdn.bootcss.com/smalot-bootstrap-datetimepicker/2.3.4/js/bootstrap-datetimepicker.min.js"></script>
<script src="https://cdn.bootcss.com/bootstrap-select/2.0.0-beta1/js/bootstrap-select.min.js"></script>
<script src="https://cdn.bootcss.com/sweetalert/1.1.0/sweetalert.min.js"></script>
<script src="https://cdn.bootcss.com/highcharts/4.1.9/highcharts.src.js"></script>
<script src="https://cdn.bootcss.com/Director/1.2.8/director.min.js"></script>
<script src="/js/out/common.js"></script>
<script src="/js/out/index.js"></script>
```

瞬间感觉好多的文件啊，当然了，这个是在一个页面要用react做很多事情的，你自己写的话就不需要这么多了，当然我技术低写不了哇。

此方法就是传说中webpack的CDN解决方案。

给大家一个参考，看不懂的可以到这几个地址去观摩一下：

> <http://www.zhihu.com/question/31352596>
>
> <http://segmentfault.com/a/1190000002552008>
>
> <http://www.cnblogs.com/vajoy/p/4650467.html>
>
> <http://code.oneapm.com/javascript/2015/07/07/webpack_performance_1/>
