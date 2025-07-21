+++
date = '2025-07-21T18:16:01.528364+08:00'
draft = false
title = '利用第三方平台crawlera做scrapy爬虫防屏蔽'
categories = [
    "技术",

]

tags = [
    "Scrapy",

]
+++

crawlera官方网址：<http://scrapinghub.com/crawlera/>

crawlera帮助文档：<http://doc.scrapinghub.com/crawlera.html>

1，注册一个crawlera账号并激活

2，登录网站获取App Key

3，激活crawlera这里注意一下，别搞错了，搞成Cloud就混淆了，我就是，哎文档没好好看，其实就是选择一个

crawlera进行激活就好了，我选择了最小的那个，以为开始看到了里面要收钱的，所以没敢点击，没想到是，后面

使用的时候，还是可以的用的

进行完上面的操作就可以在程序里面加代码了

1，安装scrapy-crawlera

```bash
pip install scrapy-crawlera
```

2，修改配置文件添加如下配置信息

```py
DOWNLOADER_MIDDLEWARES = {
    'scrapy_crawlera.CrawleraMiddleware': 600
}
CRAWLERA_ENABLED = True
CRAWLERA_USER = '<API Key>'
CRAWLERA_PASS = 'crawlera的密码'
```

根据官方文档的提示

我还加入了如下的配置，保证了我数据的正确获取,就我测试的观察，下面的配置，会使得程序能够自动的去获取数据，知道获取到正确的数据为止

```py
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600
```

好了，就这些，开始吧 crawl吧。

> 参考文章：
>
> <http://www.cnblogs.com/rwxwsblog/p/4582127.html>
