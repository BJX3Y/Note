
ipcs是Linux下显示进程间通信设施状态的工具。可以显示消息队列、共享内存和信号量的信息。

```
root@iZj6calh9xh0ham45c8ekqZ:/Users/hongbo/code/Linux# ipcs

------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status

------ Semaphore Arrays --------
key        semid      owner      perms      nsems
```


```
root@iZj6calh9xh0ham45c8ekqZ:/Users/hongbo/code/Linux# ipcs --help

Usage:
 ipcs [resource-option...] [output-option]
 ipcs -m|-q|-s -i <id>

Show information on IPC facilities.

Options:
 -i, --id <id>  print details on resource identified by <id>
 -h, --help     display this help and exit
 -V, --version  output version information and exit

Resource options:  分别查看IPC资源
 -m, --shmems      shared memory segments
 -q, --queues      message queues
 -s, --semaphores  semaphores
 -a, --all         all (default)

Output options:
 -t, --time        show attach, detach and change times
 -p, --pid         show PIDs of creator and last operator
 -c, --creator     show creator and owner
 -l, --limits      show resource limits
 -u, --summary     show status summary
     --human       show sizes in human-readable format
 -b, --bytes       show sizes in bytes

For more details see ipcs(1).
```

### 系统IPC参数查询

```
root@iZj6calh9xh0ham45c8ekqZ:/Users/hongbo/code/Linux# ipcs -l

------ Messages Limits --------
max queues system wide = 32000
max size of message (bytes) = 8192
default max size of queue (bytes) = 16384

------ Shared Memory Limits --------
max number of segments = 4096
max seg size (kbytes) = 4177919
max total shared memory (kbytes) = 17112760316
min seg size (bytes) = 1

------ Semaphore Limits --------
max number of arrays = 32000
max semaphores per array = 32000
max semaphores system wide = 1024000000
max ops per semop call = 500
semaphore max value = 32767
```


### 修改IPC系统参数

以linux系统为例，在root用户下修改/etc/sysctl.conf 文件，保存后使用sysctl -p生效:
