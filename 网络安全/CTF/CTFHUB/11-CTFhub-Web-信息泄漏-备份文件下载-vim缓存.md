# CTFHUB_vim备份文件

## 题目内容

```
备份文件下载 - vim

flag 在 index.php 源码中
```



## WriteUp
题目说明是vim备份文件，所以我们直接`.index.php.swp`

```
http://challenge-50635f851cf1a54b.sandbox.ctfhub.com:10800/.index.php.swp
```

下载下来之后使用vim -r 参数打开

![image-20210821231609508](/home/adian/note/Study_Note/网络安全/CTF/pic/9.png)

拿到flag

使用vscode等其他工具也可以打开，只是部分会乱码
