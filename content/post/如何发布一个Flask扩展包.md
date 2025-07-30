+++
date = '2025-07-30T09:56:59.068818+08:00'
draft = false
title = '如何发布一个Flask扩展包'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"
]

image = "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560310227/walkerfree/flask.png"
+++

如何开发和发布一个Flask扩展，如何开发一个Flask扩展，官方介绍在[这里](https://flask.palletsprojects.com/en/1.1.x/extensiondev/)

### 如何开发Flask扩展 - 实战篇（以我最近开发的flask\_dxcaptcha为例）

> **OS - MAX OS**

* 创建一个目录flask\_dxcaptcha

```bash

mkdir flask_dxcaptcha
cd flask_dxcaptcha

```

* 创建python虚拟环境并激活

```bash

virtualenv .env -p  /usr/local/bin/python3
source .env/bin/activate

```

* 创建包并开发具体的逻辑(flask\_dxcaptcha目录下)

```bash

mkdir flask_dxcaptcha
cd flask_dxcaptcha
touch __init__.py

```

* 编写\_\_init\_\_.py文件开始开发扩展逻辑，记录下flask\_dxcaptcha的\_\_init\_\_.py

```py

# -*- coding: utf-8 -*-
# @Author: durban.zhang
# @Date:   2019-12-25 17:02:16
# @Last Modified by:   durban
# @Last Modified time: 2019-12-25 18:43:25

from flask import current_app, _app_ctx_stack

from flask_dxcaptcha.captchaclient import CaptchaClient

class DXCaptcha(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('DX_APP_ID', '')
        app.config.setdefault('DX_APP_SECRECT', '')

    def init_captcha_client(self):
        if current_app.config['DX_APP_ID'] == '' or \
                current_app.config['DX_APP_SECRECT'] == '':
            raise Exception('DX_APP_ID and DX_APP_SECRECT can not empty.')

        return CaptchaClient(
            current_app.config['DX_APP_ID'],
            current_app.config['DX_APP_SECRECT'],
        )

    @property
    def client(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'dx_captcha'):
                ctx.dx_captcha = self.init_captcha_client()
            return ctx.dx_captcha

```

flask\_dxcaptcha包下的目录结构如下

```bash

.
├── __init__.py
├── captchaclient.py
├── captcharesponse.py
├── ctuclient.py
├── cturequest.py
├── cturesponse.py
├── cturesponsestatus.py
├── cturesult.py
├── hitrule.py
├── risklevel.py
├── risktype.py
├── suggestion.py
└── suggestpolicy.py

```

然后先项目目录下面添加如下几个文件 setup.py # 具体打包和安装配置 MANIFEST.in # 打包文件配置 README.md # 项目介绍包括如何安装、如何使用 LICENSE # 项目许可类型

这里比较重要的是setup.py和MANIFEST.in，着重记录下这两个文件，其余两个文件可以去参考这个扩展[flask\_dxcaptcha](https://github.com/durban89/flask_dxcaptcha)

* setup.py的配置如下

```py

# -*- coding: utf-8 -*-
# @Author: durban
# @Date:   2019-12-25 18:00:43
# @Last Modified by:   durban.zhang
# @Last Modified time: 2019-12-25 19:03:55

from setuptools import find_packages, setup

setup(
    name='Flask-DXCaptcha',
    version='1.0.0',
    url='https://github.com/durban89/flask_dxcaptcha',
    license='MIT',
    author='durban zhang',
    author_email='[email protected]',
    description='Flask-DXCaptcha是依赖顶象科技提供的无感验证功能开发的Flask 扩展',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=1.1.1'
    ],
    python_requires=">=3.7.4",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

```

具体关于setup参数的介绍，请点[这里](https://packaging.python.org/guides/distributing-packages-using-setuptools/)

* MANIFEST.in的配置如下

```bash

include MANIFEST.in
include README
include LICENSE
recursive-exclude *.pyc

```

具体关于参数的介绍，请点[这里](https://packaging.python.org/guides/using-manifest-in/)

### 如何发布Flask扩展

如何发布Flask扩展，具体的可以参考官方介绍，点[这里](https://packaging.python.org/)

这里以flask\_dxcaptcha为例介绍下，**前提是项目开发后，自己测试没有问题再发布**

在flask\_dxcaptcha项目目录下面运行如下命令（**注意是我们的虚拟环境**）

* 如果没有安装`setuptools`和`wheel`执行下面命令

```bash

pip install setuptools wheel

```

* 打包扩展

```bash

python3 setup.py sdist bdist_wheel

```

在dist目录下生成如下文件

```bash

$ tree dist
dist
├── Flask-DXCaptcha-1.0.0.tar.gz
└── Flask_DXCaptcha-1.0.0-py3-none-any.whl

```

* 上传包到`Test PyPI`

注册`Test PyPI`账号，点[这里](https://test.pypi.org/account/register/)注册，然后安装twine，执行下面命令

```bash

pip install twine -i https://mirrors.aliyun.com/pypi/simple/

```

> -i 参数指定了包的镜像源

上传所有打包文件到`Test PyPI`

```bash

twine upload --repository-url https://test.pypi.org/legacy/ dist/*

```

示例如下

```bash

$ twine upload --repository-url https://test.pypi.org/legacy/ ./dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: [your_username]
Enter your password:
Uploading Flask_DXCaptcha-1.0.0-py3-none-any.whl
100%|███████████████████████████████████████████████████████████████████████████████████████████████| 13.0k/13.0k [00:04<00:00, 3.01kB/s]
Uploading Flask-DXCaptcha-1.0.0.tar.gz
100%|███████████████████████████████████████████████████████████████████████████████████████████████| 9.53k/9.53k [00:01<00:00, 7.57kB/s]

View at:
https://test.pypi.org/project/Flask-DXCaptcha/1.0.0/

```

测试安装上传的包

```bash

pip install -i https://test.pypi.org/simple/ --no-deps Flask-DXCaptcha==1.0.0

```

如果安装成功，就可以正常使用了

```bash

$ python
Python 3.7.4 (default, Jul  9 2019, 18:14:44)
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import flask_dxcaptcha
>>>

```

如果以上都是正常包的话，那么将包发布到正式的PyPI中

```bash

twine upload dist/*

```

示例如下

```bash

$ twine upload dist/*
Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: durban_zhang
Enter your password:
Uploading Flask_DXCaptcha-1.0.0-py3-none-any.whl
100%|███████████████████████████████████████████████████████████████████████████████████████████████| 13.0k/13.0k [00:09<00:00, 1.41kB/s]
Uploading Flask-DXCaptcha-1.0.0.tar.gz
100%|███████████████████████████████████████████████████████████████████████████████████████████████| 9.53k/9.53k [00:01<00:00, 6.87kB/s]

View at:
https://pypi.org/project/Flask-DXCaptcha/1.0.0/

```

打开地址 <https://pypi.org/project/Flask-DXCaptcha/1.0.0/> 就能看到发布的Flask扩展了
