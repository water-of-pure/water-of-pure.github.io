+++
date = '2025-07-28T17:52:39.648135+08:00'
draft = false
title = 'Spring Boot基础学习记录之Uploading Files(上传文件)部分代码解惑'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/c_scale,w_520/v1530106198/walkerfree/221692.jpg"
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

### **实践项目**

地址:

```bash

https://github.com/durban89/spring-demo.git

tag: v1.0.1
```

上次写了篇文章。大概是按照官网的例子做了下如何上传文件，这里温故下里面的细节代码部分

主要说下storage部分的代码 src/main/java/com/gowhich/springdemo/storage

```bash

├── FileSystemStorageService.java
├── StorageException.java
├── StorageFileNotFoundException.java
├── StorageProperties.java
└── StorageService.java
```

总的来说五个文件

* StorageService.java接口定义
* FileSystemStorageService.java上面接口方法实现
* StorageProperties.java存储的属性的定义
* StorageException.java
* StorageFileNotFoundException.java

一个接口类，一个接口实现类，两个异常类，异常类没啥说的

StorageProperties.java这个类中，注意下

```java

@ConfigurationProperties("storage")
```

这段代码，这段代码加入后，还需要在启动类文件SpringDemoApplication.java中加入

```java

@EnableConfigurationProperties(StorageProperties.class)
```

这段代码，不然会出问题，这个特性还是很诱人的，具体原理还望指点

StorageService.java这个类很好理解，就是一些关于存储相关的方法，具体的还是要看实现部分，来分析下FileSystemStorageService.java这个文件，这个文件注意需要加入@Service注解，便于后面的调用能自动找到对应的实现部分。

```java

public class FileSystemStorageService implements StorageService {
    private final Path rootLocation;

    @Autowired
    public FileSystemStorageService(StorageProperties properties) {
        this.rootLocation = Paths.get(properties.getLocation());
    }

    @Override
    public void init() { // 这部分初始化创建目录
        try {
            Files.createDirectories(rootLocation);
        } catch (IOException ex) {
            throw new StorageException("初始化存储空间失败", ex);
        }

    }

    @Override
    public void store(MultipartFile file) { // 这部分根据提交的文件来上传并存储到本地
        String filename = StringUtils.cleanPath(file.getOriginalFilename());
        try {
            if (filename.isEmpty()) {
                throw new StorageException("存储文件"+filename+"失败");
            }

            if (filename.contains("..")) {
                throw new StorageException("不能存储当前路径以外的文件"+filename);
            }

            try (InputStream inputStream = file.getInputStream()) {
                Files.copy(inputStream, this.rootLocation.resolve(filename), StandardCopyOption.REPLACE_EXISTING);
            }
        } catch (IOException ex) {
            throw new StorageException("存储文件"+filename+"失败", ex);
        }
    }

    @Override
    public Stream<Path> loadAll() { // 这部分加载目录下所有的文件
        try {
            return Files.walk(this.rootLocation, 1)
                    .filter(path -> !path.equals(this.rootLocation))
                    .map(this.rootLocation::relativize);
        } catch (IOException ex) {
            throw new StorageException("读取存储文件失败", ex);
        }
    }

    @Override
    public Path load(String filename) { // 这部分加载目录下某个文件
        return rootLocation.resolve(filename);
    }

    @Override
    public Resource loadAsResource(String filename) { // 这部分加载目录下某个文件的资源
        try {
            Path file = load(filename);
            Resource resource = new UrlResource(file.toUri());
            if (resource.exists() || resource.isReadable()) {
                return resource;
            } else {
                throw new StorageFileNotFoundException("不能读取文件" + filename);
            }
        } catch (MalformedURLException ex) {
            throw new StorageFileNotFoundException("不能读取文件" + filename, ex);
        }
    }

    @Override
    public void deleteAll() {
        FileSystemUtils.deleteRecursively(rootLocation.toFile());
    }

}
```

实现上并不难，难得是如何自己不看官网的例子，自己也能写一个出来，充分理解里面的逻辑。

存储部分实现后需要在启动类文件中加入初始化需要做的事情

```java

@Bean
CommandLineRunner init(StorageService storageService) {
    return (args) -> {
        storageService.deleteAll();
        storageService.init();
    };
}
```

删除目录下的原有的文件，并创建目录【如果目录不存在的话】

在FileUploadController.java中有一部分

```java

@ExceptionHandler({StorageFileNotFoundException.class})
public ResponseEntity<?> handleStorageFileNotFound(StorageFileNotFoundException ex) {
    return ResponseEntity.notFound().build();
}
```

异常处理，如果在操作过程中遇到异常的话，会进行异常的统一处理，这里有个中文乱码的问题，后面我找到办法在详细记录。
