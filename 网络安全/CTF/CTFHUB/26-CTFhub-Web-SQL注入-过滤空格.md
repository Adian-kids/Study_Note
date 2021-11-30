# CTFHUB_过滤空格

## 题目内容

![image-20210822185008421](/home/adian/note/Study_Note/网络安全/CTF/pic/14.png)

## WriteUp
就是整数型注入，但是过滤了空格，有一个小小的waf

使用`/**/`替代空格即可

````
http://challenge-d4b9b4a89c37ac5f.sandbox.ctfhub.com:10800/?id=1/**/and/**/1=1
````

