+++
date = '2025-07-21T18:08:18.956723+08:00'
draft = false
title = 'Scrapy递归抓取网页数据'
categories = [
    "技术",

]

tags = [
    "Scrapy",
    "Python"
]
+++

在使用scrapy抓取网页的数据的过程中，我们会遇到一个问题就是，如何来抓取分页，有时候又不能一下子把所有的分页都获取过来。

这里的解决问题的思路是，获取每个当前抓取页面的下一页链接，并将链接加入要抓取的url列表中，如下是实例代码

```python
 def parse(self, response):
        items = []
        validurls = []
        newurls = response.xpath(
            "//div[@id='selectedgenre']/ul[@class='list paginate']/li/a[@class='paginate-more']/@href").extract()
        for url in newurls:
            validurls.append(url)
        # //循环抓取
        items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in list(set(validurls))])
        iTunes = ItunesItem()
        iTunes['url'] = response.xpath(
            "//div[@id='selectedcontent']/div[@class='column first']/ul/li/a/@href").extract()
        iTunes['title'] = response.xpath(
            "//div[@id='selectedcontent']/div[@class='column first']/ul/li/a/text()").extract()
        iTunes['create_time'] = int(time.time())
        items.append(iTunes)
        return items
```
