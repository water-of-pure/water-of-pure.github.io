+++
date = '2025-07-30T11:43:49.049903+08:00'
draft = false
title = 'Android 打包签名的几种方式'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",

]
+++

### Android打包签名第一种方式：通过IDE，比如Eclipse、Android Studio

这种方式，也是比较普遍的方式，通过IDE -> Build -> Generate Signed Bundle / Apk...

### Android打包签名第二种方式：通过gradle

gradle可以通过命令

```bash

gradle aR
```

或者

```bash

gradle assembleRelease
```

上面命令打Release包

```bash

gradle aD
```

或者

```bash

gradle assembleDebug
```

上面命令打Debug包

### Android打包签名第三种方式：通过keytool工具

在终端签名，不过这种方式签名前要把包生成好
