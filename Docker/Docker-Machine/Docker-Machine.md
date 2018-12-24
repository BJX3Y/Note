### 命令集

```
Usage: docker-machine [OPTIONS] COMMAND [arg...]

Create and manage machines running Docker.

Version: 0.12.2, build 9371605

Author:
  Docker Machine Contributors - <https://github.com/docker/machine>

Options:
  --debug, -D						Enable debug mode
  --storage-path, -s "/Users/hongbo/.docker/machine"	Configures storage path [$MACHINE_STORAGE_PATH]
  --tls-ca-cert 					CA to verify remotes against [$MACHINE_TLS_CA_CERT]
  --tls-ca-key 						Private key to generate certificates [$MACHINE_TLS_CA_KEY]
  --tls-client-cert 					Client cert to use for TLS [$MACHINE_TLS_CLIENT_CERT]
  --tls-client-key 					Private key used in client TLS auth [$MACHINE_TLS_CLIENT_KEY]
  --github-api-token 					Token to use for requests to the Github API [$MACHINE_GITHUB_API_TOKEN]
  --native-ssh						Use the native (Go-based) SSH implementation. [$MACHINE_NATIVE_SSH]
  --bugsnag-api-token 					BugSnag API token for crash reporting [$MACHINE_BUGSNAG_API_TOKEN]
  --help, -h						show help
  --version, -v						print the version

Commands:
  active		Print which machine is active
  config		Print the connection config for machine
  create		Create a machine
  env			Display the commands to set up the environment for the Docker client
  inspect		Inspect information about a machine
  ip			Get the IP address of a machine
  kill			Kill a machine
  ls			List machines
  provision		Re-provision existing machines
  regenerate-certs	Regenerate TLS Certificates for a machine
  restart		Restart a machine
  rm			Remove a machine
  ssh			Log into or run a command on a machine with SSH.
  scp			Copy files between machines
  start			Start a machine
  status		Get the status of a machine
  stop			Stop a machine
  upgrade		Upgrade a machine to the latest version of Docker
  url			Get the URL of a machine
  version		Show the Docker Machine version or a machine docker version
  help			Shows a list of commands or help for one command

Run 'docker-machine COMMAND --help' for more information on a command.


  active 查看活跃的 Docker 主机
  config 输出连接的配置信息
  create 创建一个 Docker 主机
  env 显示连接到某个主机需要的环境变量
  inspect 输出主机更多信息
  ip 获取主机地址
  kill 停止某个主机
  ls 列出所有管理的主机
  provision 重新设置一个已存在的主机
  regenerate-certs 为某个主机重新生成 TLS 认证信息
  restart 重启主机
  rm 删除某台主机
  ssh SSH 到主机上执行命令
  scp 在主机之间复制文件
  mount 挂载主机目录到本地
  start 启动一个主机
  status 查看主机状态
  stop 停止一个主机
  upgrade 更新主机 Docker 版本为最新
  url 获取主机的 URL
  version 输出 docker-machine 版本信息
  help 输出帮助信息
```

>负责在多种平台上快速安装 Docker 环境。

>Docker Machine 项目基于 Go 语言实现





### 使用

>Docker Machine 支持多种后端驱动，包括虚拟机、本地主机和云平台等。


#### 创建本地主机实例

使用 virtualbox 类型的驱动，创建一台 Docker 主机，命名为 test。

```
$ docker-machine create -d virtualbox test

# 你也可以在创建时加上如下参数，来配置主机或者主机上的 Docker。
--engine-opt dns=114.114.114.114 配置 Docker 的默认 DNS
--engine-registry-mirror https://registry.docker-cn.com 配置 Docker 的仓库镜像
--virtualbox-memory 2048 配置主机内存
--virtualbox-cpu-count 2 配置主机 CPU

# 更多参数请使用 docker-machine create --driver virtualbox --help 命令查看。
```
