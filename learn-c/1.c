#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
// 数据输入输出
	int num;	//num用于接收用户输入的选项
//	char *answer1;	//定义一个指针，该指针未被初始化，是个无效的地址，不能直接访问，即不能直接赋值(例如使用scanf)
//	char array[20];	//定义一个字符数组，
	char *answer = NULL;
	printf("sizeof(char)=%d\n", sizeof(char));
	answer = (char *)malloc(20 * sizeof(char));
	/*指针只是一个地址，未分配空间，不能直接赋值，如果预先分配了空间，则可以赋值/*{{{*/
	头文件<malloc.h>和<stdlib.h>都包含了malloc()函数, void *malloc(long numbytes)
	malloc返回的是void *类型指针， C/C++规定，void *类型可以强制转换成任意类型指针
	如果直接answer = malloc(20);则编译时会报错："不能将void *赋值给char *类型变量",所以必须通过(char *)来强制转换
	函数分配numbytes个字节，并返回指向这块内存的指针
	如果分配失败，返回空指针NULL
	malloc分配的内存需要用free函数释放
	void free(void *firstbyte) *//*}}}*/
	if( answer == NULL )
	{
		printf("malloc error, exit.\n");
		exit(1);
	}
	printf("would you like to test what? Reference options:\n\
	1. scanf int\n\
	2. scanf char\n");
	scanf("%d", &num);
	printf("num = %d\n", num);
//	scanf("%s", &answer);	//scanf()搭配%s使用，只能读取一个单词，遇到空格、tab键、换行符等空字符就会返回/*{{{*/
//	gets(answer);
	/*gets()从标准输入读取一行字符，遇到换行符返回，
	gets()不读取'\n',而是将其替换成空字符'\0',作为C语言字符串结束标志
	gets()与puts()配套使用，puts()显示字符串并自动在结尾处加换行标志'\n'
	gets()函数有个严重的缺陷就是不会去检查数组是否能装得下输入行
	比如char array[5];gets(array);如果输入一个大于5个字符,则gets()函数会将前5个字符依次赋值给array，
	但是接下来他就开始访问未被分配的内存空间，如果这块空间内已经有数据，这是程序就会中断报错
	由于gets()的这个缺陷，在C99标准中，gets()被不建议使用，C11开始直接废弃了gets()
	*/
//	fgets(answer, 20, stdin);
	/*C11标准新增了gets_s()函数可以代替gets()函数，但是该函数是stdio.h输入输出函数系类中的可选扩展，
	因此，即使编译器支持C11标准，也有可能不支持gets_s()函数。
	可以用c语言中的fgets()函数来代替gets()
	char *fgets(char *buf, int bufsize, FILE *stream);
	bufsize ：限制读取字符个数为：bufsize, 最后一个字符可以是'\n'
	与gets()不同的是，fgets()会读取换行符，之后在buf末尾添加一个空字符作为字符串结束符
	fgets()与fputs()配套使用，fputs()不会自动添加换行，
	但是如果你在fgets()中最后一个字符为'\n',因为fgets()会读取'\n'，所以fputs()的输出结果中就有'\n'
	*/
//	printf("answer=");
//	fputs(answer, stdout);
//	if( !strcmp(answer,"scanf int\n") )	//C语言字符串对比只能用strcmp()函数，头文件为<string.h>
										//因为我给answer指针分配了20个字节，所以一定能读到'\n'/*}}}*/
//	if( !(num - 1) )	//判断两个整数是否相等的办法：if( !(a - b) ) ; !(a ^ b)
	/*按位与：&
		0&0=0;   0&1=0;    1&0=0;     1&1=1;	//只要有一个为0结果就为0
	按位或：|
		0|0=0；   0|1=1；   1|0=1；    1|1=1；	//只要有一个为1结果就为1
	按位异或：^
		0^0=0；   0^1=1；   1^0=1；   1^1=0；	//相等为0，不等为1
	负数按补码形式参与按位运算
		
	按位取反：~
		~1=0；   ~0=1；
	左移：<<
		将一个运算对象的各二进制位全部左移若干位（左边的二进制位丢弃，右边补0）
		若左移时舍弃的高位不包含1，则每左移一位，相当于该数乘以2
	右移：>>
		将一个数的各二进制位全部右移若干位，正数左补0，负数左补1，右边丢弃
		操作数每右移一位，相当于该数除以2
	无符号右移：>>>
		右移后左边空出的位用零来填充。移出右边的位被丢弃
		var temp = -14 >>> 2
		变量 temp 的值为 -14 （即二进制的 11111111 11111111 11111111 11110010），
		向右移两位后等于 1073741820 （即二进制的 00111111 11111111 11111111 11111100）
	原码、反码、补码：
		机器数：一个数在计算机中的二进制表示形式，机器数是带符号的，
				在计算机中用一个数的最高位存放符号，正数为0，负数为1
				例：十进制数 +3 ，计算机字长为8位，转换成二进制就是；0000 0011，
					十进制数 -3 ，转换成二级制就是：1000 0011
		真值：	将带符号位的机器数对应的真正数值称为机器数的真值
				0000 0001 真值 = +000 0001 = +1
				1000 0001 真值 = -000 0001 = -1
		原码：	符号位加上真值的绝对值
				[+1]原码 = 0000 0001
				[-1]原码 = 1000 0001
				因为第一位是符号位，所以8位2进制数的取值范围：
				[1111 1111, 0111 1111] 即 [-127, 127]
		反码：	正数的反码是其本身
				负数的反码是在其原码的基础上，符号位不变，其余各个位取反
				[+1] = [0000 0001]原 = [0000 0001]反
				[-1] = [1000 0001]原 = [1111 1110]反
		补码:	正数的补码是其本身
				负数的补码是在其原码的基础上，符号位不变，其余各个位取反，最后+1
				即负数的补码是其反码+1
				[+1] = [0000 0001]原 = [0000 0001]反 = [0000 0001]补
				[-1] = [1000 0001]原 = [1111 1110]反 = [1111 1111]补
	*/
	if( !(num ^ 1) )
	{
		printf("your choice is: scanf int\n");
    	int a, b;
    	printf("please input a=%%d,b=%%d with space ,\n");
    	scanf("%d,%d", &a, &b);	/*scanf(格式控制, 地址列表); 格式控制中如果没有指定间隔符，
    							则默认以空格、tab键、回车符作为间隔符，
    							如果指定了(比如这里的逗号)，则输入数据必须以该符号作为间隔符*/
    	printf("a=%d, b=%d\n", a, b);
    	/*/*{{{*/
    	 * scanf格式字符：
    		d,i :有符号十进制整数
    		u :	无符号十进制整数
    		o :	无符号八进制整数(键入数据时不能出现8及其以上的数字，否则会出错)，
    			键入的数据可不必加前缀0
    		x,X :无符号十六进制整数(不区分大小写),键入的数据可不必加前缀0x
    		c :	单个字符
    		s :	字符串，将字符串送入一个字符数组中，以空格字符为字符串结束标志
    			字符串末尾自动添加"\0"作为字符串结束标志
    		f :	实数(float, double),支持小数或指数形式的输入
    		e,E,g,G :与f作用相同，可相互替换
    	 * scanf格式修饰符
    	 	l :	长整型(%ld, %lo, %lx), double型(%lf或%le)
    		h :	短整型(%hd, %ho, %hx)
    		域宽 :指定输入数据所占宽度(列数)，系统会自动截取，域宽应为正整数
    		* :	跳过该输入值(本输入项不会被赋值给相应的变量)，称为 禁止赋值符
    	*//*}}}*/
    	printf("please input a=%%3d b=%%5d\n");	//%%转义
    	scanf("%3d%5d", &a, &b);
    	printf("--output a=%%5d, b=%%2d : a=%5d, b=%2d--\n", a, b);
    	
    	printf("please input a=%%*d\n");
    	scanf("%*d", &a);
    	printf("a=%d\n", a);
	}
//	else if( !strcmp(answer,"scanf char\n") )
	else if( !(num - 2) )
	{
		printf("your choice is: scanf char\n");
		char c;
		printf("please input a char c=%%3c\n");
		scanf("%3c", &c);
		printf("c=%3c\n", c);
	}
	else
	{
		printf("not in map.\n");
	}

	free(answer);
	return 0;
}
