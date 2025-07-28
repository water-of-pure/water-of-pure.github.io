+++
date = '2025-07-28T17:52:15.191192+08:00'
draft = false
title = 'Spring Boot基础之数据库连接'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

1、首先配置下我们连接数据库需要的包

第一个需要的是

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>
```

第二个需要的是

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
```

将上面两个依赖加入到pom.xml中，最后的结果如下

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
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-freemarker</artifactId>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <properties>
        <java.version>1.8</java.version>
    </properties>
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

2、创建application.properties文件

创建一个文件src/main/resources/application.properties，添加如下内容

```bash
spring.jpa.hibernate.ddl-auto=create
spring.datasource.url=jdbc:mysql://localhost:3306/db_example
spring.datasource.username=username
spring.datasource.password=password
```

spring.jpa.hibernate.ddl-auto这里的值可以是none,update,create,create-drop,具体的详情，请参阅Hibernate文档

> none: 对于mysql这个是默认的，不需要对数据结构进行改变.
>
> update: 根据Entity的结构，Hibernate改变了数据结构.
>
> create: 每次都会创建数据库但是关闭的时候不会drop数据库.
>
> create-drop: 创建数据库并且当SessionFactory关闭的时候drop数据库.

3、创建一个@Entity model

src/main/java/com/walkerfree/model/User.java

```java
package com.walkerfree.model;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
@Entity // 这告诉Hibernate从这个类中创建一个表
public class User {
    @Id
    @GeneratedValue(strategy=GenerationType.AUTO)
    private Integer id;
    private String name;
    private String email;
    /**
     * @return the email
     */
    public String getEmail() {
        return email;
    }
    /**
     * @param email the email to set
     */
    public void setEmail(String email) {
        this.email = email;
    }
    /**
     * @return the id
     */
    public Integer getId() {
        return id;
    }
    /**
     * @param id the id to set
     */
    public void setId(Integer id) {
        this.id = id;
    }
    /**
     * @return the name
     */
    public String getName() {
        return name;
    }
    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }
}
```

这是Hibernate自动转换成表的实体类。

4、创建repository

```java
package com.walkerfree.repository;
import com.walkerfree.model.User;
import org.springframework.data.repository.CrudRepository;
/**
 * This will be AUTO IMPLEMENTED by Spring into a Bean called userRepository
 * CRUD refers Create, Read, Update, Delete
 */
public interface UserRepository extends CrudRepository<User, Long> {
}
```

5、创建一个controller，叫做UserController.java

```java
package com.walkerfree.controller;
import com.walkerfree.model.User;
import com.walkerfree.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
/**
 * UserController
 */
@Controller // 这里的意思是这个类是一个控制器类
@RequestMapping("/user") // 这里的意思是 URL是/user开始的
public class UserController {
    @Autowired // 这里的意思是获得一个bean叫做userRepository，userRepository是Spring自动产生的，我们将用它来控制数据
    private UserRepository userRepository;
    @GetMapping(path = "/add") // 只Map到GET请求
    public @ResponseBody String addNewUser(@RequestParam String name, @RequestParam String email) {
        // @ResponseBody 意思是返回的String是一个响应体，不是一个视图的名称
        // @RequestParam 意思是从GET或POST请求的一个参数
        User u = new User();
        u.setName(name);
        u.setEmail(email);
        userRepository.save(u);
        return "Saved";
    }
    public @ResponseBody Iterable<User> getAllUsers() {
        return userRepository.findAll();
    }
}
```

@GetMapping是@RequestMapping(method=GET)的简写

6、运行项目

运行项目后，我们查看下我们的数据库，其实是自动帮我们建立了对应的表，大家可以留意下。当我们停掉项目再次重启项目时，数据库的表会自动被新建。

实例代码需要的话到这里：<https://github.com/durban89/simple_dynamic_webpage>，tag:002
