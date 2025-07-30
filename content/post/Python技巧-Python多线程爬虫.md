+++
date = '2025-07-30T11:44:04.300573+08:00'
draft = false
title = 'Python技巧 - Python多线程爬虫'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "多线程"
]
+++

Python多线程爬虫 - 案例记录

用的库如下

* requests
* theading
* queue
* fake\_useragent
* lxml

实现原理：通过多线程方式读取Queue中的数据

代码实现思路如下

```python

# -*- coding:utf-8 -*-
from threading import Thread
from queue import Queue
from lxml import etree
from fake_useragent import Useragent

class CrawlInfo(Thread):
    def __init__(self, url_queue, html_queue):
        self.url_queue = url_queue
        self.html_queue = html_queue

    # 重写run方法
    def run(self):
        '''
        1. 模拟浏览器
        2. 请求
        3. 数据筛选
        4. 数据保存
        '''
        headers = {'User-Agetn': Useragent().random}

        while self.url_queue.empty() != False:
            url = self.url_queue.get()
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(response.text)
                self.html_queue.put(response.text)

class ParseInfo(Thread):
    def __init__(self, html_queue):
        self.html_queue = html_queue

    def run(self):
        while self.html_queue.empty() != False:
            e = etree.HTML(self.html_queue.get())
            span_contents = e.xpath('//div[@class="content"]/span[1]')
            with open('duanzi.txt', 'a', encoding='utt-8') as f:
                for span in span_contents:
                    info = span.xpath('string(.)')
                    f.write(info + '\n')

if __name__ == "__main__":
    url_queue = Queue()
    html_queue = Queue()
    base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
    for i in range(1, 14):
        url_queue.put(base_url.format(i))

    crawl_list = []
    for i in range(1, 3):
        crawl = CrawlInfo(url_queue, html_queue)
        crawl_list.append(crawl)
        crawl.start()

    for crawl in crawl_list:
        crawl.join()

    parse_list = []
    for i in range(3):
        parse = ParseInfo(html_queue)
        parse_list.append(parse)
        parse.start()

    for parse in parse_list:
        parse.join()

```

代码未运行测试
