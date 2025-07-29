+++
date = '2025-07-29T10:08:53.411968+08:00'
draft = false
title = 'Spring boot基础学习记录之使用Facebook注册一个应用'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

### **实践环境**

```bash

IDE
    Intellij IDEA[优点：自动安装新加依赖库]
JAVA
    java version "1.8.0_121"
    Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
    Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
```

实践项目初始化

我们以之前的项目为例，

地址:

```bash

https://github.com/durban89/spring-demo.git
tag: v1.0.3
```

官网的例子已经废弃了，这里还是说下整体的思路，截止今天2018-07-17，再有读者去官网如果还是看到这个例子，请不要在继续埰坑了，我已经踩雷了。而且一身的大粪。  
 不管是你在官网还是自己参照官网做了实例，最终都会报这个错误，错误的信息类似如下

> Caused by: org.springframework.web.client.ResourceAccessException: I/O error on POST request for "https://graph.facebook.com/v2.5/oauth/access\_token": Operation timed out (Connection timed out); nested exception is java.net.ConnectException: Operation timed out (Connection timed out)

我这里只演示一个具体使用的思路，如果是在其他的第三方注册应用的话，应该如何使用  
 Spring中首先是要加入需要的依赖库，这里我使用的是maven，如果想使用gradle的话，可以去官网参考下。https://spring.io/guides/gs/register-facebook-app/  
 pom.xml添加如下文件

```xml

<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-facebook</artifactId>
    <version>2.0.3.RELEASE</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-crypto</artifactId>
</dependency>
```

这里注意下

```xml

<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-facebook</artifactId>
    <version>2.0.3.RELEASE</version>
</dependency>
```

这里的引用，记得加下版本号，我在没有添加版本号的情况下，IntelliJ IDEA并没有自动安装此依赖库  
 然后创建文件内容如下

```java

package com.gowhich.springdemo;

import com.fasterxml.jackson.annotation.JsonProperty;
import org.springframework.social.facebook.api.Facebook;
import org.springframework.social.facebook.api.impl.FacebookTemplate;
import org.springframework.social.facebook.connect.FacebookConnectionFactory;
import org.springframework.social.oauth2.OAuth2Operations;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import javax.swing.*;

@Controller
public class SocialController {
    @GetMapping("social/facebook")
    public void facebook() {
        String appId = "xxx"; //promptForInput("输入App ID:");
        String appSecret = "xxx"; // promptForInput("输入App Secret:");
        String appToken = fetchApplicationAccessToken(appId, appSecret);
        AppDetail appDetail = fetchApplicationData(appId, appToken);
        System.out.println("\n 应用详情");
        System.out.println("=====================");
        System.out.println("ID:" + appDetail.getId());
        System.out.println("Name:" + appDetail.getName());
        System.out.println("Namespace: "+appDetail.getNamespace());
        System.out.println("Contact Email:"+appDetail.getContactEmail());
        System.out.println("Website Url:"+appDetail.getWebsiteUrl());
    }

    private static AppDetail fetchApplicationData(String appId, String appToken) {
        Facebook facebook = new FacebookTemplate(appToken);
        return facebook.restOperations().getForObject(
                "https://graph.facebook.com/{appId}?fields=name,namespace,contact_email,website_url",
                AppDetail.class,
                appId);
    }

    private static String fetchApplicationAccessToken(String appId, String appSecret) {
        OAuth2Operations oauth = new FacebookConnectionFactory(appId, appSecret).getOAuthOperations();
        return oauth.authenticateClient().getAccessToken();
    }

    private static String promptForInput(String promptText) {
        return JOptionPane.showInputDialog(promptText + " ");
    }

    private static final class AppDetail {
        private long id;
        private String name;
        private String namespace;

        @JsonProperty("contact_email")
        private String contactEmail;

        @JsonProperty("website_url")
        private String websiteUrl;

        public long getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public String getNamespace() {
            return namespace;
        }

        public String getContactEmail() {
            return contactEmail;
        }

        public String getWebsiteUrl() {
            return websiteUrl;
        }
    }

}
```

基础逻辑其实很清楚的

```java

String appToken = fetchApplicationAccessToken(appId, appSecret);
```

这行就是获取accessToken，通过请求Facebook的接口，根据appId和appSecret来获取AccessToken

```java

AppDetail appDetail = fetchApplicationData(appId, appToken);
```

这行代码意思通过获取的accessToken来获取指定接口需要的指定数据，这里的话就是获取应用本身的数据。实际测试的时候出现了问题，就是应用还没有走到这一步，在获取token的时候就已经出问题了。这个先不管，后面我做个解决方案在分享给大家。  
 从代码中还可以看到有一个promptForInput方法，这个我觉得官方挺奇怪的，不知道为什么突然调用了java UI的弹窗，不是web的alert之类的UI，这个别搞混，我是搞迷糊了，以为也可以弹出来，结果各种埰坑，最后弃用了。其实可以自己做一个web的输入框

AppDetail这个用来存储获取的数据的，从例子上看的话应该是会返回一个json的数据，这里就测试不到了，比较囧。

期待我下次的分享，埰坑踩到无法呼吸。

项目地址

```bash

https://github.com/durban89/spring-demo.git
tag: v1.0.4
```
