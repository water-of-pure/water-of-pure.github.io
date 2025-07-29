+++
date = '2025-07-29T10:55:42.038070+08:00'
draft = false
title = 'Flask 1.0 进阶 - 模板'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

Flask利用Jinja2作为模板引擎。你显然可以自由使用不同的模板引擎，但你仍然需要安装Jinja2来运行Flask本身。此要求是启用丰富扩展所必需的。扩展可以依赖于Jinja2存在。

本节仅简要介绍Jinja2如何集成到Flask中。如果您需要有关模板引擎语法本身的信息，请访问[官方Jinja2模板文档](http://jinja.pocoo.org/docs/templates)以获取更多信息。

### Jinja 设置

除非定制，否则Jinja2由Flask配置如下：

* 使用render\_template()时，对于以.html，.htm，.xml和.xhtml结尾的所有模板启用自动过滤。
* 使用render\_template\_string()时，为所有字符串启用自动过滤。
* 模板可以使用`{％autoescape％}`标记选择使用火不适用自动过滤。
* 除了默认存在的值之外，Flask还将一些全局函数和帮助程序插入到Jinja2上下文中。

### 标准上下文

默认情况下，Jinja2模板中提供以下全局变量：

**config**

```bash

当前配置对象(**flask.config**)

```

**request**

```bash

当前请求对象（**flask.request**）。如果在没有活动请求上下文的情况下呈现模板，则此变量不可用。

```

**session**

```bash

当前session对象（**flask.session**）。如果在没有活动请求上下文的情况下呈现模板，则此变量不可用。

```

**g**

```bash

全局变量的请求绑定对象（**flask.g**）。如果在没有活动请求上下文的情况下呈现模板，则此变量不可用。

```

**url\_for()**

```bash

**flask.url_for()**函数

```

**get\_flash\_messages()**

```bash

**flask.get_flash_messages()**函数

```

> Jinja上下文行为
>
> 这些变量被添加到变量的上下文中，它们不是全局变量。不同之处在于，默认情况下这些不会显示在导入模板的上下文中。这部分是由性能考虑因素造成的，部分原因是为了使事情明确。
>
> 这对你意味着什么？如果您有要导入的宏，则需要访问请求对象，您有两种可能：
>
> 1. 您将request显式的传递给macro作为参数，或您感兴趣的请求对象的属性。
> 2. 你可以用"with context"导入macro。
>
> 使用上下文导入如下所示：
>
> `{% from '_helpers.html' import my_macro with context %}`

### 标准过滤器

除了Jinja2本身提供的过滤器之外，Jinja2还提供了这些过滤器：

**tojson**

此函数将给定对象转换为JSON表示。例如，如果您尝试动态生成JavaScript，这将非常有用。

请注意，内部脚本标记必须不进行转义，因此如果您打算在`script`标记内使用它，请确保在Flask 0.10之前禁用转义`|safe`;

```html

<script type=text/javascript>
	doSomethingWith({{ user.username|tojson|safe }});
</script>

```

### 控制自动过滤

自动过滤是为您自动转义特殊字符的概念。HTML（或XML，因此XHTML）意义上的特殊字符是`＆`，`>`，`<`，`'`以及`"`。因为这些字符本身在文档中具有特定含义，所以如果要将它们用于文本，则必须用所谓的“entities”替换它们。不这样做不仅会导致用户因无法在文本中使用这些字符而感到沮丧，而且还会导致安全问题。（请参阅[跨站点脚本（XSS）](http://flask.pocoo.org/docs/1.0/security/#xss)）。

但有时您需要在模板中禁用自动转换。如果您想要将HTML显式地插入到页面中，例如，如果它们来自生成安全HTML的系统（如HTML转换器的markdown），则可能出现这种情况。

有三种方法可以实现这一目标：

1. 在Python代码中，将HTML字符串包装在Markup对象中，然后再将其传递给模板。这通常是推荐的方式。
2. 在模板内部，使用`|safe`过滤器将字符串显式标记为安全HTML（`{{myvariable | safe}}`）
3. 暂时禁用autoescape系统。

要在模板中禁用autoescape系统，您可以使用`{％autoescape％}`块：

```html

{% autoescape false %}
    <p>autoescaping is disabled here
    <p>{{ will_not_be_escaped }}
{% endautoescape %}

```

无论何时执行此操作，请对此块中使用的变量非常谨慎。

### 注册过滤器

如果您想在Jinja2中注册自己的过滤器，您有两种方法可以做到这一点。您可以手动将它们放入应用程序的jinja\_env中，也可以使用template\_filter())装饰器。

以下两个示例的工作方式相同，都反转了一个对象：

```py

@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

def reverse_filter(s):
    return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter

```

在装饰器的情况下，如果要将函数名称用作过滤器的名称，则参数是可选的。注册后，您可以像使用Jinja2的内置过滤器一样在模板中使用过滤器，例如，如果您在上下文中有一个名为mylist的Python列表：

```html

{% for x in mylist | reverse %}
{% endfor %}

```

### 上下文处理器

要将新变量自动注入模板的上下文，Flask中存在上下文处理器。上下文处理器在呈现模板之前运行，并且能够将新值注入模板上下文。上下文处理器是一个返回字典的函数。然后，对于应用程序中的所有模板，此字典的键和值将与模板上下文合并：

```py

@app.context_processor
def inject_user():
    return dict(user=g.user)

```

上面的上下文处理器在模板中创建了一个名为user的变量，其值为g.user。这个例子不是很有趣，因为无论如何g都可以在模板中使用，但它可以让我知道这是如何工作的。

变量不限于数值;上下文处理器也可以使函数可用于模板（因为Python允许传递函数）：

```py

@app.context_processor
def utility_processor():
    def format_price(amount, currency=u'€'):
        return u'{0:.2f}{1}'.format(amount, currency)
    return dict(format_price=format_price)

```

上面的上下文处理器使format\_price函数可用于所有模板：

```html

{{ format_price(0.33) }}

```

您还可以将format\_price构建为模板过滤器（请参阅[注册过滤器](http://flask.pocoo.org/docs/1.0/templating/#registering-filters)），但这演示了如何在上下文处理器中传递函数。
