+++
date = '2025-07-30T11:44:21.458405+08:00'
draft = false
title = 'Android小知识 - The specified Android SDK Build Tools version (28.0.3) is ignored'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",

]
+++

问题：

Android代码打包编译遇到一个错误提示（Android Studio）

“The specified Android SDK Build Tools version (28.0.3) is ignored, as it is below the minimum supported version (29.0.2) for Android Gradle Plugin 4.0.1.”

解决办法：

这个问题其实很好处理

修改`app/build.gradle`的`buildToolsVersion`配置，将

```bash

buildToolsVersion 28.0.3
```

改为

```bash

buildToolsVersion 29.0.2
```
