+++
date = '2025-07-21T18:16:05.543503+08:00'
draft = false
title = 'Scrapy 1.0.3版本 Selenium Phantomjs Downloader Middleware'
categories = [
    "技术",

]

tags = [
    "Python",
    "Scrapy",
    "Selenium"
]
+++

一直想找的这个东西Middleware，找了很久，有的是一个过期的，有的是要弹出什么框的，这里给scrapy最新版本的解决方案。

此方案排除了几个问题：

Message: 'Can not connect to GhostDriver'

对于此问题像下面这样操作就好了：

```py
driver = webdriver.PhantomJS(port=port,
                             desired_capabilities={
                                 'javascriptEnabled': True,
                                 'platform': 'windows',
                                 'browserName': 'Mozilla',
                                 'version': '5.0',
                                 'phantomjs.page.settings.userAgent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
                             })
```

本人测试通过,如果不是一个版本的话我就不晓得了。

这里分享一下我的代码好了，虽然还有几个问题没有解决，不过这个已经解决了我一个大问题了，就是有结果了。

```py
#! -*- coding:utf-8 -*-
from selenium import webdriver
from proxy import settings
from scrapy.http import HtmlResponse
import logging
import time
logger = logging.getLogger('PhantomjsDownloaderMiddleware')
class PhantomjsDownloaderMiddleware(object):
    def __init__(self, options, max_sum):
        self.options = options
        self.max_sum = max_sum
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            options=crawler.settings.get('PHANTOMJS_OPTIONS', {}),
            max_sum=crawler.settings.get('PHANTOMJS_MAXSUM', 2)
        )
    def process_request(self, request, spider):
        service_args = ['--load-image=false', '--disk-cache=true']
        if 'proxy' in request.meta:
            service_args.append('--proxy=' + request.meta['proxy'][7:])
        if 'port' in request.meta:
            port = request.meta['port']
        else:
            port = 29842
        try:
            driver = webdriver.PhantomJS(port=port,
                                         desired_capabilities={
                                             'javascriptEnabled': True,
                                             'platform': 'windows',
                                             'browserName': 'Mozilla',
                                             'version': '5.0',
                                             'phantomjs.page.settings.userAgent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
                                         })
            driver.get(request.url)
            time.sleep(10)
            content = driver.page_source.encode('utf-8')
            url = driver.current_url.encode('utf-8')
            driver.quit()
            if content == '<html><head></head><body></body></html>':
                logger.info('content is empty : 503')
                return HtmlResponse(request.url, encoding='utf-8', status=503, body='')
            else:
                logger.info('content get success : 200')
                return HtmlResponse(url, encoding='utf-8', status=200, body=content)
        except Exception, e:
            logger.warning(e)
            logger.info('Exception content is empty : 503')
            return HtmlResponse(request.url, encoding='utf-8', status=503, body='')
```

以上就是一个半成品了，但是可以用的，不过还是需要自己完善一下，根据自己的需求来吧，大概的思路就是这样的。
