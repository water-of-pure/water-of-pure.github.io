+++
date = '2025-07-22T18:31:42.002461+08:00'
draft = false
title = 'Scrapy 遇到 Filtered duplicate request 结束运行'
categories = [
    "技术",

]

tags = [
    "Scrapy",
    "Python"
]
image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1595249147/walkerfree/scrypt.jpg"
+++

今天在使用scrapy做数据抓取，抓取的过程中，突然就停止了。看了下最终的结果

> 2016-04-09 11:58:03 [scrapy] DEBUG: Filtered duplicate request: <GET <http://weibo.com/sorry?userblock&is_viewer&code=20003>> - no more duplicates will be shown (see DUPEFILTER\_DEBUG to show all duplicates)

我也不清楚『Filtered duplicate request』这个是啥错误。

于是google了一下，加了下参数

```py
dont_filter=True
```

结果最终的请求方法就改成这样子了，终于起作用了。

```py

yield scrapy.Request(
    info_url,
    cookies=self.cookie,
    callback=self.parse_info,
    dont_filter=True,
    meta={
        'item': item,
        'date': meta_data['date'],
        'weibo_id': meta_data['weibo_id']
    }
)

```
