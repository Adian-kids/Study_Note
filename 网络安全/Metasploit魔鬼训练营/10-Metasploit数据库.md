# 渗透测试信息库

## 优势

使用方便，通过db_nmap,db_import等指令可以直接将扫描器结果导入msf中，并且可与其他人共享

## 数据库支持

Metasploit支持PostgreSQL数据库，使用端口号为7175

在msf shell中检测数据库连接状态

```
db_status
```

如果数据库未连接，可以在终端下执行

```
sudo msfdb init
```

其他msfdb指令以及msf中db_xxx可自行help

## nmap与数据库

可以直接使用db_nmap来在msf内部直接使用nmap，和exec nmap的区别在于db_nmap可以直接将扫描结果存入数据库

```
db_nmap  -A ip 
```

或者使用nmap的oX参数导出扫描结果再导入msf中

```
root@kali$ nmap -A ip -oX name

msf> db_import /root/name
```



