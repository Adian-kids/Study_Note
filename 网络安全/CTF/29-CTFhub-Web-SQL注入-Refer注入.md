# CTFHUB_refer注入

## 题目内容

![image-20210824215040746](/home/adian/note/Study_Note/网络安全/CTF/pic/22.png)


## WriteUp

通过显示出来的内容可以判断注入点在refer处，使用burpsuite抓包在repeater测试即可

```
sqlmap-r xxx.txt -p referer --level 5 
```
这个题注意，题目本身访问五referer参数，需要自己加上，在其他ctf sql注入赛题中记得排查这一参数

