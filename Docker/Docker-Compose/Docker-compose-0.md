`Dockerfile` 可以让用户管理一个单独的应用容器；
而 `Compose` 则允许用户在一个模板（`YAML 格式`）中定义一组相关联的应用容器（被称为一个 project，即项目），例如一个 Web 服务容器再加上后端的数据库服务容器等。

![](../compose.png)

**负载均衡**


### 安装与卸载

Compose 可以通过 Python 的包管理工具 pip 进行安装，也可以直接下载编译好的二进制文件使用，甚至能够直接在 Docker 容器中运行。

前两种方式是传统方式，适合本地环境下安装使用；最后一种方式则不破坏系统环境，更适合云计算场景。

#### bash 补全命令






### docker-compose 命令

```
Define and run multi-container applications with Docker.

Usage:
  docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
  docker-compose -h|--help

Options:
  -f, --file FILE             Specify an alternate compose file (default: docker-compose.yml)
  -p, --project-name NAME     Specify an alternate project name (default: directory name)
  --verbose                   Show more output
  --no-ansi                   Do not print ANSI control characters
  -v, --version               Print version and exit
  -H, --host HOST             Daemon socket to connect to

  --tls                       Use TLS; implied by --tlsverify
  --tlscacert CA_PATH         Trust certs signed only by this CA
  --tlscert CLIENT_CERT_PATH  Path to TLS certificate file
  --tlskey TLS_KEY_PATH       Path to TLS key file
  --tlsverify                 Use TLS and verify the remote
  --skip-hostname-check       Don't check the daemon's hostname against the name specified
                              in the client certificate (for example if your docker host
                              is an IP address)
  --project-directory PATH    Specify an alternate working directory
                              (default: the path of the Compose file)

Commands:
  build              Build or rebuild services
  bundle             Generate a Docker bundle from the Compose file
  config             Validate and view the Compose file
  create             Create services
  down               Stop and remove containers, networks, images, and volumes
  events             Receive real time events from containers
  exec               Execute a command in a running container
  help               Get help on a command
  images             List images
  kill               Kill containers
  logs               View output from containers
  pause              Pause services
  port               Print the public port for a port binding
  ps                 List containers
  pull               Pull service images
  push               Push service images
  restart            Restart services
  rm                 Remove stopped containers
  run                Run a one-off command
  scale              Set number of containers for a service
  start              Start services
  stop               Stop services
  top                Display the running processes
  unpause            Unpause services
  up                 Create and start containers
  version            Show the Docker-Compose version information
```


**术语:**

`服务（service）`：一个应用容器，实际上可以运行多个相同镜像的实例。


`项目(project)`：由一组关联的应用容器组成的一个完整业务单元。在 docker-compose.yml 文件中定义。

可见，一个项目可以由多个服务（容器）关联而成，Compose 面向项目进行管理。Compose 的默认管理对象是项目，通过子命令对项目中的一组容器进行便捷地生命周期管理。

>注意：Compose 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 Compose 来进行编排管理。



























### 第一个 docker-compose.yml 文件

```
version:"3"
services:
  web:
    # 将 username/repo:tag 替换为您的名称和镜像详细信息
    image: username/repository:tag
    deploy:
      replicas:5
      resources:
        limits:
          cpus:"0.1"
          memory:50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:

# 从镜像库中拉取我们在步骤 2 中上传的镜像。

# 将该镜像的五个实例作为服务 web 运行，并将每个实例限制为最多使用 10% 的 CPU（在所有核心中）以及 50MB RAM。

# 如果某个容器发生故障，立即重启容器。

# 将主机上的端口 80 映射到 web 的端口 80。

# 指示 web 容器通过负载均衡的网络 webnet 共享端口 80。（在内部，容器自身将在临时端口发布到 web 的端口 80。）

# 使用默认设置定义 webnet 网络（此为负载均衡的 overlay 网络）。


<!-- 使用 deploy key（仅可用于 Compose 文件格式版本 3.x 及更高版本）及其子选项对每项服务（例如，web）进行负载均衡和优化性能 -->
```

```shell
Usage:	docker stack COMMAND

Manage Docker stacks

Options:
      --help   Print usage

Commands:
  deploy      Deploy a new stack or update an existing stack
  ls          List stacks
  ps          List the tasks in the stack
  rm          Remove one or more stacks
  services    List the services in the stack

Run 'docker stack COMMAND --help' for more information on a command.
```

```
docker stack ls              # 列出此 Docker 主机上所有正在运行的应用
docker stack deploy -c <composefile> <appname>  # 运行指定的 Compose 文件
docker stack services <appname>       # 列出与应用关联的服务
docker stack ps <appname>   # 列出与应用关联的正在运行的容器
docker stack rm <appname>                             # 清除应用
```
