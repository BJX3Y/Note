Redis 事务可以一次执行多个命令， 并且带有以下两个重要的保证：

批量操作在发送 EXEC 命令前被放入队列缓存。

+ 收到 EXEC 命令后进入事务执行，事务中任意命令执行失败，其余的命令依然被执行。
+ 在事务执行过程，其他客户端提交的命令请求不会插入到事务执行命令序列中。

一个事务从开始到执行会经历以下三个阶段：

+ 开始事务。
+ 命令入队。
+ 执行事务。


### 事务的例子

它先以 `MULTI` 开始一个事务，
然后将多个命令入队到事务中，
最后由 `EXEC` 命令触发事务， 一并执行事务中的所有命令：

```
redis 127.0.0.1:6379> MULTI
OK

redis 127.0.0.1:6379> SET book-name "Mastering C++ in 21 days"
QUEUED

redis 127.0.0.1:6379> GET book-name
QUEUED

redis 127.0.0.1:6379> SADD tag "C++" "Programming" "Mastering Series"
QUEUED

redis 127.0.0.1:6379> SMEMBERS tag
QUEUED

redis 127.0.0.1:6379> EXEC
1) OK
2) "Mastering C++ in 21 days"
3) (integer) 3
4) 1) "Mastering Series"
   2) "C++"
   3) "Programming"
```

>单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务的执行并不是原子性的。

>事务可以理解为一个打包的批量执行脚本，但批量指令并非原子化的操作，中间某条指令的失败不会导致前面已做指令的回滚，也不会造成后续的指令不做。


### Redis 事务命令

````
DISCARD
取消事务，放弃执行事务块内的所有命令。

EXEC
执行所有事务块内的命令。

MULTI
标记一个事务块的开始。

UNWATCH
取消 WATCH 命令对所有 key 的监视。

WATCH key [key ...]
监视一个(或多个) key ，如果在事务执行之前这个(或这些) key 被其他命令所改动，那么事务将被打断。
```
