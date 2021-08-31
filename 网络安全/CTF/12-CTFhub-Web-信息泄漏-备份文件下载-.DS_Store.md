# CTFHUB_.DS_Store

## 题目内容

```
备份文件下载 - DS_Store

试着寻找 flag
```

## WriteUp
根据题目，下载网站根目录中的.DS_Store文件

并使用脚本进行解析（https://github.com/gehaxelt/Python-dsstore）

此脚本需要将文件下载下来后再做解析，不可以直接http访问

结果如下

```
Count:  1
08e6c28c508073e2b66471b043934186.txt
```

访问txt文件得到flag
