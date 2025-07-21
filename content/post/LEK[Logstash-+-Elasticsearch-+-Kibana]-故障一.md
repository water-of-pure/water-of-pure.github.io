+++
date = '2025-07-21T18:16:35.597095+08:00'
draft = false
title = 'LEK[Logstash + Elasticsearch + Kibana] 故障一'
categories = [
    "技术",

]

tags = [
    "Elasticsearch",
    "Logstash",
    "Kibana"
]
+++

今早遇到如下几个问题：

> "Courier Fetch: 30 of 60 shards failed."
>
> "Data too large, data for [time] would be larger than limit"

经过Stackoverflow查看到如下几个方案

针对第一个问题，执行如下的请求，大概的意思就是说，清理缓存的意思吧，试了一下果然有效了。

```bash
curl --user es_admin:qeeniao1234 http://10.132.14.58:9200/logstash-*/_cache/clear
```

但是这个问题并没有解决我如下的问题，查看elasticsearch.log仍然会有第二个问题的提示，

根据Stackoverflow的查找，做了下面的请求操作。打开Kibana就没有对应类似的提示了。

```bash
curl --user es_admin:qeeniao1234 -XPUT http://10.132.14.58:9200/_cluster/settings -d '{
  "persistent" : {
    "indices.breaker.fielddata.limit" : "75%" 
  }
}'
```

原因就是elasticsearch默认启动是给了indices.breaker.fielddata.limit的值为60%，需要设置大一点的值，

于是我就给了75%。

经过我的再次查看，发现在使用kabana的时候尽量的选择时间区间范围小一点，这个应该是跟服务器的硬件设备有很大关系的，

一旦你查看的数据太大了，那么对应的Fielddata的数据量就对应的增加。

像我这里：rt

```bash
[FIELDDATA] Data too large, data for [rt] would be larger than limit of [422523699/402.9mb]
```

在查看过去24小时的时候，它的数据量达到了402M,可想而之其他fielddata放在一起会有多大。
