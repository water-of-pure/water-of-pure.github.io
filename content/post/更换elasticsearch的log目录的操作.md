+++
date = '2025-07-18T12:06:00.898376+08:00'
draft = false
title = '更换elasticsearch的log目录的操作'
categories = [
    "技术",

]

tags = [
    "Elasticsearch",

]
+++

一定要注意顺序，不要会出现没有raw的问题，因为这个搞死我了。

> 不用停止kibana
>
> 首先停止Logstash的运行
>
> 再停止Elasticsearch的运行

修改logstash的配置文件，将日志文件目录转移到指定的盘上,做好准备后，按照如下顺序执行

> 先启动Elasticsearch的运行
>
> 再启动Logstash的运行

查看模板【如果返回空的json说明还是会出现.raw不存在的问题】

```bash
curl -u logstashclient:qeeniao_logstash 'http://10.132.14.58:9200/_template/logstash?pretty=1'
```

更新模板【这里我试过，然并没有卵用】

```bash
curl -u logstashclient:qeeniao_logstash -XPUT 'http://10.132.14.58:9200/logstash' @template.json
```
