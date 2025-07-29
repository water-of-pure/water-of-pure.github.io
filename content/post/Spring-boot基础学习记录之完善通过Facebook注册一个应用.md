+++
date = '2025-07-29T10:08:56.388570+08:00'
draft = false
title = 'Spring boot基础学习记录之完善通过Facebook注册一个应用'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"

]
+++

继续上篇文章，来完善下如果使用Facebook注册一个应用  
 今天通过官网有查到了许多关于spring boot social相关的文章，但是进去之后都只能看到"deprecated"  
 今天我就来完善下这块知识的短缺

### **首先在社交平台注册一个应用 (Register your application)**

比如注册Facebook Twitter等应用，可以去官网看看教程，这个跟国内的微博之类的是类似的，这里不做简单介绍了。而且每个不同平台的版本升级，界面变化也是蛮快的，建议多去官网看看。

### **编辑应用的配置添加配置属性 (Edit application.properties)**

我这里修改了application.properties添加了下面的配置，其他平台的类似

```bash

facebook.appKey=xxx
facebook.appSecret=xxx
```

### **添加Spring Social依赖库 (Add Spring Social Dependencies)**

依据上篇文章已经添加的，这里的话，还需要在添加几个如下

```xml

<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-core</artifactId>
    <version>1.1.6.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-security</artifactId>
    <version>1.1.6.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-core</artifactId>
    <version>5.0.6.RELEASE</version>
</dependency>
```

最终总共需要添加的依赖如下

```xml

<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-facebook</artifactId>
    <version>2.0.3.RELEASE</version>
</dependency>
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-core</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-crypto</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-core</artifactId>
    <version>1.1.6.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework.social</groupId>
    <artifactId>spring-social-security</artifactId>
    <version>1.1.6.RELEASE</version>
</dependency>
<dependency>
    <groupId>org.springframework.security</groupId>
    <artifactId>spring-security-core</artifactId>
    <version>5.0.6.RELEASE</version>
</dependency>
```

### **配置Spring Social (Configure Spring Social)**

飙写代码开始

1、创建一个@Configuration类：

```java

@Configuration
@EnableSocial
public class SocialConfig implements SocialConfigurer {

}
```

2、在SocialConfig中添加已注册的ConnectionFactoryLocator，这里使用的是Facebook，如果是其他平台的可以继续添加

```java

@Override
public void addConnectionFactories(ConnectionFactoryConfigurer connectionFactoryConfigurer,
        Environment environment) {
    connectionFactoryConfigurer.addConnectionFactory(new FacebookConnectionFactory(
            environment.getProperty("facebook.appKey"), environment.getProperty("facebook.appSecret")));
}
```

3、在SocialConfig中添加UsersConnectionRepository以在所有用户之间保留连接数据

```java

@Override
public UsersConnectionRepository getUsersConnectionRepository(ConnectionFactoryLocator connectionFactoryLocator) {
    JdbcUsersConnectionRepository repository = new JdbcUsersConnectionRepository(dataSource,
            connectionFactoryLocator, Encryptors.noOpText());

    repository.setConnectionSignUp(new SimpleConnectionSignUp());
    return repository;
}
```

4、在SocialConfig中添加getUserIdSource以识别当前用户的连接

```java

@Override
public UserIdSource getUserIdSource() {
    return new AuthenticationNameUserIdSource();
}
```

5、在SocialConfig中添加一个或多个表示当前用户API绑定的请求范围的bean。这里添加的是Facebook：

```java

@Bean
@Scope(value = "request", proxyMode = ScopedProxyMode.INTERFACES)
public Facebook facebook(ConnectionRepository repository) {
    Connection<Facebook> connection = repository.findPrimaryConnection(Facebook.class);
    if (connection != null) {
        return connection.getApi();
    }

    return null;
}
```

6、在SocialConfig中添加ProviderSignInController，允许用户使用其提供者帐户登录

```java

@Bean
public ProviderSignInController providerSignInController(ConnectionFactoryLocator connectionFactoryLocator,
        UsersConnectionRepository usersConnectionRepository) {
    return new ProviderSignInController(connectionFactoryLocator, usersConnectionRepository,
            new SpringSecuritySignInAdapter());
}
```

### **创建视图**

创建一个"链接"视图，允许用户使用其提供者帐户登录，视图分别如下  
 connect/connectFacebook.html

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
  <meta charset="UTF-8">
  <title>连接到Facebook</title>
</head>

<body>
  <h3>连接到Facebook</h3>
  <form th:action="@{/signin/facebook}" method="POST">
    <input type="hidden" name="scope" value="email,user_friends" />
    <input type="hidden" name="redirect_uri" value="http://localhost:8080/connected/facebook" />
    <div class="formInfo">
      <p>你还没有连接到Facebook，点击连接按钮连接到Facebook账户</p>
    </div>
    <p>
      <button type="submit">连接到Facebook</button>
    </p>
  </form>
</body>

</html>
```

connected/connectFacebook.html

```html

<!DOCTYPE html>
<html lang="en" xmlns:th="http://www.thymeleaf.org">

<head>
  <meta charset="UTF-8">
  <title>已连接到Facebook</title>
</head>

<body>
  <h3>已连接到Facebook</h3>
  <div class="formInfo">
    <p>你已连接到Facebook，点击连接按钮连接到Facebook账户</p>
  </div>
  <h3>Facebook好友: <span th:text="${friendsNum}"></span></h3>
  <ul>
    <li th:each="friend : ${friends}">
      <img th:src="'http://graph.facebook.com/' + ${friend.id} + '/picture'" align="middle" />
      <span th:text="${friend.name}">name</span>
    </li>
  </ul>
  <h3>邮箱信息: <span th:text="${email}"></span></h3>
</body>

</html>
```

### **调用API**

最后，@Inject引用API绑定到需要它们的对象。检索当前用户的facebook好友的示例@Controller如下所示：

```java

@Controller
public class SocialController {
    private Facebook facebook;
    private ConnectionRepository connectionRepository;

    @Inject
    public SocialController(Facebook facebook, ConnectionRepository connectionRepository) {
        this.facebook = facebook;
        this.connectionRepository = connectionRepository;
    }

    @RequestMapping(value = "/connect/facebook", method = RequestMethod.GET)
    public ModelAndView connectFacebook(Model model) {
        ModelAndView mv = new ModelAndView("connect/connectFacebook");
        mv.addObject("email", "[email protected]");
        return mv;
    }

    @RequestMapping(value = "/connected/facebook", method = RequestMethod.GET)
    public String connectedFacebook(Model model) {
        Connection<Facebook> connection = this.connectionRepository.findPrimaryConnection(Facebook.class);

        if (connection == null) {
            return "redirect:/connect/facebook";
        }

        List<Reference> friends = facebook.friendOperations().getFriends();

        String[] fields = { "id", "email", "first_name", "last_name" };
        User userProfile = facebook.fetchObject("me", User.class, fields);

        System.out.println(friends.size());
        model.addAttribute("friends", friends);
        model.addAttribute("friendsNum", friends.size());
        model.addAttribute("email", userProfile.getEmail());
        return "connect/connectedFacebook";
    }

}
```

经过以上几个流程最终就完成了相关的配置，可以启动项目进行测试了链接了。

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/c_scale,w_520/v1532044115/walkerfree/WX20180718-234821_2x.png)

仔细看下面这部分的内容，目前网上使用官网的例子经常遇到的错误及一些疑惑，经过本次的调整，一下问题都会得到解决。可以下载本实例进行测试

```bash

git clone https://github.com/durban89/spring-demo.git
git checkout v1.0.5
```

### **第一个疑惑**

我们没有添加signin开头的路由为什么能请求的到呢，在项目启动的时候，其实这些已经跟在依赖包内做了处理了，这个在项目启动的时候让我豁然开朗

```bash

2018-07-18 11:20:55.878  INFO 66154 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/signin/{providerId}],methods=[POST]}" onto public org.springframework.web.servlet.view.RedirectView org.springframework.social.connect.web.ProviderSignInController.signIn(java.lang.String,org.springframework.web.context.request.NativeWebRequest)
2018-07-18 11:20:55.879  INFO 66154 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/signin/{providerId}],methods=[GET],params=[oauth_token]}" onto public org.springframework.web.servlet.view.RedirectView org.springframework.social.connect.web.ProviderSignInController.oauth1Callback(java.lang.String,org.springframework.web.context.request.NativeWebRequest)
2018-07-18 11:20:55.880  INFO 66154 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/signin/{providerId}],methods=[GET],params=[code]}" onto public org.springframework.web.servlet.view.RedirectView org.springframework.social.connect.web.ProviderSignInController.oauth2Callback(java.lang.String,java.lang.String,org.springframework.web.context.request.NativeWebRequest)
2018-07-18 11:20:55.903  INFO 66154 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/signin/{providerId}],methods=[GET],params=[error]}" onto public org.springframework.web.servlet.view.RedirectView org.springframework.social.connect.web.ProviderSignInController.oauth2ErrorCallback(java.lang.String,java.lang.String,java.lang.String,java.lang.String,org.springframework.web.context.request.NativeWebRequest)
2018-07-18 11:20:55.904  INFO 66154 --- [           main] s.w.s.m.m.a.RequestMappingHandlerMapping : Mapped "{[/signin/{providerId}],methods=[GET]}" onto public org.springframework.web.servlet.view.RedirectView org.springframework.social.connect.web.ProviderSignInController.canceledAuthorizationCallback()
```

### **第二个疑惑**

```bash

org.springframework.web.client.ResourceAccessException: I/O error on POST request for "https://graph.facebook.com/v2.5/oauth/access_token": Operation timed out (Connection timed out); nested exception is java.net.ConnectException: Operation timed out (Connection timed out)
```

为什么我在国内配置完之后，也跳转到了社交平台，但是返回的时候报下面的错误

这个问题的解决方案如下  
 pom.xml文件添加类似如下的配置

```xml

<jvmArguments> -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=1087 -Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=1087 -Dhttps.proxySet=true
</jvmArguments>
```

添加后的结果如下

```xml

<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <jvmArguments> -Dhttps.proxyHost=127.0.0.1 -Dhttps.proxyPort=1087 -Dhttp.proxyHost=127.0.0.1 -Dhttp.proxyPort=1087 -Dhttps.proxySet=true
                </jvmArguments>
            </configuration>
        </plugin>
    </plugins>
</build>
```

其实就是做了代理的设置

### **第三个疑问**

```bash

org.springframework.jdbc.BadSqlGrammarException: PreparedStatementCallback; bad SQL grammar [select userId from UserConnection where providerId = ? and providerUserId = ?]; nested exception is org.h2.jdbc.JdbcSQLException: Table "USERCONNECTION" not found; SQL statement:
```

为什么会提示我数据库表没有呢，不应该是自动为我建立吗，经过网上的查找，确实是没有自动帮你建立，这个需要自己去添加，可能这块的业务逻辑不能耦合的太紧密的原因吧  
 解决方案在这里  
 config/MainConfig.java

```java

@Configuration
@ComponentScan(basePackages = "com.gowhich.springdemo", excludeFilters = { @Filter(Configuration.class) })
@PropertySource("classpath:application.properties")
public class MainConfig {

    @Bean(destroyMethod = "shutdown")
    public DataSource dataSource() {
        EmbeddedDatabaseFactory factory = new EmbeddedDatabaseFactory();
        factory.setDatabaseName("springdemo");
        factory.setDatabaseType(EmbeddedDatabaseType.H2);
        factory.setDatabasePopulator(databasePopulator());
        return factory.getDatabase();
    }

    private DatabasePopulator databasePopulator() {
        ResourceDatabasePopulator populator = new ResourceDatabasePopulator();
        populator.addScript(
                new ClassPathResource("JdbcUsersConnectionRepository.sql", JdbcUsersConnectionRepository.class));
        return populator;    }
}
```

同时别忘记创建JdbcUsersConnectionRepository.sql这个文件，放在src/main/resources目录下就可以。然后在运行项目就会自动创建数据库表了。  
 JdbcUsersConnectionRepository.sql  
 内容如下，github也有的。

```sql

create table UserConnection
(
    userId varchar(255) not null,
    providerId varchar(255) not null,
    providerUserId varchar(255),
    rank int not null,
    displayName varchar(255),
    profileUrl varchar(512),
    imageUrl varchar(512),
    accessToken varchar(1024) not null,
    secret varchar(255),
    refreshToken varchar(255),
    expireTime bigint,
    primary key (userId, providerId, providerUserId)
);
create unique index UserConnectionRank on UserConnection(userId, providerId, rank);

create table UserProfile
(
    userId varchar(255) not null,
    email varchar(255),
    firstName varchar(255),
    lastName varchar(255),
    name varchar(255),
    username varchar(255),
    primary key (userId)
);
create unique index UserProfilePK on UserProfile(userId);
```

### **第四个疑问**

```bash

java.lang.IllegalStateException: No user is currently signed in
```

这个问题主要原因是官网的例子中使用的是TheadLocal，通过进程的方法共享数据，结果这个数据在再次获取的时候丢失了，具体原因我只查到在使用Spring Cloud的时候回遇到，没查到在使用Spring Boot的时候也会有，但是问题已解决，就是替换下，我这里的实例使用的是官网最新的文档中介绍的，在setCurrentUser和getCurrentUser的逻辑中做了修改，替换了TheadLocal。  
 修改的地方大概有几个地方，如下

获取用户数据的地方

```java

@Override
public UserIdSource getUserIdSource() {
    return new AuthenticationNameUserIdSource();
}
```

注册用户数据的地方，改用了SecurityContextHolder的方式

```java

@Bean
public ProviderSignInController providerSignInController(ConnectionFactoryLocator connectionFactoryLocator,
        UsersConnectionRepository usersConnectionRepository) {
    return new ProviderSignInController(connectionFactoryLocator, usersConnectionRepository,
            new SpringSecuritySignInAdapter());
}
```

和

```java

public final class SpringSecuritySignInAdapter implements SignInAdapter {

    public String signIn(String userId, Connection<?> connection, NativeWebRequest request) {
        SecurityContextHolder.getContext()
                .setAuthentication(new UsernamePasswordAuthenticationToken(userId, null, null));
        return null;
    }

}
```

### **第五个疑问**

```bash

org.springframework.social.UncategorizedApiException: (#12) bio field is deprecated for versions v2.8 and higher
```

这个是Facebook对应库版本不兼容的问题，这个网上还是很好找的  
 问题主要出在这里

```java

List<Reference> friends = facebook.friendOperations().getFriends();

String[] fields = { "id", "email", "first_name", "last_name" };
User userProfile = facebook.fetchObject("me", User.class, fields);
```

官网的例子一般是只给出了这个

```java

List<Reference> friends = facebook.friendOperations().getFriends();
```

当我们想要调用其他数据的时候 比如用户信息"facebook.userOperations()"这样调用的时候就会报错，实际上就是不支持了，要换，换成如下的方式

```java

String[] fields = { "id", "email", "first_name", "last_name" };
User userProfile = facebook.fetchObject("me", User.class, fields);
```

OK，埰坑完毕。期待我下次的分享，埰坑踩到无法呼吸。

实践项目地址

```bash

git clone https://github.com/durban89/spring-demo.git
git checkout v1.0.5
```
