“#!” 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell

```
#!/bin/bash
echo "Hello World !"
```

```
echo $$       # $表示当前 Shell 进程的 ID，即 pid
```

#### 特殊变量列表

```
$0	当前脚本的文件名
$n	传递给脚本或函数的参数。n 是一个数字，表示第几个参数。例如，第一个参数是$1，第二个参数是$2。
$#	传递给脚本或函数的参数个数。
$*	传递给脚本或函数的所有参数。
$@	传递给脚本或函数的所有参数。被双引号(" ")包含时，与 $* 稍有不同，下面将会讲到。
$?	上个命令的退出状态，或函数的返回值。
$$	当前 Shell 进程 ID。对于 Shell 脚本，就是这些脚本所在的进程 ID。
```

#### 命令行参数

```
运行脚本时传递给脚本的参数称为命令行参数。命令行参数用 $n 表示，例如，$1 表示第一个参数，$2 表示第二个参数，依次类推。
```


#### `$* 和 $@ 的区别`

```
$* 和 $@ 都表示传递给函数或脚本的所有参数，
不被双引号(" ")包含时，
都以"$1" "$2" … "$n" 的形式输出所有参数。

但是当它们被双引号(" ")包含时，
"$*" 会将所有的参数作为一个整体，以"$1 $2 … $n"的形式输出所有参数；
"$@" 会将各个参数分开，以"$1" "$2" … "$n" 的形式输出所有参数。


下面的例子可以清楚的看到 $* 和 $@ 的区别：

#!/bin/bash
echo "\$*=" $*
echo "\"\$*\"=" "$*"

echo "\$@=" $@
echo "\"\$@\"=" "$@"

echo "print each param from \$*"
for var in $*
do
    echo "$var"
done

echo "print each param from \$@"
for var in $@
do
    echo "$var"
done

echo "print each param from \"\$*\""
for var in "$*"
do
    echo "$var"
done

echo "print each param from \"\$@\""
for var in "$@"
do
    echo "$var"
done




执行 ./test.sh "a" "b" "c" "d"，看到下面的结果：

$*=  a b c d
"$*"= a b c d
$@=  a b c d
"$@"= a b c d
print each param from $*
a
b
c
d
print each param from $@
a
b
c
d
print each param from "$*"
a b c d
print each param from "$@"
a
b
c
d

```

#### 退出状态
```
$? 可以获取上一个命令的退出状态。所谓退出状态，就是上一个命令执行后的返回结果。

退出状态是一个数字，一般情况下，大部分命令执行成功会返回0，失败返回1。
```

**$? 也可以表示函数的返回值，后续将会讲**







[http://www.voidcn.com/article/p-fucequuc-bnw.html]
