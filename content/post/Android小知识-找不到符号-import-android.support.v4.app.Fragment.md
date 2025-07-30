+++
date = '2025-07-30T11:44:24.155297+08:00'
draft = false
title = 'Android小知识 - 找不到符号 import android.support.v4.app.Fragment'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",

]
+++

### 问题：

找不到符号 import android.support.v4.app.Fragment

最近做安卓开发，遇到了如上的问题提示：

在`gradle.properties`中把有关`AndroidX`的设置全部注释掉，顺便初步了解下

其原因应该是跟我在gradle.properties加入的几个配置项有关

```java

android.useAndroidX=true //  表示当前项目启用 androidx
android.enableJetifier=true // 表示将依赖包也迁移到androidx 。如果取值为false,表示不迁移依赖包到androidx，但在使用依赖包中的内容时可能会出现问题，当然了，如果你的项目中没有使用任何三方依赖，那么，此项可以设置为false
```

之所以加了这几个配置，是因为自己引入的第三方库里面要求使用androidx  
 但是加完这两个配置我自己的项目就要大动干戈，于是恐于面对无数的调整，最后放弃了

### 解决办法

上面两个配置删除或者将true改为false

另外参考文章：[点这里](https://cloud.tencent.com/developer/article/1459306)

详细的support依赖库的新旧对应关系见下表：

**支持库的旧路径**  
 com.android.support.constraint:constraint-layout  
 com.android.support.test.espresso:espresso-core  
 com.android.support.test:runner  
 com.android.support:appcompat-v7  
 com.android.support:cardview-v7  
 com.android.support:design  
 com.android.support:multidex  
 com.android.support:palette-v7  
 com.android.support:recyclerview-v7  
 com.android.support:support-v4

**支持库的新路径**  
 androidx.constraintlayout:constraintlayout:1.1.2  
 androidx.test.espresso:espresso-core:3.1.0  
 androidx.test:runner:1.1.0  
 androidx.appcompat:appcompat:1.0.0  
 androidx.cardview:cardview:1.0.0  
 com.google.android.material:material:1.0.0-rc01  
 androidx.multidex:multidex:2.0.0  
 androidx.palette:palette:1.0.0  
 androidx.recyclerview:recyclerview:1.0.0  
 androidx.legacy:legacy-support-v4:1.0.0

详细的support控件的新旧对应关系见下表：

**支持控件的旧包名**  
 android.support.v4.app.Fragment  
 android.support.v4.app.FragmentActivity  
 android.support.v4.app.FragmentManager  
 android.support.v4.app.FragmentPagerAdapter  
 android.support.v4.view.ViewPager  
 android.support.v4.view.PagerAdapter  
 android.support.v4.view.PagerTabStrip  
 android.support.v4.view.PagerTitleStrip  
 android.support.v7.app.AppCompatActivity  
 android.support.v7.widget.Toolbar  
 android.support.v7.widget.RecyclerView  
 android.support.v7.widget.GridLayoutManager  
 android.support.v7.widget.LinearLayoutManager  
 android.support.v7.widget.StaggeredGridLayoutManager  
 android.support.v7.widget.CardView  
 android.support.v7.graphics.Palette  
 android.support.v7.app.AlertDialog  
 android.support.annotation.IdRes  
 android.support.v7.app.ActionBar

**支持控件的新包名**  
 androidx.fragment.app.Fragment  
 androidx.fragment.app.FragmentActivity  
 androidx.fragment.app.FragmentManager  
 androidx.fragment.app.FragmentPagerAdapter  
 androidx.viewpager.widget.ViewPager  
 androidx.viewpager.widget.PagerAdapter  
 androidx.viewpager.widget.PagerTabStrip  
 androidx.viewpager.widget.PagerTitleStrip  
 androidx.appcompat.app.AppCompatActivity  
 androidx.appcompat.widget.Toolbar  
 androidx.recyclerview.widget.RecyclerView  
 androidx.recyclerview.widget.GridLayoutManager  
 androidx.recyclerview.widget.LinearLayoutManager  
 androidx.recyclerview.widget.StaggeredGridLayoutManager  
 androidx.cardview.widget.CardView  
 androidx.palette.graphics.Palette  
 androidx.appcompat.app.AlertDialog  
 androidx.annotation.IdRes  
 androidx.appcompat.app.ActionBar

另外还有一篇可供参考，[点这里](https://www.jianshu.com/p/504857b51e93)
