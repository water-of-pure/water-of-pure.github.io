+++
date = '2025-07-30T09:55:29.919934+08:00'
draft = false
title = 'Flask中如何获取Server的相关信息'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

在使用Flask做web开发的时候，偶尔会需要调用Request中的Server信息，比如端口号，域名之类的

在Flask中这个Server的相关信息获取是非常简单的

通过`request.environ`可以获取到几乎全部的Server信息

比如我这里访问`http://127.0.0.1:5000/post/item` 然后将`request.environ`的信息输出到日志，可以获取到类似如下的信息

```bash

{'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>, 'wsgi.version': (1, 0), 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'REQUEST_METHOD': 'GET', 'SCRIPT_NAME': '', 'RAW_PATH_INFO': '/post/item', 'PATH_INFO': '/post/item', 'CONTENT_TYPE': 'text/plain', 'SERVER_PROTOCOL': 'HTTP/1.0', 'SERVER_NAME': '127.0.0.1', 'SERVER_PORT': '5000', 'REMOTE_ADDR': '127.0.0.1', 'REMOTE_PORT': '58405', 'GATEWAY_INTERFACE': 'CGI/1.1', 'headers_raw': (('Host', '127.0.0.1:5000'), ('Connection', 'keep-alive'), ('Cache-Control', 'max-age=0'), ('Upgrade-Insecure-Requests', '1'), ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'), ('Sec-Fetch-User', '?1'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'), ('Sec-Fetch-Site', 'none'), ('Sec-Fetch-Mode', 'navigate'), ('Accept-Encoding', 'gzip, deflate, br'), ('Accept-Language', 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,lb;q=0.5,co;q=0.4'), ('Cookie', 'access_token=4b68629fe81a7982728adbea50357c1d382017b8; is_hide_download=true; isShowRedpacket=1; platform=web; QN_HIDDEN_INVEST_TIPS=; QN_HIDDEN_PRODUCT_BUY_PAGE_TIPS=; QN_saveplan_product_id=193; web_device_key=BWDFI2CF7ATW30TXPH07PK2BQTU0YE; zg_did=%7B%22did%22%3A%20%2216680adccf7a2c-0f4a3f6c3160ce-2d604637-3d10d-16680adccf8845%22%7D; _ga=GA1.1.430310970.1544409236; __wzd96bb85a21755618844b8=1556007296|d5311aa69976; UM_distinctid=16b4e888bbd24a-0fffcd4765422c-37677e05-fa000-16b4e888bbeb3; zg_99e520e4c4f745888ab0223f331b0032=%7B%22sid%22%3A%201567655012.547%2C%22updated%22%3A%201567655012.547%2C%22info%22%3A%201567395368068%7D; responseTimeline=1939; io=gwqkVXtguegCXzK5AAAD; __wzdd49646447596a96dfec7=1570773843|a90819629f09; __wzdeea8348a655ff8b452a8=1571706979|dee6f4a108b0; CNZZDATA5587427=cnzz_eid%3D52917038-1544409237-http%253A%252F%252F127.0.0.1%253A3041%252F%26ntime%3D1573781899; Hm_lvt_1ac5a848f7ad883bf5520aa84eda1200=1573781902; Hm_lpvt_1ac5a848f7ad883bf5520aa84eda1200=1573784001; __wzd3bcf756fc5845d894763=1574414880|4bfd4bec505e')), 'HTTP_HOST': '127.0.0.1:5000', 'HTTP_CONNECTION': 'keep-alive', 'HTTP_CACHE_CONTROL': 'max-age=0', 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,lb;q=0.5,co;q=0.4', 'HTTP_COOKIE': 'access_token=4b68629fe81a7982728adbea50357c1d382017b8; is_hide_download=true; isShowRedpacket=1; platform=web; QN_HIDDEN_INVEST_TIPS=; QN_HIDDEN_PRODUCT_BUY_PAGE_TIPS=; QN_saveplan_product_id=193; web_device_key=BWDFI2CF7ATW30TXPH07PK2BQTU0YE; zg_did=%7B%22did%22%3A%20%2216680adccf7a2c-0f4a3f6c3160ce-2d604637-3d10d-16680adccf8845%22%7D; _ga=GA1.1.430310970.1544409236; __wzd96bb85a21755618844b8=1556007296|d5311aa69976; UM_distinctid=16b4e888bbd24a-0fffcd4765422c-37677e05-fa000-16b4e888bbeb3; zg_99e520e4c4f745888ab0223f331b0032=%7B%22sid%22%3A%201567655012.547%2C%22updated%22%3A%201567655012.547%2C%22info%22%3A%201567395368068%7D; responseTimeline=1939; io=gwqkVXtguegCXzK5AAAD; __wzdd49646447596a96dfec7=1570773843|a90819629f09; __wzdeea8348a655ff8b452a8=1571706979|dee6f4a108b0; CNZZDATA5587427=cnzz_eid%3D52917038-1544409237-http%253A%252F%252F127.0.0.1%253A3041%252F%26ntime%3D1573781899; Hm_lvt_1ac5a848f7ad883bf5520aa84eda1200=1573781902; Hm_lpvt_1ac5a848f7ad883bf5520aa84eda1200=1573784001; __wzd3bcf756fc5845d894763=1574414880|4bfd4bec505e', 'wsgi.input': <eventlet.wsgi.Input object at 0x109933550>, 'eventlet.input': <eventlet.wsgi.Input object at 0x109933550>, 'eventlet.posthooks': [], 'flask.app': <Flask 'baby'>, 'werkzeug.request': <Request 'http://127.0.0.1:5000/post/item' [GET]>}

```

这里我们看下常见的Server有哪些

> HTTP\_HOST

> HTTP\_USER\_AGENT

> HTTP\_ACCEPT

> HTTP\_COOKIE

> SERVER\_NAME

> SERVER\_PORT

> REMOTE\_ADDR

> REMOTE\_PORT

> REQUEST\_METHOD

> SCRIPT\_NAME

> RAW\_PATH\_INFO

> PATH\_INFO

> CONTENT\_TYPE

> SERVER\_PROTOCOL

当我们想要获取其中的值的话，可以使用下面的方法 比如获取SERVER\_NAME的值

```py

request.environ.get('SERVER_NAME')
```
