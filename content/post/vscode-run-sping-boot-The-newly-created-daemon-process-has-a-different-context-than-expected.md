+++
date = '2025-07-30T11:43:40.224154+08:00'
draft = false
title = 'vscode run spring boot - The newly created daemon process has a different context than expected'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1599746333/walkerfree/spring-boot.jpg'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"
]
+++

针对问题

先说下本机器默认java版本

```bash

$ java -version
java version "1.8.0_121"
Java(TM) SE Runtime Environment (build 1.8.0_121-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.121-b13, mixed mode)
```

在使用vscode创建spring boot项目的时候，遇到一个问题，就是vscode会提示你

> “Java 11 or more recent is required to run. Please download and install a recent JDK”

我以为应该要用java 11

于是我就用brew 安装了java 11，安装后的信息如下

```bash

$ brew info openjdk@11
openjdk@11: stable 11.0.8 (bottled) [keg-only]
Development kit for the Java programming language
https://openjdk.java.net/
/usr/local/Cellar/openjdk@11/11.0.8 (650 files, 295.3MB)
  Poured from bottle on 2020-10-19 at 12:19:32
From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/[email protected]
License: GPL-2.0
==> Dependencies
Build: autoconf ✔
==> Caveats
For the system Java wrappers to find this JDK, symlink it with
  sudo ln -sfn /usr/local/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk

openjdk@11 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have openjdk@11 first in your PATH run:
  echo 'export PATH="/usr/local/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc

For compilers to find openjdk@11 you may need to set:
  export CPPFLAGS="-I/usr/local/opt/openjdk@11/include"

==> Analytics
install: 29,975 (30 days), 70,671 (90 days), 111,102 (365 days)
install-on-request: 18,766 (30 days), 30,811 (90 days), 53,043 (365 days)
build-error: 0 (30 days)
```

然后我需要用到java 11在vscode中，在setting加入如下参数配置

```ini

"java.home": "/usr/local/Cellar/openjdk@11/11.0.8/"
```

然后运行sping boot项目，遇到了类似如下的问题

> The newly created daemon process has a different context than expected.  
>  It won't be possible to reconnect to this daemon. Context mismatch:   
>  Java home is different.  
>  Wanted: DefaultDaemonContext[...]  
>  Actual: DefaultDaemonContext[...]

经过google搜索一大堆的那个什么ide的问题

主要原因在这里

https://github.com/redhat-developer/vscode-java/wiki/JDK-Requirements#java.configuration.runtimes

只需要将

```ini

"java.home": "/usr/local/Cellar/openjdk@11/11.0.8/",
```

替换并修改为如下

```ini

"java.home": "/usr/local/Cellar/openjdk@11/11.0.8/libexec/openjdk.jdk/Contents/Home/",
"java.configuration.runtimes": [
    {
        "name": "JavaSE-11",
        "path": "/usr/local/Cellar/openjdk@11/11.0.8/libexec/openjdk.jdk/Contents/Home/"
    },
]
```

再次运行，问题解决，其实[github](https://github.com/redhat-developer/vscode-java/wiki/JDK-Requirements#java.configuration.runtimes)上的一篇文章写的比较详细
