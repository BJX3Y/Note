[https://www.cnblogs.com/lienhua34/p/5170335.html]


### scratch

我一直在寻找尽可能小的容器，然后发现了这个：

`docker pull scratch`
Scratch镜像很赞，它简洁、小巧而且快速， 它没有bug、安全漏洞、延缓的代码或技术债务。这是因为它基本上是空的。除了有点儿被Docker添加的metadata (译注：元数据为描述数据的数据)。你可以用以下命令创建这个scratch镜像（官方文档上有描述）：

>**tar cv --files-from /dev/null | docker import - scratch**

这是它，非常小的一个Docker镜像。到此结束!

[http://cloud.51cto.com/art/201412/462603.htm]


### Dockerfile RUN，CMD，ENTRYPOINT命令区别

RUN命令执行命令并创建新的镜像层，通常用于安装软件包
CMD命令设置容器启动后默认执行的命令及其参数，但CMD设置的命令能够被docker run命令后面的命令行参数替换
ENTRYPOINT配置容器启动时的执行命令（不会被忽略，一定会被执行，即使运行 docker run时指定了其他命令）

[https://www.jianshu.com/p/f0a0f6a43907]
