+++
date = '2025-07-21T18:07:10.970766+08:00'
draft = false
title = 'scrapy 防止网站限制IP'
categories = [
    "技术",

]

tags = [
    "Scrapy",
    "Python"
]
+++

根据scrapy官方文档：

<http://doc.scrapy.org/en/master/topics/practices.html#avoiding-getting-banned>

里面的描述，要防止scrapy被ban，主要有以下几个策略。

> 1，动态设置user agent
>
> 2，禁用cookies
>
> 3，设置延迟下载
>
> 4，使用Google cache
>
> 5，使用IP地址池（Tor project、VPN和代理IP）
>
> 6，使用Crawlera

由于Google cache受国内网络的影响，你懂得；

Crawlera的分布式下载，我们可以在下次用一篇专门的文章进行讲解。

所以本文主要从动态随机设置User-Agent、禁用cookies、设置延迟下载和使用代理IP这几个方式。

首先设置一下setttings

```python
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]
DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'weibo.middlewares.ProxyMiddleware': 100
}
COOKIES_ENABLED = False
DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.RandomUserAgent': 1,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'weibo.middlewares.ProxyMiddleware': 100
}
```

这里的weibo可根据你自己scrapy的名称进行替换

接下来添加DOWNLOADER的中间件，在middlewares.py文件中添加如下代码：

```python
class RandomUserAgent(object):
    def __init__(self, agents):
        self.agents = agents
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))
class ProxyMiddleware(object):
    def __init__(self, mysql_host, mysql_db, mysql_user, mysql_passwd):
        self.mysql_host = mysql_host
        self.mysql_db = mysql_db
        self.mysql_user = mysql_user
        self.mysql_passwd = mysql_passwd
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host=crawler.settings.get('MYSQL_HOST'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_passwd=crawler.settings.get('MYSQL_PASSWD'),
            mysql_db=crawler.settings.get('MYSQL_DB')
        )
    def process_request(self, request, spider):
        try:
            self.conn = MySQLdb.connect(
                user=self.mysql_user,
                passwd=self.mysql_passwd,
                db=self.mysql_db,
                host=self.mysql_host,
                charset="utf8",
                use_unicode=True
            )
            self.cursor = self.conn.cursor()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        self.cursor.execute(
            'SELECT * FROM xicidaili order by verified_time DESC Limit 0,10')
        proxy_item = self.cursor.fetchall()
        proxy = random.choice(proxy_item)
        user_pass = proxy[4]
        ip = proxy[1]
        port = proxy[2]
        http_method = proxy[6]
        http_method = http_method.lower()
        if user_pass is not None:
            request.meta['proxy'] = "%s://%s:%s" % (http_method,ip,port)
            encoded_user_pass = base64.encodestring(user_pass)
            request.headers[
                'Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        else:
            request.meta['proxy'] = "%s://%s:%s" % (http_method,ip,port)
```

这里提到了代理ip的问题，可以自己去网上搜索一下，然后存储到数据库中，在进行相应的修改【前提是要搞到能用代理ip】

> 参考的文章：
>
> <http://blog.csdn.net/allen_hdh/article/details/33724805>
>
> <http://www.cnblogs.com/rwxwsblog/p/4575894.html>
