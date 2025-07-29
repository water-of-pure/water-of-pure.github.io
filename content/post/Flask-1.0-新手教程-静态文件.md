+++
date = '2025-07-29T10:09:47.705933+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 静态文件'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

身份验证视图和模板可以正常工作，但它们现在看起来很简单。可以添加一些[CSS](https://developer.mozilla.org/docs/Web/CSS)来为您构建的HTML布局添加样式。样式不会改变，因此它是*静态*文件而不是模板。

Flask会自动添加一个`static`视图，该视图采用相对于`baby/static`目录的路径并为其提供服务。`base.html`模板已经有一个指向`app.css`文件的链接

```html

<link rel="stylesheet" href="{{url_for('static', filename='app.css')}}" />

```

除了CSS之外，其他类型的静态文件可能是具有JavaScript功能的文件或logo图像。它们都放在`baby/static`目录下，并用`url_for('static'，filename ='...')`引用。

这个教程的目标不在于教你如何写CSS，因此你只需要将下面的代码复制到`baby/static/app.css`文件中即可。

baby/static/app.css

```css

html { font-family: sans-serif; background: #eee; padding: 1rem; }
body { max-width: 960px; margin: 0 auto; background: white; }
h1 { font-family: serif; color: #377ba8; margin: 1rem 0; }
a { color: #377ba8; }
hr { border: none; border-top: 1px solid lightgray; }
nav { background: lightgray; display: flex; align-items: center; padding: 0 0.5rem; }
nav h1 { flex: auto; margin: 0; }
nav h1 a { text-decoration: none; padding: 0.25rem 0.5rem; }
nav ul  { display: flex; list-style: none; margin: 0; padding: 0; }
nav ul li a, nav ul li span, header .action { display: block; padding: 0.5rem; }
.content { padding: 0 1rem 1rem; }
.content > header { border-bottom: 1px solid lightgray; display: flex; align-items: flex-end; }
.content > header h1 { flex: auto; margin: 1rem 0 0.25rem 0; }
.flash { margin: 1em 0; padding: 1em; background: #cae6f6; border: 1px solid #377ba8; }
.post > header { display: flex; align-items: flex-end; font-size: 0.85em; }
.post > header > div:first-of-type { flex: auto; }
.post > header h1 { font-size: 1.5em; margin-bottom: 0; }
.post .about { color: slategray; font-style: italic; }
.post .body { white-space: pre-line; }
.content:last-child { margin-bottom: 0; }
.content form { margin: 1em 0; display: flex; flex-direction: column; }
.content label { font-weight: bold; margin-bottom: 0.5em; }
.content input, .content textarea { margin-bottom: 1em; }
.content textarea { min-height: 12em; resize: vertical; }
input.danger { color: #cc2f2e; }
input[type=submit] { align-self: start; min-width: 10em; }

```

您可以在[示例代码中](https://github.com/pallets/flask/tree/1.0.2/examples/tutorial/flaskr/static/style.css)找到一个不太紧凑的`style.css`版本。

转到[http://127.0.0.1:5000/auth/login](http://127.0.0.1:5000/auth/login%EF%BC%8C%E8%AF%A5%E9%A1%B5%E9%9D%A2%E5%BA%94%E5%A6%82%E4%B8%8B%E9%9D%A2%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%E6%89%80%E7%A4%BA%E3%80%82)，该页面应如下面的屏幕截图所示。

[![静态文件](https://camo.githubusercontent.com/e31114c998d002420ce5ee63b5640d1b1ee96d87/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433333039302f77616c6b6572667265652f77785f3135315f322e706e67)](https://camo.githubusercontent.com/e31114c998d002420ce5ee63b5640d1b1ee96d87/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433333039302f77616c6b6572667265652f77785f3135315f322e706e67)

您可以从[Mozilla的文档](https://developer.mozilla.org/docs/Web/CSS)中了解有关CSS的更多信息。如果更改静态文件，请刷新浏览器页面。如果更改未显示，请尝试清除浏览器的缓存。

下一期继续 - [博客Blueprint](https://www.walkerfree.com/article/158)
