+++
date = '2025-07-29T10:56:29.485511+08:00'
draft = false

title = "Flask 1.0 - Flask MongoEngine 'QuerySet' object has no attribute 'get_or_404'"

categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

学习Flask 1.0中使用“flask-mongoengine==0.9.5”，遇到类似“ AttributeError: 'QuerySet' object has no attribute 'first\_or\_404'”这个错误

网上查了文档，说要在创建model类的时候添加一段代码，如下

```python

meta = {'abstract': True, 'queryset_class': BaseQuerySet}
```

从代码的逻辑上来说，应该不会有问题的，而且Flask 1.0的官方文档应该也不会傻到用错误的实例来误导大家吧

文档地址：<https://flask.palletsprojects.com/en/1.1.x/patterns/mongoengine/>中有个创建Movie Model的代码

```python

import mongoengine as me

class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()
```

于是去看了“flask-mongoengine==0.9.5”的源代码，不看不知道，一看醒然大悟呀

在源码文件中“site-packages/flask\_mongoengine/\_\_init\_\_.py”这个文件中有Document这个类如下

```python

class Document(mongoengine.Document):
    """Abstract document with extra helpers in the queryset class"""

    meta = {'abstract': True,
            'queryset_class': BaseQuerySet}

    def paginate_field(self, field_name, page, per_page, total=None):
        """Paginate items within a list field."""
        # TODO this doesn't sound useful at all - remove in next release?
        count = getattr(self, field_name + "_count", '')
        total = total or count or len(getattr(self, field_name))
        return ListFieldPagination(self.__class__.objects, self.pk, field_name,
                                   page, per_page, total=total)
```

于是明白了，官方文档果然有点傻，忽悠我们上当嘞，我将Movie的Model类代码修改下，如下

```python

from flask_mongoengine import Document
import mongoengine as me
from . import Imdb

class Movie(Document):
    title = me.StringField()
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()
    imdb = me.EmbeddedDocumentField(Imdb)
```

再次运行试试，果然代码没有再报错误了。

再次进行写入操作后，写入逻辑如下

```python

bttf = Movie(title='Back To The Feature', year=1985)
bttf.actors = [
    'Michael J. Fox',
    'Christopher Lloyd'
]
bttf.imdb = Imdb(imdb_id='tt0088763', rating=8.5)
bttf.save()

bttf = Movie.objects(title='Back To The Feature').first_or_404()
```

终于可以查到了

```bash

> use baby
switched to db baby
> db.collection
baby.collection
> coll = db.baby
baby.baby
> coll.find()
> coll.find({'title':'Back To The Feature'})
> coll.find({'title':'Back To The Feature'})
> col = db.movie
baby.movie
> col.find({'title':'Back To The Feature'})
{ "_id" : ObjectId("5dcb58d3bff86222392e8ca6"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
{ "_id" : ObjectId("5dcb5a06e08d79942ea2184b"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
{ "_id" : ObjectId("5dcb5c0299c8eebebb5f6ce0"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
{ "_id" : ObjectId("5dcb5c105a4bbdabd53bc2f6"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
{ "_id" : ObjectId("5dcb5c20fc294890b9693548"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
{ "_id" : ObjectId("5dcb5f41a6fb86c4f3bc4d4d"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
{ "_id" : ObjectId("5dcb5f42a6fb86c4f3bc4d4e"), "title" : "Back To The Feature", "year" : 1985, "actors" : [ "Michael J. Fox", "Christopher Lloyd" ], "imdb" : { "imdb_id" : "tt0088763", "rating" : 8.5 } }
>
```

最后还发现这个文档这里的一个坑，mongodb的配置如果按照下面的写法

```py

app.config['MONGODB_SETTINGS'] = {
    'db': 'baby'
}
```

会报错提示如下错误

> MongoEngineConnectionError: You have not defined a default connection

改为如下可正常运行

```py

app.config['MONGODB_SETTINGS'] = {
    'db': 'baby',
    'alias': 'default'
}
```

刚刚又遇到一个问题

在使用get\_or\_404()这个方法的时候，居然报404错误，但是如果去掉get\_or\_404()，直接使用如下代码

```py

movies = Movie.objects(title='Back To The Feature')
```

然后将数据渲染到前端居然可以获取到数据，是不是说，不需要使用get\_or\_404()还是说我使用的方法错误了，应该还需要做些什么操作。

```py

return render_template('langcode/me.j2', movies=movies)
```

渲染的html代码如下

```html

{% extends "base.j2" %}

{% block content %}
  {% for movie in movies %}
    <p>{{ movie.id }}</p>
    <p>{{ movie.title }}</p>
    <p>{{ movie.year }}</p>
    <p>{{ movie.imdb.rating }}</p>
  {% endfor %}
{% endblock %}
```
