+++
date = '2025-07-29T10:09:28.900833+08:00'
draft = false
title = 'Flask 1.0 新手教程 - 概览'
categories = [
    "技术",

]

tags = [
    "Python",
    "Flask"

]
+++

教程内容有：

1. [项目布局](https://www.walkerfree.com/article/152)
2. [应用程序设置](https://www.walkerfree.com/article/153)
3. [定义和访问数据库](https://www.walkerfree.com/article/154)
4. [Blueprint和视图](https://www.walkerfree.com/article/155)
5. [模板](https://www.walkerfree.com/article/156)
6. [静态文件](https://www.walkerfree.com/article/157)
7. [博客Blueprint](https://www.walkerfree.com/article/158)
8. [使项目可安装](https://www.walkerfree.com/article/159)
9. [测试覆盖率](https://www.walkerfree.com/article/160)
10. [部署到生产](https://www.walkerfree.com/article/161)
11. [继续开发！](https://www.walkerfree.com/article/162)

本教程将指导您创建一个名为Baby的基本博客应用程序。用户可以注册，登录，创建帖子，编辑或删除自己的帖子。您将能够在其他计算机上打包并安装该应用程序。 [![新手教程](https://camo.githubusercontent.com/c178bd4b7a95fd0e85a24a4df1d69d732f48d76b/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433313630392f77616c6b6572667265652f77785f3135315f312e706e67)](https://camo.githubusercontent.com/c178bd4b7a95fd0e85a24a4df1d69d732f48d76b/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433313630392f77616c6b6572667265652f77785f3135315f312e706e67)

假设您已熟悉Python。Python文档中的官方教程是首先学习或复习的好方法。

虽然这个新手教程旨在提供一个良好的起点，但本教程并未涵盖Flask的所有功能。查看[快速入门](http://flask.pocoo.org/docs/1.0/quickstart/#quickstart)，了解Flask可以做的事情，然后深入了解文档以了解更多信息。本教程仅使用Flask和Python提供的内容。在其他项目中，您可能决定使用[Extensions](http://flask.pocoo.org/docs/1.0/extensions/#extensions)或其他库来简化某些任务。

[![新手教程](https://camo.githubusercontent.com/e31114c998d002420ce5ee63b5640d1b1ee96d87/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433333039302f77616c6b6572667265652f77785f3135315f322e706e67)](https://camo.githubusercontent.com/e31114c998d002420ce5ee63b5640d1b1ee96d87/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433333039302f77616c6b6572667265652f77785f3135315f322e706e67)

Flask是很灵活的，它不需要您使用任何特殊的项目或者代码布局。然后，首次使用时，使用更结构化的方法会很有帮助。这意味着该新手教程需要预先考虑一些样板，但这样做是为了避免新开发人员遇到的许多常见陷阱，并创建一个易于扩展的项目。一旦你对Flask更加舒适，你可以走出这个结构并充分利用Flask的灵活性。

[![新手教程](https://camo.githubusercontent.com/4d9d28efbf22a2e432906986a32c90d2edd8bf68/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433343034312f77616c6b6572667265652f77785f3135315f332e706e67)](https://camo.githubusercontent.com/4d9d28efbf22a2e432906986a32c90d2edd8bf68/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313535383433343034312f77616c6b6572667265652f77785f3135315f332e706e67)

如果您希望在学习本教程时将项目与最终产品进行比较，那么[本教程项目可作为Flask存储库中的示例提供](https://github.com/pallets/flask/tree/1.0.2/examples/tutorial)。

下一期继续 - [项目布局](https://www.walkerfree.com/article/152)
