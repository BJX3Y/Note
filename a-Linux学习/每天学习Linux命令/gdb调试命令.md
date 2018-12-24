### gcc
+ `-g` : `加上-g 选项，会保留代码的文字信息，便于调试` 1. 创建符号表，符号表包含了程序中使用的变量名称的列表。2. 关闭所有的优化机制，以便程序执行过程中严格按照原来的C代码进行。

### Linux下core文件

Core文件其实就是内存的映像，当程序崩溃时，存储内存的相应信息，主用用于对程序进行调试。
当程序崩溃时便会产生core文件，其实准确的应该说是core dump 文件,默认生成位置与可执行程序位于同一目录下，文件名为 `core.xxx`,其中xxx是某一数字。

#### 1. 开启或关闭Core文件的生成

+ 关闭或阻止core文件生成：

```
$ulimit -c 0
```

+ 打开core文件生成：

```
$ulimit -c unlimited
```

+ 检查core文件的选项是否打开：

```
$ulimit -a

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





在shell中，每个进程都和三个系统文件相关联：标准输入stdin，标准输出stdout、标准错误stderr，三个系统文件的文件描述符分别为0，1、2。所以这里2>&1 的意思就是将标准错误也输出到标准输出当中





******************

+ 有时候程序会异常退出而不带任何日志，此时就可以使用 code 文件进行分析，它会记录程序运行的内存，寄存器，堆栈指针等信息


使用GDB调试PHP代码，解决PHP代码死循环

一般来说GDB主要调试的是C/C++的程序。要调试C/C++的程序，首先在编译时，我们必须要把调试信息加到可执行文件中。使用编译器（cc/gcc/g++）的 -g 参数可以做到这一点。如：

```
$gcc -g -Wall hello.c -o hello
```

**如果没有-g，你将看不见程序的函数名、变量名，所代替的全是运行时的内存地址.**


### gdb参数详解

```
root@iZj6calh9xh0ham45c8ekqZ:~# gdb --help
This is the GNU debugger.  Usage:

    gdb [options] [executable-file [core-file or process-id]]
    gdb [options] --args executable-file [inferior-arguments ...]

Selection of debuggee and its files:

  --args             Arguments after executable-file are passed to inferior
  --core=COREFILE    Analyze the core dump COREFILE.
  --exec=EXECFILE    Use EXECFILE as the executable.
  --pid=PID          Attach to running process PID.
  --directory=DIR    Search for source files in DIR.
  --se=FILE          Use FILE as symbol file and executable file.
  --symbols=SYMFILE  Read symbols from SYMFILE.
  --readnow          Fully read symbol files on first access.
  --write            Set writing into executable and core files.

Initial commands and command files:

  --command=FILE, -x Execute GDB commands from FILE.
  --init-command=FILE, -ix
                     Like -x but execute commands before loading inferior.
  --eval-command=COMMAND, -ex
                     Execute a single GDB command.
                     May be used multiple times and in conjunction
                     with --command.
  --init-eval-command=COMMAND, -iex
                     Like -ex but before loading inferior.
  --nh               Do not read ~/.gdbinit.
  --nx               Do not read any .gdbinit files in any directory.

Output and user interface control:

  --fullname         Output information used by emacs-GDB interface.
  --interpreter=INTERP
                     Select a specific interpreter / user interface
  --tty=TTY          Use TTY for input/output by the program being debugged.
  -w                 Use the GUI interface.
  --nw               Do not use the GUI interface.
  --tui              Use a terminal user interface.
  --dbx              DBX compatibility mode.
  -q, --quiet, --silent
                     Do not print version number on startup.

Operating modes:

  --batch            Exit after processing options.
  --batch-silent     Like --batch, but suppress all gdb stdout output.
  --return-child-result
                     GDB exit code will be the child's exit code.
  --configuration    Print details about GDB configuration and then exit.
  --help             Print this message and then exit.
  --version          Print version information and then exit.

Remote debugging options:

  -b BAUDRATE        Set serial port baud rate used for remote debugging.
  -l TIMEOUT         Set timeout in seconds for remote debugging.

Other options:

  --cd=DIR           Change current directory to DIR.
  --data-directory=DIR, -D
                     Set GDB's data-directory to DIR.

At startup, GDB reads the following init files and executes their commands:
   * system-wide init file: /etc/gdb/gdbinit

For more information, type "help" from within GDB, or consult the
GDB manual (available as on-line info or a printed manual).
Report bugs to "<http://www.gnu.org/software/gdb/bugs/>".
```




### gdb 交互式命令

启动gdb后，进入到交互模式，通过以下命令完成对程序的调试；

注意高频使用的命令一般都会有缩写，熟练使用这些缩写命令能提高调试的效率；

#### 运行
+ `run` ：简记为 r ，其作用是运行程序，当遇到断点后，程序会在断点处停止运行，等待用户输入下一步的命令。

+ `continue` （简写c ）：继续执行，到下一个断点处（或运行结束）

+ `next` ：（简写 n），单步跟踪程序，当遇到函数调用时，也不进入此函数体；此命令同 step 的主要区别是，step 遇到用户自定义的函数，将步进到函数中去运行，而 next 则直接调用函数，不会进入到函数体内。

+ `step` : （简写s）：单步调试如果有函数调用，则进入函数；与命令n不同，n是不进入调用的函数的

+ `until` ：当你厌倦了在一个循环体内单步跟踪时，这个命令可以运行程序直到退出循环体。

+ `until`+行号： 运行至某行，不仅仅用来跳出循环

+ `finish`： 运行程序，直到当前函数完成返回，并打印函数返回时的堆栈地址和返回值及参数值等信息。

+ `call` 函数(参数)：调用程序中可见的函数，并传递“参数”，如：call gdb_test(55)

+ `quit`：简记为 q ，退出gdb


#### 设置断点

+ `break n` （`简写b n`）:在第n行处设置断点

+ （可以带上代码路径和代码名称： `b OAGUPDATE.cpp:578`）

+ `b fn1 if a＞b`：条件断点设置

+ `break func`（break缩写为b）：在函数func()的入口处设置断点，如：break cb_button

+ `delete 断点号n`：删除第n个断点

+ `disable 断点号n`：暂停第n个断点

+ `enable 断点号n`：开启第n个断点

+ `clear 行号n`：清除第n行的断点

+ `info b （info breakpoints）` ：显示当前程序的断点设置情况

+ `delete breakpoints`：清除所有断点：



#### 查看源代码
+ `list` ：简记为 l ，其作用就是列出程序的源代码，默认每次显示10行。

+ `list 行号`：将显示当前文件以“行号”为中心的前后10行代码，如：list 12

+ `list 函数名`：将显示“函数名”所在函数的源代码，如：list main

+ `list` ：不带参数，将接着上一次 list 命令的，输出下边的内容。


#### 打印表达式
+ `print 表达式`：简记为 p ，其中“表达式”可以是任何当前正在被测试程序的有效表达式，比如当前正在调试C语言的程序，那么“表达式”可以是任何C语言的有效表达式，包括数字，变量甚至是函数调用。

+ `print a`：将显示整数 a 的值

+ `print ++a`：将把 a 中的值加1,并显示出来

+ `print name`：将显示字符串 name 的值

+ `print gdb_test(22)`：将以整数22作为参数调用gdb_test() 函数

+ `print gdb_test(a)`：将以变量 a 作为参数调用 gdb_test() 函数

+ `display 表达式`：在单步运行时将非常有用，使用display命令设置一个表达式后，它将在每次单步进行指令后，紧接着输出被设置的表达式及值。如： display a

+ `watch 表达式`：设置一个监视点，一旦被监视的“表达式”的值改变，gdb将强行终止正在被调试的程序。如： watch a

+ `whatis` ：查询变量或函数

+ `info function`： 查询函数

+ `扩展info locals`： 显示当前堆栈页的所有变量


#### 查询运行信息
+ `where/bt` ：当前运行的堆栈列表；

+ `bt backtrace` 显示当前调用堆栈

+ `up/down` 改变堆栈显示的深度

+ `set args 参数`:指定运行时的参数

+ `show args`：查看设置好的参数

+ `info program`： 来查看程序的是否在运行，进程号，被暂停的原因。


#### 分割窗口

+ `layout`：用于分割窗口，可以一边查看代码，一边测试：

+ `layout src`：显示源代码窗口

+ `layout asm`：显示反汇编窗口

+ `layout regs`：显示源代码/反汇编和CPU寄存器窗口

+ `layout split`：显示源代码和反汇编窗口

+ `Ctrl + L`：刷新窗口



>[**注意**] : 交互模式下直接回车的作用是重复上一指令，对于单步调试非常方便；




### 界面化测试工具

```
# gdb -tui
```


### 更为强大的工具 `cgdb`






### gdb 调试PHP
