+++
date = '2025-07-29T10:56:22.320583+08:00'
draft = false
title = '实战记录 - Flask中使用SQLAlchemy创建Model，实现“一对多”、“多对多”的方式'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask",
    "SQLAlchemy"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

Flask中使用SQLAlchemy创建Model，实现“一对多”、“多对多”的方式

> Flask==0.12.2 Flask-SQLAlchemy==2.3.2

## 实现“一对多”的情况

> 一个帖子对应一个分类，一个分类对应多个贴子

* 使用backref的方式如下

分类模型

```py

class Category(db.Model):
    '''分类'''
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return '<Category %r>' % self.title

```

帖子模型

```py

class Article(db.Model):
    ''' 帖子'''
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, doc='自增id')
    title = db.Column(db.String(100), unique=True, doc='标题')
    content = db.Column(db.Text, doc='描述内容')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # 这里是关键点 通过使用backref的方式
    category = db.relationship('Category', backref='article')

    def __repr__(self):
        return '<Article %r>' % self.title

```

* 使用back\_populates的方式如下

分类模型

```py

class Category(db.Model):
    '''分类'''
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    # 这里是关键点 通过使用backref的方式
    article = db.relationship('Article', back_populates='back_populates')

    def __repr__(self):
        return '<Category %r>' % self.title

```

帖子模型

```py

class Article(db.Model):
    ''' 帖子'''
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, doc='自增id')
    title = db.Column(db.String(100), unique=True, doc='标题')
    content = db.Column(db.Text, doc='描述内容')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # 这里是关键点 通过使用backref的方式
    category = db.relationship('Category', back_populates='article')

    def __repr__(self):
        return '<Article %r>' % self.title

```

## 实现“多对多”的情况

> 一个帖子对应多个标签，一个标签对应多个贴子

需要建立一个中间表

帖子标签关联表配置

```py

ARTICLE_TAGS = db.Table('article_tags',
                        db.Column('tag_id', db.Integer,
                                  db.ForeignKey('tags.id')),
                        db.Column('article_id', db.Integer,
                                  db.ForeignKey('article.id'))
                        )

```

帖子模型

```py

class Article(db.Model):
    '''帖子'''
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True, doc='自增id')
    title = db.Column(db.String(100), unique=True, doc='标题')
    content = db.Column(db.Text, doc='描述内容')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    # 多对多的关联配置
    tags = db.relationship(
        'Tag',
        secondary=ARTICLE_TAGS,
        backref=db.backref('article', lazy='dynamic'))

    def __repr__(self):
        return '<Article %r>' % self.title

```

标签模型

```py

class Tag(db.Model):
    '''标签'''
    __tablename__ = 'tags'

    def __init__(self, title):
        self.title = title

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

```

> * 疑问article\_tags这个需要建表吗
>
> 答：当然需要，不然怎么存储多对多的关联呢
