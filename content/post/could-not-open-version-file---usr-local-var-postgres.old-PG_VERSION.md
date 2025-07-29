+++
date = '2025-07-29T10:08:59.772121+08:00'
draft = false
title = 'could not open version file: /usr/local/var/postgres.old/PG_VERSION'
categories = [
    "技术",

]

tags = [
    "PostgreSQL",

]
+++

初次使用PostgreSQL发现了一个问题， 就是在使用mac中使用brew安装PostgreSQL时，会自动进行版本升级，但是再进行版本升级的时候会遇到如下错误

> could not open version file: /usr/local/var/postgres.old/PG\_VERSION

经过搜索，这里找到了解决办法如下地址

`https://gist.github.com/giannisp/ebaca117ac9e44231421f04e7796d5ca`

但是从内容上可以看到版本是从9.6.5到10.0  
 Upgrade PostgreSQL 9.6.5 to 10.0 using Homebrew (macOS)

本次分享下从9.6.10到10.3  
 Upgrade PostgreSQL 9.6.10 to 10.3 using Homebrew (macOS)

流程是一样的，但是记录下

# need to have both 9.6.x and latest 10.0 installed, and keep 10.0 as default

```bash

brew unlink postgresql
brew install [email protected] // 这一步如果已经安装了，则可以跳过
brew unlink [email protected]
brew link postgresql
```

# move 9.6.x db files to another directory

```bash

mv /usr/local/var/postgres /usr/local/var/postgres96
```

# init new database using 10.3

```bash

initdb /usr/local/var/postgres -E utf8
```

# make timezone and timezonesets directories available for 9.6.x installation

```bash

mkdir /usr/local/share/postgresql96
cp -r /usr/local/share/postgresql/timezone /usr/local/share/postgresql96
cp -r /usr/local/share/postgresql/timezonesets /usr/local/share/postgresql96
```

# finally the actual upgrade  
 # -b is the old binary dir, -B is the new binary dir  
 # -d is the old data dir, -D is the new data dir

```bash

pg_upgrade -b /usr/local/Cellar/[email protected]/9.6.10/bin -B /usr/local/Cellar/postgresql/10.3/bin -d /usr/local/var/postgres96 -D /usr/local/var/postgres
```

# start 10.3 to check that upgrade works

```bash

pg_ctl start -D /usr/local/var/postgres
```

# cleanup if upgrade was successful

```bash

brew uninstall [email protected]
rm -rf /usr/local/var/postgres96
rm -rf /usr/local/share/postgresql96
```

一切OK
