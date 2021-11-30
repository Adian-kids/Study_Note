# 网络管理

查看网络设备

```
sudo nmcli dev
```

 开启wifi

```
sudo nmcli r wifi on
```

扫描wifi

```
sudo nmcli dev wifi
```

连接wifi

```
sudo nmcli dev wifi conncet "ssid" password "passwd"
```

在这一步可能出现`错误：无法激活连接（7）需要密钥但未提供`

方法是加上`--ask`参数了来替代password

```
sudo nmcli dev wifi connect "ssid" --ask
```



