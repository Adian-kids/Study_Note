# 零散知识点

## 文件上传绕过

- PHP函数`getinmagesize()`可以获取到图片的长宽高，如果不是图片文件，则无法读取到长宽高，自然不会判断为图片，如果后端采用此函数，需要用图片马和修改`Content-Type`来进行绕过
- 00截断要求PHP版本小于5.3.4且`magic_quotes_gpc`为OFF，通常在`$_REQUESTS`等处被截断
- 可以用Hashdump,smart_hashdump,Quarks PwDump,WindowsCredentials(wcr.exe)，Minikatz来抓密码
- 后门可以采用Cymothoa,Persistence建立，或者直接用web后门（Meterpreter后门）