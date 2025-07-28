+++
date = '2025-07-28T17:52:36.445716+08:00'
draft = false
title = 'Spring Boot基础学习记录之Uploading Files(上传文件)'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/c_scale,w_520/v1530026369/walkerfree/133230.jpg"
+++

### **实践环境**

```bash

IDE

    Intellij IDEA[优点：自动安装新加依赖库]

JAVA

    java version "1.8.0_121"

    Java(TM) SE Runtime Environment (build 1.8.0_121-b13)

    Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
```

### **实践项目初始化**

我们以之前的项目为例，

地址:

```bash

https://github.com/durban89/spring-demo.git

tag: v1.0.1
```

### **Maven配置**

pom.xml添加下面的依赖库，主要是后面的页面以thymeleaf作为模板

```xml

<dependency>

    <groupId>org.springframework.boot</groupId>

    <artifactId>spring-boot-starter-thymeleaf</artifactId>

</dependency>
```

### **创建StorageService与存储层进行交互，如"文件系统"**

src/main/java/com/gowhich/springdemo/StorageService.java

```java

package com.gowhich.springdemo.storage;

import org.springframework.core.io.Resource;
import org.springframework.web.multipart.MultipartFile;

import java.nio.file.Path;
import java.util.stream.Stream;

public interface StorageService {

    void init();

    void store(MultipartFile file);

    Stream<Path> loadAll();

    Path load(String filename);

    Resource loadAsResource(String filename);

    void deleteAll();
}
```

\*\*\*创建了存储层就要实现对接接口方法的实现，具体的可以拉取项目看下

### **创建上传文件的控制器**

src/main/java/com/gowhich/springdemo/FileUploadController.java

```java

package com.gowhich.springdemo;

import com.gowhich.springdemo.storage.StorageFileNotFoundException;
import com.gowhich.springdemo.storage.StorageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.method.annotation.MvcUriComponentsBuilder;
import org.springframework.core.io.Resource;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.IOException;
import java.util.stream.Collectors;

@Controller
public class FileUploadController {
    private final StorageService storageService;

    @Autowired
    public FileUploadController(StorageService storageService) {
        this.storageService = storageService;
    }

    @GetMapping("/")
    public String listUploadedFiles(Model model) throws IOException {
        model.addAttribute("files", storageService.loadAll().map(
                path -> MvcUriComponentsBuilder.fromMethodName(FileUploadController.class,
                        "serveFile", path.getFileName().toString()).build().toString())
                .collect(Collectors.toList()));

        return "uploadForm";
    }

    @GetMapping("/files/{filename:.+}")
    @ResponseBody
    public ResponseEntity<Resource> serveFile(@PathVariable String filename) {
        Resource resource = storageService.loadAsResource(filename);
        return ResponseEntity.ok().header(HttpHeaders.CONTENT_DISPOSITION,
                "attachment; filename=\"" + resource.getFilename() + "\"").body(resource);
    }

    @PostMapping("/")
    public String handleFileUpload(@RequestParam("file")MultipartFile file, RedirectAttributes redirectAttributes) {
        storageService.store(file);
        redirectAttributes.addFlashAttribute("message", "成功上传了文件 " + file.getOriginalFilename() + "!");
        return "redirect:/";
    }

    @ExceptionHandler({StorageFileNotFoundException.class})
    public ResponseEntity<?> handleStorageFileNotFound(StorageFileNotFoundException ex) {
        return ResponseEntity.notFound().build();
    }
}
```

### **创建一个HTML模板**

src/main/java/com/gowhich/springdemo/src/main/resources/templates/uploadForm.html

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>UploadForm</title>
</head>
<body>
    <div th:if="${message}">
        <h2 th:text="${message}"/>
    </div>

    <div>
        <form method="post" enctype="multipart/form-data" action="/">
            <table>
                <tr>
                    <td>
                        File to upload:
                    </td>
                    <td>
                        <input type="file" name="file" />
                    </td>
                </tr>
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="上传" />
                    </td>
                </tr>
            </table>
        </form>
    </div>
    <div>
        <ul>
            <li th:each="file: ${files}">
                <a th:href="${file}" th:text="${file}" />
            </li>
        </ul>
    </div>
</body>
</html>
```

### **调整文件上传限制**

src/main/resources/application.properties中添加

```bash

spring.servlet.multipart.max-file-size=128KB

spring.servlet.multipart.max-request-size=128KB

spring.servlet.multipart.enabled=true

spring.http.encoding.charset=UTF-8
```

### **Application配置**

src/main/java/com/gowhich/springdemo/SpringDemoApplication.java修改如下

```java

package com.gowhich.springdemo;

import com.gowhich.springdemo.storage.StorageProperties;
import com.gowhich.springdemo.storage.StorageService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
@EnableConfigurationProperties(StorageProperties.class)
public class SpringDemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(SpringDemoApplication.class, args);
    }

    @Bean
    CommandLineRunner init(StorageService storageService) {
        return (args) -> {
            storageService.deleteAll();
            storageService.init();
        };
    }
}
```

启动项目，我在Intellij IDEA直接可以操作启动，很方便

项目地址

```bash

https://github.com/durban89/spring-demo.git

tag: v1.0.2
```
