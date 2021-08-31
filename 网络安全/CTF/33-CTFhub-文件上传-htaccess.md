# CTFHUB_htaccess

## 题目内容

![image-20210825040707628](/home/adian/note/Study_Note/网络安全/CTF/pic/26.png)


## WriteUp

直接上传shell会提示文件不匹配

查看源代码看到了一段注释掉的php代码，仔细查看应该是后端的文件类型验证逻辑

```PHP
if (!empty($_POST['submit'])) {
    $name = basename($_FILES['file']['name']);
    $ext = pathinfo($name)['extension'];
    $blacklist = array("php", "php7", "php5", "php4", "php3", "phtml", "pht", "jsp", "jspa", "jspx", "jsw", "jsv", "jspf", "jtml", "asp", "aspx", "asa", "asax", "ascx", "ashx", "asmx", "cer", "swf");
    if (!in_array($ext, $blacklist)) {
        if (move_uploaded_file($_FILES['file']['tmp_name'], UPLOAD_PATH . $name)) {
            echo "<script>alert('上传成功')</script>";
            echo "上传文件相对路径<br>" . UPLOAD_URL_PATH . $name;
        } else {
            echo "<script>alert('上传失败')</script>";
        }
    } else {
        echo "<script>alert('文件类型不匹配')</script>";
    }
}
```

很明显，这个地方采用了一个列表存放黑名单文件格式，我第一个想法是大小写绕过，所以尝试了`shell.phP`,上传成功，但是未解析，访问直接打印了出来

但是明显jpg文件可以成功上传，所以我们做一次.htaccess文件的上传

```
AddType application/x-httpd-php .jpg
```

此内容的意思是将.jpg文件当做php文件处理，访问/upload/shell.jpg即可解析成功，AntSword成功连接

查看后端代码

```php
if (!empty($_POST['submit'])) {
    $name = basename($_FILES['file']['name']);
    $ext = pathinfo($name)['extension'];
    $blacklist = array("php", "php7", "php5", "php4", "php3", "phtml", "pht", "jsp", "jspa", "jspx", "jsw", "jsv", "jspf", "jtml", "asp", "aspx", "asa", "asax", "ascx", "ashx", "asmx", "cer", "swf");
    if (!in_array($ext, $blacklist)) {
        if (move_uploaded_file($_FILES['file']['tmp_name'], UPLOAD_PATH . $name)) {
            echo "<script>alert('上传成功')</script>";
            echo "上传文件相对路径<br>" . UPLOAD_URL_PATH . $name;
        } else {
            echo "<script>alert('上传失败')</script>";
        }
    } else {
        echo "<script>alert('文件类型不匹配')</script>";
    }

}
```

是文件后缀黑名单
