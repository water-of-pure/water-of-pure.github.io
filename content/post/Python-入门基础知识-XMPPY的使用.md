+++
date = '2025-07-25T15:55:33.969388+08:00'
draft = false
title = 'Python 入门基础知识 - XMPPY的使用'
categories = [
    "技术",

]

tags = [
    "Python",

]
+++

**1、XMPPPY模块简介**

XMPPPY模块使用Python对XMPP协议进行了封装，使用XMPPPY可以使用Python连接到支持的XMPP协议的服务器。XMPPPY主要有以下几个模块

auth: 实现XMPP协议用户认证的模块

browser: 用户提供DISCO服务器框架

client: 用于提供扩展

debug: 用户调试

dispatcher: XMPPPY的主要模块

features: 包含一些不能分割的内容

filetransfer: 用于实现JEP-0047

protocol: 实现XMPP通信协议模块

roster: 用户实现用户列表

simplexml: 用户处理XML

transports: 底层传输协议

XMPPPY模块比较庞大，详细的内容可以参考XMPPPY的帮助文档。

**2、使用xmpppy连接Gtalk**

代码示例如下，为了方便起见，脚本中创建连接后就进入循环，当有用户发送消息，就输出消息内容和用户名，然后向用户发送消息。

```py
# _*_ coding: utf-8 -*-
import xmpp  # 导入模块

def get_message(client, message):  # 消息处理函数
    text = message.getBody()
    people = message.getFrom()
    print('GET: %s FROM: %s' % (text, people))
    client.send(xmpp.protocol.Message(people, 'GET: ' + text, type='chat'))

user = raw_input('User:')
password = raw_input('Passwd:')
jid = xmpp.protocol.JID(user + '@gmail.com')
client = xmpp.Client(jid.getDomain())  # 创建客户端
# 连接服务器 - 服务器不再支持，可以更换为可用的
client.connect(server=('hangouts.google.com', 5222))
client.auth(jid.getNode(), password)  # 用户认证
Roster = client.getRoster()  # 获取用户列表
names = Roster.getItems()

for name in names:
    status = Roster.getStatus(name)
    print(name)
    print(status)

client.RegisterHandler('message', get_message)
client.sendInitPresence()

while 1:
    try:
        client.Process(1)
    except KeyboardInterrupt:  # 处理Control+c
        break

```

**注意！**

**2016年6月26日，Google Talk正式关闭，并被Google Hangouts取代。**
