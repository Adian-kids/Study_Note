# 服务扫描打点

## Telnet

```
scanner/telnet/telnet_version
```

## SSH

```
scanner/ssh/ssh_version
```

## Oracle

```
auxiliary/scanner/oracle/tnslsnr_version
```

## 开放代理

```
auxiliary/scanner/http/open_proxy 
```

# 口令

## SSH 服务口令猜测

```
auxiliary/scanner/ssh/ssh_login
```

这个地方用Hydra替代是个不错的选择

## psnuffle口令嗅探

```
auxiliary/sniffer/psnuffle
```

## 使用nmap探测特定漏洞

```
nmap --script=smb-check-vulns ip
```

