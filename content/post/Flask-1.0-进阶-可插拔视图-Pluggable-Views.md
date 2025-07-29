+++
date = '2025-07-29T10:56:05.947960+08:00'
draft = false
title = 'Flask 1.0 进阶 - 可插拔视图（Pluggable Views）'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"
]
+++

Flask 0.7引入了可插拔视图，其灵感来自Django的通用视图，它们基于类而不是函数。主要目的是您可以替换部分实现，这种方式具有可自定义的可插拔视图。

### 基本原则

假设您有一个函数从数据库加载对象列表并呈现到模板中：

```py

@app.route('/users/')
def show_users(page):
    users = User.query.all()
    return render_template('users.html', users=users)

```

这是简单而灵活的，但如果您想以通用方式提供此视图，以便适应其他模型和模板，您可能需要更多灵活性。这是可插入的基于类的视图的地方。作为将此转换为基于类的视图的第一步，您将执行此操作：

```py

from flask.views import View

class ShowUsers(View):

    def dispatch_request(self):
        users = User.query.all()
        return render_template('users.html', objects=users)

app.add_url_rule('/users/', view_func=ShowUsers.as_view('show_users'))

```

正如您所看到的，您要做的是创建 [**flask.views.View**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.View) 的子类并实现 [**dispatch\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.View.dispatch_request) 。然后我们必须使用 [**as\_view()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.View.as_view) 类方法将该类转换为实际的视图函数。传递给该函数的字符串是视图随后具有的端点的名称。但这本身并没有用，所以让我们稍微重构一下代码：

```py

from flask.views import View

class ListView(View):

    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def dispatch_request(self):
        context = {'objects': self.get_objects()}
        return self.render_template(context)

class UserView(ListView):

    def get_template_name(self):
        return 'users.html'

    def get_objects(self):
        return User.query.all()

```

这当然对这样一个小例子没那么有用，但它足以解释基本原理。当你有一个基于类的视图时，问题出现在`self`指向的位置。这种方式的工作方式是每当调度请求时，都会创建一个新的类实例，并使用URL规则中的参数调用 [**dispatch\_request()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.View.dispatch_request) 方法。使用传递给 [**as\_view()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.View.as_view) 函数的参数来实例化类本身。例如，你可以写一个这样的类：

```py

class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name)

```

然后你可以像这样注册：

```py

app.add_url_rule('/about', view_func=RenderTemplateView.as_view(
    'about_page', template_name='about.html'))

```

### 方法提示

通过使用route()或更好的add\_url\_rule()，可插拔视图像常规函数一样附加到应用程序。但是，这也意味着您必须在附加此视图时提供视图支持的HTTP方法的名称。为了将该信息移动到类，您可以提供具有以下信息的方法属性：

```py

class MyView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'POST':
            ...
        ...

app.add_url_rule('/myview', view_func=MyView.as_view('myview'))

```

### 基于方法的调度

对于RESTful API，为每个HTTP方法执行不同的功能特别有用。使用 [**flask.views.MethodView**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.MethodView) ，您可以轻松地做到这一点。每个HTTP方法都映射到一个具有相同名称的函数（只是小写）：

```py

from flask.views import MethodView

class UserAPI(MethodView):

    def get(self):
        users = User.query.all()
        ...

    def post(self):
        user = User.from_form_data(request.form)
        ...

app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))

```

这样你就不必提供methods属性。它会根据类中定义的方法自动设置的。

### 装饰视图

由于视图类本身不是添加到路由系统的视图函数，因此装饰类本身没有多大意义。相反，你要么必须手工装饰[**as\_view()**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.View.as_view)的返回值：

```py

def user_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator

view = user_required(UserAPI.as_view('users'))
app.add_url_rule('/users/', view_func=view)

```

从Flask 0.8开始，还有另一种方法可以指定要在类声明中应用的装饰器列表：

```py

class UserAPI(MethodView):
    decorators = [user_required]

```

由于来自调用者视角的隐式`self`，您不能在视图的各个方法上使用常规视图装饰器，但请记住这一点。

### API的方法视图

Web API通常与HTTP谓词密切配合，因此基于 [**MethodView**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.MethodView) 实现这样的API非常有意义。也就是说，您会注意到API将需要不同的URL规则，这些规则在大多数情况下都会转到相同的方法视图。例如，考虑您在Web上公开用户对象：

| URL | Method | Description |
| --- | --- | --- |
| /users/ | GET | Gives a list of all users |
| /users/ | POST | Creates a new user |
| /users/ | GET | Shows a single user |
| /users/ | PUT | Updates a single user |
| /users/ | DELETE | Deletes a single user |

那么你将如何使用 [**MethodView**](https://flask.palletsprojects.com/en/1.0.x/api/#flask.views.MethodView) 做到这一点？诀窍是利用您可以为同一视图提供多个规则的事实。

我们暂时假设视图看起来像这样：

```py

class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            # return a list of users
            pass
        else:
            # expose a single user
            pass

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

```

那么我们如何将其与路由系统联系起来呢？通过添加两个规则并明确提到每个规则的方法：

```py

user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<int:user_id>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])

```

如果你有很多类似的API，你可以重构那个注册码：

```py

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])

register_api(UserAPI, 'user_api', '/users/', pk='user_id')
```
