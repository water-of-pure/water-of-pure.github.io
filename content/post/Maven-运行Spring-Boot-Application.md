+++
date = '2025-07-28T17:48:38.627551+08:00'
draft = false
title = 'Maven 运行Spring Boot Application'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot",
    "Maven"

]
+++

**1、创建pom.xml ，pom.xml内容如下**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.example</groupId>
<artifactId>myproject</artifactId>
<version>0.0.1-SNAPSHOT</version>
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.0.RELEASE</version>
</parent>
<!-- Additional lines to be added here... -->
</project>
```

执行命令

```bash
mvn depencency:tree
```

maven会自动安装默认的依赖文件

**2、添加应用依赖**

当开发一个具体类型的应用时需要添加具体的依赖，当我们开发一个WEB应用的时候，我们添加一个spring-boot-starter-web依赖，为了添加依赖我们在文件pom.xml文件的parent部分下面添加如下代码

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
```

添加后代码如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.example</groupId>
<artifactId>myproject</artifactId>
<version>0.0.1-SNAPSHOT</version>
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.0.RELEASE</version>
</parent>
<!-- Additional lines to be added here... -->
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
</dependencies>
</project>
```

**3、创建类文件**

为了完成我们的应用，我们创建一个简单的Java文件，默认情况下，Maven从src/main/java编译源文件，因为我们创建一个src/main/java结构的目录，添加文件src/main/java/Example.java 代码内容如下

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

4、运行项目

```bash
mvn spring-boot:run
```

会得到如下输出

```bash
[INFO] Scanning for projects...
[INFO]
[INFO] -----------------------< com.example:myproject >------------------------
[INFO] Building myproject 0.0.1-SNAPSHOT
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] >>> spring-boot-maven-plugin:2.0.0.RELEASE:run (default-cli) > test-compile @ myproject >>>
[INFO]
[INFO] --- maven-resources-plugin:3.0.1:resources (default-resources) @ myproject ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory /Users/durban/java/spring-test/src/main/resources
[INFO] skip non existing resourceDirectory /Users/durban/java/spring-test/src/main/resources
[INFO]
[INFO] --- maven-compiler-plugin:3.7.0:compile (default-compile) @ myproject ---
[INFO] Nothing to compile - all classes are up to date
[INFO]
[INFO] --- maven-resources-plugin:3.0.1:testResources (default-testResources) @ myproject ---
[INFO] Using 'UTF-8' encoding to copy filtered resources.
[INFO] skip non existing resourceDirectory /Users/durban/java/spring-test/src/test/resources
[INFO]
[INFO] --- maven-compiler-plugin:3.7.0:testCompile (default-testCompile) @ myproject ---
[INFO] No sources to compile
[INFO]
[INFO] <<< spring-boot-maven-plugin:2.0.0.RELEASE:run (default-cli) < test-compile @ myproject <<<
[INFO]
[INFO]
[INFO] --- spring-boot-maven-plugin:2.0.0.RELEASE:run (default-cli) @ myproject ---
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v2.0.0.RELEASE)
2018-03-18 21:28:07.473  INFO 53370 --- [           main] Example                                  : Starting Example on durbanzhangdeMacBook-Pro with PID 53370 (/Users/durban/java/spring-test/target/classes started by durban in /Users/durban/java/spring-test)
2018-03-18 21:28:07.478  INFO 53370 --- [           main] Example                                  : No active profile set, falling back to default profiles: default
2018-03-18 21:28:07.593  INFO 53370 --- [           main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@66705b68: startup date [Sun Mar 18 21:28:07 CST 2018]; root of context hierarchy
2018-03-18 21:28:09.585  INFO 53370 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2018-03-18 21:28:09.679  INFO 53370 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2018-03-18 21:28:09.680  INFO 53370 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/8.5.28
2018-03-18 21:28:09.718  INFO 53370 --- [ost-startStop-1] o.a.catalina.core.AprLifecycleListener   : The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path: [/Users/durban/Library/Java/Extensions:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java:.]
2018-03-18 21:28:09.970  INFO 53370 --- [ost-startStop-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2018-03-18 21:28:09.970  INFO 53370 --- [ost-startStop-1] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 2384 ms
2018-03-18 21:28:10.143  INFO 53370 --- [ost-startStop-1] o.s.b.w.servlet.ServletRegistrationBean  : Servlet dispatcherServlet mapped to [/]
2018-03-18 21:28:10.149  INFO 53370 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'characterEncodingFilter' to: [/*]
2018-03-18 21:28:10.150  INFO 53370 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'hiddenHttpMethodFilter' to: [/*]
2018-03-18 21:28:10.150  INFO 53370 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'httpPutFormContentFilter' to: [/*]
2018-03-18 21:28:10.150  INFO 53370 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'requestContextFilter' to: [/*]
2018-03-18 21:28:10.597  INFO 53370 --- [           main] s.w.s.m.m.a.RequestMappingHandlerAdapter : Looking for @ControllerAdvice: org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext@66705b68: startup date [Sun Mar 18 21:28:07 CST 2018]; root of context hierarchy
2018-03-18 21:28:10.726  INFO 53370 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/]}" onto java.lang.String Example.home()
2018-03-18 21:28:10.734  INFO 53370 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.servlet.error.BasicErrorController.error(javax.servlet.http.HttpServletRequest)
2018-03-18 21:28:10.735  INFO 53370 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error],produces=[text/html]}" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.servlet.error.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)
2018-03-18 21:28:10.785  INFO 53370 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-18 21:28:10.785  INFO 53370 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-18 21:28:10.836  INFO 53370 --- [           main] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-18 21:28:11.058  INFO 53370 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2018-03-18 21:28:11.133  INFO 53370 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2018-03-18 21:28:11.139  INFO 53370 --- [           main] Example                                  : Started Example in 4.908 seconds (JVM running for 10.071)
```

访问localhost:8080，你将看到输出如下内容

```bash
Hello World!
```

**4、创建一个可执行的jar文件**

为了创建可执行的jar文件,我们添加spring-boot-maven-plugin到我们的pom.xml文件

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
        </plugin>
    </plugins>
</build>
```

添加后文件内容如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.example</groupId>
<artifactId>myproject</artifactId>
<version>0.0.1-SNAPSHOT</version>
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>2.0.0.RELEASE</version>
</parent>
<!-- Additional lines to be added here... -->
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

然后执行如下命令

```bash
mvn package
```

执行完后查看target目录，可以看到myproject-0.0.1-SNAPSHOT.jar文件，

为了运行项目，执行如下命令

```bash
java -jar target/myproject-0.0.1-SNAPSHOT.jar
```

得到的结果跟第4步一样的输出
