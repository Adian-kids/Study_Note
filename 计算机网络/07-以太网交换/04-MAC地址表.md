# 交换机基础知识

既然您已经了解了所有关于以太网MAC地址的知识，现在就该讨论交换机如何使用这些地址将帧转发(或丢弃)到网络上的其他设备。如果交换机只是转发出它接收到的每一帧到所有端口，您的网络将会非常拥挤，以至于它可能会完全停止工作。

第 2 层以太网交换机使用 MAC 地址做出转发决策。它完全忽视帧的数据部分的协议，例如 IPv4 数据包，一个ARP消息或一个IPv6 ND数据包。交换机仅根据第 2 层以太网 MAC 地址做出转发决策。

一个以太网交换机检查它的MAC地址表，为每个帧做出一个转发决策，不像传统的以太网集线器，向除了传入端口以外的所有端口重复发出比特位。如图所示，四端口交换机已启动。如表所示，MAC地址表还未获知四台连接的 PC 的 MAC 地址。

**注意**: 缩短 MAC 地址是为了便于演示。

![](pic/8.png)

# 交换机学习和转发

交换机通过检查端口传入帧的源 MAC 地址来动态构建 MAC 地址表。交换机通过匹配帧中的目的 MAC 地址与 MAC 地址表中的条目来转发帧。

## 学习

**检查源MAC地址**

进入交换机的每个帧被检查，以确定其中是否有可被学习的新信息。它是通过检查帧的源 MAC 地址和帧进入交换机的端口号来完成这一步的。如果源 MAC 地址不存在，会将其和传入端口号一并添加到表中。如果源 MAC 地址已存在于表中，则交换机会更新该条目的刷新计时器。默认情况下，大多数以太网交换机将条目在表中保留 5 分钟。

如图所示，PC-A 正在向 PC-D 发送以太网帧。如表所示该交换机将 PC-A 的 MAC 地址添加到MAC地址表中。

**注意**: 如果源 MAC 地址已经保存在表中，但是对应的是不同的端口，那么交换机会将其视为一个新的条目。使用相同的 MAC 地址和最新的端口号来替换该条目。

![](pic/9.png)

## 转发

**查找目的MAC地址**

如果目的 MAC 地址为单播地址，该交换机会看帧中的目的 MAC 地址与 MAC 地址表中的条目是否匹配。如果表中存在该目的MAC地址，交换机会从指定端口转发帧。如果表中不存在该目的MAC地址，交换机会从除传入端口外的所有端口转发帧。这称为未知单播。

如图所示，交换机的表中没有目的主机 PC-D 的 MAC 地址，因此交换机会从除端口 1 外的所有端口转发帧。

**注意**: 如果目的 MAC 地址为广播或组播，该帧也将被泛洪到除传入端口外的所有端口。

## 过滤帧

交换机是从不同的设备接收帧，因此它可以通过检查每个帧的源 MAC 地址来填充它的 MAC 地址表。如果MAC 地址表包含目的MAC 地址，则交换机将“滤过”该帧并将其从单个端口转发出去。

## 将帧发送到默认网关

如果一台设备的 IP 地址在远程网络上，则不能将以太网帧直接发送到目的设备。而是将以太网帧发送到默认网关（路由器）的 MAC 地址。

**注意**: 在视频中，从 PC-A 发送到远程网络中的目的地的 IP 数据包具有 PC-A 的源 IP 地址和远程主机的目的 IP 地址。返回的 IP 数据包将具有远程主机的源 IP 地址和 PC-A 的目的 IP 地址。