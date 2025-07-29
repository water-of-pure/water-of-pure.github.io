+++
date = '2025-07-28T17:52:18.177683+08:00'
draft = false
title = 'Spring Boot基础之调度任务'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot",

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1599746333/walkerfree/spring-boot.jpg"
+++

1、首先创建一个调度任务

src/main/java/com/walkerfree/ScheduledTasks.java

```java

package com.walkerfree;
import java.text.SimpleDateFormat;
import java.util.Date;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
@Component
public class ScheduledTasks {
    private static final Logger log = LoggerFactory.getLogger(ScheduledTasks.class);
    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
    @Scheduled(fixedRate = 5000)
    public void reportCurrentTime() {
        log.info("The time is now {}", dateFormat.format(new Date()));
    }
}
```

@Scheduled注解定义了特定方法的运行时间。

此示例使用fixedRate，它指定从每次调用的开始时间开始测量的方法调用之间的时间间隔。

还有其他选项，比如fixedDelay，它指定了从任务完成之后测量的调用之间的时间间隔。

您还可以使用@Scheduled（cron =“...”）表达式来执行更复杂的任务计划。

2、启用调度任务

src/main/java/com/walkerfree/Application.java

```java

package com.walkerfree;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;
@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

@SpringBootApplication是一个很方便的注释，它增加了以下所有内容：

1】@Configuration 将类标记为定义了应用程序上下文的bean资源。

2】@EnableAutoConfiguration 通知Spring Boot根据类路径设置，其他bean和各种属性设置来开始添加beans

3】通常情况下，会为Spring MVC应用程序添加@EnableWebMvc，但Spring Boot在类路径中看到spring-webmvc时自动添加它。 这将该应用程序标记为Web应用程序并激活关键行为，例如设置DispatcherServlet。

4】@ComponentScan告诉Spring在com.walkerfree包中查找其他组件，配置和服务，以便找到控制器。

main()方法使用Spring Boot的SpringApplication.run()方法启动应用程序。 你有没有注意到没有一行XML？ 没有web.xml文件。 这个Web应用程序是100％纯Java，您不必处理配置任何管道或基础设施。

@EnableScheduling确保创建后台任务执行程序。 没有它调度任务不会执行

3、运行项目

```bash

mvn spring-boot:run
```

留意日志的输入，会有如下的输出

```bash

2018-04-27 11:38:11.572  INFO 11747 --- [pool-1-thread-1] com.walkerfree.ScheduledTasks            : The time is now 11:38:11
2018-04-27 11:38:16.571  INFO 11747 --- [pool-1-thread-1] com.walkerfree.ScheduledTasks            : The time is now 11:38:16
2018-04-27 11:38:21.572  INFO 11747 --- [pool-1-thread-1] com.walkerfree.ScheduledTasks            : The time is now 11:38:21
2018-04-27 11:38:26.572  INFO 11747 --- [pool-1-thread-1] com.walkerfree.ScheduledTasks            : The time is now 11:38:26

```

实例代码参考：<https://github.com/durban89/simple_dynamic_webpage>，tag:003
