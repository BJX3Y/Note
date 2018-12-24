http://www.redis.net.cn/order/3531.html

#### DEL
Redis DEL 命令 - 该命令用于在 key 存在是删除 key。
> DEL KEY_NAME

**返回值**:被删除 key 的数量。




#### Dump
Redis Dump 命令 - 序列化给定 key ，并返回被序列化的值。
> DUMP KEY_NAME

**返回值**:如果 key 不存在，那么返回 nil 。 否则，返回序列化之后的值。



#### exists

Redis EXISTS 命令 - 检查给定 key 是否存在。

> EXISTS KEY_NAME

**返回值**:若 key 存在返回 1 ，否则返回 0 。



#### Expire
Redis Expire 命令 - seconds 为给定 key 设置过期时间。
> Expire KEY_NAME TIME_IN_SECONDS

**返回值**:设置成功返回 1 。 当 key 不存在或者不能为 key 设置过期时间时(比如在低于 2.1.3 版本的 Redis 中你尝试更新 key 的过期时间)返回 0 。


#### Expireat

Redis Expireat 命令 - EXPIREAT 的作用和 EXPIRE 类似，都用于为 key 设置过期时间。 不同在于 EXPIREAT 命令接受的时间参数是 UNIX 时间戳(unix timestamp)。

> Expireat KEY_NAME TIME_IN_UNIX_TIMESTAMP

**返回值**:设置成功返回 1 。 当 key 不存在或者不能为 key 设置过期时间时(比如在低于 2.1.3 版本的 Redis 中你尝试更新 key 的过期时间)返回 0 。




#### keys

Redis Keys 命令 - 查找所有符合给定模式( pattern)的 key .

> KEYS PATTERN

**返回值**:符合给定模式的 key 列表 (Array)。


#### move

Redis Move 命令 - 将当前数据库的 key 移动到给定的数据库 db 当中。

> MOVE KEY_NAME DESTINATION_DATABASE

**返回值**:移动成功返回 1 ，失败则返回 0 。





#### persist

Redis PERSIST 命令 - 移除 key 的过期时间，key 将持久保持。

> PERSIST KEY_NAME

**返回值**:当过期时间移除成功时，返回 1 。 如果 key 不存在或 key 没有设置过期时间，返回 0 。







#### TTL

Redis TTL 命令 - 以秒为单位，返回给定 key 的剩余生存时间(TTL, time to live)。

> TTL KEY_NAME

**返回值**:当 key 不存在时，返回 -2 。 当 key 存在但没有设置剩余生存时间时，返回 -1 。 否则，以毫秒为单位，返回 key 的剩余生存时间。



#### pttl

Redis Pttl 命令 - 以毫秒为单位返回 key 的剩余的过期时间。

> PTTL KEY_NAME

**返回值**:当 key 不存在时，返回 -2 。 当 key 存在但没有设置剩余生存时间时，返回 -1 。 否则，以毫秒为单位，返回 key 的剩余生存时间。



#### Randomkey

Redis RANDOMKEY 命令 - 从当前数据库中随机返回一个 key 。

> RANDOMKEY

**返回值**:当数据库不为空时，返回一个 key 。 当数据库为空时，返回 nil 。



#### rename

Redis Rename 命令 - 修改 key 的名称

> RENAME OLD_KEY_NAME NEW_KEY_NAME

**返回值**:改名成功时提示 OK ，失败时候返回一个错误。 当 OLD_KEY_NAME 和 NEW_KEY_NAME 相同，或者 OLD_KEY_NAME 不存在时，返回一个错误。 当 NEW_KEY_NAME 已经存在时， RENAME 命令将覆盖旧值。



#### renamenx

Redis Renamenx 命令 - 仅当 newkey 不存在时，将 key 改名为 newkey 。

> RENAMENX OLD_KEY_NAME NEW_KEY_NAME

**返回值**:修改成功时，返回 1 。 如果 NEW_KEY_NAME 已经存在，返回 0 。



#### Type
Redis Type 命令用于返回 key 所储存的值的类型。
> TYPE KEY_NAME

`返回值:`返回 key 的数据类型，数据类型有：

+ none (key不存在)
+ string (字符串)
+ list (列表)
+ set (集合)
+ zset (有序集)
+ hash (哈希表)











#
