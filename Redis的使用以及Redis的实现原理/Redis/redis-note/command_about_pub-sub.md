Redis 发布订阅`(pub/sub)`是一种`消息通信`模式：
+ 发送者(pub)发送消息，
+ 订阅者(sub)接收消息。

Redis 客户端可以订阅`任意数量的频道`。


```
PSUBSCRIBE pattern [pattern ...]
订阅一个或多个符合给定模式的频道。

PUBSUB subcommand [argument [argument ...]]
查看订阅与发布系统状态。

PUBLISH channel message
将信息发送到指定的频道。

PUNSUBSCRIBE [pattern [pattern ...]]
退订所有给定模式的频道。

SUBSCRIBE channel [channel ...]
订阅给定的一个或多个频道的信息。

UNSUBSCRIBE [channel [channel ...]]
指退订给定的频道。
```

{
  audio_source: xxx,          // audio来源，现在有youtube和pandarow
  audio_url: xxx,             // 视频文件的地址(主要针对自己服务器的视频)
  audio_site: xxx,            // 第三方视频 的访问地址
  audio_code:xxx,             // 第三方网站的视频都应该有一个唯一性标识码
  audio_image: xxx,           // 封面图片地址
  audio_update_image:xxx      // 合成更新图片的url   (不建议加)
  audio_len:xxx               // 时长 默认值0
 }


以后自己服务器视频文件大小
以后服务器需不需要有不同 清晰度 的视频

audio_size:xxx              // 视频文件大小(自己服务器视频使用) 默认值0
audio_height:xxx            // 默认值0
audio_width:xxx             // 默认值0
