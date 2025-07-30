+++
date = '2025-07-30T11:44:18.252687+08:00'
draft = false
title = 'Android小知识 - “android.support.v4.content” that cannot be safely rewritten. for androidx'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",

]
+++

遇到的问题：

“android.support.v4.content” that cannot be safely rewritten. for androidx

解决办法：

参考：https://stackoverflow.com/questions/53484988/the-given-artifact-contains-a-string-literal-with-a-package-reference-android-s

主要是添加一个依赖

添加依赖

```groovy

dependencies {
    implementation 'com.jakewharton:butterknife:10.0.0'
    annotationProcessor 'com.jakewharton:butterknife-compiler:10.0.0'
}
```
