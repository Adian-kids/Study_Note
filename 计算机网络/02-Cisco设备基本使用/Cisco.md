# Cisco Switch

## Connect Method

默认情况下，交换机将转发流量，无需配置即可工作。例如，连接到同一新交换机的两个已配置了的主机能够进行通信。

无论新交换机的默认特性如何，都应配置并保护所有交换机。

| **方法**             | **描述**                                                     |
| :------------------- | :----------------------------------------------------------- |
| **控制台 (Console)** | 这是一种物理管理端口，可通过该端口对思科设备进行带外访问。带外访问是指通过仅用于设备维护的专用管理通道进行访问。使用控制台端口的优势在于，即使没有配置任何网络服务，也可以访问设备，例如执行初始配置时。控制台连接需要运行终端仿真软件的计算机和用于连接设备的特殊控制台电缆。 |
| **安全外壳(SSH)**    | SSH 是一种带内且被推荐的方法，它使用虚拟接口通过网络远程建立安全的 CLI连接。不同于控制台连接，SSH 连接需要设备上具有有效的网络服务，包括配置了地址的有效接口。大部分思科 IOS 版本配备了 SSH 服务器和 SSH 客户端，可用于与其他设备建立 SSH 会话。 |
| **Telnet**           | Telnet 使用虚拟接口通过网络远程建立 CLI 会话，这种带内方法并不安全。与 SSH 不同，Telnet 不提供安全的加密连接，只能在实验室环境中使用。用户身份验证、密码和命令通过网络以明文形式发送。最好的做法是使用 SSH 而不是 Telnet。思科 IOS 包括 Telnet 服务器和 Telnet 客户端。 |

**注意:** 某些设备，比如路由器，还可以支持传统辅助端口，这种辅助端口可使用调制解调器通过电话连接远程建立 CLI 会话。类似于控制台连接，AUX 端口也是带外连接，且不需要配置或提供网络服务。

## IOS Command

| **命令模式**                   | **描述**                                                     | **默认设备提示符** |
| :----------------------------- | :----------------------------------------------------------- | :----------------- |
| **用户 EXEC 模式（用户模式）** | 该模式仅允许访问数量有限的基本监控 命令。它通常被称为“仅查看”模式。 | `Switch> Router>`  |
| **特权 EXEC 模式（特权模式）** | 该模式允许访问所有命令和功能。用户可以使用任何监控命令以及执行配置 和管理命令。 | `Switch# Router#`  |

多种命令用于进出命令提示符。要从用户模式切换到特权模式，请使用 **enable** 命令。使用特权模式命令 **disable** 返回用户模式。

**注意**: 特权模式有时称为使能模式。

要进出全局配置模式，请使用特权模式命令 **configure terminal** 。要返回特权模式，请输入全局配置模式命令 **exit**。

有许多不同的子配置模式。例如，要进入线路子配置模式，您可以使用 **line** 命令后跟您要访问的管理线路类型和编号来实现。使用 **exit** 命令来退出子配置模式并返回全局配置模式。

```
Switch(config)# line console 0
Switch(config-line)# exit
Switch(config)#
```

此处的`line console 0`表示进入的控制台接口编号，多数交换机有且只有一个编号

要从全局配置模式的任何子配置模式切换到模式层级中的上一级模式，请输入 **exit** 命令。

要从任何子配置模式切换到特权模式，请输入 **end** 命令或输入组合键 **Ctrl+Z**。

```
Switch(config-line)# end
Switch#
```

您还可以直接从一个子配置模式切换到另一个子配置模式。注意在选择接口后，命令提示符如何从 **(config-line)#** 到 **(config-if)#**。

```
Switch(config-line)# interface FastEthernet 0/1
Switch(config-if)#
```

## Config Method

要配置设备，用户必须进入全局配置模式。

在全局配置模式下， CLI 配置所做的更改将影响整个设备的运行。全局配置模式由在设备名称之后加(config)#结尾的提示符标识，比如Switch(config)#。

访问全局配置模式之后才能访问其他具体的配置模式。在全局配置模式下，用户可以进入不同的子配置模式。其中的每种模式可以用于配置 IOS 设备的特定部分或特定功能。两个常见的子配置模式包括：

- **线路配置模式** - 用于配置控制台、SSH、Telnet 或 AUX 访问。
- **接口配置模式** - 用于配置交换机端口或路由器网络接口。

当使用 CLI 时，每种模式由该模式独有的命令提示符来标识。默认情况下，每个提示符都以设备名称开头。命令提示符中设备名称后的部分用于表明模式。例如，线路配置模式的默认提示符是 **Switch(config-line)#** 默认的接口配置模式提示符是 **Switch(config-if)#**。

## Command

### Command Struct

思科 IOS 设备支持许多命令。每个 IOS 命令都有特定的格式或语法，并且只能在相应的模式下执行。如图所示，常规命令语法为命令后接相应的关键字和参数。

该图显示了交换机命令的一般语法（即提示符、命令、空格和关键字或参数），并提供了两个示例。在第一个示例中，提示符是 Switch>，命令是show，后面跟有一个空格，关键字是 ip protocols。在第二个示例中，提示符是 Switch>，命令是 ping，后面跟有一个空格，参数是 192.168.10.5。

![](1.png)

提示符命令空格关键字或参数

- **关键字** - 这些是在操作系统中定义的特定参数。（在图中为 **ip protocols**）。
- **参数** - 这些没有预先定义，它是由用户来定义的值或变量。（在图中为 **192.168.10.5**）。

输入包括关键字和参数在内的完整命令后，按 **Enter** 键将该命令提交给命令解释程序。

### Command Help

IOS 提供两种形式的帮助：上下文相关帮助和命令语法检查。

上下文相关帮助使您能够快速找到以下问题的答案：

- 每个命令模式中有哪些命令可用?
- 哪些命令以特定字符或字符组开头?
- 哪些参数和关键字可用于特定命令？

要访问上下文相关帮助，请直接在 CLI 中输入一个**?**。

命令语法检查用于验证用户输入的命令是否有效。输入命令后，命令行解释程序将从左向右评估命令。如果解释程序可以理解该命令，则用户要求执行的操作将被执行，且 CLI 将返回到相应的提示符。然而，如果解释程序无法理解用户输入的命令，它将提供反馈，说明该命令存在的问题。

### Command  Check 

一条命令可能需要一个或多个参数。要确定命令所需的关键字和参数，请参阅命令语法。语法提供输入命令时必须使用的模式或格式。

如表中所标识的那样，粗体文本表示需要原样输入的命令和关键字。斜体文本表示由用户提供值的参数。

| **约定**                      | **描述**                                                     |
| :---------------------------- | :----------------------------------------------------------- |
| **粗体**                      | 粗体文本表示您需要原样输入的命令和关键字， 如显示的那样。    |
| *斜体*                        | 斜体文本指示由您提供值的参数。                               |
| **[**x**]**                   | 方括号表示可选元素（关键字或参数）。                         |
| **{**x**}**                   | 大括号表示必需元素（关键字或参数）。                         |
| **[**x **{**y **\|** z **}]** | 方括号中的大括号和垂直线表示 可选元素中的必填选项。空格用于清楚地描述 命令的各个部分。 |

例如，使用 **description** 命令的语法是 **description** 空格加字符串。参数是用户提供的空格加字符串的值。**description**命令通常用于描述接口的用途。例如，输入命令 **description Connects to the main headquarter office switch**，描述的是另一台设备在连接末端的什么位置。

以下示例说明了记录和使用 IOS 命令的约定：

- **ping** *ip-address* - 其中的命令是 ping，用户定义的参数是目的设备的IP地址。例如，**ping 10.10.10.5**。
- **traceroute** *ip-address* - 其中的命令是 traceroute，用户定义的参数是目的设备的IP地址。例如 **traceroute 192.168.254.254**。

如果一个复杂命令具有多个参数，您可能会看到它是这样表示的：

```
Switch(config-if)# switchport port-security aging { static | time time | type {absolute | inactivity}}
```

该命令通常会遵循我们对该命令和每个参数的详细描述。

思科 IOS 命令参考是我们了解具体 IOS 命令信息的主要来源。

### Hot Key

IOS CLI 提供热键和快捷方式，以使配置、监控和故障排除更加轻松。

命令和关键字可缩写为可唯一确定该命令或关键字的最短字符数。例如，**configure** 命令可缩写为 **conf**，因为 **configure** 是唯一一个以 **conf** 开头的命令。不能缩写为 **con**，因为以 **con** 开头的命令不止一个。关键字也可缩写。

该表列出了用于增强命令行编辑的键盘输入。

| **键盘输入**                           | **描述**                                            |
| :------------------------------------- | :-------------------------------------------------- |
| **Tab**                                | 补全部分输入的命令项。                              |
| **Backspace**                          | 删除光标左边的字符。                                |
| **Ctrl-D**                             | 删除光标所在的字符。                                |
| **Ctrl-K**                             | 删除从光标到命令行尾的所有字符。                    |
| **Esc D**                              | 删除从光标到词尾的所有字符。                        |
| **Ctrl+U** 或 **Ctrl+X**               | 删除从光标到命令行首的 所有字符。                   |
| **Ctrl-W**                             | 删除光标左边的单词。                                |
| **Ctrl-A**                             | 将光标移至行首。                                    |
| **向左箭头** 或 **Ctrl+B**             | 将光标左移一个字符。                                |
| **Esc B**                              | 将光标向后左移一个单词。                            |
| **Esc F**                              | 将光标向前右移一个单词。                            |
| **向右箭头** 或 **Ctrl+F**             | 将光标右移一个字符。                                |
| **Ctrl-E**                             | 将光标移至命令行尾。                                |
| **向上箭头** 或 **Ctrl+P**             | 调出历史记录缓冲区中的命令， 从最近输入的命令开始。 |
| **Ctrl+R** 或 **Ctrl+I** 或 **Ctrl+L** | 收到控制台消息后重新显示系统提示符和 命令行。       |

**注意**: 虽然 **Delete** 键通常用于删除提示符右侧的字符，但 IOS 命令结构无法识别 Delete 键。

当命令输出产生的文本超过终端窗口中可以显示的文本时，IOS 将显示一个 **“--More--”** 提示。下表描述了显示此提示时可以使用的键盘输入。

| **键盘输入** | **描述**                       |
| :----------- | :----------------------------- |
| **回车** 键  | 显示下一行。                   |
| **空格**键   | 显示下一屏。                   |
| 任何其他按键 | 结束显示字符串，返回特权模式。 |

此表列出了用于退出操作的命令。

| **键盘输入**     | **描述**                                                     |
| :--------------- | :----------------------------------------------------------- |
| **Ctrl-C**       | 处于任何配置模式下时，用于结束该配置模式并返回 特权模式。处于设置模式下时，用于中止并返回命令 提示符。 |
| **Ctrl-Z**       | 处于任何配置模式下时，用于结束该配置模式并返回 特权模式。    |
| **Ctrl-Shift-6** | 通用中断序列用于中止 DNS lookup、traceroutes、 pings等。     |

## Configure Host

### Hostname

您已经学到了很多关于思科 IOS、IOS 导航和命令结构的知识。现在，您已经准备好配置设备了！任何设备上的第一个配置命令应该是为其提供一个唯一的设备名称或主机名。默认情况下，所有设备都有一个出厂的默认名称。例如，思科 IOS 交换机是出厂名称是 “Switch。”

问题是如果所有网络中的交换机都采用其默认名称，则会很难识别特定设备。例如，在使用 SSH 远程访问设备时，您如何知道您已连接到了正确的设备？主机名让您确认您已经连接到了正确的设备。

默认主机名应更改为更具描述性的名称。通过审慎地选择名称，就很容易记住、记录和鉴别网络设备。以下是对主机的一些重要命名指南：

- 以字母开头
- 不包含空格
- 以字母或数字结尾
- 仅使用字母、数字和破折号
- 长度少于 64 个字符

组织必须选择一个命名约定，以便能够轻松直观地识别特定设备。IOS 设备中所用的主机名会保留字母的大小写状态。例如，在图中，三台交换机，跨越三个不同的楼层，在网络中互连起来。所使用的命名约定中，合并了每台设备的位置和用途。网络文档中应该说明这些名称是如何选出的，以便其他设备可按相应方法命名。

该图显示了三个相互连接的交换机，跨越了三个楼层。最上面的交换机名为 Sw-Floor-3，中间的交换机名为 Sw-Floor-2，底部的交换机名为 Sw-Floor-1。坐在主机 PC 前的用户连接到了 Sw-Floor-1 交换机。底部的文字显示：当网络设备有了其命名，他们可以轻松识别网络设备，从而进行配置。



Sw-Floor-3Sw-Floor-2Sw-Floor-1

当网络设备有了其命名，他们可以轻松识别网络设备，从而进行配置。

当确定命名约定后，接下来的步骤就是使用 CLI 将名称应用到设备。如示例所示，在特权模式下，输入 **configure terminal** 命令访问全局配置模式。注意命令提示符的变化。

```
Switch# configure terminal
Switch(config)# hostname Sw-Floor-1
Sw-Floor-1(config)#
```

从全局配置模式下，输入 **hostname** 命令后跟交换机的名称，然后按 **Enter** 键。注意命令提示符的变化。

**注意**: 要使交换机返回默认提示符，请使用 **no hostname** 全局配置命令。

每次添加或修改设备时，请始终确保更新相关文档。请在文档中通过地点、用途和地址来标识设备。

### Password



当您最初连接到设备时，您处于用户 EXEC 模式。使用控制台保护此模式的安全。

要保护用户 EXEC 模式访问的安全，请使用全局配置命令 **line console 0** 进入线路控制台配置模式，如示例所示。0 用于代表第一个（而且在大多数情况下是唯一的一个）控制台接口。接下来，使用 **password** *password* 命令指定用户 EXEC 模式密码。最后，使用 **login** 命令启用用户 EXEC 访问。

```
Sw-Floor-1 # configure terminal
Sw-Floor-1(config)# line console 0
Sw-Floor-1(config-line)# password cisco
Sw-Floor-1(config-line)# login
Sw-Floor-1(config-line)# end
Sw-Floor-1#
```

现在控制台访问需要输入密码，然后才能访问用户 EXEC 模式。

要使管理员能够访问所有 IOS 命令（包括配置设备），您必须获得特权 EXEC 模式访问权限。这是最重要的访问方法，因为它提供了对设备的完整访问权限。

要保护特权 EXEC 访问，请使用 **enable secret** *password* 全局配置命令，如示例所示。

```
Sw-Floor-1# **configure terminal** Sw-Floor-1(config)# **enable secret class** Sw-Floor-1(config)# **exit** Sw-Floor-1#
```

虚拟终端 (VTY) 线路支持通过Telnet或SSH对设备的远程访问。许多思科交换机支持第 0 到 15 的 16 条 VTY 线路。

要保护 VTY 线路的安全，请使用 **line vty 0 15** 全局配置命令进入线路 VTY 模式。接下来，使用 **password** *password* 命令指定VTY密码。最后，使用 **login** 命令启用 VTY 访问。

下面展示了一个在交换机上保护 VTY 线路的示例。

```
Sw-Floor-1 # configure terminal
Sw-Floor-1(config)# line vty 0 15
Sw-Floor-1(config-line)# password cisco 
Sw-Floor-1(config-line)# login 
Sw-Floor-1(config-line)# end
Sw-Floor-1#
```

### Encrypt Pass

启动配置文件和运行配置文件以明文显示大多数密码。这会带来安全威胁，因为任何人如果访问这些文件，就可以发现这些密码。

要加密所有明文密码，请使用全局配置命令 **service password-encryption** ，如示例所示。

```
Sw-Floor-1 # configure terminal
Sw-Floor-1(config)# service password-encryption
Sw-Floor-1(config)#
```

该命令对所有未加密的密码进行弱加密。这种加密仅适用于配置文件中的密码，而不适用于通过网络发送的密码。此命令的用途在于防止未经授权的人员查看配置文件中的密码。

使用 **show running-config** 命令验证密码现在是否已加密。

```
Sw-Floor-1(config)# end
Sw-Floor-1# show running-config
!!line con 0password 7 094F471A1A0A login!line vty 0 4password 7 03095A0F034F38435B49150A1819login!!end
```

### Banner

尽管要求用户输入密码是防止未经授权的人员进入网络的有效方法，但同时必须向试图访问设备的人员声明仅授权人员才可访问设备。出于此目的，可向设备输出中加入一条标语。当控告某人侵入设备时，标语可在诉讼程序中起到重要作用。某些法律体系规定，若不事先通知用户，则既不允许起诉该用户，甚至连对该用户进行监控都不允许。

要在网络设备上创建当日消息标语，请使用 **banner motd #** *当日消息***#**全局配置命令。命令语法中的“#”称为定界符。它会在消息前后输入。定界符可以是未出现在消息中的任意字符。因此，经常使用“#”之类的字符。命令执行完毕后，系统将向之后访问设备的所有用户显示该标语，直到该标语被删除为止。

以下示例显示了在 Sw-Floor-1 上配置标语的步骤。

```
Sw-Floor-1 # configure terminal
Sw-Floor-1(config)# banner motd #Authorized Access Only#
```

## Configfile

您现在了解了如何在交换机上执行基本配置，包括密码和标语消息。本主题将向您展示如何保存您的配置。

有两种系统文件用于存储设备配置：

- **startup-config(启动配置文件)** - 存储在 NVRAM 中的配置文件。它包含在启动时或重启时用到的所有命令。当设备断电后，其中的内容不会消失。

- **running-config(运行配置文件)** - 存储在随机存取存储器（RAM）中。它反映了当前的配置。修改运行配置会立即影响思科设备的运行。RAM 是易失性存储器。如果设备断电或重新启动，则它会丢失所有内容。

  特权 EXEC 模式命令 **show running-config** 用于查看正在运行的配置。如示例所示，命令将列出当前存储在 RAM 中的完整配置。

```
Sw-Floor-1# show running-config
Building configuration...
Current configuration : 1351 bytes
!
! Last configuration change at 00:01:20 UTC Mon Mar 1 1993
!
version 15.0
no service pad
service timestamps debug datetime msec
service timestamps log datetime msec
service password-encryption
!
hostname Sw-Floor-1
!
(output omitted)
```

要查看启动配置文件，请使用特权 EXEC 命令 **show startup-config**。

如果设备断电或重新启动，所有未保存的配置更改都会丢失。要将对运行配置所作的更改保存到启动配置文件中，请使用特权 EXEC 模式命令 **copy running-config startup-config**。

## Interfaces and ports

网络通信取决于最终用户设备接口、网络设备接口以及连接设备的线缆。每个物理接口都有对其进行定义的规范或标准。连接接口的线缆必须设计为匹配接口的物理标准。网络介质类型包括双绞线铜缆、光缆、同轴电缆和无线，如图所示。



![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daaaff1-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daaaff2-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daad700-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daad701-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daad702-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daad703-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daafe10-1c25-11ea-81a0-ffc2c49b96bc.png)![img](https://contenthub-cn.netacad.com/courses/itn/2d9d1b60-1c25-11ea-853e-2fb91ac44bf9/2da9c590-1c25-11ea-b0b6-4daf98e51c95/assets/2daafe11-1c25-11ea-81a0-ffc2c49b96bc.png)

铜缆无线光纤

不同类型的网络介质有不同的特性和优点。并非所有网络介质都具有相同的特征。并非所有介质都适用于同一目的。各种介质类型之间的差异包括：

- 介质可以成功传送信号的距离
- 要安装介质的环境
- 必须传输的数据量和速度
- 介质和安装的成本

互联网上的每条链路不仅需要采用特定的网络介质，而且需要采用特定的网络技术。例如，以太网是当今最常用的局域网 (LAN) 技术。在使用线缆物理连接到网络的最终用户设备、交换设备和其他网络设备上，均可找到以太网端口。

思科 IOS 第 2 层交换机有物理端口，可用于连接设备。这些端口不支持第 3 层 IP 地址。因此，交换机有一个或多个交换机虚拟接口 (SVI)。这些是虚拟接口，是因为设备上没有任何物理硬件与之关联。SVI 会在软件中创建。

虚拟接口可以让您使用 IPv4和IPv6 通过网络远程管理交换机。每台交换机的默认配置中都“现成”带有一个 SVI。默认 SVI 是接口 VLAN1。

**注意**: 第2 层交换机不需要 IP 地址。分配给 SVI 的 IP 地址用于远程访问交换机。2层交换机无需使用 IP 地址就可以工作。

## Switch interface config

交换机虚拟接口配置

要远程访问交换机，SVI 上必须配置 IP 地址和子网掩码。要在交换机上配置 SVI，请使用全局配置命令 **interface vlan 1**。Vlan 1 并不是一个实际物理接口，而是一个虚拟接口。然后使用接口配置命令 **ip address** *ip-address subnet-mask* 配置 IPv4 地址。最后，使用接口配置命令 **no shutdown** 启用虚拟接口。

在这些命令配置后，交换机即可使用所有 IPv4 要素进行网络通信。

```
Sw-Floor-1# configure terminal
Sw-Floor-1(config)# interface vlan 1
Sw-Floor-1(config-if)# ip address 192.168.1.20 255.255.255.0
Sw-Floor-1(config-if)# no shutdown
Sw-Floor-1(config-if)# exit
Sw-Floor-1(config)# ip default-gateway 192.168.1.1
```

## Test interface config

### display ip

```
show ip interface brief
```

