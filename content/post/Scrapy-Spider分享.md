+++
date = '2025-07-21T18:16:39.602175+08:00'
draft = false
title = 'Scrapy Spider分享'
categories = [
    "技术",

]

tags = [
    "Scrapy",
    "Python"
]
+++

代码片段如下：

```python
class MySpider(BaseSpider):
    name = 'myspider'
    start_urls = (
        'http://example.com/page1',
        'http://example.com/page2',
        )
    def parse(self, response):
        # collect `item_urls`
        for item_url in item_urls:
            yield Request(url=item_url, callback=self.parse_item)
    def parse_item(self, response):
        item = MyItem()
        # populate `item` fields
        yield Request(url=item_details_url, meta={'item': item},
            callback=self.parse_details)
    def parse_details(self, response):
        item = response.meta['item']
        # populate more `item` fields
        return item
```

举个比较是利用的例子，比如这个sipider想要获取微博用户的基本信息和他是否加V的话，那么地址肯定是不一个地址，于是，可以通过这种方式，先获取到基本信息然后将结果通过meta传递给下一个parse，然后下一个parse就可以将上一个parse的结果一起通过item返回了。
