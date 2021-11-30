# 第二天

## 继续开发

```
; hello-os
; TAB=4

		ORG		0x7c00			; 指令程序的装载地址

; FAT12标准格式

		JMP		entry
		DB		0x90
.....
.....
.....


; 程序主体

entry:
		MOV		AX,0			; 初始化寄存器
		MOV		SS,AX
		MOV		SP,0x7c00
		MOV		DS,AX
		MOV		ES,AX

	
putloop:
		MOV		AL,[SI]
		ADD		SI,1			; 给SI+1
		CMP		AL,0
		JE		fin
		MOV		AH,0x0e			; 显示一个文字
		MOV		BX,15			; 指定字符颜色
		INT		0x10			; 调用显卡BIOS
		JMP		putloop
fin:
		HLT						; 让CPU停止，等待指令
		JMP		fin				; 无限循环

msg:
		DB		0x0a, 0x0a		; 换两行
		DB		"hello, world"
		DB		0x0a			; 换行
		DB		0

		RESB	0x7dfe-$		; 填写0x00直到0x7dfe

		DB		0x55, 0xaa
```



### 新的指令

`ROG`指令的英文是origin源头，这个指令会告诉nask,在开始执行的时候，把这些机器语言指令装载到哪个内存地址，使用这一条指令的话，`$`符号也随之发生变化，它不再是 指输出文件的第几个字节，而是代表将要读入的内存地址,至于为什么是0x7c00，是因为很多内存地址被占用，比如BIOS就占用了0号地址，并且0x00007c00-0x00007dff规定是启动区程序的装载地址

`JMP`指令相当于c语言中的goto

`msg:`作为标签，和bat批处理文件相同，用于指定JMP的目的地

`MOV`指令(MOV)用于赋值

> MOV AX,0相当于AX=0这样的一条赋值语句
>
> MOV SS,AX相当于SS=AX

### 关于寄存器

CPU中有一种名为寄存器的存储电路，在机器语言中就相当于变量的功能，具有代表性的寄存器共八个

- AX——accumulator,累加寄存器
- CX——counter,计数寄存器
- DX——data,数据寄存器
- BX——base,基址寄存器
- SP——stack pointer,栈指针寄存器
- BP——base pointer,基址指针寄存器
- SI——source index,源变址寄存器
- DI——destination index,目的变址寄存器

这些寄存器全是16位寄存器，因此可以存储16位的二进制数，其中的X表示扩展(extend)，因为在此之前的CPU寄存器都是8位的，所以16位的加了X。

这八个寄存器全部结合起来也才只有16个字节，如果想要32位寄存器，在他们前面加上E

- ES——附加段寄存器(extra segment)
- CS——代码段寄存器(code segment)
- SS——栈段寄存器(stack segment)
- DS——数据段寄存器(data segment)

### 代码解读

在程序主体中，有一行

```
MOV		SI,msg
```

看上去将标号赋值给了SI寄存器，其实是将msg的内存地址赋值给了SI

就像JMP entity可以写成JMP 0X7c50一样，对应的都只是内存地址



其次还有一行

```
MOV AL,[SI]
```

这个里面的[]代表内存条中的位置，没错，就是电脑里8G,16G的那个内存条



MOV指令的源和目的位置不仅可以是寄存器或常数

```
MOV BYTE [678],123
```

这条指令是要用内存的678位置存储123,但是CPU并没有数值的概念，678不过是一大堆0或1的电信号罢了，当内存收到这一串电信号的时候，电路中的某八个存储单元就会响应，这8个存储单元会记住代表123的电信号，为什么是8位呢，因为我们使用的是byte,同样如果用word就是16位，代表123的二进制数就是000000000111011，679号内存也需要被使用，低位的0111011保存到678，高位的0000000保存到679，那么为什么不是前面的00000000存到678呢，没办法，规定就是规定，order is order

关于内存地址的指定，我们不仅可以用常数，还可以用寄存器，比如`BYTE [SI]`这样，如果SI中保存的是987，则会被执行为`BYTE [987]`

`ADD`是加法指令

`ADD SI,1`的话，就是SI=SI + 1

`CMP`是比较指令，`CMP A,3`告诉比较的对象，类似于C语言中的`if(a == 3)`然后下一步再写如果结果相等，该执行什么

`JE`是跳转指令之一，意思是jump if equal，表示如果相同就跳转

```
CMP AL,0
JE fin
```

相当于

```c
if (AL == 0){
    goto fin
}
```

`INT`是中断指令，作者还没讲，说后面会讲





电脑里有个名为BIOS(Basic Input Output System基本输入输出系统)的程序，直接写在电脑主板的rom(只读存储器，断电不消除)中，BIOS中预先写入了一些操作系统开发人员经常会用到的一些程序，`INT`就是用来调用这些程序的指令



最后有一个`HLT`的指令，类似于BAT批处理文件中的pause

## Makefile

makefile在Linux中太常见了，就像是一个非常聪明的批处理文件

```
# 默认操作
# #号表示注释

# default表示没有指令时运行
default :
    ../z_tools/make.exe img

# 文件生成规则
# ipl.bin : ipl.nas Makefile 表示如果想要生成ipl.bin文件，就要检查ipl.nas, Makefile文件是否存在
# 如果两个都有了Make工具就会自动执行Makefle的下一行
ipl.bin : ipl.nas Makefile
    ../z_tools/nask.exe ipl.nas ipl.bin ipl.lst

# \是续行符号，表示这一行太长，跳转到下一行继续写
helloos.img : ipl.bin Makefile
    ../z_tools/edimg.exe   imgin:../z_tools/fdimg0at.tek \
        wbinimg src:ipl.bin len:512 from:0 to:0   imgout:helloos.img

# 命令
# 有了以下命令，只需要输入make img就可以达到与make -r ipl.bin命令相同的效果，就不需要.bat文件

asm :
    ../z_tools/make.exe -r ipl.bin

img :
    ../z_tools/make.exe -r helloos.img

# Windows和Linux在copy, del中的返回值不一样。
# 所以需要前面加上cmde.exe /C

run :
    ../z_tools/make.exe img
    cmd.exe /C copy helloos.img ..\z_tools\qemu\fdimage0.bin    
    ../z_tools/make.exe -C ../z_tools/qemu

install :
    ../z_tools/make.exe img
    ../z_tools/imgtol.com w a: helloos.img

# 删除掉除最终结果以外的所有文件
clean :
    cmd.exe /C del ipl.bin
    cmd.exe /C del ipl.lst

# 删除掉原文件以外的所有文件
src_only :
    ../z_tools/make.exe clean
    cmd.exe /C del helloos.img
```
