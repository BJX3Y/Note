```
root@iZj6calh9xh0ham45c8ekqZ:~# ps --help

Usage:
 ps [options]

 Try 'ps --help <simple|list|output|threads|misc|all>'
  or 'ps --help <s|l|o|t|m|a>'
 for additional help text.

For more details see ps(1).
```

```
root@iZj6calh9xh0ham45c8ekqZ:~# ps --help a

Usage:
 ps [options]

Basic options:
 -A, -e               all processes
 -a                   all with tty, except session leaders
  a                   all with tty, including other users
 -d                   all except session leaders
 -N, --deselect       negate selection
  r                   only running processes
  T                   all processes on this terminal
  x                   processes without controlling ttys

Selection by list:
 -C <command>         command name
 -G, --Group <GID>    real group id or name
 -g, --group <group>  session or effective group name
 -p, p, --pid <PID>   process id
        --ppid <PID>  parent process id
 -q, q, --quick-pid <PID>
                      process id (quick mode)
 -s, --sid <session>  session id
 -t, t, --tty <tty>   terminal
 -u, U, --user <UID>  effective user id or name
 -U, --User <UID>     real user id or name

  The selection options take as their argument either:
    a comma-separated list e.g. '-u root,nobody' or
    a blank-separated list e.g. '-p 123 4567'

Output formats:
 -F                   extra full
 -f                   full-format, including command lines
  f, --forest         ascii art process tree
 -H                   show process hierarchy
 -j                   jobs format
  j                   BSD job control format
 -l                   long format
  l                   BSD long format
 -M, Z                add security data (for SELinux)
 -O <format>          preloaded with default columns
  O <format>          as -O, with BSD personality
 -o, o, --format <format>
                      user-defined format
  s                   signal format
  u                   user-oriented format
  v                   virtual memory format
  X                   register format
 -y                   do not show flags, show rss vs. addr (used with -l)
     --context        display security context (for SELinux)
     --headers        repeat header lines, one per page
     --no-headers     do not print header at all
     --cols, --columns, --width <num>
                      set screen width
     --rows, --lines <num>
                      set screen height

Show threads:
  H                   as if they were processes
 -L                   possibly with LWP and NLWP columns
 -m, m                after processes
 -T                   possibly with SPID column

Miscellaneous options:
 -c                   show scheduling class with -l option
  c                   show true command name
  e                   show the environment after command
  k,    --sort        specify sort order as: [+|-]key[,[+|-]key[,...]]
  L                   show format specifiers
  n                   display numeric uid and wchan
  S,    --cumulative  include some dead child process data
 -y                   do not show flags, show rss (only with -l)
 -V, V, --version     display version information and exit
 -w, w                unlimited output width

        --help <simple|list|output|threads|misc|all>
                      display help and exit

For more details see ps(1).
```


**ps命令是Process Status的缩写**

ps命令用来列出系统中当前运行的那些进程。ps命令列出的是当前那些进程的快照，就是执行ps命令的那个时刻的那些进程，如果想要动态的显示进程信息，就可以使用top命令。

要对进程进行监测和控制，首先必须要了解当前进程的情况，也就是需要查看当前进程，而 ps 命令就是最基本同时也是非常强大的进程查看命令。使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵死、哪些进程占用了过多的资源等等。


>注：kill 命令用于杀死进程。

### linux上进程有5种状态:

+ 运行(正在运行或在运行队列中等待)
+ 中断(休眠中, 受阻, 在等待某个条件的形成或接受到信号)
+ 不可中断(收到信号不唤醒和不可运行, 进程必须等待直到有中断发生)
+ 僵死(进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放)
+ 停止(进程收到SIGSTOP, SIGTSTP, SIGTTIN, SIGTTOU信号后停止运行运行)


ps工具标识进程的5种状态码:

+ D 不可中断 uninterruptible sleep (usually IO)
+ R 运行 runnable (on run queue)
+ S 中断 sleeping
+ T 停止 traced or stopped
+ Z 僵死 a defunct (”zombie”) process



### 命令参数

```
a 显示所有进程
-a 显示同一终端下的所有程序
-A 显示所有进程
c 显示进程的真实名称
-N 反向选择
-e 等于“-A”
e 显示环境变量
f 显示程序间的关系
-H 显示树状结构
r 显示当前终端的进程
T 显示当前终端的所有程序
u 指定用户的所有进程
-au 显示较详细的资讯
-aux 显示所有包含其他使用者的行程
-C<命令> 列出指定命令的状况
–lines<行数> 每页显示的行数
–width<字符数> 每页显示的字符数
–help 显示帮助信息
–version 显示版本显示
```

### 输出列的含义

+ F      代表这个程序的旗标 (flag)， 4 代表使用者为 super user
+ S      代表这个程序的状态 (STAT)，关于各 STAT 的意义将在内文介绍
+ UID    程序被该 UID 所拥有
+ PID    进程的ID
+ PPID   则是其上级父程序的ID
+ C CPU  使用的资源百分比
+ PRI    这个是 Priority (优先执行序) 的缩写，详细后面介绍
+ NI     这个是 Nice 值，在下一小节我们会持续介绍
+ ADDR   这个是 kernel function，指出该程序在内存的那个部分。如果是个 + running的程序，一般就是 “-“
+ SZ     使用掉的内存大小
+ WCHAN  目前这个程序是否正在运作当中，若为 - 表示正在运作
+ TTY    登入者的终端机位置
+ TIME   使用掉的 CPU 时间。
+ CMD    所下达的指令为何
