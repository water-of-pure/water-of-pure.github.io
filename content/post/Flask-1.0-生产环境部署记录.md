+++
date = '2025-07-29T10:09:06.726538+08:00'
draft = false
title = 'Flask 1.0 生产环境部署记录'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/c_scale,w_520/v1554886328/walkerfree/wf_41.jpg"
+++

Flask 1.0 开始支持Python3啦，一直在使用Flask构建自己的博客，今天重温看了下Flask1.0，感觉还是有很多优点的，随后根据官网的教程搞了一个简易的小博客，整体使用下来，还算是比较轻便的。唯独在部署上不是那么的轻松，但是经过查询也算是找到了解决办法，跟之前的Flask版本不同的是，我这次想试下Gunicorn+Nginx+Supervisor。

安装的部分就不用我多说，我是把Gunicorn安装在了项目目录下，实际上作为一个项目的话Gunicorn是没必要放在项目中的，毕竟一个是服务层一个是逻辑层。

为了Gunicorn的启动配置项简单明了，最好是建立一个配置文件，这样下次也能清楚里面启动的时候配置了哪些参数，网上找了一个配置，仅供参考

gunicorn.conf

```bash

# 并行工作进程数
workers = 4
# 指定每个工作者的线程数
threads = 2
# 监听内网端口5000
bind = '127.0.0.1:8000'
# 设置守护进程,将进程交给supervisor管理
daemon = 'false'
# 设置最大并发量
worker_connections = 2000
# 设置进程文件目录
pidfile = '/var/tmp/gunicorn.pid'
# 设置访问日志和错误信息日志路径
accesslog = '/var/tmp/gunicorn_access.log'
errorlog = '/var/tmp/gunicorn_error.log'
# 设置日志记录水平
loglevel = 'warning'
```

这里的配置注意daemon为false

然后添加supervisor的配置，这里要做的只是简单的添加supervisor配置，至于supervisor的安装还是很简单的，mac下建议使用brew安装

贴出一份我这边测试时使用的配置

baby.ini

```bash

[program:baby]
directory = /Users/durban/python/baby ; 程序的启动目录
command = gunicorn -c /Users/durban/python/baby/gunicorn.conf baby  ; 启动命令，可以看出与手动在命令行启动的命令是一样的
autostart = true     ; 在 supervisord 启动的时候也自动启动
startsecs = 5        ; 启动 5 秒后没有异常退出，就当作已经正常启动了
autorestart = true   ; 程序异常退出后自动重启
startretries = 3     ; 启动失败自动重试次数，默认是 3
user = durban          ; 用哪个用户启动
redirect_stderr = true  ; 把 stderr 重定向到 stdout，默认 false
stdout_logfile_maxbytes = 20MB  ; stdout 日志文件大小，默认 50MB
stdout_logfile_backups = 20     ; stdout 日志文件备份数
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile = /var/tmp/baby_stdout.log

; 可以通过 environment 来添加需要的环境变量，一种常见的用法是修改 PYTHONPATH
; environment=PYTHONPATH=$PYTHONPATH:/path/to/somewhere
```

然后重启下supervisor就可以了

这里注意下supervisor的问题，如果你supervisor的配置文件是在/etc/等supervisor默认搜索的目录下的话直接使用supervisorctl reload是没有任何问题的，如果配置文件不在默认的搜索目录下的话，就会报类似refused connection的错误提示，建议操作supervisor的时候，指定下配置文件，如下

```bash

supervisorctl -c /usr/local/etc/supervisord.ini reload
```

然后配置nginx，简单的配置示例如下

```bash

server {
	charset utf-8;

	client_max_body_size 128M;

	listen 80;

	server_name flask1.walkerfree.local; # 这是HOST机器的外部域名，用地址也行

	access_log /var/log/flask1.walkerfree.local.access.log;
	error_log /var/log/flask1.walkerfree.local.error.log;

	location / {
		proxy_pass http://127.0.0.1:8000; # 这里是指向 gunicorn host 的服务地址
		proxy_set_header Host $host;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	}

	location ~ /\.(git|svn|ht) {
		deny all;
	}
}
```
