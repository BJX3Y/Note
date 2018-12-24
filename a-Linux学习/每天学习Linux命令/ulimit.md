**ulimit命令用来限制系统用户对shell资源的访问**

>当一台 Linux 主机上同时登陆了 10 个人，在系统资源无限制的情况下，这 10 个用户同时打开了 500 个文档，而假设每个文档的大小有 10M，这时系统的内存资源就会受到巨大的挑战。
而实际应用的环境要比这种假设复杂的多，例如在一个嵌入式开发环境中，各方面的资源都是非常紧缺的，对于开启文件描述符的数量，分配堆栈的大 小，CPU 时间，虚拟内存大小，等等，都有非常严格的要求。资源的合理限制和分配，不仅仅是保证系统可用性的必要条件，也与系统上软件运行的性能有着密不可分的联 系。这时，ulimit 可以起到很大的作用，它是一种简单并且有效的实现资源限制的方式。


### ulimit 用于限制 `shell 启动进程` 所占用的资源，
支持以下各种类型的限制：
+ 所创建的内核文件的大小、
+ 进程数据块的大小、
+ Shell 进程创建文件的大小、
+ 内存锁住的大小、
+ 常驻内存集的大小、
+ 打开文件描述符的数量、
+ 分配堆栈的最大大小、
+ CPU 时间、
+ 单个用户的最大线程数、
+ Shell 进程所能使用的最大虚拟内存。
+ 同时，它支持硬资源和软资源的限制。

作为临时限制，ulimit 可以作用于通过使用其命令登录的 shell 会话，在会话终止时便结束限制，并不影响于其他 shell 会话。而对于长期的固定限制，ulimit 命令语句又可以被添加到由登录 shell 读取的文件中，作用于特定的 shell 用户。

```
-a：显示目前资源限制的设定；
-c <core文件上限>：设定core文件的最大值，单位为区块；
-d <数据节区大小>：程序数据节区的最大值，单位为KB；
-f <文件大小>：shell所能建立的最大文件，单位为区块；
-H：设定资源的硬性限制，也就是管理员所设下的限制；
-m <内存大小>：指定可使用内存的上限，单位为KB；
-n <文件数目>：指定同一时间最多可开启的文件数；
-p <缓冲区大小>：指定管道缓冲区的大小，单位512字节；
-s <堆叠大小>：指定堆叠的上限，单位为KB；
-S：设定资源的弹性限制；
-t <CPU时间>：指定CPU使用时间的上限，单位为秒；
-u <程序数目>：用户最多可开启的程序数目；
-v <虚拟内存大小>：指定可使用的虚拟内存上限，单位为KB。
```

```
(env3.6.1) ➜  ~ ulimit -a
-t: cpu time (seconds)              unlimited
-f: file size (blocks)              unlimited
-d: data seg size (kbytes)          unlimited
-s: stack size (kbytes)             8192
-c: core file size (blocks)         0
-v: address space (kbytes)          unlimited
-l: locked-in-memory size (kbytes)  unlimited
-u: processes                       709
-n: file descriptors                4864
```

```
[root@localhost ~]# ulimit -a
core file size          (blocks, -c) 0           #core文件的最大值为100 blocks。
data seg size           (kbytes, -d) unlimited   #进程的数据段可以任意大。
scheduling priority             (-e) 0
file size               (blocks, -f) unlimited   #文件可以任意大。
pending signals                 (-i) 98304       #最多有98304个待处理的信号。
max locked memory       (kbytes, -l) 32          #一个任务锁住的物理内存的最大值为32KB。
max memory size         (kbytes, -m) unlimited   #一个任务的常驻物理内存的最大值。
open files                      (-n) 1024        #一个任务最多可以同时打开1024的文件。
pipe size            (512 bytes, -p) 8           #管道的最大空间为4096字节。
POSIX message queues     (bytes, -q) 819200      #POSIX的消息队列的最大值为819200字节。
real-time priority              (-r) 0
stack size              (kbytes, -s) 10240       #进程的栈的最大值为10240字节。
cpu time               (seconds, -t) unlimited   #进程使用的CPU时间。
max user processes              (-u) 98304       #当前用户同时打开的进程（包括线程）的最大个数为98304。
virtual memory          (kbytes, -v) unlimited   #没有限制进程的最大地址空间。
file locks                      (-x) unlimited   #所能锁住的文件的最大个数没有限制。
```

### 永久配置

以上配置只对当前会话起作用，下次重新登陆后，还是得重新配置。要想配置永久生效，得在`/etc/profile`或者`/etc/security/limits.conf`文件中进行配置。


### /etc/security/limits.conf配置文件

```
root@iZj6calh9xh0ham45c8ekqZ:~# cat /etc/security/limits.conf
# /etc/security/limits.conf
#
#Each line describes a limit for a user in the form:
#
#<domain>        <type>  <item>  <value>
#
#Where:
#<domain> can be:
#        - a user name
#        - a group name, with @group syntax
#        - the wildcard *, for default entry
#        - the wildcard %, can be also used with %group syntax,
#                 for maxlogin limit
#        - NOTE: group and wildcard limits are not applied to root.
#          To apply a limit to the root user, <domain> must be
#          the literal username root.
#
#<type> can have the two values:
#        - "soft" for enforcing the soft limits
#        - "hard" for enforcing hard limits
#
#<item> can be one of the following:
#        - core - limits the core file size (KB)
#        - data - max data size (KB)
#        - fsize - maximum filesize (KB)
#        - memlock - max locked-in-memory address space (KB)
#        - nofile - max number of open files
#        - rss - max resident set size (KB)
#        - stack - max stack size (KB)
#        - cpu - max CPU time (MIN)
#        - nproc - max number of processes
#        - as - address space limit (KB)
#        - maxlogins - max number of logins for this user
#        - maxsyslogins - max number of logins on the system
#        - priority - the priority to run user process with
#        - locks - max number of file locks the user can hold
#        - sigpending - max number of pending signals
#        - msgqueue - max memory used by POSIX message queues (bytes)
#        - nice - max nice priority allowed to raise to values: [-20, 19]
#        - rtprio - max realtime priority
#        - chroot - change root to directory (Debian-specific)
#
#<domain>      <type>  <item>         <value>
#

#*               soft    core            0
#root            hard    core            100000
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#ftp             -       chroot          /ftp
#@student        -       maxlogins       4

# End of file
root soft nofile 65535
root hard nofile 65535
* soft nofile 65535
* hard nofile 65535
```

```
或者在/etc/profile中作如下配置：
#vim /etc/profile
ulimit -S -c unlimited >/dev/null 2>&1

或者想配置只针对某一用户有效，则修改此用户的~/.bashrc或者~/.bash_profile文件：
limit -c unlimited
ulimit -c 0 是禁止产生core文件，而ulimit -c 1024则限制产生的core文件的大小不能超过1024kb
```

### 设置Core Dump的核心转储文件目录和命名规则

+ `/proc/sys/kernel/core_uses_pid`可以控制产生的core文件的文件名中是否添加pid作为扩展，如果添加则文件内容为1，否则为0

+ `/proc/sys/kernel/core_pattern`可以设置格式化的core文件保存位置或文件名，比如原来文件内容是core-%e

可以这样修改:
```
echo "/corefile/core-%e-%p-%t" > /proc/sys/kernel/core_pattern
```
将会控制所产生的core文件会存放到/corefile目录下，产生的文件名为core-命令名-pid-时间戳

以下是参数列表:
```
%p - insert pid into filename 添加pid
%u - insert current uid into filename 添加当前uid
%g - insert current gid into filename 添加当前gid
%s - insert signal that caused the coredump into the filename 添加导致产生core的信号
%t - insert UNIX time that the coredump occurred into filename 添加core文件生成时的unix时间
%h - insert hostname where the coredump happened into filename 添加主机名
%e - insert coredumping executable name into filename 添加命令名
```


### 如何让一个正常的程序down:
```
#kill -s SIGSEGV pid
```

### 生成core文件测试

### 导致 core 的信号如下:

信号（signal）   |    描述
----------------|--------------------
SIGABRT	        |    异常终止（abort()）
SIGBUS	        |    硬件异常，通常是错误的内存访问
SIGEMT	        |    硬件异常
SIGTRAP	        |    硬件异常。一般是调试异常
SIGILL	        |    非法指令异常
SIGIOT	        |    硬件异常，一般对应SIGABRT
SIGFPE	        |    算术异常，如被0除，浮点溢出等
SIGILL	        |    非法指令异常
SIGQUIT	        |    终端退出符
SIGSEGV	        |    非法内存访问
SIGSYS	        |    非法系统调用
SIGXCPU	        |    CPU时间限制超时(setrlimit)
SIGXFSZ	        |    超过文件长度限制(setrlimit)
