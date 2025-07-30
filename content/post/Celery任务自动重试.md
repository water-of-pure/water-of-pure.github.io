+++
date = '2025-07-30T09:56:53.426907+08:00'
draft = false
title = 'Celery任务自动重试'
categories = [
    "技术",

]

tags = [
    "Python",
    "Celery"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1577243198/walkerfree/celery.png"
+++

使用flask框架开发中，开始只是简单的使用celery做异步任务的，但是最近发现在用户注册环节中发现，如果邮件发送系统出现问题，比如我使用的是腾讯QQ邮箱，由于发送的邮件速度过快直接提示我“Connection frequency limited”，结果就是邮件系统不能发送了，但是如果你了解这个QQ发送频率的话，可以设置一个重新发送的设置，等待状态恢复正常，在此发送也是一个比较好的策略，不过要确定好这个重试的次数，那么如何才能实现重新发送呢？

celery提供了很完美的接口给我们用，可以到[这里](https://docs.celeryproject.org/en/latest/userguide/tasks.html)查看详细文档

这里记录下自己实际使用celery的情况

celery.task原始的代码如下

```py

@celery.task()
def send_register_email(self, domain, username, email, code):
    subject = 'Please verify your email address'
    html = '''
......
'''
    link = '%s/auth/register/activate?code=%s' % (domain, code)

    with mail.connect() as conn:

        msg = Message(
            sender='Walkerfree <%s>' % celery.conf['MAIL_FROM'],
            subject=subject,
            html=html % (username, link, link),
            recipients=[email]
        )

        conn.send(msg)

```

celery.task改完之后的代码如下

```py

@celery.task(bind=True,
             default_retry_delay=1 * 60,
             retry_kwargs={'max_retries': 3},
             name='tasks.send_register_email')
def send_register_email(self, domain, username, email, code):
    subject = 'Please verify your email address'
    html = '''
......
'''
    link = '%s/auth/register/activate?code=%s' % (domain, code)

    with mail.connect() as conn:

        msg = Message(
            sender='Walkerfree <%s>' % celery.conf['MAIL_FROM'],
            subject=subject,
            html=html % (username, link, link),
            recipients=[email]
        )

        try:
            conn.send(msg)
        except SMTPDataError as e:
            raise self.retry(exc=e)

```

我这里只是简单的加了如下celery任务的接口参数

```py

bind=True,
default_retry_delay=1 * 60,
retry_kwargs={'max_retries': 3},

```

并且在执行celery任务的时候捕获到异常并调用如下代码

```py

raise self.retry(exc=e)

```

然后就可以使用了，比如我这里调用celery任务的时候，会遇到这样的提示

```bash

[2019-12-25 10:14:58,749: INFO/ForkPoolWorker-1] Task tasks.send_register_email[9acaaf96-6574-4c54-b46c-e3a35bf3935a] retry: Retry in 60s: SMTPDataError(550, b'Connection frequency limited')

```

意思是在遇到"**SMTPDataError(550, b'Connection frequency limited')**"的时候，celery将在60秒内重试任务

还是很简单的
