# 第三天 进入32位模式并导入c语言

## 制作真正的IPL

> IPL:启动区

完整代码

```
; haribote-ipl
; TAB=4

		ORG		0x7c00			; このプログラムがどこに読み込まれるのか

; 以下は標準的なFAT12フォーマットフロッピーディスクのための記述

		JMP		entry
		DB		0x90
		DB		"HARIBOTE"		; ブートセクタの名前を自由に書いてよい（8バイト）
		DW		512				; 1セクタの大きさ（512にしなければいけない）
		DB		1				; クラスタの大きさ（1セクタにしなければいけない）
		DW		1				; FATがどこから始まるか（普通は1セクタ目からにする）
		DB		2				; FATの個数（2にしなければいけない）
		DW		224				; ルートディレクトリ領域の大きさ（普通は224エントリにする）
		DW		2880			; このドライブの大きさ（2880セクタにしなければいけない）
		DB		0xf0			; メディアのタイプ（0xf0にしなければいけない）
		DW		9				; FAT領域の長さ（9セクタにしなければいけない）
		DW		18				; 1トラックにいくつのセクタがあるか（18にしなければいけない）
		DW		2				; ヘッドの数（2にしなければいけない）
		DD		0				; パーティションを使ってないのでここは必ず0
		DD		2880			; このドライブ大きさをもう一度書く
		DB		0,0,0x29		; よくわからないけどこの値にしておくといいらしい
		DD		0xffffffff		; たぶんボリュームシリアル番号
		DB		"HARIBOTEOS "	; ディスクの名前（11バイト）
		DB		"FAT12   "		; フォーマットの名前（8バイト）
		RESB	18				; とりあえず18バイトあけておく

; プログラム本体

entry:
		MOV		AX,0			; レジスタ初期化
		MOV		SS,AX
		MOV		SP,0x7c00
		MOV		DS,AX

; ディスクを読む

		MOV		AX,0x0820
		MOV		ES,AX
		MOV		CH,0			; シリンダ0
		MOV		DH,0			; ヘッド0
		MOV		CL,2			; セクタ2

		MOV		AH,0x02			; AH=0x02 : ディスク読み込み
		MOV		AL,1			; 1セクタ
		MOV		BX,0
		MOV		DL,0x00			; Aドライブ
		INT		0x13			; ディスクBIOS呼び出し
		JC		error

; 読み終わったけどとりあえずやることないので寝る

fin:
		HLT						; 何かあるまでCPUを停止させる
		JMP		fin				; 無限ループ

error:
		MOV		SI,msg
putloop:
		MOV		AL,[SI]
		ADD		SI,1			; SIに1を足す
		CMP		AL,0
		JE		fin
		MOV		AH,0x0e			; 一文字表示ファンクション
		MOV		BX,15			; カラーコード
		INT		0x10			; ビデオBIOS呼び出し
		JMP		putloop
msg:
		DB		0x0a, 0x0a		; 改行を2つ
		DB		"load error"
		DB		0x0a			; 改行
		DB		0

		RESB	0x7dfe-$		; 0x7dfeまでを0x00で埋める命令

		DB		0x55, 0xaa
```



本次新增的内容

```
MOV		AX,0x0820
		MOV		ES,AX
		MOV		CH,0			; 柱面0
		MOV		DH,0			; 磁头0
		MOV		CL,2			; 扇区2

		MOV		AH,0x02			; AH=0x02 : 读盘
		MOV		AL,1			; 1个扇区
		MOV		BX,0
		MOV		DL,0x00			; A驱动器
		INT		0x13			; 调用磁盘BIOS
		JC		error
```

这里出现的JC是jump carry，在上面的INT 0x13这个指令是硬盘的BIOS指令，根据作者给出的资料

```
AH = 0x02; 读盘
AH = 0x03; 写盘
AH = 0x04; 校验
AH = 0x0c; 寻道
AL = 处理对象的扇区数，只能同时处理连续的扇区
CH = 柱面号 &oxff
CL = 扇区号
DH = 磁头号
DL = 驱动器号
ES:BX = 缓冲地址 存在硬盘的哪个位置
FLAGS.CF == 0;没有错误，AH = 0
FLAGS.CF == 1;错误,错误号码存在AH内
```

所以JC如果发现FLAGS.CF == 1就跳转到实体error内，执行

```
MOV		SI,msg ;将msg写入SI源变址寄存器内
```

msg:

```
msg:
		DB		0x0a, 0x0a		; 改行を2つ
		DB		"load error"
		DB		0x0a			; 改行
		DB		0

		RESB	0x7dfe-$		; 0x7dfeまでを0x00で埋める命令

		DB		0x55, 0xaa
```

由于软盘可能出现一些奇怪的bug，所以做一个容错机制

将SI寄存器赋值为0,在`retry`中每次执行都给SI+1,并判断是否大于5,如果大于5则跳转到`error`

````
		MOV		SI,0			; 失敗回数を数えるレジスタ
retry:
		MOV		AH,0x02			; AH=0x02 : ディスク読み込み
		MOV		AL,1			; 1セクタ
		MOV		BX,0
		MOV		DL,0x00			; Aドライブ
		INT		0x13			; ディスクBIOS呼び出し
		JNC		fin				; エラーがおきなければfinへ
		ADD		SI,1			; SIに1を足す
		CMP		SI,5			; SIと5を比較
		JAE		error			; SI >= 5 だったらerrorへ
		MOV		AH,0x00
		MOV		DL,0x00			; Aドライブ
		INT		0x13			; ドライブのリセット
		JMP		retry

error:
		MOV		SI,msg
````

然后作者又给出了读到18扇区的代码

```
; ディスクを読む

		MOV		AX,0x0820
		MOV		ES,AX
		MOV		CH,0			; シリンダ0
		MOV		DH,0			; ヘッド0
		MOV		CL,2			; セクタ2
readloop:
		MOV		SI,0			; 失敗回数を数えるレジスタ
retry:
		MOV		AH,0x02			; AH=0x02 :读入磁盘，BIOS INT0x13的参数
		MOV		AL,1			; 1个扇区
		MOV		BX,0
		MOV		DL,0x00			; Aドライブ
		INT		0x13			; ディスクBIOS呼び出し
		JNC		next			; 没出错就儿跳转到next
		ADD		SI,1			; SIに1を足す
		CMP		SI,5			; SIと5を比較
		JAE		error			; 如果SI >= 5跳转到error
		MOV		AH,0x00
		MOV		DL,0x00			; Aドライブ
		INT		0x13			; ドライブのリセット
		JMP		retry
next:
		MOV		AX,ES			; 把内存地址后移0x200
		ADD		AX,0x0020
		MOV		ES,AX			; 再赋值给es,因为es没有add,所以借用一下ax
		ADD		CL,1			; CL+1
		CMP		CL,18			; CLと18を比較
		JBE		readloop		; CL <= 18 だったらreadloopへ
```

新出现的`JBE`是jump if below or equal，小于等于则跳转

关于为什么不用循环，是因为BIOS读盘函数中说明

>指定处理的扇区书，范围在0x01~0xff(指定0x02以上的数值时，要特别注意能够连续处理多个扇区的条件。如果是FD的话，似乎不能跨越多个磁道，也不能超过64kb的限制)

然后再读10个柱面

```
next:
		MOV		AX,ES			; アドレスを0x200進める
		ADD		AX,0x0020
		MOV		ES,AX			; ADD ES,0x020 という命令がないのでこうしている
		ADD		CL,1			; CLに1を足す
		CMP		CL,18			; CLと18を比較
		JBE		readloop		; CL <= 18 だったらreadloopへ
		MOV		CL,1
		ADD		DH,1
		CMP		DH,2
		JB		readloop		; DH < 2 だったらreadloopへ
		MOV		DH,0
		ADD		CH,1
		CMP		CH,CYLS
		JB		readloop		; CH < CYLS だったらreadloopへ
```

这里主要就是在后面添加了如果读到了18,没有跳转到readloop,就重置`CL`寄存器为1,给`DH`寄存器+1代表第二个柱面

开头加了一个

```
CYLS	EQU		10			
```

这里的CYLS类似于C语言中的`#define`定义常量，定义CYLS值为10，`EQU`表示常量

## 着手开发操作系统

`IPL启动区`的开发告一段落，先写一个小程序，功能很简单，就是HLT

```
fin:
	HTL
	JMP fin
```

在这里可以直接用作者给出的makefile,顺便好像发现这个nask编译器貌似是作者自己整得？

## 从启动区启动操作系统

通过十六进制编辑器可以发现hlt的程序位于`0xc200`处，因为启动区将硬盘的内容装载到`0x8000`,所以硬盘`0x4200`处的内容就在`0x8000+0x4200=0xc200`处，所以在hlt程序的文件中加一条`ORG 0xc200`

## 确认操作系统执行情况

调用`INT 0x10`显卡相关参数，切换显卡状态，如果正常则全黑屏

```
MOV		AL,0x13			; VGAグラフィックス、320x200x8bitカラー
MOV		AH,0x00
INT		0x10
```

## 32位的准备和导入C语言

这个地方其实我不想看了，C的编译器是作者自己写的，Main函数叫做`HariMain()`,直接用就可以

32位的准备还是有必要看看的

进入了32位模式后就不可以调用BIOS的方法了，所以在进入32位之前，我们先把需要BIOS做的事情做完

```
; BOOT_INFO
CYLS	EQU		0x0ff0			; 设定启动区
LEDS	EQU		0x0ff1
VMODE	EQU		0x0ff2			; 有关颜色的信息
SCRNX	EQU		0x0ff4			; 分辨率X
SCRNY	EQU		0x0ff6			; 分辨率Y
VRAM	EQU		0x0ff8			; 图像缓冲区开始地址

		ORG		0xc200			; 程序装载位置

		MOV		AL,0x13			; VGA 320x200x8bit
		MOV		AH,0x00
		INT		0x10
		MOV		BYTE [VMODE],8	; 记录画面模式
		MOV		WORD [SCRNX],320
		MOV		WORD [SCRNY],200
		MOV		DWORD [VRAM],0x000a0000

; 获得键盘LED指示灯转台

		MOV		AH,0x02
		INT		0x16 			; keyboard BIOS
		MOV		[LEDS],AL

fin:
		HLT
		JMP		fin
```

