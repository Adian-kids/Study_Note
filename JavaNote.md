# Jdk and Jre

## Jdk

### Linux安装jdk

```
sudo apt install openjdk~~~(自己选择版本)
```

### 寻找路径

```
whereis java
```

找到

```
java: /usr/bin/java /usr/share/java
```

我们

```
ls -l /usr/bin/java
```

可以发现其指向路径为

```
/usr/bin/java -> /etc/alternatives/java
```

再次

```
ls -l /etc/alternatives/java
```

得到

```
/etc/alternatives/java -> /usr/lib/jvm/java-11-openjdk-amd64/bin/java
```



## Jre

`jre/lib`文件夹下的rt.java就是Java语言的核心类库(openjdk我还没找到，好像需要自己整)

# Java的类和包

## 类 Class

如果定义一个

```java
class A{}
```

无论程序名如何命名，都可以正常编译

但是如果我们用public修饰

```java
public class A{}
```

文件命名就必须是`A.java`

我们也可以把多个类写到一个Java程序里

```java
A.java
public class A{}
class B{}
class C{}
```

我们可以编译通过，但是会分别释放`A.class`,`B.class`,`C.class`

因为Java是以类为单位进行封装，而不是文件

## 包 Package

包是类的容器，用来分隔类名空间

### 实例——创建一个package

```java
package com.test;					//定义一个包
public class B{						//定义一个类
    public void add(int i; int j){  
        System.out.println(i + j);
    }
}
```

调用刚才创建的package

```java
import com.test.*;
public class A{
    public static void main(String[] args){
        B b = new B();
        b.add(3,4);
    }
}
```

# Java的类和对象



# 类

类成员：类封装与该类有关的数据以及操作这些数据的方法，各种各样的类有机的结合在一起便构成了Java程序





