# CTFHUB_upload无验证

## 题目内容

![image-20210824231032580](/home/adian/.config/Typora/typora-user-images/image-20210824231032580.png)


## WriteUp

从网站源码中可以看出验证文件类型判断是否可以上传验证在前端函数中

```
function checkfilesuffix()
{
    var file=document.getElementsByName('file')[0]['value'];
    if(file==""||file==null)
    {
        alert("请添加上传文件");
        return false;
    }
    else
    {
        var whitelist=new Array(".jpg",".png",".gif");
        var file_suffix=file.substring(file.lastIndexOf("."));
        if(whitelist.indexOf(file_suffix) == -1)
        {
            alert("该文件不允许上传");
            return false;
        }
    }
}
```

通过返回的true 和 false决定是否可以上传

```
<form action="" method="post" enctype="multipart/form-data" onsubmit="return checkfilesuffix()">
```

两种方案

1. 浏览器禁用JS
2. 前端上传.jpg后使用burpsuite抓包改成.php

我禁用了浏览器js直接上传成功
