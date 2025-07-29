+++
date = '2025-07-29T10:56:33.348987+08:00'
draft = false
title = 'Flask 1.0 - Celery管理后台任务-工厂模式'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

管理后台任务，在许多项目中都是必不可少的，Flask的文档中推荐的Celery，但是官方文档简单介绍了非工厂模式的使用方式，简单的介绍了使用方法，但是对于使用工厂模式创建应用的我来说，完全达不到我使用的目的，根本不完美

文章参考

> https://citizen-stig.github.io/2016/02/17/using-celery-with-flask-factories.html

经过搜索找到了这篇文章，给了我启发。so，记录下我自己项目的使用方式吧

baby/\_\_init\_\_.py保持create\_app不变

添加文件

baby/celery.py文件，代码如下

```python

# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-11-13 17:19:11
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-11-13 17:19:25
from celery import Celery

def create_celery(app=None):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask

    return celery

```

然后创建baby/task.py文件，代码如下

```python

# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-11-13 16:30:07
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-11-13 17:19:48
from baby import create_app
from baby.celery import create_celery
celery = create_celery(create_app())

@celery.task(name="tasks.add_together")
def add_together(a, b):
    return a + b

```

这些添加完之后，运行celery

```bash

celery -A baby.task worker -E --loglevel=info
```

输入类似如下

```bash

celery@durbanzhangdeMacBook-Pro v4.3.0 (rhubarb)

Darwin-16.7.0-x86_64-i386-64bit 2019-11-13 17:20:02

[config]
.> app:         baby:0x1030c1310
.> transport:   redis://localhost:6379//
.> results:     redis://localhost:6379/
.> concurrency: 4 (prefork)
.> task events: ON

.> celery           exchange=celery(direct) key=celery

[tasks]
  . tasks.add_together

[2019-11-13 17:20:03,547: INFO/MainProcess] Connected to redis://localhost:6379//
[2019-11-13 17:20:03,561: INFO/MainProcess] mingle: searching for neighbors
[2019-11-13 17:20:04,617: INFO/MainProcess] mingle: all alone
[2019-11-13 17:20:04,649: INFO/MainProcess] celery@durbanzhangdeMacBook-Pro ready.
```

Celery相关的参数配置如下（使用的是Redis）

```py

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'
```

下面看下在view中如何调用这个任务吧

```py

from baby.celery import create_celery

@bp.route('/together')
def together():
    celery = create_celery(current_app)
    result = celery.send_task(name='tasks.add_together', args=(2, 3))
    print(result.wait())
    return 'success'
```

我这里使用的是Blueprint，所以只说使用Blueprint的情况

运行项目，访问http://localhost:5000/stream/together

看下celery的输出

```bash

[2019-11-13 17:51:47,160: INFO/MainProcess] Received task: tasks.add_together[b37ca0cc-1fa3-4182-9ca8-3404aafc6ad3]
[2019-11-13 17:51:47,201: INFO/ForkPoolWorker-2] Task tasks.add_together[b37ca0cc-1fa3-4182-9ca8-3404aafc6ad3] succeeded in 0.0225263449999602s: 5
[2019-11-13 17:52:19,636: INFO/MainProcess] Received task: tasks.add_together[223f1ead-cbf4-46c3-b5fc-18f362d9a3b5]
[2019-11-13 17:52:19,672: INFO/ForkPoolWorker-1] Task tasks.add_together[223f1ead-cbf4-46c3-b5fc-18f362d9a3b5] succeeded in 0.01702427300006093s: 5
[2019-11-13 17:52:20,395: INFO/MainProcess] Received task: tasks.add_together[87b47fde-daae-4a9a-940a-3d038577af0d]
[2019-11-13 17:52:20,398: INFO/ForkPoolWorker-2] Task tasks.add_together[87b47fde-daae-4a9a-940a-3d038577af0d] succeeded in 0.0009092729999338189s: 5
```

一切运行正常。当然我这边也有一个输出

```bash

127.0.0.1 - - [13/Nov/2019 17:52:19] "GET /stream/together HTTP/1.1" 200 160 0.212275
5
```

注意这里输出的值“5”

好了，记录到此结束。
