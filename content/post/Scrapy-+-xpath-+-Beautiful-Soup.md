+++
date = '2025-07-21T18:08:14.024654+08:00'
draft = false
title = 'Scrapy + xpath + Beautiful Soup'
categories = [
    "技术",

]

tags = [
    "Python",
    "Scrapy"
]
+++

在使用scrapy的过程中会遇到一个问题就是类似如下的代码

```html
<tr>
    <td>元素一</td>
    <td>元素二</td>
    <td>元素三</td>
</tr>
<tr>
    <td>元素一</td>
    <td><a href='#'>元素二</a></td>
    <td>元素三</td>
</tr>
<tr>
    <td>元素一</td>
    <td>元素二</td>
    <td>元素三</td>
</tr>
```

在scrapy中的xpath应该是这样的

```html
'//tr/td[0]' 获取 元素一
'//tr/td[1]' 获取 元素二
'//tr/td[2]' 获取 元素三
```

但是获取完之后 我们要存到数据库的数据是一个纯文本的，不希望里里面有html标签，好吧，这个例子

里面就有这样的一个标签，怎么办？正则？如果文本里面也有这样的标签呢？考虑后发现Beautiful Soup

其实在将获取的元素存储的时候，使用Beautiful Soup进行整理一下就可以获取到了。给个实例代码

```python
soup = BeautifulSoup(item['location'][i], "lxml")
location = soup.get_text()
location = re.sub(r'\s+','',location)
```


其实只要使用`get_text()`这个方法就可以比较完整的获取到文本数据了
