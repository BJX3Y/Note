`负载均衡`：扩展了网络设备和服务器的带宽，增加吞吐量，加强网络数据处理能力，提供网络的灵活性和可用性

HAPROXY是基于Linux的负载均衡软件，

基于TCP和HTTP应用的代理，支持虚拟主机，其最高极限支持10G并发

对于大型的Web服务器可以使用HAProxy，因为这些站点需要会话保持或七层处理,HAPROXY完全可以支持数以万计的并发连接，整合项目简单安全，能够保护web服务器不被暴露到网络上.

HAPROXY能够补充Nginx的缺点，比如支持`Session保持` `Cookie引导`,支持通过`检测url获取后端服务状态`,nginx做反向代理负载均衡时候，对后端的健康检查功能较弱，而Haproxy配置简单，拥有强大的`健康检查功能`（健康检查相当于Nginx+keepalived）还有专门的系统监控页面

**HAPROXY负载均衡http 也可以负载均衡 MYSQL 而Nginx仅支持http https email协议,在HTTP代理性能上HAPROXY优于Nginx.**

Haproxy并不是HTTP服务器，nginx是HTTP服务器，需要自己提供静态或动态文件的传输以及处理，而Haproxy是一款`用于负载均衡的应用服务器，并不提供HTTP服务`.

HAproxy作负载均衡时，当其代理的后端服务器故障，它会自动将该服务器剔除，故障恢复后再自动将该服务添加进去.


HAProxy 是单线程，事件驱动架构。
haproxy是一款非常的专业的全7层的反向代理负载均衡器，采用的是`epoll机制`，**可以实现4层和7层的负载均衡，4层使用的是tcp模式可以模拟lvs，7层使用的是http模式可以模拟nginx，nginx和haproxy的处理速度都远不及lvs，因为他们是工作在用户空间的，而lvs是工作在内核空间的**.
