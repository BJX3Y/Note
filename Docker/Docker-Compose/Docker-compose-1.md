### 实例

#### 场景

下面，我们创建一个经典的 Web 项目：`一个 Haproxy，挂载三个 Web 容器`。

创建一个 compose-haproxy-web 目录，作为项目工作目录，并在其中分别创建两个子目录：haproxy 和 web。






### Compose 命令说明

大部分命令都可以运行在一个或多个服务上,如果没有特别的说明，命令则应用在项目所有的服务上。

```
Define and run multi-container applications with Docker.

Usage:
  docker-compose [-f <arg>...] [options] [COMMAND] [ARGS...]
  docker-compose -h|--help

Options:
  -f, --file FILE             Specify an alternate compose file (default: docker-compose.yml)  使用特定的 compose 模板文件，默认为 docker-compose.yml。
  -p, --project-name NAME     Specify an alternate project name (default: directory name) 指定项目名称，默认使用目录名称。
  --verbose                   Show more output 输出更多调试信息。
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


### docker-compose.yml文件模板说明

```
version: '2'
services:
  web:
    image: dockercloud/hello-world
    ports:
      - 8080
    networks:
      - front-tier
      - back-tier

  redis:
    image: redis
    links:
      - web
    networks:
      - back-tier

  lb:
    image: dockercloud/haproxy
    ports:
      - 80:80
    links:
      - web
    networks:
      - front-tier
      - back-tier
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

networks:
  front-tier:
    driver: bridge
  back-tier:
driver: bridge
```

**一份标准配置文件应该包含 version、services、networks 三大部分，其中最关键的就是 services 和 networks 两个部分.**


#### services

##### image

```
services:
  web:
    image:dockercloud/hello-world
```

`web` 是自己定义的 `服务[service]名`

image : 是指定服务的镜像名称或镜像 ID。如果镜像在本地不存在，Compose 将会尝试拉取这个镜像。

>**如下格式,都OK**：
```
image: redis
image: ubuntu:14.04
image: tutum/influxdb
image: example-registry.com:4000/postgresql
image: a4bc65fd
```

##### build

服务除了可以基于指定的镜像，还可以 **基于一份 Dockerfile，在使用 up 启动之时执行构建任务，这个构建标签就是 build，它可以指定 Dockerfile 所在文件夹的路径。Compose 将会利用它自动构建这个镜像，然后使用这个镜像启动服务容器**。


```
# 绝对路径
build: /path/to/build/dir

# 相对路径
build: ./dir

# 也可以先指定上下文
build:
  context: ../
  dockerfile: path/of/Dockerfile
```

>**注意 build 都是一个目录，如果你要指定 Dockerfile 文件需要在 build 标签的子级标签中使用 dockerfile 标签指定**


**如果你同时指定了 image 和 build 两个标签，那么 Compose 会构建镜像并且把镜像命名为 image 后面的那个名字。**


既然可以在 `docker-compose.yml` 中定义构建任务，那么一定少不了 `arg` 这个标签，就像 Dockerfile 中的 `ARG 指令`，**它可以在构建过程中指定环境变量，但是在构建成功后取消**，在 docker-compose.yml 文件中也支持这样的写法：

```
build:
  context: .
  args:
    buildno: 1
    password: secret

# 另一种写法
build:
  context: .
  args:
    - buildno=1
    - password=secret
```

与 ENV 不同的是，ARG 是允许空值的。例如：

```
args:
  - buildno
  - password
```

##### command

使用 command 可以覆盖容器启动后默认执行的命令。

```
command: bundle exec thin -p 3000
```

##### container_name

>**前面说过 Compose 的容器名称格式是：<项目名称><服务名称><序号>**

虽然可以自定义项目名称、服务名称，但是如果你想完全控制容器的命名，可以使用这个标签指定：

```
container_name: app
```

这样容器的名字就指定为 app 了。




##### depends_on

在使用 Compose 时，最大的好处就是少打启动命令，但是一般项目 **容器启动的顺序** 是有要求的，如果直接从上到下启动容器，必然会因为容器依赖问题而启动失败。
例如在没启动数据库容器的时候启动了应用容器，这时候应用容器会因为找不到数据库而退出，为了避免这种情况我们需要加入一个标签，就是 depends_on，这个标签解决了容器的依赖、启动先后的问题。
例如下面容器会先启动 redis 和 db 两个服务，最后才启动 web 服务:

```
version: '2'
services:
  web:
    build: .
    depends_on:
      - db
      - redis
  redis:
    image: redis
  db:
    image: postgres
```

##### dns
和 --dns 参数一样用途，格式如下：

```
dns: 8.8.8.8

# 也可以是一个列表：
dns:
  - 8.8.8.8
  - 9.9.9.9

# 此外 dns_search 的配置也类似：
dns_search: example.com
dns_search:
  - dc1.example.com
  - dc2.example.com
```

##### tmpfs

挂载临时目录到容器内部，与 run 的参数一样效果：

```
tmpfs: /run
tmpfs:
  - /run
  - /tmp
```


#####  entrypoint 【配置容器启动后执行的命令】
在 Dockerfile 中有一个指令叫做 ENTRYPOINT 指令，用于指定接入点。
在 docker-compose.yml 中可以定义接入点，覆盖 Dockerfile 中的定义：

```
entrypoint: /code/entrypoint.sh

# 格式和 Docker 类似，不过还可以写成这样：
entrypoint:
    - php
    - -d
    - zend_extension=/usr/local/lib/php/extensions/no-debug-non-zts-20100525/xdebug.so
    - -d
    - memory_limit=-1
    - vendor/bin/phpunit
```

##### expose 【暴露接口】
这个标签与Dockerfile中的EXPOSE指令一样，用于指定暴露的端口，但是只是作为一种参考，实际上docker-compose.yml的端口映射还得ports这样的标签。

```
expose:
 - "3000"
 - "8000"
```


##### ports 【映射端口的标签】

使用HOST:CONTAINER格式或者只是指定容器的端口，宿主机会随机映射端口。

```
ports:
 - "3000"
 - "8000:8000"
 - "49100:22"
 - "127.0.0.1:8001:8001"
```

##### privileged

>使用该参数，container内的root拥有真正的root权限。
否则，container内的root只是外部的一个普通用户权限。
privileged启动的容器，可以看到很多host上的设备，并且可以执行mount。甚至允许你在docker容器中启动docker容器.

当操作者执行docker run --privileged时，Docker将拥有访问主机所有设备的权限


##### restart 【Docker容器的重启策略】

```
Docker容器的重启策略如下：

no，默认策略，在容器退出时不重启容器
on-failure，在容器非正常退出时（退出状态非0），才会重启容器
on-failure:3，在容器非正常退出时重启容器，最多重启3次
always，在容器退出时总是重启容器
unless-stopped，在容器退出时总是重启容器，但是不考虑在Docker守护进程启动时就已经停止了的容器
```

##### volumes 挂载数据卷容器

挂载一个目录或者一个已存在的数据卷容器，可以直接使用 [HOST:CONTAINER] 这样的格式，或者使用 [HOST:CONTAINER:ro] 这样的格式，后者对于容器来说，数据卷是只读的，这样可以有效保护宿主机的文件系统。

```
volumes:
  // 只是指定一个路径，Docker 会自动在创建一个数据卷（这个路径是容器内部的）。
  - /var/lib/mysql

  // 使用绝对路径挂载数据卷
  - /opt/data:/var/lib/mysql

  // 以 Compose 配置文件为中心的相对路径作为数据卷挂载到容器。
  - ./cache:/tmp/cache

  // 使用用户的相对路径（~/ 表示的目录是 /home/<用户目录>/ 或者 /root/）。
  - ~/configs:/etc/configs/:ro

  // 已经存在的命名的数据卷。
  - datavolume:/var/lib/mysql
```

如果你不使用宿主机的路径，你可以指定一个volume_driver。

```
volume_driver: mydriver
```

##### volumes_from 【从其它容器或者服务挂载数据卷】
从其它容器或者服务挂载数据卷，可选的参数是 :ro或者 :rw，前者表示容器只读，后者表示容器对数据卷是可读可写的。默认情况下是可读可写的。

```
volumes_from:
  - service_name
  - service_name:ro
  - container:container_name
  - container:container_name:rw
```

##### extends

这个标签可以扩展另一个服务，扩展内容可以是来自在当前文件，也可以是来自其他文件，相同服务的情况下，后来者会有选择地覆盖原有配置。


##### links

还记得上面的depends_on吧，那个标签解决的是启动顺序问题，这个标签解决的是容器连接问题，与Docker client的--link一样效果，会连接到其它服务中的容器。
格式如下：

```
links:
 - db
 - db:database
 - redis
```


##### environment
与上面的 env_file 标签完全不同，反而和 arg 有几分类似，这个标签的作用是设置镜像变量，它可以保存变量到镜像里面，也就是说启动的容器也会包含这些变量设置，这是与 arg 最大的不同。
一般 arg 标签的变量仅用在构建过程中。而 environment 和 Dockerfile 中的 ENV 指令一样会把变量一直保存在镜像、容器中，类似 docker run -e 的效果。

```
environment:
  RACK_ENV: development
  SHOW: 'true'
  SESSION_SECRET:

environment:
  - RACK_ENV=development
  - SHOW=true
  - SESSION_SECRET
```


##### networks
加入指定网络，格式如下：

```
services:
  some-service:
    networks:
     - some-network
     - other-network


# 关于这个标签还有一个特别的子标签aliases，这是一个用来设置服务别名的标签，例如：
services:
  some-service:
    networks:
      some-network:
        aliases:
         - alias1
         - alias3
      other-network:
        aliases:
         - alias2
相同的服务可以在不同的网络有不同的别名。
```



##### network_mode

设置网络模式。使用和 docker run 的 --network 参数一样的值。
```
network_mode: "bridge"
network_mode: "host"
network_mode: "none"
network_mode: "service:[service name]"
network_mode: "container:[container name/id]"
```


#### networks

```
# 配置容器连接的网络。
version: "3"
services:

  some-service:
    networks:
     - some-network
     - other-network

networks:
  some-network:
  other-network:
```
