+++
date = '2025-06-04T15:25:48+08:00'
draft = false
title = 'SCP传输命令的基本使用'
categories = [
	"linux"
]

tags = [
	"scp"
]
+++

scp是linux中功能最强大的文件传输命令，下面简单的讲解一些关于scp命令的操作

1,本地到远程的操作-复制文件

```bash
scp local_file remote_username@remote_ip:remote_folder
```

指定了用户名，命令执行后需要再输入密码，指定了远程的目录，文件名字不变

```bash
scp /home/space/walkerfree.sql root@www.xxx.cn:/home/root/others
```

```bash
scp local_file remote_username@remote_ip:remote_file
```

指定了用户名，命令执行后需要再输入密码，指定了文件名

```bash
scp /home/space/walkerfree.sql root@www.xxx.cn:/home/root/others/walkerfree_copy.sql
```

```bash
scp local_file remote_ip:remote_folder
```

没有指定用户名，命令执行后需要输入用户名和密码，指定了远程的目录，文件名字不变

```bash
scp /home/space/walkerfree.sql www.xxx.cn:/home/root/others
```

```bash
scp local_file remote_ip:remote_file
```
没有指定用户名，命令执行后需要输入用户名和密码，指定了文件名

```bash
scp /home/space/walkerfree.sql www.xxx.cn:/home/root/others/walkerfree_copy.sql
```
2,本地到远程的操作-复制目录

```bash
scp -r local_folder remote_username@remote_ip:remote_folder
```

指定了用户名，命令执行后需要再输入密码

```bash
scp -r /home/space/walkerfree/ root@www.xxx.cn:/home/root/others/
```

```bash
scp -r local_folder remote_ip:remote_folder
```

没有指定用户名，命令执行后需要输入用户名和密码

```bash
scp -r /home/space/walkerfree/ www.xxx.cn:/home/root/others/
```
3,从远程到本地的文件传输操作

从 远程 复制到 本地，只要将 从 本地 复制到 远程 的命令 的 后2个参数 调换顺序 即可；

```bash
scp root@www.xxx.cn:/home/root/others/walkerfree.sql /home/space/walkerfree_copy.sql
scp -r www.xxx.cn:/home/root/walkerfree/ /home/space/others/
scp [本地用户名@IP地址:文件名1] [远程用户名@IP地址:文件名2]
```
有用的几个参数:


>-v 和大多数 linux 命令中的 -v 意思一样 , 用来显示进度 . 可以用来查看连接 , 认证 , 或是配置错误 . 
>
>-C 使能压缩选项 . 
>
>-P 选择端口 . 注意 -p 已经被 rcp 使用 . 
>
>-4 强行使用 IPV4 地址 . 
>
>-6 强行使用 IPV6 地址 .  
