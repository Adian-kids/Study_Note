# 连接WiFi

使用以下命令查看网卡信息

```
ip link
```

此处我可以看到我的无线网卡名为wlan0，然后我们打开他

```
ip link set wlan0 up
```

 此

步骤可以省略，因为wlan0默认是打开的

下一步即是搜索wifi,此处`nmcli`不可用，所以使用`iwlist使用`

```
iwlist wlan0 scan
```

此时

会输出一段非常详细的信息，我们用管道将结果导入`grep `并搜索`ESSID`

```
iwlist wlan0 scan | grep ESSID
```

 然后我们使用以下命令连接到wifi

``` 
wpa_passphrase <ssid> <password> > wifi.conf // 生成配置文件
wps_supplicant -c wifi.conf -i wlan0 & //使用wlan0通过wifi.conf连接到wifi,并使用&指定后台运行
```

此时已经可以ping通baidu了，接下来同步时间服务器

```
timedatectl set-ntp true
```

# 分区

查看硬盘信息

```
fdisk -l
```

我这里的一块七彩虹120G硬盘被识别成了sda，进入相关的硬盘配置

```
fdisk /dev/sda
```

接下来格式化磁盘

```
g
```

单字母即可创建一个新的GPT分区表

然后分别创建`BOOT`,`/`,`SWAP`分区

```
n  // add a new partition
First sector //开始位置，第一次默认2048
Last sector  //结束位置，可以直接写+512M,表示增加512M后的位置
w //写入
```

这个位置有个坑，需要用

```
t
```

来分别设置efi  swap type等，不然会无法引导



然后启动分区需要是`FAT32`格式

```
mkfs.fat -F32 /dev/sda1(boot分区)
```

主分区需要`ext4`格式

```
mkfs.ext4 /dev/sda3（主分区）
```

`swap`分区也需要

```
mkswap /dev/sda2(swap)
```

然后开启这段swap分区

```
swapon /dev/sda2
```

# 修改pacman源

访问

```
/etc/pacman.d/mirrolist
```

删除国内源以外的其他源，然后更新

```
pacman -Syy
```

# 安装

## 挂载分区

将主分区挂载到/mnt上

```
mount /dev/sda3 /mnt
```

将boot分区挂载

```
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
```

## 安装

使用arch提供的`pacstrap`,安装内核等基础文件

```
pacstrap /mnt base linux linux-firmware
```

生成fstab文件，启动arch自动挂载分区

```
genfstab -U /mnt >> /mnt/etc/fstab
```

# 配置

进入新的arch linux中

````
arch-chroot /mnt
````

更改时区

```
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

同步系统时间

```
hwclock --systohc
```

退出chroot并编辑

```
vim /mnt/etc/locale.gen
```

将UTF8前面的注释删掉

```
en_US.UTF-8 UTF-8
```

在硬盘上的arch中装一个vim,之后就可以直接用vim了

```
pacstrap /mnt vim
```

然后再进入chroot环境

```
arch-chroot /mnt
```

生成本地化文件

```
locale-gen
```

话说这个时候pacman的源和一开始在u盘启动的arch里面的mirrolist是一样的

编辑一下hostname

```
vim /etc/hostname
vim /etc/hosts
```

在hosts中加入

```
127.0.0.1 localhost
::1       localhost
127.0.0.1 ThinkPad.localdomain ThinkPad
```

设定root密码

```
passwd
```

然后使用pacman安装以下软件

```
grub 引导管理
efibootmgr efi管理
intel-ucode 更新驱动用
os-prober  寻找电脑上的其他程序
```

生成grub配置文件

```
mkdir /boot/grub
grub-mkconfig > /boot/grub/grub.cfg
```

安装grub

```
grub-install --target=x86_64_efi --efi-directory=/boot
```

