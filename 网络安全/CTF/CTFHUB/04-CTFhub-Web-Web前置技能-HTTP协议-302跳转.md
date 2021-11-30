# CTFHUB_302跳转

## 题目内容

```html
html>
	<head>
		<title>No Flag here!</title>
	</head>
	<body>
		<center>
			<h1>No Flag here!</h1>
            <a href="index.php">Give me Flag</a>
		</center>
	</body>
</html>
```
## WriteUp
有一个指向index.php的跳转连接，但是点击之后无法跳转，根据题目可以判断出index.php 302跳转到了index.html

**什么是HTTP 302 跳转？**

首先我们要知道**状态码**，状态码是HTTP请求过程**结果的描述**，由三位数字组成。这三位数字描述了请求过程中所发生的情况。状态码位于**响应的起始行**中，如在 HTTP/1.0 200 OK 中，状态码就是 200。

每个状态码的**第一位数字**都用于描述状态（“成功”、“出错”等）。如200 到 299 之间的状态码表示成功；300 到 399 之间的代码表示资源已经转移。400 到 499 之间的代码表示客户端的**请求出错**了。500 到 599 之间的代码表示**服务器出错**了。

| 整体范围 | 已定义范围 | 分　　类   |
| -------- | ---------- | ---------- |
| 100～199 | 100～101   | 信息提示   |
| 200～299 | 200～206   | 成功       |
| 300～399 | 300～305   | 重定向     |
| 400～499 | 400～415   | 客户端错误 |
| 500～599 | 500～505   | 服务器错误 |

那么302就属于重定向的状态码，它表示你要访问的资源在别的地方。

|      |                   |                                                              |
| ---- | ----------------- | ------------------------------------------------------------ |
| 301  | Moved Permanently | 在请求的URL已被移除时使用。响应的Location首部中应该包含资源现在所处的URL |
| 302  | Found             | 与301状态码类似；但是，客户端应该使用Location首部给出的URL来临时定位资源。将来的请求仍应使用老的URL |

302表示临时重定向，而301表示永久重定向



在此情况下，我们可以使用curl来请求index.php,因为curl不会跟随跳转

```
adian@pentest:curl http://challenge-556e33b3a27e7c31.sandbox.ctfhub.com:10800/index.php                         
ctfhub{442970c988dd88b4984900f5}
```

拿到对应的flag



以下为curl部分文档

|                            参数组                            | 参数                                                         | 描述                                                         |
| :----------------------------------------------------------: | :----------------------------------------------------------- | :----------------------------------------------------------- |
|                             url                              | url                                                          | 需要抓取的一到多个URLs； 多个下面通配符的方式： 　　1、http://{www,ftp,mail}.aiezu.com； 　　2、http://aiezu.com/images/[001-999].jpg； 　　3、http://aiezu.com/images/[1-999].html； 　　4、ftp://aiezu.com/file[a-z].txt |
|                           请 求 头                           | -H "name: value" --header "name: value"                      | (HTTP)添加一个http header(http请求头)；                      |
|                 -H "name:" --header "name:"                  | (HTTP)移除一个http header(http请求头)；                      |                                                              |
| -A "string" --user-agent "string" [【参考】](http://aiezu.com/article/linux_curl_referer_useragent.html) | (HTTP)设置Http请求头“User-Agent”，服务器通过“User-Agent”可以判断客户端使用的浏览器名称和操作系统类型，伪造此参数能导致服务器做出错误判断。 也可以使用“-H”, “--header option”设置此选项； |                                                              |
| -e <URL> --referer <URL> [【参考】](http://aiezu.com/article/linux_curl_referer_useragent.html) | (HTTP)设置访问时的来源页面，告诉http服务从哪个页面进入到此页面； -e "aiezu.com"相当于“-H "Referer: www.qq.com"”； |                                                              |
|                           响 应 头                           | -I --head                                                    | (HTTP)只输出HTTP-header，不获取内容(HTTP/FTP/FILE)。 用于HTTP服务时，获取页面的http头；  （如：curl -I http://aiezu.com） 用于FTP/FILE时，将会获取文件大小、最后修改时间；  （如：curl -I file://test.txt） |
|                         -i --include                         | (HTTP)输出HTTP头和返回内容；                                 |                                                              |
|                -D <file> --dump-header <file>                | (HTTP)转储http响应头到指定文件；                             |                                                              |
|                            cookie                            | -b name=data --cookie name=data [【参考】](http://aiezu.com/article/linux_curl_http_cookie.html) | (HTTP)发送cookie数据到HTTP服务器，数据格式为："NAME1=VALUE1; NAME2=VALUE2"；  如果行中没有“=”，将把参数值当作cookie文件名；  这个cookie数据可以是由服务器的http响应头“Set-Cookie:”行发送过来的； |
| -c filename --cookie-jar file name [【参考】](http://aiezu.com/article/linux_curl_http_cookie.html) | (HTTP)完成操作后将服务器返回的cookies保存到指定的文件； 指定参数值为“-”将定向到标准输出“如控制台”； |                                                              |
|                  -j --junk-session-cookies                   | (HTTP)告诉curl放弃所有的"session cookies"； 相当于重启浏览器； |                                                              |
|                             代理                             | -x host:port -x [protocol://[user:pwd@]host[:port] --proxy [protocol://[user:pwd@]host[:port] [【参考】](http://aiezu.com/article/linux_curl_proxy_http_socks.html) | 使用HTTP代理访问；如果未指定端口，默认使用8080端口; protocol默认为http_proxy，其他可能的值包括： http_proxy、HTTPS_PROXY、socks4、socks4a、socks5； 如： --proxy 8.8.8.8:8080； -x "http_proxy://aiezu:123@aiezu.com:80" |
|                       -p --proxytunnel                       | 将“-x”参数的代理，作为通道的方式去代理非HTTP协议，如ftp；    |                                                              |
| --socks4 <host[:port]> --socks4a <host[:port]> --socks5 <host[:port]> [【参考】](http://aiezu.com/article/linux_curl_proxy_http_socks.html) | 使用SOCKS4代理； 使用SOCKS4A代理； 使用SOCKS5代理； 此参数会覆盖“-x”参数； |                                                              |
| --proxy-anyauth --proxy-basic --proxy-diges --proxy-negotiate --proxy-ntlm | http代理认证方式，参考： --anyauth --basic --diges --negotiate --ntlm |                                                              |
|       -U <user:password> --proxy-user <user:password>        | 设置代理的用户名和密码；                                     |                                                              |
|                          数据 传输                           | -G --get [【参考】](http://aiezu.com/article/linux_curl_getpost_datafile_json.html) | 如果使用了此参数，“-d/”、“--data”、“--data-binary”参数设置的数据，讲附加在url上，以GET的方式请求； |
| -d @file -d "string" --data "string" --data-ascii "string" --data-binary "string" --data-urlencode "string" [【参考】](http://aiezu.com/article/linux_curl_getpost_datafile_json.html) | (HTTP)使用HTTP POST方式发送“key/value对”数据，相当于浏览器表单属性（method="POST"，enctype="application/x-www-form-urlencoded"） 　　-d，--data：HTTP方式POST数据； 　　--data-ascii：HTTP方式POST ascii数据； 　　--data-binary：HTTP方式POST二进制数据； 　　--data-urlencode：HTTP方式POST数据（进行urlencode）； 如果数据以“@”开头，后紧跟一个文件，将post文件内的内容； |                                                              |
| -F name=@file -F name=<file -F name=content --form name=content [【参考】](http://aiezu.com/article/linux_curl_getpost_datafile_json.html) | (HTTP)使用HTTP POST方式发送类似“表单字段”的多类型数据，相当于同时设置浏览器表单属性（method="POST"，enctype="multipart/form-data"），可以使用此参数上传二进制文件。  如果字段内容以“@”开头，剩下的部分应该是文件名，curl将会上传此文件，如： curl -F "pic=@pic.jpg" http://aiezu.com； curl -F "page=@a.html;type=text/html" http://aiezu.com curl -F "page=@/tmp/a;filename=a.txt" http://aiezu.com  如果字段内容以“<”开头，剩下的部分应该是文件名，curl将从文件中获取作为此字段的值，如：curl -F "text=<text.txt" http://aiezu.com； |                                                              |
|                  --form-string <key=value>                   | (HTTP)类似于“--form”，但是“@”、“<”无特殊含义；               |                                                              |
|                  -T file --upload-file file                  | 通过“put”的方式将文件传输到远程网址；  选项参数只使用字符"-"，将通过stdin读入文件内容； 如： cat test.txt\|curl "http://aiezu.com/a.php" -T -  curl "http://aiezu.com/a.php" -T - <test.txt  此参数也可以使用通配符： curl -T "{file1,file2}" http://aiezu.com curl -T "img[1-1000].png" http://aiezu.com |                                                              |
|                          断点 续传                           | -C <offset> --continue-at <offset>                           | 断点续转，从文件头的指定位置开始继续下载/上传； offset续传开始的位置，如果offset值为“-”，curl会自动从文件中识别起始位置开始传输； |
|                  -r <range> --range <range>                  | (HTTP/FTP/SFTP/FILE) 只传输内容的指定部分： 0-499：最前面500字节； -500：最后面500字节； 9500-：最前面9500字节； 0-0,-1：最前面和最后面的1字节； 100-199,500-599：两个100字节； |                                                              |
|                             认证                             | --basic                                                      | (HTTP)告诉curl使用HTTP Basic authentication（HTTP协议时），这是默认认证方式； |
|                            --ntlm                            | (HTTP)使用NTLM身份验证方式，用于HTTP协议； 一般用于IIS使用NTLM的网站； |                                                              |
|                           --digest                           | (HTTP)使用HTTP Digest authentication加密，用于HTTP协议； 配合“-u/--user”选项，防止密码使用明文方式发送； |                                                              |
|                         --negotiate                          | (HTTP)使用GSS-Negotiate authentication方式，用于HTTP协议； 它主要目的是为它的主要目的是为kerberos5认证提供支持支持； |                                                              |
|                          --anyauth                           | (HTTP)告诉curl自动选择合适的身份认证方法，并选用最安全的方式； |                                                              |
|            -u user:password --user user:password             | 使用用户名、密码认证，此参数会覆盖“-n”、“--netrc”和“--netrc-optional”选项；  如果你只提供用户名，curl将要求你输入密码；  如果你使用“SSPI”开启的curl库做“NTLM”认证，可以使用不含用户名密码的“-u:”选项，强制curl使用当前登录的用户名密码进行认证；  此参数相当于设置http头“Authorization：”； |                                                              |
|                             证书                             | -E <证书[:密码]> --cert <证书[:密码]>                        | (SSL)指定“PEM”格式的证书文件和证书密码；                     |
|                      --cert-type <type>                      | (SSL)告诉curl所提供证书的类型：PEM、DER、ENG等； 默认为“PEM”； |                                                              |
|                      --cacert <CA证书>                       | (SSL)告诉curl所以指定的CA证书文件，必须是“PEM”格式；         |                                                              |
|                    --capath <CA证书路径>                     | (SSL)告诉curl所以指定目录下的CA证书用来验证； 这些证书必须是“PEM”格式； |                                                              |
|                       --crlfile <file>                       | (HTTPS/FTPS)提供一个PEM格式的文件，用于指定被吊销的证书列表； |                                                              |
|                        -k --insecure                         | (SSL)设置此选项将允许使用无证书的不安全SSL进行连接和传输。   |                                                              |
|                           SSL 其他                           | --ciphers <list of ciphers>                                  | (SSL)指定SSL要使用的加密方式；如：“aes_256_sha_256”；        |
|                       --engine <name>                        | 设置一个OpenSSL加密引擎用于加密操作； 使用“curl --engine list”查看支持的加密引擎列表； |                                                              |
|                        --random-file                         | (SSL)指定包含随机数据的文件路径名；数据是用来为SSL连接产生随机种子为； |                                                              |
|                      --egd-file <file>                       | (SSL)为随机种子生成器EGD(Entropy Gathering Daemon socket)指定的路径名； |                                                              |
| -1/--tlsv1 --tlsv1.0 --tlsv1.1 --tlsv1.2 -2/--sslv2 -3/--sslv3 | (SSL)使用TLS版本2与远程服务器通讯； (SSL)使用TLS 1.0版本与远程服务器通讯； (SSL)使用TLS 1.1版本与远程服务器通讯； (SSL)使用TLS 1.2版本与远程服务器通讯； (SSL)使用SSL版本2与远程服务器通讯； (SSL)使用SSL版本3与远程服务器通讯； |                                                              |
|                          私钥 公钥                           | --key <key>                                                  | (SSL/SSH)指定一个私钥文件名；为指定时自动尝试使用下面文件：“~/.ssh/id_rsa”、“~/.ssh/id_dsa”、“./id_rsa'”、 “./id_dsa”； |
|                      --key-type <type>                       | (SSL)指定私钥文件类型，支持：DER、PEM、ENG，默认是PEM；      |                                                              |
|                       --pass <phrase>                        | (SSL/SSH)指定私钥文件的密码；                                |                                                              |
|                        --pubkey <key>                        | (SSH)使用指定文件提供的您公钥；                              |                                                              |
|                             FTP                              | -P --ftp-port <接口>                                         | (FTP)FTP主动模式时，设置一个地址等待服务器的连接，如： 网卡：eth1 IP：8.8.8.8 主机名：aiezu.com 可以加端口号：eth1:20000-21000; |
|                            --crlf                            | (FTP)上传时将换行符(LF)转换为回车换行(CRLF)；                |                                                              |
|                     --ftp-account [data]                     | (FTP)ftp帐号信息；                                           |                                                              |
|                    --ftp-method [method]                     | (FTP)可选值：multicwd/nocwd/singlecwd；                      |                                                              |
|                          --ftp-pasv                          | (FTP)使用使用PASV(被动)/EPSV模式；                           |                                                              |
|                      --ftp-skip-pasv-ip                      | (FTP)使用PASV的时,跳过指定IP；                               |                                                              |
|                      --ftp-create-dirs                       | (FTP)上传时自动创建远程目录；                                |                                                              |
|                        -l --list-only                        | (FTP)列出ftp文件列表；                                       |                                                              |
|                        -B --use-ascii                        | (FTP/LDAP)使用Ascii传输模式，用于FTP、LDAP；在ftp中相当与使用了“type=A;”模式。 |                                                              |
|                        --disable-epsv                        | (FTP)告诉curl在PASV(被动模式)时不要使用EPSV；                |                                                              |
|                        --disable-eprt                        | (FTP)告诉curl在主动模式时禁用EPRT和LPRT；                    |                                                              |
|                             限速                             | --limit-rate <speed>                                         | 限制curl使用的最大带宽；如果未指定单位，默认单位为“bytes/秒”，你也可以指定单位为“K”、“M”、“G”等单位，如：“--limit-rate 1m”为限制最大使用带宽为“1m字节/秒”； |
|                    -y --speed-time <time>                    | If a download is slower than speed-limit bytes per second during a speed-time period, the download gets aborted. If speed-time is used, the default speed-limit will be 1 unless set with -Y. This option controls transfers and thus will not affect slow connects etc. If this is a concern for you, try the --connect-timeout option. |                                                              |
|                   -Y --speed-limit <speed>                   | If a download is slower than this given speed (in bytes per second) for speed-time seconds it gets aborted. speed-time is set with -y and is 30 if not set. |                                                              |
|                          其他 选项                           | -0/--http1.0                                                 | (HTTP) 强制curl使用HTTP 1.0而不是使用默认的HTTP 1.1；        |
|                      --interface <name>                      | 使用指定的网卡接口访问； curl --interface eth0 http://aiezu.com curl --interface 10.0.0.101 http://aiezu.com |                                                              |
|               -X <command> --request <command>               | （HTTP）指定与服务器通信使用的请求方法，如：GET、PUT、POST、DELETE等，默认GET； |                                                              |
|                  --keepalive-time <seconds>                  | 设置keepalive时间                                            |                                                              |
|                        --no-keepalive                        | 关闭keepalive功能；                                          |                                                              |
|                         --no-buffer                          | 禁用对输出流缓冲；                                           |                                                              |
|                           --buffer                           | 启用输出流缓冲；                                             |                                                              |
|                        -L --location                         | (HTTP/HTTPS)追随http响应头“Location：”定向到跳转后的页面； (在http响应码为3XX时使用，如301跳转、302跳转) |                                                              |
|                      --location-trusted                      | (HTTP/HTTPS)同“--location”，但跳转后会发送跳转前的用户名和密码； |                                                              |
|                         --compressed                         | (HTTP)请求对返回内容使用压缩算法进行压缩；curl支持对gzip压缩进行解压； |                                                              |
|                 --connect-timeout <seconds>                  | 指定最大连接超时，单位“秒”；                                 |                                                              |
|                -m seconds --max-time seconds                 | 限制整个curl操作的最长时间，单位为秒；                       |                                                              |
|                         -s --silent                          | 安静模式。不要显示进度表或错误消息；                         |                                                              |
|                      -# --progress-bar                       | 显示进度条；                                                 |                                                              |
|                          错误 选项                           | -f --fail                                                    | (HTTP)连接失败时（400以上错误）不返回默认错误页面，而是返回一个curl错误码“22”； |
| --retry <num> --retry-delay <seconds> --retry-max-time <seconds> | 失败重试次数； 重试间隔时间； 最大重试时间；                 |                                                              |
|                       -S --show-error                        | 安静模式下显示错误信息；                                     |                                                              |
|                       --stderr <file>                        | 错误信息保存文件；                                           |                                                              |
|                             输出                             | -o file --output file                                        | 将返回内容输出到文件。 如果是用过通配符获取多个url，可以使用“#”后跟“数字序号”，curl会自动将它替换对应的关键词，如： 　　curl "http://aiezu.com/{a,b}.txt" -o "#1.txt"; 　　将保存为：“a.txt”,“b.txt”;  　　curl "http://aiezu.com/{a,b}_[1-3].txt" -o "#1#2.txt"; 　　将保存为：a1.txt、a2.txt、a3.txt、b1.txt、b2.txt、b3.txt  　　如果要根据规则创建保存目录，参考：“--create-dirs”  指定“-”将定向到标准输出“如控制台”； |
|                       -O --remote-name                       | 将返回内容输出到当前目录下，和url中文件名相同的文件中（不含目录）； |                                                              |
|                        --create-dirs                         | 与“-o”参数配合使用，创建必要的本地目录层次结构               |                                                              |
|                    -w --write-out format                     | 操作完成后在返回信息尾部追加指定的内容；要追加的内容可以是一个字符串“string”、从文件中获取“@filename”、从标准输入中获取“@-”  格式参数中可以用%{variable_name} 方式使用响应信息的相关变量，如：%{content_type}、%{http_code}、%{local_ip}...，更多变量参考“man curl”获取；  格式参数可以使用“\n”、“\r”、“\t”等转义字符； |                                                              |
|                             调试                             | --trace <file>                                               | 转储所有传入和传出的数据到文件，包括描述信息； 使用“-”作为文件名将输出发送到标准输出。 |
|                      --trace-ascii file                      | 转储所有传入和传出的数据到文件，包括描述信息，只转储ASCII部分，更容易阅读； 使用“-”作为文件名将输出发送到标准输出。 这个选项会覆盖之前使用的-v、 --verbose、 --trace-ascii选项； |                                                              |
|                         --trace-time                         | 转储文件中添加时间信息；                                     |                                                              |
|                  -K --config <config file>                   | 从配置文件中读取参数，参考：http://curl.haxx.se/docs/        |                                                              |
|                         -v --verbose                         | 显示更详细的信息，调试时使用；                               |                                                              |
|                             帮助                             | -M --manual                                                  | 显示完整的帮助手册；                                         |
|                          -h --help                           | linux curl用法帮助；                                         |                                                              |

## Reference

https://www.ruanyifeng.com/blog/2019/09/curl-reference.html
