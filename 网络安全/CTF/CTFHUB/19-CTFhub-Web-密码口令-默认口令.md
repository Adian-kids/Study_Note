# CTFHUB_默认口令

## 题目内容

![image-20210822183919392](/home/adian/note/Study_Note/网络安全/CTF/pic/12.png)

## WriteUp
根据Web可以得出这是一个Eyou的邮件网关，百度查询

![image-20210822184236814](/home/adian/note/Study_Note/网络安全/CTF/pic/13.png)



使用这个帐号登录，提示user is not exists，说明不是这个用户名

再次查询得知亿邮的邮件网关系统，系统有三个默认的帐号（admin:+-ccccc、eyougw:admin@(eyou)、eyouuser:eyou_admin） 的账户信息，分别测试之后即可

最终通过`eyougw:admin@(eyou)`拿到flag

```
Hello CTFHub eyougw admin, ctfhub{27ad1cdc87b9d0bcb52c125f}
```

