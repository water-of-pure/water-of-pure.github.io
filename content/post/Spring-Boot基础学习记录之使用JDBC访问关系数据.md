+++
date = '2025-07-28T17:52:31.982571+08:00'
draft = false
title = 'Spring Boot基础学习记录之使用JDBC访问关系数据'
categories = [
    "技术",

]

tags = [
    "Java",
    "Spring-Boot"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528606078/walkerfree/16080123389158.jpg"
+++

1、依赖添加

```xml

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
</dependency>
```

2、mav自动安装依赖，如果没有的话，请检查

3、创建对象Customer

```java

package com.gowhich.springdemo;
public class Customer {
    private long id;
    private String firstName, lastName;
    public Customer(long id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }
    @Override
    public String toString() {
        return String.format("Customer[id=%d, firstName=%s, lastName=%s]", id, firstName, lastName);
    }
}
```

这个对象可以理解为Model，就是要跟数据库表对应的关系

假设表customers有三个字段

id,first\_name,last\_name

> id对应这里的Customer Model 的 id
>
> first\_name对应这里的Customer Model 的 firstName
>
> last\_name对应这里的Customer Model 的 lastName

4、修改Application.java[程序启动的入库文件，也许你的名字并不是这个]，如我的demo中是SpringDemoApplication.java，修改后的结果是

```java

public class SpringDemoApplication implements CommandLineRunner {
	public static void main(String[] args) {
		SpringApplication.run(SpringDemoApplication.class, args);
	}
    // 创建日志
	private static final Logger log = LoggerFactory.getLogger(SpringDemoApplication.class);
    // 初始化JdbcTemplate 会自动连接h2database数据库
	@Autowired
    JdbcTemplate jdbcTemplate;
	@Override
    public void run(String... strings) throws Exception {
        log.info("Creating tables");
        // 创建表
        jdbcTemplate.execute("DROP TABLE customers IF EXISTS ");
        jdbcTemplate.execute("CREATE TABLE customers ("+
                "id SERIAL, first_name VARCHAR(255), last_name VARCHAR(255))");
        // 输入数据
        List<Object[]> splitUpNames = Arrays.asList("John Woo","Jeff Dean", "Josn Bokch", "Josh Long").stream()
                .map(name -> name.split(" ")).collect(Collectors.toList());
        splitUpNames.forEach(name -> log.info(String.format("Inserting customers record for %s %s", name[0], name[1])));
        jdbcTemplate.batchUpdate("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", splitUpNames);
        // 查询数据
        log.info("Querying for customers records where first_name = 'Josh");
        jdbcTemplate.query(
                "SELECT id, first_name, last_name FROM customers WHERE first_name = ?",
                new Object[] {"Josh"},
                (rs, column) -> new Customer(rs.getLong("id"), rs.getString("first_name"), rs.getString("last_name")))
        .forEach(customer -> log.info(customer.toString()));
    }
}
```

5、启动项目

启动项目后，会看到如下的输出

[![Spring Boot基础学习记录之使用JDBC访问关系数据](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528605843/walkerfree/WX20180610-123916_2x.png)](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1528605843/walkerfree/WX20180610-123916_2x.png)
