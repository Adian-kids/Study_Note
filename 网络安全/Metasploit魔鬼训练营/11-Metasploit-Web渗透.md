# 基于Metasploit的Web渗透测试

# 辅助模块

Metasploit的辅助模块都在`modules/auxiliary/`下，Web应用辅助扫描、漏洞查找等模块也都在上面，metasploit内置了wmap扫描器，允许用户配置和使用复制模块

## WMAP

```
load wmap
```

在这里，我遇到了问题，在执行`db_status`时提示数据库已连接，但是load wmap会报错，提示数据库未连接，在重启msf后解决，load成功后，输入`help`会出现wmap的帮助文档

```
wmap Commands
=============

    Command       Description
    -------       -----------
    wmap_modules  Manage wmap modules
    wmap_nodes    Manage nodes
    wmap_run      Test targets
    wmap_sites    Manage sites
    wmap_targets  Manage targets
    wmap_vulns    Display web vulns
```

以wmap_sites为例，在执行后，会输出帮助文档

```
msf6 > wmap_sites
[*] Usage: wmap_sites [options]
        -h        Display this help text
        -a [url]  Add site (vhost,url)
        -d [ids]  Delete sites (separate ids with space)
        -l        List all available sites
        -s [id]   Display site structure (vhost,url|ids) (level) (unicode output true/false)
```

将目标网站添加

```
msf6 > wmap_sites -a http://10.10.10.129
[*] Site created.
```

使用`-l`参数进行查看

wmap和awvs的模式一样，要讲website添加到扫描任务，在这里使用`wmap_target`

```
msf6 > wmap_targets 
[*] Usage: wmap_targets [options]
        -h              Display this help text
        -t [urls]       Define target sites (vhost1,url[space]vhost2,url) 
        -d [ids]        Define target sites (id1, id2, id3 ...)
        -c              Clean target sites list
        -l              List all target sites
```

我们可以使用两种方式导入站点，分别为使用`-d`和`-t`

-t 参数后接url，直接进行扫描

-d 参数后接已添加到sites里面的id

比如上面添加的10.10.10.129站点，id为0

```
msf6 > wmap_sites -l
[*] Available sites
===============

     Id  Host          Vhost         Port  Proto  # Pages  # Forms
     --  ----          -----         ----  -----  -------  -------
     0   10.10.10.129  10.10.10.129  80    http   0        0
```

找到id后，可通过`-d 0 `添加

```
msf6 > wmap_targets -d 0
[*] Loading 10.10.10.129,http://10.10.10.129:80/.
```

随后即可通过`wmap_run`进行扫描

```
msf6 > wmap_run 
[*] Usage: wmap_run [options]
        -h                        Display this help text
        -t                        Show all enabled modules
        -m [regex]                Launch only modules that name match provided regex.
        -p [regex]                Only test path defined by regex.
        -e [/path/to/profile]     Launch profile modules against all matched targets.
                                  (No profile file runs all enabled modules.)
```

使用`-e`参数可以测试所有模块，或者使用`-p`.`-m`参数进行指定

## 其他工具

很多开源工具都和Metasploit结合

| 工具   | 描述                              |
| ------ | --------------------------------- |
| W3AF   | web扫描工具                       |
| SQLMAP | 这就不用描述了吧....              |
| wXf    | 开源渗透测试框架                  |
| XSSF   | XSS框架                           |
| BeEF   | 浏览器攻击平台框架--------------- |



