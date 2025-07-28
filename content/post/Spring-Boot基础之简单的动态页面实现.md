+++
date = '2025-07-28T17:52:11.860026+08:00'
draft = false
title = 'Spring Boot基础之简单的动态页面实现'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

之前的文章已经写过如何实现一个简单的静态页面，这里简单介绍下如何写一个动态的页面，

这里已最简单为主，项目的常见我就不具体介绍了

pom.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project 
    xmlns="http://maven.apache.org/POM/4.0.0" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.walkerfree</groupId>
    <artifactId>simple_dynamic_webpage</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.0.0.RELEASE</version>
    </parent>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-freemarker</artifactId>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

Application.java

```java
package com.walkerfree;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

WelcomeController.java

```java
package com.walkerfree.controller;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
/**
 * WelcomeController
 */
@Controller
public class WelcomeController {
    @RequestMapping("/")
    public String index(Model model) {
        // 这里我们设置动态数据 - 每访问页面一次，数据都会从服务器重新获取新的数据
        SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-d HH:mm:ss");
        String dateString = df.format(new Date());
        model.addAttribute("time", dateString);
        return "welcome/index";
    }
}
```

目录结果如下

```bash
.
├── pom.xml
├── src
│   └── main
│       ├── java
│       │   └── com
│       │       └── walkerfree
│       │           ├── Application.java
│       │           └── controller
│       │               └── WelcomeController.java
│       └── resources
│           ├── public
│           └── templates
│               └── welcome
│                   └── index.ftl
└── target
```

运行项目mvn spring-boot:run

访问页面我会看到一个动态变化的时间，如下

![Image](https://cdn.xiaorongmao.com/up/128-1.png)

具体的代码可以去github上获取:<https://github.com/durban89/simple_dynamic_webpage>

只是一个简单的时间动态展示，后面会有个复杂一点的，比如一个简单的博客。再次之前我们还是要把一些基础的了解完。
