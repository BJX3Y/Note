### 网络相关

docker 提供给我们多种(4种)网络模式，我们可以根据自己的需求来使用。

**例如我们在一台主机（host）或者同一个docker engine上面运行continer的时候，我们就可以选择bridge网络模式；**

**而当我们需要在多台host上来运行多个container来协同工作的时候，overlay模式就是我们的首选。**

#### 网络驱动

Docker的网络子系统是可插拔的，使用驱动程序。默认情况下存在几个驱动程序，并提供核心网络功能：

+ bridge：`默认的网络驱动程序`。如果您不指定驱动程序，则这是您正在创建的网络类型。当您的应用程序运行在需要通信的独立容器中时，通常会使用桥接网络。

+ host：对于独立容器，删除容器和Docker主机之间的网络隔离，并直接使用主机的网络。host 仅适用于Docker 17.06及更高版本的群集服务。**这种网络模式将container与宿主机的网络相连通，虽然很直接，但是却破获了container的隔离性**。

+ **overlay**：覆盖网络将多个Docker守护进程连接在一起，并使群集服务能够相互通信。您还可以使用覆盖网络来促进swarm服务和独立容器之间的通信，或者不同Docker守护进程上的两个独立容器之间的通信。这种策略消除了在这些容器之间进行操作系统级路由的需求。请参阅覆盖网络。

+ macvlan：Macvlan网络允许您为容器分配MAC地址，使其显示为网络上的物理设备。Docker守护进程通过其MAC地址将流量路由到容器。使用macvlan 驱动程序有时是处理希望直接连接到物理网络的传统应用程序的最佳选择，而不是通过Docker主机的网络堆栈进行路由。请参阅 Macvlan网络。

+ none：对于此容器，禁用所有网络。通常与自定义网络驱动程序一起使用。none不适用于群组服务。**顾名思义，所有加入到这个网络模式中的container，都"不能”进行网络通信。**。


+ 网络插件[Network plugins]：您可以在Docker上安装和使用第三方网络插件。这些插件可从 Docker Store 或第三方供应商处获得。有关安装和使用给定网络插件的信息，请参阅供应商的文档。




```
services:
  python-server:
    image: python-falcon
    build: ./images/python
    container_name: web_python
    volumes:
      - ./app/python_web:/app
    ports:
      - "28000:8000"
    command: ['gunicorn', 'app', '--bind', '0.0.0.0:8000', '--timeout', '100']
    privileged: true
    restart: always
    networks:
      vpcbr:
        ipv4_address: 10.0.0.7

networks:
  vpcbr:
    driver: bridge
    ipam:
     config:
       - subnet: 10.0.0.0/16
         gateway: 10.0.0.1
```


Docker网络插件（IPAM Driver）:IPAM 驱动
在docker网络中，CNM(Container Network Management)模块通过IPAM(IP address management)驱动管理IP地址的分配。


为什么docker能够做到container之间的通信呢？ 答案就是 docker 内置的 DNS server.










**********

















### 网络相关命令


```
(env2.7.10) ➜  ~ docker network --help

Usage:	docker network COMMAND

Manage networks

Options:
      --help   Print usage

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
```


```
(env2.7.10) ➜  ~ docker network ls
NETWORK ID          NAME                   DRIVER              SCOPE
384f7b74e6d9        bridge                 bridge              local
d942fa0e0f0d        composeflask_default   bridge              local
025769a29896        host                   host                local
2f1c517c0be0        none                   null                local
```


```
(env2.7.10) ➜  ~ docker network connect --help

Usage:	docker network connect [OPTIONS] NETWORK CONTAINER

Connect a container to a network

Options:
      --alias stringSlice           Add network-scoped alias for the container
      --help                        Print usage
      --ip string                   IPv4 address (e.g., 172.30.100.104)
      --ip6 string                  IPv6 address (e.g., 2001:db8::33)
      --link list                   Add link to another container
      --link-local-ip stringSlice   Add a link-local address for the container
```

>**可见,不同的容器在不同的网络是可以起到隔离作用的,所以,自定义一个网络可以保证容器和容器之间通信安全.**
