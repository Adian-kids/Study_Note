# 主机探测常用模块

## 常用的内网主机探测模块

### scanner/discovery/arp_sweep

```
msf6 auxiliary(scanner/discovery/arp_sweep) > set RHOSTS 10.10.10.0/24
RHOSTS => 10.10.10.0/24
msf6 auxiliary(scanner/discovery/arp_sweep) > run

[+] 10.10.10.1 appears to be up (VMware, Inc.).
[+] 10.10.10.2 appears to be up (VMware, Inc.).
[+] 10.10.10.129 appears to be up (VMware, Inc.).
[+] 10.10.10.130 appears to be up (VMware, Inc.).
[+] 10.10.10.254 appears to be up (VMware, Inc.).
[+] 10.10.10.254 appears to be up (VMware, Inc.).
[*] Scanned 256 of 256 hosts (100% complete)
[*] Auxiliary module execution completed
```

### scanner/discovery/uwp_sweep

```
msf6 auxiliary(scanner/discovery/udp_sweep) > set RHOSTS 10.10.10.0/24
RHOSTS => 10.10.10.0/24
msf6 auxiliary(scanner/discovery/udp_sweep) > run

[*] Sending 13 probes to 10.10.10.0->10.10.10.255 (256 hosts)
[*] Discovered NetBIOS on 10.10.10.129:137 (OWASPBWA:<00>:U :OWASPBWA:<03>:U :OWASPBWA:<20>:U :WORKGROUP:<1e>:G :WORKGROUP:<00>:G :00:00:00:00:00:00)
[*] Discovered NetBIOS on 10.10.10.130:137 (ROOT-TVI862UBEH:<00>:U :WORKGROUP:<00>:G :ROOT-TVI862UBEH:<20>:U :SNTL_ROOT-TVI86:<32>:U :WORKGROUP:<1e>:G :00:0c:29:09:18:c6)
[*] Discovered NetBIOS on 10.10.10.254:137 (METASPLOITABLE:<00>:U :METASPLOITABLE:<03>:U :METASPLOITABLE:<20>:U :__MSBROWSE__:<01>:G :WORKGROUP:<00>:G :WORKGROUP:<1d>:U :WORKGROUP:<1e>:G :00:00:00:00:00:00)
[*] Discovered DNS on 10.10.10.254:53 (BIND 9.4.2)
[*] Scanned 256 of 256 hosts (100% complete)
[*] Auxiliary module execution completed
```



# 端口扫描探测

常用模块可以通过`search portscan`进行查找

```
   #  Name                                              Disclosure Date  Rank    Check  Description
   -  ----                                              ---------------  ----    -----  -----------
   0  auxiliary/scanner/portscan/ftpbounce                               normal  No     FTP Bounce Port Scanner
   1  auxiliary/scanner/natpmp/natpmp_portscan                           normal  No     NAT-PMP External Port Scanner
   2  auxiliary/scanner/sap/sap_router_portscanner                       normal  No     SAPRouter Port Scanner
   3  auxiliary/scanner/portscan/xmas                                    normal  No     TCP "XMas" Port Scanner
   4  auxiliary/scanner/portscan/ack                                     normal  No     TCP ACK Firewall Scanner
   5  auxiliary/scanner/portscan/tcp                                     normal  No     TCP Port Scanner
   6  auxiliary/scanner/portscan/syn                                     normal  No     TCP SYN Port Scanner
```

这里用`syn`方式扫描,因为`syn`扫描速度快，结果准确且不容易被发现

```
use auxiliary/scanner/portscan/syn 
```

扫描结果如下

```\
msf6 auxiliary(scanner/portscan/syn) > run

[+]  TCP OPEN 10.10.10.129:21
[+]  TCP OPEN 10.10.10.129:22
[+]  TCP OPEN 10.10.10.129:80
```

# 在msf中直接调用nmap

## 发现存活主机

```
nmap -sn 10.10.10.0/24
```

扫描结果

```
msf6 auxiliary(scanner/discovery/udp_sweep) > nmap -sn 10.10.10.0/24
[*] exec: nmap -sn 10.10.10.0/24

Starting Nmap 7.91 ( https://nmap.org ) at 2021-05-13 17:14 CST
Nmap scan report for 10.10.10.1
Host is up (0.00013s latency).
MAC Address: 00:50:56:C0:00:08 (VMware)
Nmap scan report for 10.10.10.2
Host is up (0.00021s latency).
MAC Address: 00:50:56:E0:A9:C5 (VMware)
Nmap scan report for www.dvssc.com (10.10.10.129)
Host is up (0.00034s latency).
MAC Address: 00:0C:29:C5:A6:2B (VMware)
Nmap scan report for service.dvssc.com (10.10.10.130)
Host is up (0.00042s latency).
MAC Address: 00:0C:29:09:18:C6 (VMware)
Nmap scan report for 10.10.10.254
Host is up (0.00012s latency).
MAC Address: 00:0C:29:79:92:14 (VMware)
Nmap scan report for 10.10.10.128
Host is up.
Nmap done: 256 IP addresses (6 hosts up) scanned in 2.11 seconds
```

## 端口扫描

nmap将扫描结果分成六类

| 类别            | 描述                         |
| --------------- | ---------------------------- |
| open            | 有应用在此端口监听           |
| close           | 主机相应，无应用监听，无价值 |
| filtered        | nmap无法确定，可能被过滤     |
| unfitered       | 仅使用ack扫描，nmap无法确定  |
| open\|filtered  | 开放或被过滤                 |
| close\|filtered | 关闭或被过滤                 |

常用参数

| 参数        | 说明                     |
| ----------- | ------------------------ |
| -sT         | TCP扫描                  |
| -sS         | SYN扫描                  |
| -sF/-sX/-sN | 发送特殊标志位避开检测   |
| -sP         | 发送icmp包               |
| -sU         | 探测开放哪些UDP端口      |
| -sA         | ACK扫描                  |
| -O          | 操作系统指纹识别         |
| -Pn         | 不发送icmp包探测是否存活 |
| -V          | 输出详细信息             |



## 识别操作系统

```
nmap -O 10.10.10.129
```