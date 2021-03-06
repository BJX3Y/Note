[TOC]

## 消息通知(队列 、PUB/SUB)


### 队列特点

>**任务队列** ：顾名思义，就是“传递消息的队列”。
与任务队列进行交互的实体有两类，一类是 `生产者（producer）` ，另一类则是 `消费者（consumer）`。生产者将需要处理的任务放入任务队列中，而消费者则不断地从任务独立中读入任务信息并执行。

任务队列的好处：

+ 松耦合。生产者和消费者只需按照约定的任务描述格式，进行编写代码。
+ 易于扩展。多消费者模式下，消费者可以分布在多个不同的服务器中，由此降低单台服务器的负载。

### Redis实现任务队列

使用Redis实现任务队列首先想到的就是`Redis的列表类型`，因为在Redis内部，**列表类型是由双向链表实现** 的。

实现任务队列，只需让生产者将任务使用`LPUSH`加入到某个键中，然后另一个消费者不断地使用`RPOP`命令从该键中取出任务即可。

```
//生产者只需将task LPUSH到队列中
127.0.0.1:6379> LPUSH queue task
(integer) 1
127.0.0.1:6379> LRANGE queue 0 -1
1) "task"
//消费者只需从队列中LPOP任务，如果为空则轮询。
127.0.0.1:6379> LPOP queue
"task"
```

BLPOP指令可以在队列为空时处于阻塞状态。就不用处于轮询的状态。

```
127.0.0.1:6379> BLPOP queue 0   //0表示无限制等待
//消费者当队列为空则处于阻塞状态。
//生产者将task LPUSH到队列中，处于阻塞状态的消费者离开返回
127.0.0.1:6379> LPUSH queue task
(integer) 1

//消费者立刻“消费”，取出task。
127.0.0.1:6379> BLPOP queue 0
1) "queue"
2) "task"
(13.38s)
```

#### 优先级队列

BLPOP命令可以同时接收多个键BLPOP key [key ...] timeout，当所有键（列表类型）都为空时，则阻塞，当其中一个有元素则会从该键返回。 **如果多个键都有元素则按照从左到右的顺序取第一个键中的一个元素，因此可以借此特性实现优先级队列** 。

```
127.0.0.1:6379> LPUSH queue1 first
(integer) 1
127.0.0.1:6379> LPUSH queue2 second
(integer) 1

//当两个键都有元素时，按照从左到右的顺序取第一个键中的一个元素
127.0.0.1:6379> BRPOP queue1 queue2 0
1) "queue1"
2) "first"
127.0.0.1:6379> BRPOP queue1 queue2 0
1) "queue2"
2) "second"
```


### 发布订阅pub/sub

“发布/订阅”（publish/subscribe）模式也可以实现 **进程间通信** ，
>订阅者可以订阅一个或多个频道（channel），
而发布者可以向指定的频道发送消息，
所有订阅次频道的订阅者都会收到次消息。


+ PUBLISH
  >将信息 message 发送到指定的频道 channel。返回收到消息的客户端数量。

+ SUBSCRIBE
  >订阅给指定频道的信息。
  一旦客户端进入订阅状态，客户端就只可接受订阅相关的命令SUBSCRIBE、PSUBSCRIBE、UNSUBSCRIBE和PUNSUBSCRIBE除了这些命令，其他命令一律失效。

+ UNSUBSCRIBE
  >取消订阅指定的频道，如果不指定，则取消订阅所有的频道。

```
127.0.0.1:6379> PUBLISH channel1.1 test
(integer) 0 //有0个客户端收到消息

127.0.0.1:6379> SUBSCRIBE channel1.1
Reading messages... (press Ctrl-C to quit)
1) "subscribe"  //"subscribe"表示订阅成功的信息
2) "channel1.1" //表示订阅成功的频道
3) (integer) 1  //表示当前订阅客户端的数量
//当发布者发布消息时，订阅者会收到如下消息
1) "message"    //表示接收到消息
2) "channel1.1" //表示产生消息的频道
3) "test"       //表示消息的内容
//当订阅者取消订阅时会显示如下：
127.0.0.1:6379> UNSUBSCRIBE channel1.1
1) "unsubscribe"    //表示成功取消订阅
2) "channel1.1" //表示取消订阅的频道
3) (integer) 0  //表示当前订阅客户端的数量

//注：在redis-cli中无法测试UNSUBSCRIBE命令
```


+ PSUBSCRIBE
  >订阅给定的模式(patterns)。

+ PUNSUBSCRIBE
  >可以退订指定的规则，如果没有参数会退订所有的规则。


```
127.0.0.1:6379> PSUBSCRIBE channel1.*
Reading messages... (press Ctrl-C to quit)
1) "psubscribe"
2) "channel1.*"
3) (integer) 1
//等待发布者发布消息
127.0.0.1:6379> PUBLISH channel1.1 test1.1
(integer) 1 //发布者在channel1.1发布消息

1) "pmessage"   //表示通过PSUBSCRIBE命令订阅而收到的
2) "channel1.*" //表示订阅时使用的通配符
3) "channel1.1" //表示收到消息的频道
4) "test1.1"        //表示消息内容

127.0.0.1:6379> PUBLISH channel1.2 test1.2
(integer) 1 //发布者在channel1.2发布消息

1) "pmessage"
2) "channel1.*"
3) "channel1.2"
4) "test1.2"

127.0.0.1:6379> PUBLISH channel1.3 test1.3
(integer) 1 //发布者在channel1.3发布消息

1) "pmessage"
2) "channel1.*"
3) "channel1.3"
4) "test1.3"

127.0.0.1:6379> PUNSUBSCRIBE channal1.*
1) "punsubscribe"   //退订成功
2) "channal1.*" //退订规则的通配符
3) (integer) 0  //表示当前订阅客户端的数量
```

>**PUNSUBSCRIBE 注意**：
>+ 使用PUNSUBSCRIBE命令只能退订通过PSUBSCRIBE命令订阅的规则，不会影响SUBSCRIBE订阅的频道。
>+ 使用PUNSUBSCRIBE命令退订某个规则时不会将其中通配符展开，而是严格的进行==字符串匹配==，所以 `PUNSUBSCRIBE *` 无法退订 `PUNSUBSCRIBE channal1.*` 规则，而必须使用 `PUNSUBSCRIBE channal1.*` 才能退订
