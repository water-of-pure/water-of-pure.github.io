+++
date = '2025-07-28T17:52:21.339067+08:00'
draft = false
title = 'Spring Boot基础之构建一个REST风格的Web服务'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

1、创建一个资源表示类

该服务将处理/playing的GET请求，可选地在查询字符串中使用名称参数。 GET请求时应该返回带有JSON的200 OK响应。 它应该看起来像这样：

```bash
{
    "autokid": 1,
    "content": "Playing Football!"
}
```

> autokid字段是唯一标识符
>
> content是内容的文字表示

2、建模，创建一个资源表示类。

为autokid和content数据提供一个普通的java对象，其中包含字段，构造函数和访问器：

src/main/java/com/walkerfree/Playing.java

```java
package com.walkerfree;
/**
 * Playing
 */
public class Playing {
    private final long autokid;
    private final String content;
    public Playing(long autokid, String content) {
        this.autokid = autokid;
        this.content = content;
    }
    /**
     * @return the autokid
     */
    public long getAutokid() {
        return autokid;
    }
    /**
     * @return the content
     */
    public String getContent() {
        return content;
    }
}
```

3、创建资源控制器

在Spring构建RESTful Web服务的方法中，HTTP请求由控制器处理。 这些组件可以通过@RestController轻松识别，并且PlayingController通过返回Playing类的新实例来处理/playing的GET请求：

src/main/java/com/walkerfree/controller/PlayingController.java

```java
package com.walkerfree.controller;
import java.util.concurrent.atomic.AtomicLong;
import com.walkerfree.Playing;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
/**
 * PlayingController
 */
@RestController
public class PlayingController {
    private static final String template = "Playing %s!";
    private final AtomicLong atomic = new AtomicLong();
    @RequestMapping("/playing")
    public Playing playing(@RequestParam(value = "name", defaultValue = "Football") String name) {
        return new Playing(atomic.incrementAndGet(), String.format(template, name));
    }
}
```

这个控制器是比较简练的，但是它却做了很多事情，让我们一步一步分解它

@RequestMapping注解确保HTTP请求到/playing的时候能够映射到playing()方法

@RequestParam绑定了查询参数字符串的name参数到playing()方法中.如果请求的name参数不存在, 默认的“Football”将被使用

方法体的实现了带有autokid和content属性的Playing对象的返回，autokid是基于atomic生成值，content是模板格式化name后生成的字符串

重点：传统的MVC控制器和上面的RESTful Web服务控制器之间的一个主要区别在于HTTP响应主体的创建方式。 这个RESTful Web服务控制器只需填充并返回一个Playing对象，而不是依赖视图技术将生成数据的服务器端呈现给HTML。 对象数据将作为JSON直接写入HTTP响应。

此代码使用Spring 4的新的@RestController注释，该注释将类标记为控制器，其中每个方法都返回一个域对象而不是视图。 它是@Controller和@ResponseBody的缩写。

Playing对象必须转换为JSON。 由于Spring的HTTP消息转换器支持，您不需要手动执行此转换。 由于Jackson 2位于类路径中，因此会自动选择Spring的MappingJackson2HttpMessageConverter将Playing实例转换为JSON。

4、运行代码

```bash
mvn spring-boot:run
```

访问<http://localhost:8080/playing?name=pingpang>会得到类似如下输出

```bash
{
    autokid: 3,
    content: "Playing pingpang!"
}
```

实例代码参考：<https://github.com/durban89/simple_dynamic_webpage>，tag:004
