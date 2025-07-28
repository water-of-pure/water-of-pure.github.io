+++
date = '2025-07-28T17:48:47.322751+08:00'
draft = false
title = 'Spring Boot 基础之简单的静态页面实现'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"
]
+++

**1、使用maven创建Spring Boot Application [gradle的实现版本可以参考之前的文章]**

项目根目录创建pom.xml ，内容如下

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

**2、创建目录src/main/java**

```bash
mkdir -p src/main/java
```

**3、添加项目启动文件**

启动文件Application.java 内容如下

```java
package com.gowhich;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

整体的目录结构如下

**![Image](https://cdn.xiaorongmao.com/up/126-1.png)**

**4、创建目录src/main/resources/static**

在static目录下创建index.html文件，内容如下

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Static Page</title>
</head>
<body>
    <div>
        <center>Simple Static Page</center>
    </div>
</body>
</html>
```

5、启动项目

```bash
mvn spring-boot:run
```

得到如下输出代表启动成功

```bash
[INFO] Scanning for projects...
[INFO]
[INFO] ----------------------< com.gowhich:simple_page >-----------------------
[INFO] Building simple_page 0.0.1-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] >>> spring-boot-maven-plugin:2.0.0.RELEASE:run (default-cli) > test-compile @ simple_page >>>
[INFO]
[INFO] --- maven-resources-plugin:3.0.1:resources (default-resources) @ simple_page ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] Copying 0 resource
[INFO] Copying 1 resource
[INFO]
[INFO] --- maven-compiler-plugin:3.7.0:compile (default-compile) @ simple_page ---
[INFO] Changes detected - recompiling the module!
[INFO] Compiling 1 source file to /xxxxx/java/simple-page/target/classes
[INFO]
[INFO] --- maven-resources-plugin:3.0.1:testResources (default-testResources) @ simple_page ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory /xxxxx/java/simple-page/src/test/resources
[INFO]
[INFO] --- maven-compiler-plugin:3.7.0:testCompile (default-testCompile) @ simple_page ---
[INFO] No sources to compile
[INFO]
[INFO] <<< spring-boot-maven-plugin:2.0.0.RELEASE:run (default-cli) < test-compile @ simple_page <<<
[INFO]
[INFO]
[INFO] --- spring-boot-maven-plugin:2.0.0.RELEASE:run (default-cli) @ simple_page ---
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.0.0.RELEASE)
2018-03-27 13:46:21.107  INFO 5559 --- [           main] com.gowhich.Application                  : Starting Application on durbanzhangdeMacBook-Pro with PID 5559 (/xxxxx/java/simple-page/target/classes started by durban in /xxxxx/java/simple-page)
2018-03-27 13:46:21.115  INFO 5559 --- [           main] com.gowhich.Application                  : No active profile set, falling back to default profiles: default
2018-03-27 13:46:21.208  INFO 5559 --- [           main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@3434bc22: startup date [Tue Mar 27 13:46:21 CST 2018]; root of context hierarchy
2018-03-27 13:46:23.629  INFO 5559 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2018-03-27 13:46:23.701  INFO 5559 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2018-03-27 13:46:23.701  INFO 5559 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/8.5.28
2018-03-27 13:46:23.732  INFO 5559 --- [ost-startStop-1] o.a.catalina.core.AprLifecycleListener   : The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path: [/xxxxx/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.]
2018-03-27 13:46:23.887  INFO 5559 --- [ost-startStop-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2018-03-27 13:46:23.888  INFO 5559 --- [ost-startStop-1] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 2686 ms
2018-03-27 13:46:24.099  INFO 5559 --- [ost-startStop-1] o.s.b.w.servlet.ServletRegistrationBean  : Servlet dispatcherServlet mapped to [/]
2018-03-27 13:46:24.108  INFO 5559 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'characterEncodingFilter' to: [/*]
2018-03-27 13:46:24.109  INFO 5559 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'hiddenHttpMethodFilter' to: [/*]
2018-03-27 13:46:24.110  INFO 5559 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'httpPutFormContentFilter' to: [/*]
2018-03-27 13:46:24.114  INFO 5559 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'requestContextFilter' to: [/*]
2018-03-27 13:46:24.755  INFO 5559 --- [           main] s.w.s.m.m.a.RequestMappingHandlerAdapter : Looking for @ControllerAdvice: org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@3434bc22: startup date [Tue Mar 27 13:46:21 CST 2018]; root of context hierarchy
2018-03-27 13:46:24.909  INFO 5559 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.servlet.error.BasicErrorController.error(javax.servlet.http.HttpServletRequest)
2018-03-27 13:46:24.911  INFO 5559 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error],produces=[text/html]}" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.servlet.error.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)
2018-03-27 13:46:24.984  INFO 5559 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-27 13:46:24.984  INFO 5559 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-27 13:46:25.090  INFO 5559 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-27 13:46:25.147  INFO 5559 --- [           main] o.s.b.a.w.s.WelcomePageHandlerMapping    : Adding welcome page: class path resource [static/index.html]
2018-03-27 13:46:25.401  INFO 5559 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2018-03-27 13:46:25.488  INFO 5559 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2018-03-27 13:46:25.493  INFO 5559 --- [           main] com.gowhich.Application                  : Started Application in 5.141 seconds (JVM running for 11.502)
```

6、打开浏览器访问<http://localhost:8080/index.html>

得到类似如下输出的结果

![Image](https://cdn.xiaorongmao.com/up/126-2.png)

7、如果想添加其他的静态页面可以在static目录下继续添加你需要的静态文件

实例代码可参考Github:<https://github.com/durban89/spring_boot_simple_page/tree/master>
