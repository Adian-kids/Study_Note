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

java定义的整形变量默认为0;

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

## 类

类成员：类封装与该类有关的数据以及操作这些数据的方法，各种各样的类有机的结合在一起便构成了Java程序

### 方法重载

如果有两个方法的方法名相同，但参数不一致，哪么可以说一个方法是另一个方法的重载

- 方法名相同
- 方法的参数类型，参数个不一样
- 方法的返回类型可以不相同
- 方法的修饰符可以不相同
- main 方法也可以被重载

```java
class MyClass {
    int height;
    MyClass() {
        System.out.println("无参数构造函数");
        height = 4;
    }
    MyClass(int i) {
        System.out.println("房子高度为 " + i + " 米");
        height = i;
    }
    void info() {
        System.out.println("房子高度为 " + height + " 米");
    }
    void info(String s) {
        System.out.println(s + ": 房子高度为 " + height + " 米");
    }
}
public class MainClass {
    public static void main(String[] args) {
        MyClass t = new MyClass(3);
        t.info();
        t.info("重载方法");
        //重载构造函数
        new MyClass();
    }
}
```

得到的结果为

```
房子高度为 3 米
房子高度为 3 米
重载方法: 房子高度为 3 米
无参数构造函数
```

### 修饰符

#### 权限修饰符

- **default** (即默认，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。
- **private** : 在同一类内可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**
- **public** : 对所有类可见。使用对象：类、接口、变量、方法
- **protected** : 对同一包内的类和所有子类可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**。

接口里的变量都隐式声明为 **public static final**

| 修饰符      | 当前类 | 同一包内 | 子孙类(同一包) | 子孙类(不同包)                                               | 其他包 |
| :---------- | :----- | :------- | :------------- | :----------------------------------------------------------- | :----- |
| `public`    | Y      | Y        | Y              | Y                                                            | Y      |
| `protected` | Y      | Y        | Y              | Y/N（[说明](https://www.runoob.com/java/java-modifier-types.html#protected-desc)） | N      |
| `default`   | Y      | Y        | Y              | N                                                            | N      |
| `private`   | Y      | N        | N              | N                                                            | N      |

#### 方法修饰符

- static 修饰符，用来修饰类方法和类变量。
- final 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。
- abstract 修饰符，用来创建抽象类和抽象方法。
- synchronized 和 volatile 修饰符，主要用于线程的编程。

##### Static关键字

1. 只能调用其他static方法和使用static属性
2. 不能使用关键字this和super
3. static代码块将只被执行一次

静态变量

```java
static int var = 22;
```

静态方法

```java
public class Test{
    static int var;
    static void call(){
        System.out.println("Testcall");
    }
}
```

调用静态方法不需要创建对象，直接通过类名调用就可以(变量同理)

```java
Test.call();
System.out.println(Test.var);
```

静态代码块也仅仅会执行一次,**每次创建对象的时候，都会调用类中的代码块**

```java
static{
    System.out.println("TestA");
}
```

static成员变量是一个类中的所有对象共享的

在访问static成员变量时会发生static成员初始化过程，再次建立对象时，不会重复初始化

##### final关键字

1. 被final修饰的类不能被继承
2. 被final修饰的变量，值不能被修改
3. 用final修饰的方法不能被重写 

##### abstract修饰符

抽象类不能被实例化，abstract类的任何子类必须实现在父类中实现的所有抽象方法，否则子类必须为抽象类

### 构造方法

构造方法的名字必须和所在类的名字一致，没有返回值，但不能声明void，访问权限可以为任意，但是一般情况下使用public方法权限，构造方法中的参数可以根据需要自行定义，参数的不同的构造方法构成重载

#### 对象的初始化

如果没有构造方法，编译器会制定一个默认的，没有任何参数的构造方法去进行初始化，所以以下的两个类的定义是等价的

```java
//未定以构造方法
public class MyClass{System.out.println("Test")}

//定义了构造方法
public class MyClass{
    public MyClass(){
  		System.out.println("Test")
    }
}
```

这两种都可以直接`new`

**也可以定义多个构造方法**，如果定义了有参的构造方法，那么就不会自动生成无参的方法，需要自己手动定义

#### String类的特性

在创建了str1后

```java
String str1 = "Hello";
```

此时会给str1创建一个新对象，但是如果

```java
String str2 = "Hello";
```

此时不会再新建对象，会把str1赋值给str2,如果想要str2新建对象

```java
String str2 = new String("Hello");
```



### 对象的销毁与内存回收

```java
System.gc();
finalize();
```

# Java的数据类型

## 各数据类型默认值

| **数据类型**           | **默认值** |
| :--------------------- | :--------- |
| byte                   | 0          |
| short                  | 0          |
| int                    | 0          |
| long                   | 0L         |
| float                  | 0.0f       |
| double                 | 0.0d       |
| char                   | 'u0000'    |
| String (or any object) | null       |
| boolean                | false      |

## 强制转换

byte->short->int->long->float->double

```java
int a = 32;
byte b = (byte)a
```



# 类的特性

## 类的继承

Java使用extends来继承

```java
class Subclass extends superclass{}
```

## 方法重写

子类重写的方法必须与父类中对应的方法具有相同的方法名，返回值类型和参数列表，方法重写也被称为方法覆盖

## Super关键字

子类在重写了父类的关键字之后，常常还需要用到父类中被重写的方法

```java
//调用父类的构造方法
super();
//调用父类中被重写的方法
super.funcname();
```

# 抽象类

Java允许在类中只声明方法而不提供方法的实现，这种方法被称为抽象方法，这种类被称为抽象类，功能一般由子类实现

```java
abstract class function{}
```

抽象类的作用：程序中定义抽象类的目的是为同一类对象建立抽象的模板，在同类对象所对应的体系中，抽象类往往在顶层中

# 内部类和匿名类

## 内部类

内部类是嵌套定义在一个类中的类，也被成为嵌套类。包含内部类的类成为外部类，也称为包容类

### 内部类的特征

1. 一般只用于定义他的类或语句块之内，在外部引用他时必须给出带有外部类名的完整名称，内部类的名称不需与外部类的名字相同
2. 可以使用外部类的静态成员变量或实例成员变量
3. 可以被定义在外部类的成员方法中，该方法的局部变量或参数只有是final时才可以被内部类使用
4. 可以是抽象类
5. 可以声明为private或protected
6. 可以声明为static，这时内部类变成顶层类，相当于放在外面，不再是嵌套的内部类，且不能引用外部类对象
7. 内部类中声明static成员，要求该内部类必须声明为static

内部类可以作为外部类的一个成员使用，可以访问外部类的所有成员，包括private的成员

如果需要在外部创建内部类的对象，可以采用以下格式来声明

```java
Country.Citizen cizizen = new Country().new Citizen();
```

## 匿名类

匿名类是不能有名称的类,所以不能直接引用,必须在创建时作为new语句的一部分来声明匿名类

```java
new <类或接口><类的主体>
```

# 接口

Java不允许多重继承，也就是说一个子类只能有一个父类，但是使用接口可以实现多重继承

## 定义与实现接口

接口的定义包括接口声明和接口体两部分，其中接口体包括属性常量和抽象方法

```java
[public] interface 接口名{
    属性常量
    ···
    抽象方法
    ···
}
```

interface是接口的关键字，接口中的属性只允许是静态常量，也就是static或者final类型的

java用implements表示实现一个接口，在实现类中必须实现接口中定义的方法，且可以使用接口中定义的变量，此外，**一个类可以实现多个接口**

## 接口的特性

- 接口中的方法可以有参数列表和返回类型，但不能有任何方法体实现
- 接口中可以包含属性，但是会隐式的声明为static和final,存储在该接口的静态存储区域内，而不属于该接口
- 接口中的方法可以呗声明为public或者不声明，但是结果都会按照public处理
- 如果没有实现接口中的所有方法，那么创建的仍然是一个接口，即接口可以继承接口（使用extends）。在继承时，父接口传给子接口的只是方法声明，而不是具体实现
- 一个接口可以有一个以上的父接口，一个类可以在继承父类的同时实现多个接口



## 接口与抽象类的区别

抽象类可以提供部分已经实现的方法，而接口所有的方法都是抽象的

# 多态

多态通过分离做什么和怎么做，从另一个角度将接口和实现分离开来，可以实现可扩展性的程序

## 向上转型

由于继承关系的存在，对象既可以作为自己本身的类型使用，也可以作为父类，这种将某个对象的引用是为对其父类类型引用的做法被称为向上转型

例子如书P88

# 异常处理

## try-catch

一词从上到下进行比较，是否符合异常类型

catch语句的参数类似与方法的声明，包括一个异常类型和一个类型对象

## finally

是对try-catch最佳的补充，无论有无异常，finally都会被执行

## throws

是一种被动异常处理方式

## throw

是主动抛出异常

# 对象管理

## 使用对象数组









