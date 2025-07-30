+++
date = '2025-07-30T11:43:52.149412+08:00'
draft = false
title = 'Android 如何打包'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",

]
+++

1、打开**Android Studio**，进入需要打包**apk**的项目工程；

**2**、找到 **Android Studio** 顶部菜单栏里面的 **Build** 选项，点击 **”Generate Signed Bundle/APK…”**选项进入；

3、选择keyStore/jks

如果没有keyStore/jks的话，需要点击**Create new创建一个新的，如果已经有了可以直接选择Choose existing...**

**针对有**有keyStore/jks的话按照下面来选择：

如果已经新建有keyStore/jks文件，就直接选择对应的keyStore/jks文件即可。接着输入密钥密码、密钥别名、公钥密码，确认无误之后，点击**Next**；

针对没有keyStore/jks的话按照下面来选择：

点击**Create new，进入创建**keyStore/jks界面，然后填入相关的信息，具体如何填写，其实没有固定要求，里面的内容尽量正规一些，方便记忆。

4、进入选择生成**apk**导出的文件路径，然后选择**apk**的模式：**release**，勾选下面的**V1**和**V2**，二者缺一不可，选择无误之后，点击**Finish**按钮即可开始打包**apk**；

5、短暂的等待之后，在右下角会提示一个弹框，提示打包**apk**成功，那么根据第**4**步选择的**apk**生成导出的文件夹（不知道的话，重新再走一遍）就可以看到打包好的**apk**文件了。
