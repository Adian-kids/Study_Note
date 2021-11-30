# CTFHUB_bak文件

## 题目内容

```
Flag in index.php source code.
```

## WriteUp
题目说文件在index.php的源代码里，有两种可能，

- index.php的备份文件index.php.bak
- index.php的vim备份index.php.swp

经过尝试，是在index.php.bak中

```
<!DOCTYPE html>
<html>
<head>
    <title>CTFHub 备份文件下载 - bak</title>
</head>
<body>
<?php

// FLAG: ctfhub{baa474d24a928121d058b36d}

echo "Flag in index.php source code.";
?>
</body>
</html>
```

