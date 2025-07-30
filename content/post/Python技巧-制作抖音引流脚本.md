+++
date = '2025-07-30T11:43:59.128747+08:00'
draft = false
title = 'Python技巧 - 制作抖音引流脚本'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg'
categories = [
    "技术",

]

tags = [
    "Python",
    "脚本"
]
+++

技巧记录

1、安装ApowerMirror软件（一个投屏软件）

2、安装adb驱动即Android Debug Bridge（安卓测试桥） tools，一个命令行窗口

3、了解命令

截屏命令

```bash

adb shell screencap -p /sdcard/screen.png
```

保存图片命令

```bash

adb pull /sdcard/screen.png
```

点击命令

```bash

adb shell input tap x y
```

翻页命令

```bash

adb shell input swipe x1 y1 x2 y2
```

4、脚本

```python

import os
os.system('') # 执行截屏命令
os.system('') # 执行保存图片命令
# 根据关注按钮坐标执行点击操作
os.system('') # 执行点击关注命令
# 循转执行翻页命令
os.system('') # 执行翻页命令

```
