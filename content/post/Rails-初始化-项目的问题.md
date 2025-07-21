+++
date = '2025-07-21T18:17:06.686958+08:00'
draft = false
title = 'rails 初始化 项目的问题'
categories = [
    "技术",

]

tags = [
    "Rails",

]
+++

出现的问题大概就是这样的

```bash
Gem::RemoteFetcher::FetchError: Errno::ECONNRESET: Connection reset by peer - SSL_connect
```

我已经将gem的源设置为taobao的源，但是初始化的结果确实用了本源

解决办法是

```bash
bundle config mirror.https://rubygems.org https://ruby.taobao.org
```

解决地址：

<https://github.com/rapid7/metasploit-framework/issues/5187>
