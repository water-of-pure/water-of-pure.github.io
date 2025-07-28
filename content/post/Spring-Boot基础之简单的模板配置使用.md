+++
date = '2025-07-28T17:48:51.340452+08:00'
draft = false
title = 'Spring Boot基础之简单的模板配置使用'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

具体的项目创建这里不再介绍，可以参考之前的文章

这里先介绍下项目初始状态的目录结构

```bash
├── pom.xml
├── simple_page.iml
└── src
    └── main
        ├── java
        │   └── com
        │       └── gowhich
        │           └── Application.java
        └── resources
            └── static
                └── index.html
```

**1、FreeMarker模板的使用**

FreeMarker模板的使用很简单，默认就是被支持的

***1) 修改pom.xml添加如下内容***

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-freemarker</artifactId>
</dependency>
```

最后pom.xml文件如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.gowhich</groupId>
	<artifactId>simple_page</artifactId>
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

***2) 在resources目录下建立一个文件夹templates,在templates下面创建一个文件index.ftl,里面的内容如下***

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The FreeMarker Template Page</title>
</head>
<body>
<div>
    <center>The FreeMarker Template Page - ${title}</center>
</div>
</body>
</html>
```

***3) 创建一个controller来调用我们创建的index.ftl***

创建WelcomeController.java ，内容如下

```java
package com.gowhich.controller;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
@Controller
public class WelcomeController {
    @RequestMapping("web/index")
    public String webIndex() {
        return "index";
    }
}
```

目录结构如下

```bash
├── pom.xml
├── simple_page.iml
└── src
    └── main
        ├── java
        │   └── com
        │       └── gowhich
        │           ├── Application.java
        │           └── controller
        │               └── WelcomeController.java
        └── resources
            ├── static
            │   └── index.html
            └── templates
                └── index.ftl
```

***4) 运行项目，并访问<http://localhost:8080/web/index>，会得到如下输出***

![Image](https://cdn.xiaorongmao.com/up/127-1.png)

**2、Thymeleaf模板的使用**

***1) 修改pom.xml添加如下内容***

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
```

最后pom.xml文件如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>
	<groupId>com.gowhich</groupId>
	<artifactId>simple_page</artifactId>
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
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-thymeleaf</artifactId>
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

***2) 为了跟FreeMaker区分，在templates目录下建立一个目录thymeleaf，然后添加文件user.html，里面的内容如下***

```html
<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title th:text="${title}"></title>
</head>
<body>
<div>
    <center th:text="${content}"></center>
</div>
</body>
</html>
```

***3) 修改controller文件，WelcomeController.java ，变更后的内容如下***

```java
package com.gowhich.controller;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
@Controller
public class WelcomeController {
    @RequestMapping("/web/index")
    public String webIndex(Model model) {
        model.addAttribute("title", "Walkerfree");
        return "index";
    }
    @RequestMapping("/web/user")
    public String webUser(Model model) {
        model.addAttribute("title", "Walkerfree");
        model.addAttribute("content", "The FreeMarker Template Page - Walkerfree");
        return "thymeleaf/user";
    }
}
```

更改后的目录结构如下

```bash
├── pom.xml
├── simple_page.iml
└── src
    └── main
        ├── java
        │   └── com
        │       └── gowhich
        │           ├── Application.java
        │           └── controller
        │               └── WelcomeController.java
        └── resources
            ├── static
            │   └── index.html
            └── templates
                ├── index.ftl
                └── thymeleaf
                    └── user.html
```

4) 运行项目，并访问<http://localhost:8080/web/user>，会得到如下输出

![Image](https://cdn.xiaorongmao.com/up/127-2.png)
