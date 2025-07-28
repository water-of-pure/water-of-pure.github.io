+++
date = '2025-07-28T17:48:35.638212+08:00'
draft = false
title = '初步了解Spring Boot'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

**1、安装Spring Boot CLI**

可以通过下载Spring CLI安装包进行安装

具体的版本安装可以到这里下载

<https://docs.spring.io/autorepo/docs/spring-boot/current/reference/html/getting-started-installing-spring-boot.html#getting-started-homebrew-cli-installation>

本人使用OSX，演示下如何在OSX下安装,【brew的安装请自行百度】

执行如下命令

```bash
brew tap pivotal/tap
```

得到如下输出，表示执行成功

```bash
Cloning into '/usr/local/Homebrew/Library/Taps/pivotal/homebrew-tap'...
remote: Counting objects: 15, done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 15 (delta 0), reused 6 (delta 0), pack-reused 0
Unpacking objects: 100% (15/15), done.
Tapped 10 formulae (50 files, 37.3KB)
```

在执行下面命令

```bash
brew install springboot
```

得到如下输出，表示执行成功

```bash
==> Installing springboot from pivotal/tap
==> Downloading https://repo.spring.io/release/org/springframework/boot/spring-boot-cli/2.0.0.RELEASE/spring-boot-cli-2.0.0.RELEASE-bin.tar.gz
Already downloaded: /Users/durban/Library/Caches/Homebrew/springboot-2.0.0.RELEASE.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
zsh completions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
/usr/local/Cellar/springboot/2.0.0.RELEASE: 7 files, 9.6MB, built in 1 second
```

下面我们来演示一个例子

创建文件hello.groovy

代码内容如下

```groovy
@RestController
class WebApplication {
	@RequestMapping('/')
	String home() {
		"Hello World! Spring"
	}
}
```

保存后，执行下面命令

```bash
spring run hello.groovy
```

得到如下输出后，表示执行运行成功

```bash
$ spring run hello.groovy

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::        (v1.5.9.RELEASE)

2018-03-14 21:51:28.977  INFO 44846 --- [       runner-0] o.s.boot.SpringApplication               : Starting application on durbanzhangdeMacBook-Pro with PID 44846 (started by durban in /Users/durban/java)
2018-03-14 21:51:28.993  INFO 44846 --- [       runner-0] o.s.boot.SpringApplication               : No active profile set, falling back to default profiles: default
2018-03-14 21:51:29.352  INFO 44846 --- [       runner-0] ationConfigEmbeddedWebApplicationContext : Refreshing org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@f88b4c3: startup date [Wed Mar 14 21:51:29 CST 2018]; root of context hierarchy
2018-03-14 21:51:31.638  INFO 44846 --- [       runner-0] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat initialized with port(s): 8080 (http)
2018-03-14 21:51:31.656  INFO 44846 --- [       runner-0] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2018-03-14 21:51:31.658  INFO 44846 --- [       runner-0] org.apache.catalina.core.StandardEngine  : Starting Servlet Engine: Apache Tomcat/8.5.23
2018-03-14 21:51:31.772  INFO 44846 --- [ost-startStop-1] org.apache.catalina.loader.WebappLoader  : Unknown loader org.springframework.boot.cli.compiler.ExtendedGroovyClassLoader$DefaultScopeParentClassLoader@22d12a12 class org.springframework.boot.cli.compiler.ExtendedGroovyClassLoader$DefaultScopeParentClassLoader
2018-03-14 21:51:31.913  INFO 44846 --- [ost-startStop-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2018-03-14 21:51:31.914  INFO 44846 --- [ost-startStop-1] o.s.web.context.ContextLoader            : Root WebApplicationContext: initialization completed in 2567 ms
2018-03-14 21:51:32.126  INFO 44846 --- [ost-startStop-1] o.s.b.w.servlet.ServletRegistrationBean  : Mapping servlet: 'dispatcherServlet' to [/]
2018-03-14 21:51:32.135  INFO 44846 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'characterEncodingFilter' to: [/*]
2018-03-14 21:51:32.136  INFO 44846 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'hiddenHttpMethodFilter' to: [/*]
2018-03-14 21:51:32.136  INFO 44846 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'httpPutFormContentFilter' to: [/*]
2018-03-14 21:51:32.136  INFO 44846 --- [ost-startStop-1] o.s.b.w.servlet.FilterRegistrationBean   : Mapping filter: 'requestContextFilter' to: [/*]
2018-03-14 21:51:32.586  INFO 44846 --- [       runner-0] s.w.s.m.m.a.RequestMappingHandlerAdapter : Looking for @ControllerAdvice: org.springframework.boot.context.embedded.AnnotationConfigEmbeddedWebApplicationContext@f88b4c3: startup date [Wed Mar 14 21:51:29 CST 2018]; root of context hierarchy
2018-03-14 21:51:32.719  INFO 44846 --- [       runner-0] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/]}" onto public java.lang.String WebApplication.home()
2018-03-14 21:51:32.722  INFO 44846 --- [       runner-0] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error]}" onto public org.springframework.http.ResponseEntity<java.util.Map<java.lang.String, java.lang.Object>> org.springframework.boot.autoconfigure.web.BasicErrorController.error(javax.servlet.http.HttpServletRequest)
2018-03-14 21:51:32.723  INFO 44846 --- [       runner-0] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/error],produces=[text/html]}" onto public org.springframework.web.servlet.ModelAndView org.springframework.boot.autoconfigure.web.BasicErrorController.errorHtml(javax.servlet.http.HttpServletRequest,javax.servlet.http.HttpServletResponse)
2018-03-14 21:51:32.791  INFO 44846 --- [       runner-0] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/webjars/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-14 21:51:32.791  INFO 44846 --- [       runner-0] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-14 21:51:32.865  INFO 44846 --- [       runner-0] o.s.w.s.handler.SimpleUrlHandlerMapping  : Mapped URL path [/**/favicon.ico] onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
2018-03-14 21:51:33.565  INFO 44846 --- [       runner-0] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2018-03-14 21:51:33.689  INFO 44846 --- [       runner-0] s.b.c.e.t.TomcatEmbeddedServletContainer : Tomcat started on port(s): 8080 (http)  

```

访问[http://localhost:8080](http://localhost:8080/)可以看到输出“Hello World! Spring”

Ctrl+c 可以终止运行

```bash
$ java -version
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)  

```
