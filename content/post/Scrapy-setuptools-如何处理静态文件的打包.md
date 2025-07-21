+++
date = '2025-07-21T18:16:13.498127+08:00'
draft = false
title = 'Scrapy setuptools 如何处理静态文件的打包'
categories = [
    "技术",

]

tags = [
    "Scrapy",

]
+++

这里主要是因为涉及到了scrapyd的一个客户端的工具scrapyd-client，很容易的就可以帮助我们去部署一个scrapy项目

此次遇到的问题是，我的项目中需要用到一个静态的文件，但是默认的打包方式，并没有帮我把静态文件打包到egg里面去，经过查询，

是因为默认的配置文件并没有做相关的配置，于是修改了配置文件加入了下面的代码：

```py
package_data = {
    '': ['*.txt'],
},
```

zip\_safe=False,

整个setup.py文件看起来的话就是这样的：

```py
from setuptools import setup, find_packages
setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    package_data = {
        '': ['*.txt'],
    },
    zip_safe=False,
    entry_points={'scrapy': ['settings = weibo.settings']},
)
```

但是对应的项目里面的调用也要响应的修改一下：

```py
def init_cookie(self):
        # 初始化cookie
        data = pkgutil.get_data('weibo', 'cookie.txt').splitlines()
        if len(data):
            for r in data:
                r = re.sub(r'\s+', ' ', r)
                r_tuple = r.split(" ")
                self.cookie[r_tuple[5]] = re.sub('\n', '', r_tuple[6])
```

这里调用了pkgutil这个工具，是scrapyd-deploy推荐的方式，后来才注意到

然后运行命令

```bash
scrapyd-deplay -p weibo 
```

再次运行 对应的抓取程序，就可以了。
