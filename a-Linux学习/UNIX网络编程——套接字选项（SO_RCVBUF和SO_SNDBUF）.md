### 套接字选项（SO_RCVBUF和SO_SNDBUF）


有时候我们需要控制套接字的行为(如修改缓冲区的大小),这个时候我们就要学习套接字选项。

```

int getsockopt(int sockfd,int level,int optname,void *optval,socklen_t *optlen)
int setsockopt(int sockfd,int level,int optname,const void *optval,socklen_t *optlen)
```

+ level指定控制套接字的层次.可以取三种值：

  + SOL_SOCKET：通用套接字选项.
  + IPPROTO_IP：IP选项.
  + IPPROTO_TCP：TCP选项.

+ optname指定控制的方式(选项的名称)

+ optval获得或者是设置套接字选项.根据选项名称的数据类型进行转换  

+ 返回值说明：
    成功执行时，返回0。失败返回-1，errno被设为以下的某个值  
    + EBADF：sock不是有效的文件描述词
    + EFAULT：optval指向的内存并非有效的进程空间
    + EINVAL：在调用setsockopt()时，optlen无效
    + ENOPROTOOPT：指定的协议层不能识别选项
    + ENOTSOCK：sock描述的不是套接字


SO_RCVBUF和SO_SNDBUF每个套接口都有一个发送缓冲区和一个接收缓冲区，使用这两个套接口选项可以改变缺省缓冲区大小。

```
// 接收缓冲区
int nRecvBuf=32*1024;         //设置为32K
setsockopt(s,SOL_SOCKET,SO_RCVBUF,(const char*)&nRecvBuf,sizeof(int));
//发送缓冲区
int nSendBuf=32*1024;//设置为32K
setsockopt(s,SOL_SOCKET,SO_SNDBUF,(const char*)&nSendBuf,sizeof(int));
```

>注意：
 当设置TCP套接口接收缓冲区的大小时，函数调用顺序是很重要的，因为TCP的窗口规模选项是在建立连接时用SYN与对方互换得到的。对于客户，SO_RCVBUF选项必须在connect之前设置；对于服务器，SO_RCVBUF选项必须在listen前设置。

 每个套接口都有一个发送缓冲区和一个接收缓冲区，使用SO_SNDBUF & SO_RCVBUF可以改变缺省缓冲区大小。

 对于客户端，SO_RCVBUF选项须在connect之前设置.
 对于服务器，SO_RCVBUF选项须在listen前设置.
