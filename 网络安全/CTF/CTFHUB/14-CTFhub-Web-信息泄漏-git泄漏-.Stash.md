# CTFHUB_git

## 题目内容

```
Where is flag?
```

## WriteUp
使用githack clone项目，仍然发现git log有add flag

```
commit d272e57c5e193885d9e87d580be6c60198f0a6cc (HEAD -> master)
Author: CTFHub <sandbox@ctfhub.com>
Date:   Sat Aug 21 15:58:53 2021 +0000

    remove flag

commit 27008c4baff10b093fd4af890b7464b75c942fc7
Author: CTFHub <sandbox@ctfhub.com>
Date:   Sat Aug 21 15:58:53 2021 +0000

    add flag

commit 5585b23b55f7cf181bd1f757715d2365d3a5e645
Author: CTFHub <sandbox@ctfhub.com>
Date:   Sat Aug 21 15:58:53 2021 +0000

    init
```

尝试获取版本差异，未获取到flag

获取stash,`stash`命令可用于临时保存和回复修改，**可跨分支**。

我们可以查看到有stash

```
stash@{0}: WIP on master: 27008c4 add flag
```

我们使用以下命令获取stash

```
git stash pop
```

得到

```
冲突（修改/删除）：211892831419447.txt 在 Updated upstream 中被删除，在 Stashed changes 中被 修改。211892831419447.txt 的 Stashed changes 版本被保留。
贮藏条目被保留以备您再次需要。
```

此时目录下已经有了211892831419447.txt

```
cat 211892831419447.txt
```

得到flag

**方法二**

获取stash对应的hash

```
cat .git/refs/stash
```

得到hash

```
65ea98382c2567be65e3c1058c07bf9c6d4202ef
```

然后我们显示差异

```
git diff 65ea9
```

得到flag
