### 压力测试工具 ab


##### 吞吐率（Requests per second）
概念：服务器并发处理能力的量化描述，单位是reqs/s，指的是某个并发用户数下单位时间内处理的请求数。某个并发用户数下单位时间内能处理的最大请求数，称之为最大吞吐率。
计算公式：总请求数 / 处理完成这些请求数所花费的时间，即
Request per second = Complete requests / Time taken for tests

##### 并发连接数（The number of concurrent connections）
概念：某个时刻服务器所接受的请求数目，简单的讲，就是一个会话。

##### 并发用户数（The number of concurrent users，Concurrency Level）
概念：要注意区分这个概念和并发连接数之间的区别，一个用户可能同时会产生多个会话，也即连接数。

##### 用户平均请求等待时间（Time per request）
计算公式：处理完成所有请求数所花费的时间/ （总请求数 / 并发用户数），即
Time per request = Time taken for tests /（ Complete requests / Concurrency Level）

##### 服务器平均请求等待时间（Time per request: across all concurrent requests）
计算公式：处理完成所有请求数所花费的时间 / 总请求数，即
Time taken for / testsComplete requests
可以看到，它是吞吐率的倒数。
同时，它也=用户平均请求等待时间/并发用户数，即
Time per request / Concurrency Level









>注意：如果不想安装apache但是又想使用ab命令的话，我们可以直接安装apache的工具包httpd-tools。


```
# ubuntu: apt-get install apache2-utils  
# centos: yum -y install httpd-tools


root@iZj6calh9xh0ham45c8ekqZ:/usr/local/nginx# ab -h
Usage: ab [options] [http[s]://]hostname[:port]/path
Options are:
    -n requests     Number of requests to perform
    -c concurrency  Number of multiple requests to make at a time
    -t timelimit    Seconds to max. to spend on benchmarking
                    This implies -n 50000
    -s timeout      Seconds to max. wait for each response
                    Default is 30 seconds
    -b windowsize   Size of TCP send/receive buffer, in bytes
    -B address      Address to bind to when making outgoing connections
    -p postfile     File containing data to POST. Remember also to set -T
    -u putfile      File containing data to PUT. Remember also to set -T
    -T content-type Content-type header to use for POST/PUT data, eg.
                    'application/x-www-form-urlencoded'
                    Default is 'text/plain'
    -v verbosity    How much troubleshooting info to print
    -w              Print out results in HTML tables
    -i              Use HEAD instead of GET
    -x attributes   String to insert as table attributes
    -y attributes   String to insert as tr attributes
    -z attributes   String to insert as td or th attributes
    -C attribute    Add cookie, eg. 'Apache=1234'. (repeatable)
    -H attribute    Add Arbitrary header line, eg. 'Accept-Encoding: gzip'
                    Inserted after all normal header lines. (repeatable)
    -A attribute    Add Basic WWW Authentication, the attributes
                    are a colon separated username and password.
    -P attribute    Add Basic Proxy Authentication, the attributes
                    are a colon separated username and password.
    -X proxy:port   Proxyserver and port number to use
    -V              Print version number and exit
    -k              Use HTTP KeepAlive feature
    -d              Do not show percentiles served table.
    -S              Do not show confidence estimators and warnings.
    -q              Do not show progress when doing more than 150 requests
    -l              Accept variable document length (use this for dynamic pages)
    -g filename     Output collected data to gnuplot format file.
    -e filename     Output CSV file with percentages served
    -r              Don't exit on socket receive errors.
    -m method       Method name
    -h              Display usage information (this message)
    -Z ciphersuite  Specify SSL/TLS cipher suite (See openssl ciphers)
    -f protocol     Specify SSL/TLS protocol
                    (TLS1, TLS1.1, TLS1.2 or ALL)
```


`ab -n 100 -c 10 http://test.com/`
其中`－n`表示请求数，`－c`表示并发数




##### 先用账户和密码登录后，用开发者工具找到标识这个会话的Cookie值（Session ID）记下来

复制Cookie信息

```
ab -n 100 -c 100 -H "Cookie: JSESSIONID=01BCDA8D30F3011A1C8136ED9B0A3ED6.server;USER.oooooooooooooooo=ab84b0125a24ecb263c6b677b989683ca26da6b4076ae09e1d5ccb8595a92a6d28233e61d860c9d0b745b0dfd8426494"  http://127.0.0.1:8007/shopCenter/zcyAccount/checkZcyAccount.do
```


##### 关于（GET带参数的请求），加引号" "

ab -n 2000 -c 150 "http://127.0.0.1:8007/app/appShopGoods/allow/getGoodsDetail.action?areaid=2013&detailid=50353974"  >>c:\wap_good.html
