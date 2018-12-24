```
root@iZj6calh9xh0ham45c8ekqZ:/# wc --help
Usage: wc [OPTION]... [FILE]...
  or:  wc [OPTION]... --files0-from=F
Print newline, word, and byte counts for each FILE, and a total line if
more than one FILE is specified.  A word is a non-zero-length sequence of
characters delimited by white space.

With no FILE, or when FILE is -, read standard input.

The options below may be used to select which counts are printed, always in
the following order: newline, word, character, byte, maximum line length.
  -c, --bytes            print the byte counts
  -m, --chars            print the character counts
  -l, --lines            print the newline counts
      --files0-from=F    read input from the files specified by
                           NUL-terminated names in file F;
                           If F is - then read names from standard input
  -L, --max-line-length  print the maximum display width
  -w, --words            print the word counts
      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <http://www.gnu.org/software/coreutils/>
Full documentation at: <http://www.gnu.org/software/coreutils/wc>
or available locally via: info '(coreutils) wc invocation'
```

```
who | wc -l
```

`|(管道) `符号可以在两个程序之间建立管道 (pipeline):who 的输出，成了 wc 的输入。


### 脚本位于第一行的 #!

当 shell 执行一个程序时，会要求 linux 内核启动一个新的进程，以便在该进程里执行所指定的程序。 内核知道如何为编译性程序做这件事。 但是我们的nusers Shell 脚本并非编译性程序; 当 shell 要求内核执行它的时候，内核无法处理，并且回应“not executable format file”，接着会启动一个新的 /bin/sh(标准 shell) 副本来执行该程序。


shell 脚本的第一行通常是 #!/bin/sh。如果不这样是不符合标准的，自觉修改这个路径，将其改为符合 POSIX 标准的 shell。






**如果多个命令之间使用的是 & 符号，而不是分号，则 shell 将在后台执行其前面的命令，这意味着 shell 不用等到该命令的完成，就可以继续执行下一个命令。**
