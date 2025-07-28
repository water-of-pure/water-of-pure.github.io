+++
date = '2025-07-28T17:48:53.972385+08:00'
draft = false
title = 'Spring Boot基础之自定义错误页面'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

自定义错误页面网上有很多种方式，我这里只介绍下我认为很高效的方法

直接在模板目录下建立对应错误状态码的页面，比如错误码是404，我们建立一个404.ftl页面放入目录中，目录结构如下

```bash
├── java
│   └── com
│       └── walkerfree
│           ├── Application.java
│           └── controller
│               └── WelcomeController.java
└── resources
    ├── public
    │   └── error
    │       └── 404.html
    ├── static
    └── templates
        ├── error
        │   └── 404.ftl
        └── welcome
            └── index.ftl
```

运行项目，在遇到404的时候就会访问到templates/error/404.ftl这个页面

从上面的目录可以发现resources/public目录下面也有对应的错误页面，如果我们删除templates/error下面的文件会发现，在遇到错误404的时候会自动调用public目录下面的错误页面

注：resources/templates/error/ 这个的优先级比较 resources/public/error/高

当然也有通过Controller实现的，具体的我们下次再介绍

WelcomeController.java 的内容如下

```java
package com.walkerfree.controller;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
@Controller
public class WelcomeController {
    @RequestMapping("welcome/index")
    public String index(Model model) {
        model.addAttribute("title", "index");
        return "welcome/index";
    }
}
```

Application.java的代码如下

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

项目参考地址：<https://github.com/durban89/spring_boot_simple_custom_error_pages>
