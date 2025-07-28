+++
date = '2025-07-28T17:48:43.049072+08:00'
draft = false
title = 'Gradle 运行Spring Boot Application'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot",
    "Gradle"

]
+++

**1、gradle初始化**

执行如下命令

```bash
gradle init
```

执行后会生成如下文件

```bash
drwxr-xr-x  8 durban  staff   272  3 25 12:37 .
drwxr-xr-x  7 durban  staff   238  3 25 12:36 ..
drwxr-xr-x  4 durban  staff   136  3 25 12:37 .gradle
-rw-r--r--  1 durban  staff   201  3 25 12:37 build.gradle
drwxr-xr-x  3 durban  staff   102  3 25 12:37 gradle
-rwxr-xr-x  1 durban  staff  5296  3 25 12:37 gradlew
-rw-r--r--  1 durban  staff  2260  3 25 12:37 gradlew.bat
-rw-r--r--  1 durban  staff   351  3 25 12:37 settings.gradle
```

**2、编辑build.gradle**

在build.gradle文件下加入如下内容

```bash
plugins {
	id 'org.springframework.boot' version '2.0.0.RELEASE'
        id "io.spring.dependency-management" version "1.0.4.RELEASE"
	id 'java'
}
jar {
	baseName = 'myproject'
	version =  '0.0.1-SNAPSHOT'
}
repositories {
	jcenter()
}
dependencies {
	compile("org.springframework.boot:spring-boot-starter-web")
	testCompile("org.springframework.boot:spring-boot-starter-test")
}
```

**3、创建Spring Boot 实例代码**

在跟目录下创建src/main/java结构的目录，并创建文件src/main/java/Example.java

添加如下代码

```java
import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;
@RestController
@EnableAutoConfiguration
public class Example {
    @RequestMapping("/")
    String home() {
        return "Hello World!";
    }
    public static void main(String[] args) throws Exception {
        SpringApplication.run(Example.class, args);
    }
}
```

4、启动实例项目

执行如下命令

```bash
gradle bootRun
```

会得到如下内容

```bash
Starting a Gradle Daemon, 1 stopped Daemon could not be reused, use --status for details
> Task :bootRun
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.0.0.RELEASE)
2018-03-25 12:58:25.611  INFO 62057 --- [           main] Example                                  : Starting Example on durbanzhangdeMacBook-Pro with PID 62057 (/Users/durban/java/test/build/classes/java/main started by durban in /Users/durban/java/test)
2018-03-25 12:58:25.615  INFO 62057 --- [           main] Example                                  : No active profile set, falling back to default profiles: default
2018-03-25 12:58:25.694  INFO 62057 --- [           main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@6279cee3: startup date [Sun Mar 25 12:58:25 CST 2018]; root of context hierarchy
2018-03-25 12:58:27.350  INFO 62057 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2018-03-25 12:58:27.400  INFO 62057 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2018-03-25 12:58:27.400  INFO 62057 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/8.5.28
2018-03-25 12:58:27.417  INFO 62057 --- [ost-startStop-1] o.a.catalina.core.AprLifecycleListener   : The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path: [/Users/durban/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.]
2018-03-25 12:58:27.561  INFO 62057 --- [ost-startStop-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2018-03-25 12:58:27.561  INFO 62057 --- [ost-startStop-1] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 1870 ms
2018-03-25 12:58:27.758  INFO 62057 --- [ost-startStop-1] o.s.b.w.servlet.ServletRegistrationBean  : Servlet dispatcherServlet mapped to [/]
2018-03-25 12:58:27.764  INFO 62057 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'characterEncodingFilter' to: [/*]
2018-03-25 12:58:27.765  INFO 62057 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'hiddenHttpMethodFilter' to: [/*]
2018-03-25 12:58:27.765  INFO 62057 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'httpPutFormContentFilter' to: [/*]
2018-03-25 12:58:27.765  INFO 62057 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'requestContextFilter' to: [/*]
2018-03-25 12:58:28.259  INFO 62057 --- [           main] s.w.s.m.m.a.RequestMappingHandlerAdapter : Looking for @ControllerAdvice: org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@6279cee3: startup date [Sun Mar 25 12:58:25 CST 2018]; root of context hierarchy
2018-03-25 12:58:28.377  INFO 62057 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/]}" onto java.lang.String Example.home()
2018-03-25 12:58:28.389  INFO 62057 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.servlet.error.BasicErrorController.error(javax.servlet.http.HttpServletRequest)
2018-03-25 12:58:28.390  INFO 62057 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error],produces=[text/html]}" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.servlet.error.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)
2018-03-25 12:58:28.432  INFO 62057 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-25 12:58:28.432  INFO 62057 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-25 12:58:28.480  INFO 62057 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-25 12:58:28.701  INFO 62057 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2018-03-25 12:58:28.770  INFO 62057 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2018-03-25 12:58:28.776  INFO 62057 --- [           main] Example                                  : Started Example in 3.815 seconds (JVM running for 4.321)
<=========----> 75% EXECUTING [19s]
> :bootRun
```

打开浏览器访问localhost:8080

会得到输出内容 “Hello World!”

**5、创建可执行的jar文件**

修改build.gradle,在jar中添加enabled=true,最后build.gradle结果如下

```bash
plugins {
	id 'org.springframework.boot' version '2.0.0.RELEASE'
        id "io.spring.dependency-management" version "1.0.4.RELEASE"
	id 'java'
}

jar {
	baseName = 'myproject'
	version =  '0.0.1-SNAPSHOT'
        enabled = true
}

repositories {
	jcenter()
}

dependencies {
	compile("org.springframework.boot:spring-boot-starter-web")
	testCompile("org.springframework.boot:spring-boot-starter-test")
}
```

修改完后执行如下命令

```bash
spring bootRun
```

会在build目录下下libs目录下生成文件\*.jar

通过命令运行jar文件

```bash
java -jar xxx.jar
```

会得到4步骤中的输出。
