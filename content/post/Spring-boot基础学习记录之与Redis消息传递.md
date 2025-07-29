+++
date = '2025-07-29T10:09:03.390917+08:00'
draft = false
title = 'Spring boot基础学习记录之与Redis消息传递'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1537517093/walkerfree/wf_2.jpg"
+++

## **与Redis消息传递(Messaging with Redis)**

本篇文章学习下如何使用Spring Data Redis发布和订阅通过Redis发送的消息的过程。

一改之前的风格，之前的依赖库都使用的是Maven，本次换个风格，来尝试下Gradle，啊！敲个字都比Maven多一个字母，累呀，希望能体验到Gradle的优点，带给我一些开发效率的提升

## 1、Build With Gradle

Gradle原来的库如下，修改了很多，开始的时候，手动创建， 然后参考官网，将依赖一个一个的加进来了，最后发现少了一个gradlew，当时奇怪为什么没有，查了资料原来可以使用  
 gradle init创建，不过build.gradle需要重新生成，我就备份了一下，然后又重新的copy进来的，最后就有了下面的结果，开始的时候使用VScode，哎废了半天时间，也没有找到具体如何自动进行更新依赖的。  
 最后换了IntelliJ IDEA，果然强大，也说明了，要做Java开发，还是要有个这么强大的工具才行，果然体量重。

```groovy

buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("org.springframework.boot:spring-boot-gradle-plugin:2.0.5.RELEASE")
    }
}

apply plugin: 'java'
apply plugin: 'maven'
apply plugin: 'eclipse'
apply plugin: 'idea'
apply plugin: 'org.springframework.boot'
apply plugin: 'io.spring.dependency-management'

group = 'com.gowhich'
version = '0.0.1-SNAPSHOT'

description = """Demo project for Spring Boot"""

bootJar {
    baseName = 'spring-demo'
    version = '1.0'
}

sourceCompatibility = 1.8
targetCompatibility = 1.8
tasks.withType(JavaCompile) {
	options.encoding = 'UTF-8'
}

repositories {
    mavenCentral()
}
dependencies {
    compile group: 'org.springframework.boot', name: 'spring-boot-starter-web', version:'2.0.2.RELEASE'
    compile group: 'org.springframework.boot', name: 'spring-boot-starter-jdbc', version:'2.0.2.RELEASE'
    compile group: 'com.h2database', name: 'h2', version:'1.4.197'
    compile group: 'org.springframework.boot', name: 'spring-boot-starter-thymeleaf', version:'2.0.2.RELEASE'
    compile group: 'org.springframework.boot', name: 'spring-boot-starter-security', version:'2.0.2.RELEASE'
    compile group: 'org.springframework.ldap', name: 'spring-ldap-core', version:'2.3.2.RELEASE'
    compile group: 'org.springframework.security', name: 'spring-security-ldap', version:'5.0.5.RELEASE'
    compile group: 'com.unboundid', name: 'unboundid-ldapsdk', version:'4.0.5'
    compile group: 'org.springframework.social', name: 'spring-social-facebook', version:'2.0.3.RELEASE'
    compile group: 'com.fasterxml.jackson.core', name: 'jackson-core', version:'2.9.5'
    compile group: 'org.springframework.security', name: 'spring-security-crypto', version:'5.0.5.RELEASE'
    compile group: 'org.springframework.social', name: 'spring-social-core', version:'1.1.6.RELEASE'
    compile group: 'org.springframework.social', name: 'spring-social-security', version:'1.1.6.RELEASE'
    compile group: 'org.springframework.security', name: 'spring-security-core', version:'5.0.6.RELEASE'
    compile group: 'org.springframework.boot', name: 'spring-boot-starter-data-redis', version: '2.0.4.RELEASE'
    testCompile group: 'org.springframework.boot', name: 'spring-boot-starter-test', version:'2.0.2.RELEASE'
    testCompile group: 'org.springframework.security', name: 'spring-security-test', version:'5.0.5.RELEASE'
}
```

贴出来这么多，其实只有下面两行跟本次内容有关

```groovy

compile group: 'org.springframework.boot', name: 'spring-boot-starter-data-redis', version: '2.0.4.RELEASE'
```

主要是这个。

## 2、启动Redis服务器

在构建消息传递应用程序之前，需要设置将处理接收和发送消息的服务器。  
 Redis是一个开源的，BSD许可的键值数据存储，它还附带了一个消息传递系统。  
 该服务器可在http://redis.io/download免费获得。  
 您可以手动下载，或者如果您使用带自制程序的Mac：

```bash

brew install redis
```

解压缩Redis后，可以使用默认设置启动它。

```bash

redis-server
```

你应该看到这样的消息：

```bash

69673:C 21 Sep 15:38:57.755 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
69673:C 21 Sep 15:38:57.756 # Redis version=4.0.9, bits=64, commit=00000000, modified=0, pid=69673, just started
69673:C 21 Sep 15:38:57.756 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
69673:M 21 Sep 15:38:57.758 * Increased maximum number of open files to 10032 (it was originally set to 7168).
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 4.0.9 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 69673
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           http://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

69673:M 21 Sep 15:38:57.759 # Server initialized
69673:M 21 Sep 15:38:57.759 * DB loaded from disk: 0.000 seconds
69673:M 21 Sep 15:38:57.759 * Ready to accept connections
```

## 3、创建Redis消息接收器

在任何基于消息传递的应用程序中，都有消息发布者和消息接收者。  
 要创建消息接收器，需要实现具有响应消息的方法的接收器：  
 `src/main/java/com/gowhich/springdemo/Receiver.java`

```java

package com.gowhich.springdemo;

import java.util.concurrent.CountDownLatch;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;

public class Receiver {

    private static final Logger LOGGER = LoggerFactory.getLogger(Receiver.class);

    private CountDownLatch latch;

    @Autowired
    public Receiver(CountDownLatch latch) {
        this.latch = latch;
    }

    public void receiveMessage(String message) {
        LOGGER.info("Received <" + message + ">");
        latch.countDown();
    }
}
```

Receiver是一个简单的POJO，它定义了一种接收消息的方法。  
 正如您在将Receiver注册为消息侦听器时所看到的那样，您可以根据需要为消息处理方法命名。

> 出于演示目的，它由构造函数自动装配，具有倒计时锁存器。这样，它可以在收到消息时发出信号。

## 4、注册监听器并发送消息

Spring Data Redis提供了使用Redis发送和接收消息所需的所有组件。具体来说，您需要配置：  
 1. 连接工厂  
 2. 消息侦听器容器  
 3. Redis模板

您将使用Redis模板发送消息，并且您将使用消息侦听器容器注册Receiver，以便它将接收消息。  
 连接工厂驱动模板和消息侦听器容器，使它们能够连接到Redis服务器。

此示例使用Spring Boot的默认RedisConnectionFactory，这是一个基于Jedis Redis库的JedisConnectionFactory实例。  
 连接工厂将注入消息侦听器容器和Redis模板。启动文件`src/main/java/com/gowhich/springdemo/SpringDemoApplication.java`中加入如下代码

```java

private static final Logger LOGGER = LoggerFactory.getLogger(SpringDemoApplication.class);

@Bean
RedisMessageListenerContainer container(RedisConnectionFactory connectionFactory, MessageListenerAdapter listenerAdapter) {
    RedisMessageListenerContainer container = new RedisMessageListenerContainer();
    container.setConnectionFactory(connectionFactory);
    container.addMessageListener(listenerAdapter, new PatternTopic("chat"));
    return container;
}

@Bean
MessageListenerAdapter listenerAdapter(Receiver receiver) {
    return new MessageListenerAdapter(receiver, "receiveMessage");
}

@Bean
Receiver receiver(CountDownLatch latch) {
    return new Receiver(latch);
}

@Bean
CountDownLatch latch() {
    return new CountDownLatch(1);
}

@Bean
StringRedisTemplate template(RedisConnectionFactory connectionFactory) {
    return new StringRedisTemplate(connectionFactory);
}

public static void main(String[] args) throws InterruptedException {
    ApplicationContext ctx = SpringApplication.run(SpringDemoApplication.class, args);

    StringRedisTemplate template = ctx.getBean(StringRedisTemplate.class);
    CountDownLatch latch = ctx.getBean(CountDownLatch.class);

    LOGGER.info("Sending message ...");

    template.convertAndSend("chat", "Hello from walkerfree!");

    latch.await();

    System.exit(0);
}
```

listenerAdapter方法中定义的bean在容器中定义的消息侦听器容器中注册为消息侦听器，并将侦听"chat"主题上的消息。  
 由于Receiver类是POJO，因此需要将其包装在消息侦听器适配器中，该适配器实现addMessageListener()所需的MessageListener接口。  
 消息侦听器适配器还配置为在消息到达时调用Receiver上的receiveMessage()方法。  
 连接工厂和消息监听器容器bean是监听消息所需的全部内容。  
 要发送消息，您还需要Redis模板。  
 这里，它是一个配置为StringRedisTemplate的bean，它是RedisTemplate的一个实现，专注于Redis的常用用法，其中键和值都是`String`s。  
 main()方法通过创建Spring应用程序上下文来解决所有问题。  
 然后，应用程序上下文启动消息侦听器容器，并且消息侦听器容器bean开始侦听消息。  
 然后main()方法从应用程序上下文中检索StringRedisTemplate bean，并使用它发送"Hello from walkerfree!"  
 关于"chat"主题的消息。  
 最后，它关闭Spring应用程序上下文，应用程序结束。

## 5、构建可执行的JAR

您可以使用Gradle或Maven从命令行运行该应用程序。  
 或者，您可以构建一个包含所有必需依赖项，类和资源的可执行JAR文件，并运行该文件。  
 这使得在整个开发生命周期中，跨不同环境等将服务作为应用程序发布，版本和部署变得容易。

使用`./gradlew bootRun`运行该应用程序。  
 或者可以使用`./gradlew build`构建JAR文件。  
 然后你可以运行JAR文件：

```bash

java -jar build/libs/spring-demo-1.0.jar
```

您应该看到以下输出：

```bash

2018-09-21 15:25:48.158  INFO 69170 --- [           main] o.s.j.e.a.AnnotationMBeanExporter        : Registering beans for JMX exposure on startup
2018-09-21 15:25:48.179  INFO 69170 --- [           main] o.s.c.support.DefaultLifecycleProcessor  : Starting beans in phase 2147483647
2018-09-21 15:25:48.359  INFO 69170 --- [    container-1] io.lettuce.core.EpollProvider            : Starting without optional epoll library
2018-09-21 15:25:48.364  INFO 69170 --- [    container-1] io.lettuce.core.KqueueProvider           : Starting without optional kqueue library
2018-09-21 15:25:48.755  INFO 69170 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2018-09-21 15:25:48.764  INFO 69170 --- [           main] c.g.springdemo.SpringDemoApplication     : Started SpringDemoApplication in 9.342 seconds (JVM running for 9.993)
2018-09-21 15:25:48.783  INFO 69170 --- [           main] c.g.springdemo.SpringDemoApplication     : Sending message ...
2018-09-21 15:25:48.806  INFO 69170 --- [    container-2] com.gowhich.springdemo.Receiver          : Received <Hello from walkerfree!>
```
