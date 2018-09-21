1. 前例：编译.c
# head thanks*.c
==> thanks_2.c <==
#include <stdio.h>

void thanks_2(void)
{
        printf("Thank you!\n");
}

==> thanks.c <==
#include <stdio.h>

int main(void)
{
        printf("Hello World\n");
        thanks_2();	//调用副程序
}
//gcc -c : 仅将源代码编译成为目标文件，并不制作链接等功能
# gcc -c thanks.c thanks_2.c
# ll thanks*
-rw-r--r--. 1 root root   69 Sep 21 03:54 thanks_2.c
-rw-r--r--. 1 root root 1504 Sep 21 03:54 thanks_2.o
-rw-r--r--. 1 root root   78 Sep 21 03:54 thanks.c
-rw-r--r--. 1 root root 1560 Sep 21 03:54 thanks.o
//多个源代码可能产生多个目标文件（.o）,将这多个目标文件链接制作成为一个binary可执行文件
# gcc -o thanks thanks.o thanks_2.o
# ll thanks*
-rwxr-xr-x. 1 root root 8512 Sep 21 03:57 thanks
-rw-r--r--. 1 root root   69 Sep 21 03:54 thanks_2.c
-rw-r--r--. 1 root root 1504 Sep 21 03:54 thanks_2.o
-rw-r--r--. 1 root root   78 Sep 21 03:54 thanks.c
-rw-r--r--. 1 root root 1560 Sep 21 03:54 thanks.o
# ./thanks
Hello World
Thank you!
注：gcc的参数：
	gcc -c xxx.c	仅将源代码编译成为目标文件，并不制作链接等功能
	gcc -O xx.c -c	在编译的时候，依据作业环境给予最优化执行速度
	gcc sin.c -lm -L/lib -I/usr/include		在进行 binary file 制作时，将链接的函数库与相关的路径填入
		-l : “加入某个函数库（library）”的意思，
		 m : libm.so 这个函数库，其中， lib 与扩展名（.a 或 .so）不需要写
		-L : 函数库的位置（Linux 默认是将函数库放置在 /lib 与 /lib64，
			 如果函数库在这两个目录下，可以省略不写）
		-I ：相关include文件的路径（默认放置在/usr/include下，如果include在这个目录下，可以不写）
	gcc -o		将编译的结果输出成某个特定文件名
	gcc -Wall	在编译的时候，输出较多的讯息说明
	注：通常称 -Wall 或者 -O 这些非必要的参数为旗标 （FLAGS），
		因为我们使用的是C 程序语言，所以有时候也会简称这些旗标为 CFLAGS

2. makefile
# head makefile
thanks: thanks.o thanks_2.o
        gcc -o thanks thanks.o thanks_2.o
# rm -rf thanks thanks.o thanks_2.o
# make	//或者# make thanks
cc    -c -o thanks.o thanks.c
cc    -c -o thanks_2.o thanks_2.c
gcc -o thanks thanks.o thanks_2.o
# ./thanks
Hello World
Thank you!
注：1. makefile中gc之前是一个tab键
	2. 只需要写出binary文件(thanks)需要的目标文件(thanks.o,thanks_2.o),make会自动去判断每个目标文件相关的源代码文件，并直接予以编译，最后在直接进行链接的动作。如果某些源代码更新了，make也可以主动判断出哪一个源代码与相关的目标文件有更新过，并仅更新该文件（仅对有更新的文件进行重新编译）。
	3. Makefile基本规则：
		---------------------------------------------------
		标的（target）: 目标文件1 目标文件2
		<tab> gcc -o 欲创建的可执行文件 目标文件1 目标文件2
		---------------------------------------------------
		在 makefile 当中的 # 代表注解；
		<tab> 需要在命令行 （例如 gcc 这个编译器指令） 的第一个字符；
		标的 （target） 与相依文件（就是目标文件）之间需以“:”隔
	4. 有多个不同的标的时，除了第一个可以省略标的(target)名直接make，执行其他target都需要指定target名：
		thanks: 1.o 2.o
			gcc thanks 1.o 2.o
		clean:
			rm *.o
		# make //执行的是target thanks
		# make clean //加上target名clean才会去执行该target
		# make clean thanks	//先执行clean再执行thanks
	5. 简化Makefile（变量）：
		---------------------------------------------------------------
		# head main.c mysin.c makefile
		==> main.c <==
		#include <stdio.h>
		#define pi 3.14159
		float angle;
		
		int main(void)
		{
		        printf ("\nPlease enter the degree angle (ex>= 90): " );
		        scanf  ("%f", &angle );
		        mysin( angle );
		}
		
		==> mysin.c <==
		#include <stdio.h>
		#include <math.h>
		#define pi 3.14159
		float angle;
		
		void mysin(void)
		{
		        float value;
		        value = sin ( angle / 180. * pi );
		        printf ("\nThe Sin is: %5.2f\n",value);
		
		==> makefile <==
		LIBS = -lm
		OBJS = main.o mysin.o
		main: ${OBJS}
		        gcc -o main ${OBJS} ${LIBS}
		clean:
		        rm -f main ${OBJS}
		# make
		cc    -c -o mysin.o mysin.c
		gcc -o main main.o mysin.o -lm
		# ./main
		
		Please enter the degree angle (ex>= 90): 90
		
		The Sin is:  1.00
		---------------------------------------------------------------
		注：数学函数库使用的是libm.so 这个函数库，编译的时候要将这个函数库纳进去。libm.so 在编译的写法上，使用的是 -lm （lib 简写为 l）。
		
