Redis 脚本使用 `Lua 解释器` 来执行脚本。

Redis 2.6 版本通过内嵌支持 Lua 环境。`执行脚本的常用命令为 EVAL`。



### Redis 脚本命令

```
EVAL script numkeys key [key ...] arg [arg ...]
执行 Lua 脚本。

EVALSHA sha1 numkeys key [key ...] arg [arg ...]
执行 Lua 脚本。

SCRIPT EXISTS script [script ...]
查看指定的脚本是否已经被保存在缓存当中。

SCRIPT FLUSH
从脚本缓存中移除所有脚本

SCRIPT KILL
杀死当前正在运行的 Lua 脚本。

SCRIPT LOAD script
将脚本 script 添加到脚本缓存中，但并不立即执行这个脚本。
```
