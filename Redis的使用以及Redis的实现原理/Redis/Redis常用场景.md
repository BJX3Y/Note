[TOC]

### 字符串缓存实战

```
<?php

$redis = new Redis();

$redis->connect('127.0.0.1', 6379);
$strCacheKey  = 'Test_String_Cache';
$hashCacheKey  = 'Test_Hash_Cache';

//SET 应用
$arrCacheData = [
    'name' => 'job',
    'sex'  => '男',
    'age'  => '30'
];
$redis->set($strCacheKey, json_encode($arrCacheData));
$redis->expire($strCacheKey, 30);  # 设置30秒后过期
$json_data = $redis->get($strCacheKey);
$data = json_decode($json_data);
print_r($data->age); //输出数据

//HSET 应用
$arrWebSite = [
    'google' => [
        'google.com',
        'google.com.hk'
    ],
];
$redis->hSet($hashCacheKey, 'google', json_encode($arrWebSite['google']));
$json_data = $redis->hGet($hashCacheKey, 'google');
$data = json_decode($json_data);
print_r($data); //输出数据
```



### Queue实战

使用 `List` 结构

```
<?php

use Redis as PHPRedis;
use Predis\Client as Predis;

$redis = new PHPRedis();

$redis->connect('127.0.0.1', 6379);
$strQueueName  = 'Test_Redis_Queue';

//进队列
$redis->rpush($strQueueName, json_encode(['uid' => 1,'name' => 'Job']));
$redis->rpush($strQueueName, json_encode(['uid' => 2,'name' => 'Tom']));
$redis->rpush($strQueueName, json_encode(['uid' => 3,'name' => 'John']));
echo "---- 进队列成功 ---- <br /><br />".PHP_EOL;

//查看队列
$strCount = $redis->lrange($strQueueName, 0, -1);
echo "当前队列数据为： <br />".PHP_EOL;
print_r($strCount);

//出队列
$redis->lpop($strQueueName);
echo "<br /><br /> ---- 出队列成功 ---- <br /><br />".PHP_EOL;

//查看队列
$strCount = $redis->lrange($strQueueName, 0, -1);
echo "当前队列数据为： <br />".PHP_EOL;
print_r($strCount);
```






### 发布订阅  PUB/SUB

**Redis 发布订阅**

PHP远程访问函数default_socket_timeout (integer)
适用范围：PHP_INI_ALL;默认值：60
该指令确定基于套接字的流的超时值，单位为秒。


```
//以下是 pub.php 文件的内容 cli下运行
ini_set('default_socket_timeout', -1);
$redis->connect('127.0.0.1', 6379);
$strChannel = 'Test_bihu_channel';

//发布
$redis->publish($strChannel, "来自{$strChannel}频道的推送");
echo "---- {$strChannel} ---- 频道消息推送成功～ <br/>";
$redis->close();
```


```
//以下是 sub.php 文件内容 cli下运行
ini_set('default_socket_timeout', -1);
$redis->connect('127.0.0.1', 6379);
$strChannel = 'Test_bihu_channel';

//订阅
echo "---- 订阅{$strChannel}这个频道，等待消息推送...----  <br/><br/>";
$redis->subscribe([$strChannel], 'callBackFun');
function callBackFun($redis, $channel, $msg)
{
    print_r([
        'redis'   => $redis,
        'channel' => $channel,
        'msg'     => $msg
    ]);
}
```


### 计数器实战

**Redis String**

```
$redis = new Redis();

$redis->connect('127.0.0.1', 6379);
$strKey = 'Test_comments';

//设置初始值
$redis->set($strKey, 0);

$redis->INCR($strKey);  //+1
$redis->INCR($strKey);  //+1
$redis->INCR($strKey);  //+1

$strNowCount = $redis->get($strKey);

echo "---- 当前数量为{$strNowCount}。 ---- ";
```



### 排行榜实战

**Redis ZSET**


```
<?php

$redis = new Redis();

$redis->connect('127.0.0.1', 6379);
$strKey = 'Test_Rank_Score';

//存储数据
$redis->zadd($strKey, '50', json_encode(['name' => 'Tom']));
$redis->zadd($strKey, '70', json_encode(['name' => 'John']));
$redis->zadd($strKey, '90', json_encode(['name' => 'Jerry']));
$redis->zadd($strKey, '30', json_encode(['name' => 'Job']));
$redis->zadd($strKey, '100', json_encode(['name' => 'LiMing']));

$dataOne = $redis->ZREVRANGE($strKey, 0, -1, true);
echo "---- {$strKey}由大到小的排序 ---- <br /><br />";
print_r($dataOne);

$dataTwo = $redis->ZRANGE($strKey, 0, -1, true);
echo "<br /><br />---- {$strKey}由小到大的排序 ---- <br /><br />";
print_r($dataTwo);
```



### 字符串悲观锁实战

解释：悲观锁(Pessimistic Lock), 顾名思义，就是很悲观。

每次去拿数据的时候都认为别人会修改，所以每次在拿数据的时候都会上锁。

场景：如果项目中使用了缓存且对缓存设置了超时时间。

当并发量比较大的时候，如果没有锁机制，那么缓存过期的瞬间，

大量并发请求会穿透缓存直接查询数据库，造成雪崩效应。


```
<?php

/**
 * 获取锁
 * @param  String  $key    锁标识
 * @param  Int     $expire 锁过期时间
 * @return Boolean
 */
function lock($key = '', $expire = 5) {
    $is_lock = $this->_redis->setnx($key, time()+$expire);
    //不能获取锁
    if(!$is_lock){
        //判断锁是否过期
        $lock_time = $this->_redis->get($key);
        //锁已过期，删除锁，重新获取
        if (time() > $lock_time) {
            unlock($key);
            $is_lock = $this->_redis->setnx($key, time() + $expire);
        }
    }

    return $is_lock? true : false;
}

/**
 * 释放锁
 * @param  String  $key 锁标识
 * @return Boolean
 */
function unlock($key = ''){
    return $this->_redis->del($key);
}

// 定义锁标识
$key = 'Test_Pess_lock';

// 获取锁
$is_lock = lock($key, 10);

if ($is_lock) {
    echo 'get lock success<br>';
    echo 'do sth..<br>';
    sleep(5);
    echo 'success<br>';
    unlock($key);
} else { //获取锁失败
    echo 'request too frequently<br>';
}
```





### 事务的乐观锁实战

解释：乐观锁(Optimistic Lock), 顾名思义，就是很乐观。

每次去拿数据的时候都认为别人不会修改，所以不会上锁。

watch命令会监视给定的key，当exec时候如果监视的key从调用watch后发生过变化，则整个事务会失败。

也可以调用watch多次监视多个key。这样就可以对指定的key加乐观锁了。

注意watch的key是对整个连接有效的，事务也一样。

如果连接断开，监视和事务都会被自动清除。

当然了exec，discard，unwatch命令都会清除连接中的所有监视。

```
<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$strKey = 'Test_age';

$redis->set($strKey,10);

$age = $redis->get($strKey);
echo "---- Current Age:{$age} ---- <br/><br/>".PHP_EOL;

$redis->watch($strKey);

// 开启事务
$redis->multi();

//在这个时候新开了一个新会话执行
$redis->set($strKey,30);  //新会话

echo "---- Current Age:{$age} ---- <br/><br/>".PHP_EOL; //30

$redis->set($strKey,20);

$redis->exec();

$age = $redis->get($strKey);
echo "---- Current Age:{$age} ---- <br/><br/>".PHP_EOL; //30

//当exec时候如果监视的key从调用watch后发生过变化，则整个事务会失败
```
