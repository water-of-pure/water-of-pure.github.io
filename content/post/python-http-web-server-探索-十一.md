+++
date = '2025-07-30T11:27:33.761439+08:00'
draft = false
title = 'python http web server 探索（十一）'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

模板如何选择

这里参考了网上的一篇文章，其中写到的三个模板库记录如下

第一个模板库：[Mako](https://www.makotemplates.org/)

[Mako](https://www.makotemplates.org/) 是以 MIT 许可证发布的 Python 模板工具，专为快速展现而设计的（与 Jinja2 不同）。Reddit 已经使用 Mako 来展现他们的网页，它同时也是 Pyramid 和 Pylons 等 web 框架的默认模板语言。它相当简单且易于使用。你可以使用几行代码来设计模板；支持 Python 2.x 和 3.x，它是一个功能强大且功能丰富的工具，具有[良好的文档](http://docs.makotemplates.org/en/latest/)，这一点我认为是必须的。其功能包括过滤器、继承、可调用块和内置缓存系统，这些系统可以被大型或复杂的 web 项目导入。

第二个模板库：Jinja2

Jinja2 是另一个快速且功能全面的选项，可用于 Python 2.x 和 3.x，遵循 BSD 许可证。Jinja2 从功能角度与 Mako 有很多重叠，因此对于新手来说，你在两者之间的选择可能会归结为你喜欢的格式化风格。Jinja2 还将模板编译为字节码，并具有 HTML 转义、沙盒、模板继承和模板沙盒部分的功能。其用户包括 Mozilla、 SourceForge、 NPR、 Instagram 等，并且还具有[强大的文档](http://jinja.pocoo.org/docs/2.10/)。与 Mako 在模板内部使用 Python 逻辑不同的是，Jinja2 使用自己的语法。

第三个模板库：[Genshi](https://genshi.edgewall.org/)

[Genshi](https://genshi.edgewall.org/) 是我会提到的第三个选择。它是一个 XML 工具，具有强大的模板组件，所以如果你使用的数据已经是 XML 格式，或者你需要使用网页以外的格式，Genshi 可能成为你的一个很好的解决方案。HTML 基本上是一种 XML（好吧，不是精确的，但这超出了本文的范围，有点卖弄学问了），因此格式化它们非常相似。由于我通常使用的很多数据都是 XML 或其他类型的数据，因此我非常喜欢使用我可以用于多种事物的工具。
