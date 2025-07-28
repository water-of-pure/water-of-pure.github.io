+++
date = '2025-07-28T17:48:57.305568+08:00'
draft = false
title = 'Spring Boot基础之简单的路由配置'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"
]
+++

使用mavn创建项目我就不多说了，可以根据前面的历史文章进行操作，启动文件的内容我也不展示里，跟前面文章介绍的是一样的，这里介绍下路由具体使用，代码如下

创建一个文件UserController.java

```java
package com.walkerfree.controller;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
@Controller
@RequestMapping("/user")
public class UserController {
    @RequestMapping(value="/{user}", method= RequestMethod.GET)
    public String getUser(@PathVariable Long user, Model model) {
        model.addAttribute("user", user);
        return "user/detail";
    }
    @RequestMapping(value = "/{user}/customers", method = RequestMethod.GET)
    public String getUserCustomers(@PathVariable Long user, Model model) {
        model.addAttribute("user", user);
        return "user/customer";
    }
    @RequestMapping(value="/{user}", method = RequestMethod.DELETE)
    public String deleteUser(@PathVariable Long user, Model model) {
        model.addAttribute("user", user);
        return "user/delete";
    }
}
```

可以看到

```java
@RequestMapping(value="/{user}", method=RequestMethod.GET)
```

value对应的是访问的路径，method对应的是访问的方法配置

method支持的方法如下

> DELETE
>
> GET
>
> HEAD
>
> OPTIONS
>
> PATCH
>
> POST
>
> PUT
>
> TRACE

```java
value="/{user}"
```

这里的{user}是个需要传出的参数值，如果你对其他框架熟悉的话，应该会比较容易理解

```bash
http://localhost:8080/user/1
```

这里的1就是对应的{user}这个参数，我们可以在模板中进行调用

```java
@Controller
@RequestMapping("/user")
```

这里的"/user"其实是在所有方法中设置的路径的前面加上都会默认加入此路径，这个是比较好的，防止自己多次重复操作了。

由于这里使用了模板，所以还需要建立对应的模板，具体模板的目录resources结构如下

```bash
├── public
└── templates
    └── user
        ├── customer.ftl
        ├── delete.ftl
        └── detail.ftl
```

上面一切做完之后，启动项目就可以正常访问了

项目的代码我放在这里了需要的可以下载看下

<https://github.com/durban89/spring_boot_simple_router_configuration>
