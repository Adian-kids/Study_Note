# CTFHUB_.hhg

## 题目内容

```
信息泄露 - Mercurial

Flag 在服务端旧版本的源代码中, 不太好使的情况下, 试着手工解决。
```

## WriteUp
目录扫描发现存在.hg文件，我们使用rip-hg.pl来获取

```
./rip-hg.pl http://challenge-9de604a14dea467f.sandbox.ctfhub.com:10800/.hg 
[i] Getting correct 404 responses
cannot find hg: No such file or directory at ./rip-hg.pl line 140.
```

虽然这么提示，但是我发现.hg文件还是下来了，工具确实不靠谱

我们切换到.hg目录下，使用hg status查看

```
M index.html
! 50x.html
! flag_1438018392.txt
? .gitignore
? .svn/entries
? .svn/format
? .svn/pristine/bf/bf45c36a4dfb73378247a6311eac4f80f48fcb92.svn-base
? .svn/pristine/da/da1d09efc67182e5de16cce1b7bd22cfe7ee0ee9.svn-base
? .svn/wc.db
? .svn/wc.db-journal
? LICENSE
? README.md
? hg-decode.pl
? rip-bzr.pl
? rip-cvs.pl
? rip-git.pl
? rip-hg.pl
? rip-svn.pl
```

拿到flag文件名





服务端删掉了flag.txt也可以通过历史文件获取flag

```
.hg/store/data/flag__1438018392.txt.i
```

使用curl请求

```
curl http://challenge-9de604a14dea467f.sandbox.ctfhub.com:10800/.hg/store/data/flag__1438018392.txt.i
```

## Reference

https://www.wolai.com/ctfhub/sjCVy36wVjJALBR9rHw2JK

