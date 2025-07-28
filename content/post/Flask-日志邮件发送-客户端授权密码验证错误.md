+++
date = '2025-07-28T17:52:42.651657+08:00'
draft = false
title = 'Flask 日志邮件发送 客户端授权密码验证错误'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/c_scale,w_520/v1530152883/walkerfree/stockvault-feet-of-an-athlete-running-on-a-deserted-road179154.jpg"
+++

最近在使用flask的日志邮件发送功能，就是程序出现问题的时候，可以通过邮件发送到指定的邮箱，当时使用的是QQ邮箱的

基本上会有如下的错误

> smtplib.SMTPAuthenticationError: (535, b'Error: authentication failed')
>
> smtplib.SMTPServerDisconnected: Connection unexpectedly closed
>
> Connection unexpectedly closed: timed out

开始的配置如下

```py

ADMINS = ['xxx@xxx']
MAIL_SUBJECT_PREFIX = '[Walkerfree]'
MAIL_SENDER = 'xxx@xxx'
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'xxx@xxx'
MAIL_PASSWORD = '123456'
```

在测试的时候会遇到超时，但是是这里的问题

```py

mail_handler = SMTPHandler(
        application.config['MAIL_SERVER']
        application.config['MAIL_SENDER'],
        application.config['ADMINS'],
        'application error',
        (
            application.config['MAIL_USERNAME'],
            application.config['MAIL_PASSWORD'],
        )
    )
```

第一个参数没有传递端口号，可以看源码

```py

self.mailhost, self.mailport = mailhost
```

有mailhost和mailport，没有端口号怎么能行呢

修改后如下

```py

mail_handler = SMTPHandler(
        (
            application.config['MAIL_SERVER'],
            application.config['MAIL_PORT']
        ),
        application.config['MAIL_SENDER'],
        application.config['ADMINS'],
        'application error',
        (
            application.config['MAIL_USERNAME'],
            application.config['MAIL_PASSWORD'],
        )
    )
```

报错如下

```bash

SMTPServerDisconnected: Connection unexpectedly closed: timed out
```

最后修改了配置，如下

```py

ADMINS = ['xxx@xxx']
MAIL_SUBJECT_PREFIX = '[Walkerfree]'
MAIL_SENDER = 'xxx@xxx'
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 25
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'xxx@xxx'
MAIL_PASSWORD = '123456'
```

最后发送成功。客户端授权码的这个需要自己去搞，QQ帮助中心有指引的。

快捷链接:http://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256%27)
