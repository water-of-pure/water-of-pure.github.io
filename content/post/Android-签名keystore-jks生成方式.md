+++
date = '2025-07-30T11:44:07.680691+08:00'
draft = false
title = 'Android 签名keystore/jks生成方式'
image = 'https://res.cloudinary.com/dy5dvcuc1/image/upload/v1603808282/walkerfree/Ju3ceiZzGSSQacR2juGN98.png'
categories = [
    "技术",

]

tags = [
    "Android",
    "签名"
]
+++

### 生成签名证书

使用keytool -genkey命令生成证书：

```bash

keytool -genkey -alias testalias -keyalg RSA -keysize 2048 -validity 36500 -keystore test.keystore
```

* testalias是证书别名，可修改为自己想设置的字符，建议使用英文字母和数字
* test.keystore是证书文件名称，可修改为自己想设置的文件名称，也可以指定完整文件路径

```ini

输入密钥库口令:
再次输入新口令:
您的名字与姓氏是什么?
  [Unknown]:
您的组织单位名称是什么?
  [Unknown]:
您的组织名称是什么?
  [Unknown]:
您所在的城市或区域名称是什么?
  [Unknown]:
您所在的省/市/自治区名称是什么?
  [Unknown]:
该单位的双字母国家/地区代码是什么?
  [Unknown]:
CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown是否正确?
  [否]:
您的名字与姓氏是什么?
  [Unknown]:
您的组织单位名称是什么?
  [Unknown]:
您的组织名称是什么?
  [Unknown]:
您所在的城市或区域名称是什么?
  [Unknown]:
您所在的省/市/自治区名称是什么?
  [Unknown]:
该单位的双字母国家/地区代码是什么?
  [Unknown]:
CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown是否正确?
  [否]:  是

输入 <testalias> 的密钥口令
	(如果和密钥库口令相同, 按回车):
```

以上命令运行完成后就会生成证书，路径为当前目录

### 查看证书信息

可以使用以下命令查看：

```bash

$ keytool -list -v -keystore  test.keystore
输入密钥库口令:

```

会输出以下格式信息：

```bash

密钥库类型: JKS
密钥库提供方: SUN

您的密钥库包含 1 个条目

别名: testalias
创建日期: 2020-11-15
条目类型: PrivateKeyEntry
证书链长度: 1
证书[1]:
所有者: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
发布者: CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown
序列号: 3f43c8dc
有效期开始日期: Sun Nov 15 22:17:41 CST 2020, 截止日期: Tue Oct 22 22:17:41 CST 2120
证书指纹:
	 MD5: C7:23:DB:D6:09:CD:CA:77:77:FA:D8:2F:58:FB:83:0F
	 SHA1: E8:07:B6:F8:70:C1:0B:87:D8:C8:C5:64:43:C5:40:3A:0C:AA:E6:7F
	 SHA256: 82:18:C1:28:3C:E3:30:02:31:3F:E1:13:2A:2F:DC:75:A8:65:86:5D:97:F1:12:C7:A9:05:61:C2:E7:D5:5F:32
	 签名算法名称: SHA256withRSA
	 版本: 3

扩展:

#1: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 9B FF CE 5E 27 12 02 96   E9 B3 44 8C 80 DF CE A5  ...^'.....D.....
0010: ED 4C A4 81                                        .L..
]
]

*******************************************
*******************************************

```

其中证书指纹信息（Certificate fingerprints）：

* MD5    证书的MD5指纹信息（安全码MD5）
* SHA1    证书的SHA1指纹信息（安全码SHA1）
* SHA256    证书的SHA256指纹信息（安全码SHA245）
