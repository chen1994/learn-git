#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
第一行告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释
第二行告诉Python解释器，按照utf-8编码读取源代码，使中文等字符不乱码
coding : 声明编码格式，如果脚本中出现中文（哪怕是在注释中），也需要声明编码格式为：utf-8或gbk,
如果不声明，则Python默认会使用ASKII码来保存脚本，此时代码中出现中文的话，执行时就会出错
这个声明还可以写成如下：
#coding=utf-8
'''
#Python官网: https://docs.python.org/3/

【python2.7升级Python3】
'''
https://www.cnblogs.com/Cherry-Linux/p/7553580.html
make install时有如下错误：
zipimport.ZipImportError: can't decompress data; zlib not available
解决办法：
1. 首先安装zlib:
    # yum install -y zlib*
2. 修改modules内的setup文件
取消如下行的注释：
#zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz
'''
【修改默认Python版本】
'''
python3比起Python2来，并不好用,上面安装好Python3后，将/usr/bin/python修改成了/usr/local/python3.6.0
所以要改回Python2.7就需要删除这个软连接，将/usr/lib/python重新连接到python2:
# python -V
Python 3.6.0
# ls -l /usr/bin/python
lrwxrwxrwx. 1 root root 34 Jun  5 01:16 /usr/bin/python -> /usr/local/python3.6.0/bin/python3
# rm -rf /usr/bin/python
# ln -s python2 /usr/bin/python
# ls -l /usr/bin/python
lrwxrwxrwx. 1 root root 7 Jun  5 02:47 /usr/bin/python -> python2
# python -V
Python 2.7.5
'''

#raw_input()从命令行读取用户输入
input = raw_input('test input. please input anython words:')
#print 遇到逗号会输出一个空格
print 'output your input:', input

#当语句以冒号“:”结尾时，缩进的语句视为代码块
'''定义一个变量a并赋值'haha' 的过程Python的操作是：
1. 在内存中创建字符串'haha'
2. 在内存中创建变量a，并将它指向'haha'
如果再将变量a赋值给变量b，Python的操作是将变量b指向变量a所指向的数据'''

#使用转义字符
print "i\'m ctt"
# r'' 表示引号内的字符默认不转义
print r"i'm ctt"
# '''...''' 格式表示多行内容
print '''ha
ha'''

#python中使用全部大写的变量名来表示常量
PI=3.14159265359
#整数的运算结果永远是整数，比方说4/3=1

【字符编码】：
'''
1. ASCII编码只有一个字节，用来处理中文至少要两个字节，所以不能用ASCII编码来表示中文
2. 中国制定了GB2312编码，用来编译中文
3. Unicode编码实现将全世界所有语言都统一到一套编码里，使多种语言放在一起不会出现乱码问题
字母A用ASCII编码：十进制是 65 ，二进制是 01000001
汉字中SCII编码的范围，用Unicode编码：十进制是 20013 ，二进制是01001110 00101101
字母A用Unicode编码只要在前面补0就行：00000000 01000001
4. 如果文本中基本上全是英文，使用比ASCII多一倍存储空间的Unicode，在存储和传输上十分不划算
5. 本着节约精神，出现了可变长编码的utf-8编码，他可以将Unicode字符根据不同的数字大小编码成1-6个字节，
比方说英文字母是1个字节，汉字是3个字节，只有很生僻的字符才会被编译成4-6个字节：
------------------------------------------------------------------
字符    ASCII       Unicode             UTF-8
A       01000001    00000000 01000001   01000001
中      x           01001110 00101101   11100100 10111000 10101101
------------------------------------------------------------------
6. 计算机系统通用的字符编码工作方式：
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
例如很多网页的源码上会有类似<meta charset="UTF-8" />的信息，表示该网页正是用的UTF-8编码
7. python的诞生比Unicode标准发布的时间要早，所以最早的Python只支持ASCII编码。
Python提供了ord()和chr()函数将字母和对应的数字进行转换
8. python后来添加了对Unicode的支持，用 u'...' 来表示Unicode字符
9. u'...'只能表示Unicode编码，使用 encode('utf-8') 将Unicode转换成utf-8
10. 使用len()函数返回字符串的长度
11. 使用decode('utf-8')将utf-8转换成Unicode
'''
print r"ord('A'),chr(65) : ",ord('A'),chr(65)
print r"u'中' : ",u'中'
print r"encode() : ",u'中'.encode('utf-8')
print r"len() : ",len(u'中'),len(u'中'.encode('utf-8'))
print r"decode() : ",'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

【格式化字符串】:
'''
使用%运算符来格式化字符串：
-------------------
占位符  字符串类型
%d      整数
%f      浮点数
%s      字符串
%x      十六进制整数
-------------------
'''
print r'% : ','-%2d-%03d-' % (3, 1),'-%.2f-' % 3.14159
#%字符使用%来转义,在格式化字符串时，如果不使用r'...'来输出%符号，就必须用%%来转义，不能用\%来转义（会报错）
print '-%%-%d' % 2
#b'...'以字节形式表示的字符串
print b'haha'

【列表】:
'''
list是Python内置的一种数据类型，list是一种有序的集合，可以随时添加删除其中的元素,list中元素的数据类型可以不同
'''
class1 = ['wang', 'wu']
print "====== list ======\n",class1,len(class1)
print class1[0],class1[1]
#取list中最后一个元素,倒数第二个元素
print class1[-1],class1[-2]
#追加元素到列表末尾
class1.append('ctt')
#在指定位置插入元素,例如索引号为1的位置
class1.insert(1,'li')
#删除list末尾的元素
class1.pop()
#删除指定索引位置的元素
class1.pop(0)
#list中的元素也可以是另一个list,如下例中的school包含class1，所以school也相当于一个二维数组
school = ['grade', class1, 'classmates']

【 元祖】：
'''
另一种有序列表叫 元祖 ：tuple，和list不同的是：tuple一旦初始化就不能修改,不可修改的tuple对于代码来说更加安全，所以能使用tuple就尽量不要使用list
class1 = ('A', 'B', 'C')
#定义一个空的tuple
class1 = ()
#只有一个元素的tuple,元素后面一定要加逗号，不然(1)既可以表示tuple，也可以表示数学公式中的1，按Python的规定，会优先按小括号进行计算，计算结果是1
class1 = (1,)
#“可变的”tuple,下例中的tuple class1中的第三个元素是一个list，我们修改list中元素的值，并不会改变tuple指向的list
class1 = ('A', 'B', ['C', 'D'])
class1[2][0] = 'X'
print "====== tuple ======\n",class1
'''

【条件判断】：
'''
if x:
    只要x是非零值、非空字符串、非空list等，就判定为True，否则为False
elif x:
else:
print "====== 条件判断 ======"
age = 3
if age >= 18:
    print "you are %d years old." % age,"so you are already a adult."
elif age >= 6:
    print "you are %d years old." % age,"you are a teenager."
else:
    print "you are only %d years old." % age,"so you are still a kid."
'''

【循环】：
'''
for x in y:
===========
while x:
A = (1, 2, 3)
sum = 0
for num in A:
    sum += num
print "====== 循环 ======\n",'sum = ',sum
#使用 range() 函数生成一个整数序列
for x in range(6):
    sum += x
print 'sum = ',sum

x = 3
while x > 0:
    x -= 1
print 'x = ',x

!!!使用 raw_input() 函数从命令行读取的输入内容永远是以字符串的形式返回，
所以如果用在整数判断相关的场合不能直接使用raw_input()， 需要使用 int() 将字符串转换为整数后在进行计算或判断
#num = int(raw_input('please input a number:'))
'''

【字典】：
'''
dict全程dictionary,其他语言中也称为map，使用键-值(key-value)存储，具有极快的查找速度
dict比list的查找和插入的速度快，且不会随着key的增加而增加（dict内部的存放顺序和key的放入顺序是没有关系的
但是dict需要占用大量的内存，内存浪费多。而list占用空间小，内存浪费少
所以dict是用空间换时间的一种方法，适用于需要告诉查找的场合
注意：dict中的key值必须是不可变对象，因为dict是根据key值来计算value的存储位置的，这个算法就是哈希算法(hash)
dict = {'A':1, 'B':2, 'C':3}
print "====== dict ======\n",'dict : ',dict['A']
dict['A'] = 0
print 'dict : ',dict['A']
#对dict中的key进行赋值的时候，首先要确认key是存在的，否则会报错，使用如下方法确认key存在,如果key存在，则返回key对应的value，不存在则返回None或者自己指定的值
dict.get('A', -1)
#删除key
dict.pop('B')
print dict
'''

set
'''
和dict类似，set也是一组key的集合，但是不存储value，由于key是不能重复的，所以set中没有重复的key,
重复的元素在set中会被自动过滤掉，所以set可以用来做数学意义上的交集、并集
set和dict一样，key都必须是不可变对象，否则无法判断两个可变对象是否相等，也无法保证set内没有重复元素
s1 = set([1,1,2,3,4,4])
print "====== set ======\ns1 : ",s1
#添加删除元素
s1.add(5)
print "add 5 : ",s1
s1.remove(1)
print "remove 1 : ",s1
#交并集
s2 = set([1,2,6,7])
print "s2 : ",s2
s = s1 & s2
print "s1 & s2 : ",s
s = s1 | s2
print "s1 | s2 : ",s
'''

【函数】：
'''
比方说求圆的面积：数学上：s = πr²，在Python里面就专门有个函数用来求圆的面积：s = area_of_circle(r),这样的函数就类似于数学上的公式
求绝对值：abs(x)
比较大小：cmp(x, y)
数据类型转换函数：int(), float(), str(), unicode(), bool()
'''

【函数别名】：
'''
函数名就是指向一个函数对象的引用，所以可以把函数名赋给一个变量，实现给函数别名：
a = abs
print a(-1) 输出的就是1，相当于通过a调用abs,实际执行的是abs(-1)

【定义函数】：
-------------
def func(x):
    ....
    return x
-------------
函数的返回值用return返回，如果没有return语句，函数也会返回一个None，"return None"可以简写为"return"
'''

【空函数】：
'''
如果想定义一个什么都不做的函数，可以使用"pass"语句，pass相当于放置了一个占位符
-------------
def nop():
    pass
-------------
pass还可以用在其他语句里，用于还没想好写什么样的代码，但是要先让程序运行起来：
-------------
if a > 10:
    pass
-------------
这里如果不写pass就会有语法错误
'''

【函数参数检查】：
'''
Python解释器只对内置的函数进行参数检查，而自定义的函数没有，所以我们可以自己对函数参数类型进行检查:
---------------------------------------------
def func(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    ....
---------------------------------------------
上例的意思是：检查参数x，如果x不是整数或浮点数，就报错
'''

【返回多个值】：
'''
Python支持函数返回多个值
--------------------------------------------------------------------------
游戏中经常需要从一个点移动到另一个点，给出坐标、位移、角度，计算出新坐标：
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y
--------------------------------------------------------------------------
注： 函数参数中"angle=0"是给第四个参数angle设定了一个默认值0
表面上看起来函数确实是返回了多个值，但是实际上是返回的一个tuple。
语法上返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋值
>>> r = move(100, 100, 60, math.pi / 6)
>>> print r
(151.96152422706632, 70.0)
'''

【函数的参数】：
【【1.默认参数】】：
'''
上例中有设置一个默认参数angle，设置默认参数可以简化函数的调用，设置默认参数时有以下几点要注意：
1. 必选参数在前，默认参数在后，否则Python解释器会报错（想一下都知道为什么啦，默认参数在前，你不写，谁知道你第二个参数是赋给第一个还是第二个）
2. 当函数有多个参数时，把变化大的参数放在前面，变化小的放在后面，变化小的参数就可以作为默认参数。
如果有多个默认参数，在传参时只修改个别默认值，需如下处理：
-------------------------------------------------
def enroll(name, gender, age=6, city='Beijing'):
    print name
enroll('Liu', 'M', city='Nanjing')
-------------------------------------------------
这样调用时，age取默认值
注意：默认参数必须指向不变的对象，比方说如果用一个列表来做默认参数，那么函数在定义的时候，记住的是该列表的地址，一旦列表的内容变更，那默认参数的值虽然没有变仍然是这个列表，但是他指向的内容却变了，这样就会导致意想不到的错误
使用不便对象做默认参数，除了可以防止由于修改数据导致的错误，还有一个优点就是：
由于对象不变，多任务环境下同时读取对象不需要加锁
'''

【【2.可变参数】】：
'''
比如我们需要设计个函数用来计算一组数字的和，可以传入一个list或者tuple，在函数里面用for循环去遍历：
---------------------------
def calc(nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum
#这样调用的时候就得传入一个list或者tuple
calc([1, 2, 3])
calc((1, 2, 3))
---------------------------
但是这样比较繁琐，所以就可以使用可变参数，可变参数在函数内部自动组装为一个tuple，简化函数调用：
---------------------------
def calc(*nums):
    ...同上
#这样调用时就可以直接有多少参数就直接传，0个就为空
calc(1, 2, 3)
calc()
---------------------------
传参的时候也可以传递可变参数：
-----------------
#如果要传递的参数是一个list或者tuple：
list = [1, 2, 3]
#如下这样传参就很繁琐：
calc(list[0], list[1], list[2])
calc(*list)
-----------------
'''

【【3.关键字参数】】:
'''
关键字参数允许传入0个或任意多个key-value组合的参数，他们在函数内部自动组装为一个dict：
---------------------------------------------------
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
print person('Li', 30)
#输出为： name: Li age: 30 other: {}
print person('Li', 30, city='Beijing')
#输出为：name: Li age: 30 other: {'city': 'Beijing'}
#和可变参数类似，也可以组装出一个dict再传入：
kw = {'city': 'Beijing', 'job': 'IT'}
person('Li', 30, **kw)
---------------------------------------------------
关键字参数的作用是可以扩展函数的功能，person函数里能保证收到name和age这两个参数，
这种功能可以应用在网页中比方name和age是必选项，其他是可选项
'''

【【4.参数顺序】】：
'''
以上四种参数可以一起使用，但是注意参数定义的顺序必须是：必选参数、默认参数、可变参数、关键字参数
--------------------------------------------------------------------------------------------
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)  #输出是：a = 1 b = 2 c = 0 args = () kw = {}
func(1, 2, 3, 'a', 'b', x=99)   #输出是：a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
#还可以传入tuple和dict:
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)   #输出是：a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
--------------------------------------------------------------------------------------------
注意：默认参数一定要是不可变对象
*args是可变参数，接收的是一个tuple
**kw是关键字参数，接收的是一个dict
'''

【【5.递归函数】】：
'''
在函数内部调用自身的函数就是递归函数
例如，计算阶乘：n! = 1 * 2 * 3 * ... * n
用函数表示：
---------------------------
def fact(n):
    if n = 1:
        return 1
    return n * fact(n - 1)
---------------------------
使用递归函数需要注意：不能递归太多次，防止栈溢出。
因为计算机中所有的函数调用都是通过栈(stack)这种数据结构来实现的。
堆栈访问效率高，速度快，但是空间有限。
栈的I/O顺序是先进后出，所以每进入一次函数调用，栈就会加一层栈帧，
每当函数返回，栈就会减一层栈帧
而栈的大小是系统控制的，无法改变（操作系统分配给一个进程的栈空间是2M,堆空间在32位机器上是4G）
每调用一个函数，在这个函数执行前都会先将函数的代码地址（调用点）入栈，
等被调用的函数执行完再地址出栈，程序才能根据这个数据返回调用点，
所以如果递归调用次数太多，却还没有到达结束条件，就会只入栈不出栈，栈就会被压爆，此为栈溢出
上述阶乘递归函数计算过程如下：
==> fact(3)
==> 3 * fact(2)
==> 3 * fact(2 * fact(1))
==> 3 * fact(2 * 1)
==> 3 * 2
==> 6
比方说上述阶乘函数：fact(1000)就会栈溢出了

对于支持尾递归优化的编程语言来说，可以使用尾递归来防止栈溢出
虽然Python标准的解释器没有针对尾递归做优化，也就是说就算使用尾递归，在Python中还是会溢出
但这里我们还是科普一下什么是尾递归：
'''
【【尾递归】】：
'''
尾递归是指，在函数返回时调用自身，并且return语句中 不能包含表达式，
这样编译器或Python解释器就会将尾递归做优化，
无论递归本身调用多少次，都只占用一个栈帧，就不会栈溢出了
上面的return时引入了乘法表达式，比能算递归，使用尾递归改成如下：
----------------------------------------------
def fact(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
----------------------------------------------
return时调用函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用
上述阶乘尾递归函数计算过程如下：
fact(3)对应的fact_iter(3, 1)
==> fact_iter(3, 1)
==> fact(2, 3)
==> fact(1, 6)
==> 6
'''

【切片】：
'''
Python提供切片(slice)操作符，来简化从一个list或者tuple中提取部分元素的操作（其他很多编程语言都使用截取函数来实现）：
-----------------------------------
L = [1, 2, 3, 4, 5, 6]
print L[0:2]    #第一个索引是0可以省略，写为L[:2],
                #表示从索引0开始取，到索引2为止，但不包括索引2，
                #输出为：[1, 2]
-----------------------------------
取倒数第1个元素：L[-1],取后三个元素：L[-3:]
取前4个数中的奇数（每两个取一个：L[:4:2]    输出为：[1, 3]
取所有的奇数：L[::2]    输出为：[1, 4, 5]
复制一个list: L[:]
list切片操作的结果是一个list，tuple切片操作的结果也是一个tuple
字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list进行切片操作，只是操作结果仍然是字符串
'''

【迭代】：
'''
使用for循环来遍历list或tuple或其他可迭代对象的操作称为迭代
Python中的迭代是通过for...in来实现的，例如C或者Java等语言都是通过下标来完成迭代
Python的迭代，无论有无下标都可以实现：
---------------------------
#迭代dict
d = {'a':1, 'b':2}
for key in d:
    print key   #输出为：a
                         b
---------------------------

如何判断一个对象是可迭代对象：通过collections模块的Iterable类型判断：
-----------------------------------------
from collections import Iterable
isinstance('abc', Iterable) #输出为True
isinstance(123, Iterable)   #输出为False
-----------------------------------------

如果要对list实现类似C语言的下标循环，可以使用Python内置的enumerate函数将一个list变成'索引-元素对'
#在for循环中同时迭代索引和元素本身：
---------------------------------------
for i, value in enumerate(['A', 'B']):
    print i, value
#输出为：0 A
         1 B
---------------------------------------
在for循环里可以同时引用两个变量：
-----------------------------
for x, y in [(1, 1), (2, 4)]:
    pritn x, y
#输出为：1 1
         2 4
-----------------------------
'''

【列表生成式】：
'''
列表生成式即List Comprehensions,是Python内置的非常简单却强大的可以用来创建list的生成式
---------------------------------------------------
#生成list[1, 2, 3, 4]：
range(1, 5)
#生成list[1*1, 2*2, 3*3]:
#方法一：循环
L = []
for x in range(1, 5):
    L.append(x * x)
#循环就比较繁琐，使用列表生成式一行语句就可以代替：
[x * x for x in range(1, 5)]
#两层循环：
[m + n for m in 'AB' for n in 'XY']
#输出为：['AX', 'AY', 'BX', 'BY']
#三层和三层以上的循环很少用到
---------------------------------------------------

例1：列出当前目录下所有文件和目录名：
----------------------------------------------------------------------------
import os   #导入os模块
[d for d in os.listdir('.')]    #os.listdir可以列出文件和目录(包括隐藏文件)
----------------------------------------------------------------------------

例2：迭代dict：
----------------------------------------------------------------------------------
d = {'x':1, 'y':2}
方法一：迭代
for k, v in d.iteritems():
    print k, '=', v
#输出为：y = 2
         x = 1  #因为dict本身在内存中的存放是没有顺序的，所以取出来的时候是乱序的
方法二：列表生成式
[k + '=' + v for k, v in d.iteritems()]
#输出为一个list：['y=2', 'x=1']
----------------------------------------------------------------------------------

例3：将一个list中所有字符串变成小写
--------------------------
L = ['Hello', 'World']
[s.lower() for s in L]
#输出为： ['hello', 'world']
--------------------------
'''

【生成器】：
'''
受到内存的限制，列表的容量是有限的，如果我们要创建一个100万个元素的列表，但是每次就只需要访问其中的几个元素，那直接用列表生成式创建出来是很浪费存储空间的，甚至会内存告急而出错
Python中提供一种叫做生成器(Generator)的机制，可以将列表元素通过某种算法推算出来，一边循环一边推算：
创建generator有很多种方法：
-----------------------------------------------------------------------------------------
方法一：将列表生成式的[]改成()
l = [x * x for x in range(2)]   #使用列表生成式，生成的是完整的列表：[0, 1]
g = (x * x for x in range(2))   #将[]改成()，生成的是一个generator
print g #输出是：<generator object <genexpr> at 0x104feab40>
#打印出generator中的每一个元素
print g.next()  #输出是: 0
print g.next()  #输出是：1
print g.next()  #到这里会报错：StopIteration
                #表示已经遍历到最后一个元素没有下一个了
#由于generator保存的是算法，所以每次调用next()，就会计算出下一个元素的值，直到最后一个
#这种不断调用next()的方法太垃圾了，一般人都不会使用，
#正确的方法是使用for循环，因为generator也是可迭代对象：
for n in g:
    print n #输出是：0
                     1
-----------------------------------------------------------------------------------------

-------------------------------------------------------------------------------
方法二：函数
如果推算的算法比较复杂，无法用类似列表生成式的for循环实现的时候，可以使用函数：
例：斐波拉契数列(Fibonacci):除前两个数外，任意一个数都可由前两个数相加得到：
函数的实现如下：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n +1
fib(4)    #输出为：1
                   1
                   2
                   3
要将函数变成generator，只需要把'print b'改成'yield b'就行了：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print fib(4)  #输出为：<generator ibject fib at 0x7f2684861b40>
for n in fib(4):
    print n #输出为：1
                     1
                     2
                     3

只要一个函数中包含'yield'关键字，那这个函数就不再是一个普通的函数，而是一个generator
generator和函数的执行流程不一样，函数是顺序执行遇到return语句或者最后一行函数语句就返回
而变成generator的函数，则是在每次调用next()的时候执行，一遇到yield语句就返回，下次执行的时候直接从上次返回的yield语句处继续往下执行：
def odd():
    print 'p1'
    yield 'y1'
    print 'p2'
    yield 'y2'
for n in odd():
    print n
#输出为：p1
         y1
         p2
         y2
-------------------------------------------------------------------------------
'''

【高阶函数】：
'''
可以接收另一个函数作为参数的函数称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)
print add(-5, 6, abs)   #abs为求绝对值的函数，输出为：11
'''

【【map/reduce】】：
'''
map()函数接收两个参数：函数，序列。
map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
例1：有个函数f(x)=x²，要将这个函数作用在一个list[1, 2, 3]上,使用map()实现如下：
def f(x):
    return x * x
print map(f, [1, 2, 3]) #输出是：[1, 4, 9]
例2：将list中所有数字转换为字符串：
print map(str, [1, 2, 3]) #输出为：['1', '2', '3']

reduce()函数接收两个参数：函数，序列。
reduce将结果和序列的下一个元素做累积计算，效果如下：
reduce(f, [x, y, z]) = f(f(x, y), z)
例1：将list[1, 2, 3]变成整数123：
def fn(x, y):
    return x * 10 + y
print reduce(fn, [1, 2, 3]) #输出为：123
'''

【【filter】】：
'''
Python内置filter()函数用于过滤序列，接收两个参数：函数，序列
filter将传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
例1：过滤出奇数：
def is_odd(n):
    return n % 2 == 1
print filter(is_odd, [1, 2, 3, 4, 5, 6])    #输出为：[1, 3, 5]
例2：删除list中的空字符串：
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['A', '', ' ', None, 'B'])  #输出为：['A', 'B']
所以，要使用filter()这个高阶函数，关键在于正确实现一个‘筛选’函数
'''

【【排序算法】】：
'''
1. 使用sorted()函数
例1：正序
print sorted([1, 5, 7, 3, 5])   #输出为：[1, 3, 5, 5, 7]
例2：倒序
sorted()是一个高阶函数，所以他还可以接收一个比较函数来实现自定义的排序，例如倒序：
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([8, 3, 6, 1, 10], reversed_cmp)    #输出为：[10, 8, 6, 3, 1]
例3：忽略大小写比较字符串
sorted()对字符串排序，默认是按照ASCII的大小来比较的，比如'Z' < 'a',这样的结果是我们不想看到的
def cmp_ignore_case(s1, s2):
    u1 = s1.upper() #都改成大写（或者小写）
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Aha'], cmp_ignore_case)
#输出为：['about', 'Aha', 'bob', 'Zoo']
'''

【【函数作为返回值】】：
'''
在一个函数中再定义一个内部函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
当调用函数lazy_sum()时，返回的不是求和结果，而是求和函数sum()
f = lazy_sum(1, 2, 3, 4)
当调用函数f()时才真正计算求和结果：
f()
内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum，相关参数和变量都保存在返回的函数中，这种称为“闭包(Closure)”
注意：每次调用lazy_sum()时返回的都是一个新的函数，即使传入的参数相同
'''

【【闭包】】：
'''
使用闭包的时候要注意，返回函数中不要引用任何循环变量：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count
f1()
f2()
f3()

f1(),f2(),f3()的返回结果都是9，而不是1,4,9，这是因为返回的函数引用了循环变量i，但它并非立刻执行，而是等到3个函数都返回时，它的值已经变成了3
如果一定要引用循环变量，可以使用如下方法，再创建一个函数，该函数的参数绑定循环变量当前的值：
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) #f(i)是立刻执行的，此时i的当前值就会被传入f()
    return fs
f1()    #1
f2()    #4
f3()    #9
例：利用闭包返回一个计数器函数，每次调用他返回递增的整数：
def createCounter():
    def counter():
        return 1
    return counter
counterA = createCounter()
if [counterA(), counterA(), counterA()] == [1, 2, 3]:
    print('测试通过！')
else:
    print('测试失败！')
'''

【【传入匿名函数】】：
'''
list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
这里的匿名函数：lambda x: x * x实际上就是
def f(x):
    return x * x
lambda为匿名函数关键字，冒号前面的x表示函数参数。
匿名函数有个限制就是只能有一个表达式，不用写return，返回值就是该表达式的结果
匿名函数没有名字，所以不存在函数名冲突的问题。
匿名函数也是一个函数对象，所以可以将匿名函数赋值给一个变量，再通过变量来调用该函数
f = lambda x: x * x
f(5)    #25
匿名函数作为返回值返回：
def build(x, y):
    return lambda: x * x + y * y
'''

【装饰器】：
'''
函数对象有一个__name__属性，用于获取函数名
def now():
    print('haha')
f = now
f.__name__  #now
装饰器也叫做包装器。即对一个既有的函数func(args),在调用它之前和之后，我们都希望做一些事，将这个函数包装起来。
python中的装饰器分为两类：函数装饰器和类装饰器
'''

【【函数装饰器】】：
'''
1. 不带参数的decorator
def decorator1(func):
    def dec(*args):
        print 'pre action'
        result = func(*args)
        print 'post action'
        return result
    return dec

@decorator1
def test_fun(name):
    print name
    return None

test_fun('name1')   #输出为：   pre action
                    #           name1
                    #           post action
这种现象的内部原理：
@decorator1
def test_fun(name):
这两行在Python内部相当于 test_fun = decorator(test_fun)
即将test_fun作为参数传递给func之后test_fun就是装饰其中的dec函数对象了，而不是原来的函数名称，当调用test_fun('name1')时，实际上调用的是dec('name1')函数，而在dec函数内部，又调用了func,这样就造成了装饰器的效果

2. 带参数的decorator
def wap(name):
    def decorator1(func):
        def dec(*args):
            print name
            print 'pre action'
            result = func(*args)
            print 'post action'
            return result
        return dec
    return decorator1

@wap('heihei')
def test_fun(name):
    print name
    return None

test_fun('name1')   #输出为：   heihei
                    #           pre action
                    #           name1
                    #           post action
这种现象的内部原理：
@wap('heihei')
def test_fun(name):
这两行的内部逻辑为：test_fun = wap('heihei')(test_fun)
这里wap('heihei')返回的是的decorator1函数对象，所以wap('heihei')(test_fun)实际上就是decorator1(test_fun),到这里接下来就和上面不带参数的装饰器原理一样了。
与带参数的装饰器不同的是，这里我们传递了一个参数’heihei'进入decorator内部。使得我们可以操作这个参数
'''
【【函数decorator修饰类成员函数】】：
'''
class F00:
    @decorator1
    def fun(self):
        print self.name
'''
【【函数decorator的叠加】】：
'''
def decorator1(func):
    ... #同上不带参数的decorator
def decorator2(func):
    ... #同上不带参数的decorator

@decorator1
@decorator2
def test(name):
    print name

test('test')    #输出为：   (decorator1)pre action
                            (decorator2)pre action
                            test
                            (decorator1)post action
                            (decorator2)post action
原理：
test = decorator1(decorator2(test))
注意：decorator1(decorator2(test))，不是说先执行decorator2(test),而是把decorator2(test)作为参数，最先执行decorator1，再执行decorator2.
'''

【偏函数】：
'''
Python的functools模块提供了很多有用的功能，其中一个就是偏函数，和数学意义上的偏函数不一样。
当函数的参数个数太多，需要简化是，使用 functools.partial 可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
之前有通过设定参数的默认值，可以简化函数调用，偏函数也能做到这一点：
int()函数默认按十进制将字符串转换为整数：
int('12345')    #12345
int()函数还提供额外的base参数，默认值为10.传入base参数可以做N进制的转换：
int('12345', base=8)    #5349
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
此时就可以定义一个int2()函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)
int2('1000000') #64

functools.partial 就是帮助我们创建一个偏函数，而不需要我们自己定义int2()：
import functools
int2(functools.partial(int, base=2))
int2('1000000') #64
这里 functools.partial实现的就是将函数int()的base值固定为2，然后返回一个新函数int2()
注意int2()只是将base参数重新设定默认值为2，也可以在函数调用时传入其他值：
int2('1000000', base=10)    #1000000

在创建偏函数时，可以接收函数对象、*args、**kw 这3个参数：
int2 = functools.partial(int, base=2)
int2('10010')
相当于：
kw = {'base': 2}
int('10010', **kw)
当调用：
max2 = functools.partial(max, 10)
max2(5, 6, 7)
实际上会将10 作为*args的一部分自动加到左边
相当于：
args = (10, 5, 6, 7)
max(*args)  #最大值为10
'''

【模块】：
'''
为了提高代码的可维护性，会将很多函数分组，分别放到不同的文件里，这样每个文件的代码就相对较少
这种组织代码的方式，在Python中，一个.py文件就称之为一个模块(Module)
使用模块除了大大提高代码的可维护性和方便引用外，还可以避免函数名和变量名的冲突（相同名字的函数和变量完全可以分别存在不同的模块中），但还是要注意不要与内置函数名冲突,否则将无法导入系统自带的这些模块
Python的所有内置函数参见：
检查系统是否已经存在该模块：在Python交互环境执行：>>>import abc,若成功则说明系统存在该模块

为了避免模块名冲突，Python引入了按照目录来组织模块的方法，称为包（Package）
例：
mycompany
├─ __init__.py
└─ abc.py
只需要保证顶层包名mycompany不与别人冲突，里面的所有模块就不会与别人冲突。
abc.py模块名就变成了mycompany.abc
注意：每个包目录下都必须有一个__init__.py文件。
如果没有__init__.py文件。Python会将该目录识别成一个普通目录，而不是一个包
__init__.py可以是一个空文件，也可以包含Python代码，因为__init__.py本身就是一个模块，模块名为mycompany
类似的，可以有多级目录，组成多级层次的包结构：
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ xyz.py
这样，文件www.py的模块名就是: mycompany.web.www
'''
【【使用模块】】：
'''
编写一个hello模块：'''
#!/usr/bin/env python3  #让该hello.py文件能直接在Unix/Linux/Mac上直接运行
# -*- coding: utf-8 -*- #.py文件本身使用标准UTF-8编码

' a test module '       #任何模块代码的第一个字符串都被视为模块的文档注释，可以不写

__author__ = 'ctt'      #__author__变量保存作者名，可以不写

import sys              #导入内建的sys模块

def test():
    args = sys.argv     #sys模块的argv变量，用list存放命令行的所有参数，argv至少有一个元素，为该.py的文件名
    if len(args)==1:
        print('hello')
    elif len(args)==2:
        print('hello, %s' % args[1])
    else:
        print('Too many arguments')

if __name__=='__main__':
    test()
#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__>置为__main__,而如果在其他地方导入该hello模块时,if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
#当不是在命令行执行该模块文件时，使用hello.test()来执行test()函数

【【【作用域】】】：
'''一个模块中会有很多的函数和变量，有些可以给别人使用，有些我们希望仅在模块内部使用.在Python中通过_前缀实现
正常的函数和变量名是公开的(public)，可以被直接引用
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，例如__author__,__name__.hello模块定义的文档注释也可以用特殊变量__doc__访问，所以我们自己定义的变量不要使用这种变量名。
类似_xxx和__xxx这样的函数或者变量就是非公开的(private),不应该被直接引用
注意：private函数和变量是不应该被直接引用，而不是不能。因为Python还没有一种方法可以完全限制访问private函数或变量，但是从变成习惯上不应该引用private函数或变量。
例：
def _private_1(name):
    return 'hello, %s' % name
def greeting(name):
    return _private_1(name)
这样，我们在模块里公开greeting()函数，而把内部逻辑用的private函数隐藏起来了，这样调用greeting()函数就不用关心内部private函数细节，这是一种非常有用的代码封装和抽象的方法，即将外部不需要引用的函数全部定义成private。
'''
【【【安装第三方模块】】】：
'''
使用pip install Pillow安装第三方库Pillow，关于第三方库的名称可以在Python官网或者pypi.python.org上搜索。anaconda模块中已经内置了许多非常有用的第三方库，，可以从官网：https://www.anaconda.com/download/下载安装包后安装使用。anaconda安装的第三方模块会安装在anaconda自己的路径下，不会影响系统已经安装的Python目录。'''
【【【模块搜索路径】】】：
'''
当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，找不到就会报错。该路径存放在sys模块的path变量中：
>>> sys.path
如果我们要添加自己的搜索目录，有两种方法：
1. 直接修改sys.path,添加要搜索的目录：
   >>> sys.path.append('...')
    这种方法只在运行时修改，运行结束后失效
2. 设置环境变量：PYTHHONPATH ，该环境变量的内容会被自动添加到搜索路径中
'''

【面向对象编程】：
'''
面向对象编程--Object Oriented Programming，简称OOP，将对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行，为了简化程序设计，面向过程把函数继续切分为子函数来降低复杂度。
而面向对象的程序设计吧计算机程序视为一组对象的集合，每个对象都可以接收并处理其他对象发过来的消息，计算机程序的执行就是一系列的消息在各个对象之间传递。
在Python中所有的数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类(Class)的概念。
举例区别：处理学生的成绩表
【面向过程】：
首先用一个dict来表示一个学生的成绩：
std1 = { 'name': 'A', 'score': 98 }
std2 = { 'name': 'B', 'score': 80 }
然后用函数实现处理成绩：
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))
【面向对象】：
首先思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象有name和score这两个属性(Property).要打印一个学生的成绩，首先必须创建出这个学生对应的对象，再给该对象发一个print_score消息，让对象自己把自己的数据打印出来：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
给对象发消息实际上就是调用对象对应的关联函数，即对象的方法(Method)
面向对象的程序写出来就像这样：
A = Student('A', 89)    #Student是类(Class)，而A就是其一个实例(Instance)
B = Student('B', 90)
A.print_score()
B.print_score()
'''
【【类和实例】】：
'''
class Student(object):
    pass
类用class关键字声明，类名通常是大写开头的单词，(object)表示该类是从哪个类继承下来的，如果没有合适的继承类，就用object类，这是所有的类最终都会继承的类
定义好了类后，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
A = Student()
此时A指向的就是一个Student的实例，每个实例在内存中的地址是不一样的
------------------------------------
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
------------------------------------
class包含：
    1. 类的属性：类中所涉及的变量
    2. 类的方法：类中的函数
其中 __init__() 这个函数使得class可以带参数，他是解释器创建实例后调用的第一个方法，其他函数都需要调用才能执行，而__init__()函数是只要其所在的类被实例化了，他就会被调用，所以他可以用来做相当于初始化类的工作（例如定义一些变量以供类中的其他函数使用），当然也可以不定义__init__()
如果定义了__init__()函数，那么在创建实例的时候传递的所有参数都会交给__init__()，__init__()的第一个参数(self（可以是别的名字）)代表实例对象本身，传参的时候不用传递这个
__init__()函数中定义的变量例如上例中的self.name，在该class中的其他函数中就可以直接当变量使用了。

类就相当于是将若干个函数(方法)封装起来，好处就是，调用很简单，不用关心里面的数据和逻辑，并且函数(方法)可以随意修改。

【私有】
在变量前加两个下划线__，将变量变为私有变量，之后该变量就只能在内部访问：
比如上面的Student中的name属性，可以用一个实例对象：A.name = 'haha'，来修改，但是如果将它定义为私有变量：
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    ...
这样该变量就只能就无法从外部访问实例变量.__name了。确保外部代码不能随意修改对象内部状态。
如果外部代码要获取name：
class Student(object):
    ...

    def get_name(self):
        return self.__name
外部代码要修改name：
class Student(object):
    ...

    def set_score(self, score):
        self.__score = score
这样大费周折的方法是因为可以在set_score()这个方法中对参数score进行检查，避免穿入无效参数：
class Student(object):
    ...

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
python中以__开头和结尾的变量是特殊变量，可以直接访问，不是private变量，所以不能用__name__, __score__这样的变量名
有如下错误写法：
A.__name = 'haha'
这样做是可以成功设置__name这个变量，但是它和class中的__name变量并不是同一个变量，class内部的__name变量已经被Python解释器自动改成了_Student__name（或者其他名字），而此时外部代码只是给实例A新增了一个__name变量。
'''

【继承和多态】：
'''
当我们定义一个class时，可以从某个现有的class继承，新的class称为子类(Subclass),而被继承的class称为基类、父类或者超类(Base class、Super class):

继承最大的好处就是子类可以获得父类的全部功能
class Father(object):
    def run(self):
        print("i'm father")
class Child(Father):
    pass
A = Child()
A.run() #输出：i'm father

继承还有一个好处就是子类可以用在子类中重新写函数内容的方法覆盖重写父类中不合适的方法：
class Child(Father):
    def run(self):
        print("i'm child")
A = Child()
A.run() #输出：i'm child
这就是继承的另一个好处：多态

当我们定义class时，实际上就是定义了一个数据类型（和Python自带的数据类型如str、list、dict一样）：
F = Father()    #F是Father类型，但不是Child类型
C = Child()     #C是Child类型，同时也是Father类型
判断一个变量是否是某个类型：
>>> ininstance(F, Child)
False
>>> instance(C, Father)
True

多态的好处：
def test(a):
    a.run()
>>> test(Father())
i'm Father
>>> test(Child())
i'm Child
这个好处就是：当我们需要传入Child时，test()只需要接收Father类型，因为Child也是Father类型。因为Father类型有run()方法，所以传入的任意类型只要是Father类或者其子类，都会自动调用实际类型的run()方法，这就是多态的意义：调用方只管调用，不用管细节
当我们新增一种Father的子类时，只要确保该子类的run()方法编写正确，不用管原来的代码是如何调用的，这就是著名的‘开闭’原则：
对扩展开放: 允许新增Father子类
对修改封闭：不需要修改依赖Father类型的test()等函数

继承还可以一级一级的继承下来，子类、孙子类最终都可以溯源到根类object：
                ┌───────────────┐
                │    object     │
                └───────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
           ▼                         ▼
    ┌─────────────┐           ┌─────────────┐
    │   Animal    │           │    Plant    │
    └─────────────┘           └─────────────┘
           │                         │
     ┌─────┴──────┐            ┌─────┴──────┐
     │            │            │            │
     ▼            ▼            ▼            ▼
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│   Dog   │  │   Cat   │  │  Tree   │  │ Flower  │
└─────────┘  └─────────┘  └─────────┘  └─────────┘

【【静态语言 VS 动态语言】】：
静态语言（如Java）：如果函数需要传入Father类型，传入的对象就必须是Father类型或者其子类，否则将无法调用run()方法
动态语言（如Python）：传入的对象不一定要是Father类型，只需要保证传入的对象有一个run()方法：
class Nochild(object):
    def run(self):
        print("i'm Nochild")
这就是动态语言的“鸭子类型”，他并不要求严格的继承体系，只要一个对象看起来像“鸭子”，走起路来像“鸭子”，那它就可以被看做是鸭子。
Python的“file-like object”就是一种鸭子类型。对真正的文件对象，他有一个read()方法，返回其内容。但，对于不是file的对象，只要有read()方法，就被视为“file-like object”。许多函数接受的参数就是“file-like object”，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
'''

【获取对象信息】
【【type()函数】】
'''
判断基本的对象类型（int，str等）：
>>> type(123)
<class 'int'>
对上一节的类Father和函数run():
>>> type(Father)
<type 'type'>
>>> type(run)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  NameError: name 'run' is not defined
#这里会报错，是因为run是类中的函数，外部只能通过实例访问
>>> def haha():
... print('haha')
...
>>> type(haha)
<type 'function'>
>>> type('abc') == str
True
>>> type(123) == int
True
>>> type(Student) == type(Father)
True
'''
【【types模块】】
'''
判断一个对象是否是函数：使用types模块中定义的常亮：
>>> import types
>>> def fn():
...     pass
...
>>> type(fn) == types.FunctionType
True
'''
【【isinstance()函数】】
'''
判断一个对象的类型：
>>> F = Father()
>>> isinstance(F, Father)
True
>>> class Child(Father):
...     def run(self):
...             print('Child')
...
>>> C = Child()
>>> isinstance(C, Father)
True
>>> isinstance(F, Child)
False
能用type()判断的基本类型也能用isinstance()判断：
>>> isinstance(5, int)
True
>>> isinstance(b'a', bytes)
True
还可以判断某一个变量是否是某些类型中的一种：
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance([1, 2, 3], list)
True
>>> isinstance([1, 2, 3], tuple)
False
'''
【【dir()函数】】
'''
dir()函数用于获取一个对象的所有属性：
>>> dir('abc')
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
这些属性和方法在Python中是有特殊用途的：
>>> 'abc'.isalpha()
True
>>> 'abc'.isdigit()
False
>>> 'abc'.upper()
'ABC'
>>> 'abc'.__len__()
3
>>> len('abc')
3   #实际上在Python中调用len()函数去获取一个对象的长度，在len()函数内部，他也是自动去调用的该对象的__len__()方法
'''
【【操作对象的属性状态】】
'''
使用getattr()获取属性，setattr()设置属性，hasattr()判断属性是否存在：
>>> class Test(object):
...     def __init__(self):
...             self.x = 10
...     def run(slef):
...             return self.x * self.x
...
>>> A = Test()
>>> hasattr(A, 'x') #有属性'x'吗
True
>>> hasattr(A, 'y')
False
>>> setattr(A, 'y', 20) #设置一个属性'y'
>>> hasattr(A, 'y')
True
>>> getattr(A, 'x') #获取属性'x'
10
>>> A.x #获取属性'x'
10
如果获取一个不存在的属性，就会抛出AttributeError错误：
>>> getattr(A, 'z')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Test' object has no attribute 'z'
可以传入一个default参数，如果属性不存在，就返回默认值：
>>> getattr(A, 'z', 404)
404
也可以获得对象方法：
>>> hasattr(A, 'run')
True
>>> getattr(A, 'run')
<bound method Test.run of <__main__.Test instance at 0x7f31601449e0>>
>>> fn = getattr(A, 'run')  #获取属性'run'并赋值到变量fn
>>> fn  #fn指向A.run
<bound method Test.run of <__main__.Test instance at 0x7f31601449e0>>
>>> fn()    #相当于调用A.run()
100
注意：只有在不知道对象信息的时候，才会去获取对象信息，比如如果可以直接写A.x就不要写getattr(A, 'x')
>>> def readImage(fp):
...     if hasattr(fp, 'read'): #如果对象fp存在read方法，则fp是一个文件流，可以读取，如果不存在就无法读取
...             return readData(fp)
...     return None
...
>>> 
'''
【【实例属性、类属性】】
'''
Python是动态语言，所以可以通过创建的实例任意绑定属性，给实例绑定属性的方法：通过实例变量 或者 self变量
如果class本身需要绑定一个属性，可以直接在class中定义，这种属性就是类属性：
>>> class Test(object):
...     name = 'Test'   #类属性，相当于默认值
...
>>> T = Test()
>>> T.name  #实例的name属性，因为实例没有name属性，所以会继续查找class的name属性
'Test'
>>> Test.name   #类的name属性
'Test'
>>> T.name = 'T'    #给实例绑定name属性
>>> T.name  #实例属性优先级比类属性高，所以会屏蔽掉类的name属性
'T'
>>> Test.name   #类属性并未消失
'Test'
>>> del T.name  #删除实例的name属性
>>> T.name  #实例没有name属性，所以继续查找class的name属性
'Test'
so:
    实例属性属于各个实例所有，互不干扰；
    类属性属于类所有，所有实例共享一个属性；
    不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误
'''

【面向对象高级编程】
【【给对象或类绑定方法】】
'''
除了可以给对象或类绑定属性，还可以绑定方法：
>>> class Test(object):
...     pass
...
>>> T = Test()
>>> def run(self, age):
...     self.age = age
...
>>> from types import MethodType
>>> T.run = MethodType(run, T)
>>> T.run(5)
>>> T.age
5
给一个实例绑定的属性或方法，对其他实例是无效的
为了给所有的实例都绑定方法，可以给class绑定方法：
>>> def get_score(self, score):
...     self.score = score
...
>>> Test.get_score = get_score
>>> T1 = Test()
>>> T1.get_score(7)
>>> T1.score
7
通常情况下，get_score方法可以直接定义在class中，但是动态绑定允许我们在程序运行的过程中动态的给class加上功能，这在静态语言中很难实现
'''
【【限制实例属性__slots__】】
'''
在定义class时定义一个特殊的__slots__变量，来限制class实例能添加的属性：
只允许对Test实例添加name，age属性
>>> class Test(object):
...     __slots__ = ('name', 'age')
...
>>> T = Test()
>>> T.name = 'T'
>>> T.haha = 11
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Test' object has no attribute 'haha'
试图绑定一个__slots__中没有的属性，就会报AttributeError的错误
注意：
    __slots__定义的属性限制，只对当前类的实例起作用，对继承子类是不起作用的
    除非在子类中也定义__slots__,这样子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
>>> class Test1(Test):
...     pass
...
>>> T1 = Test1()
>>> T1.haha = 11
>>> class Test2(Test):
...     __slots__ = ('haha')
...
>>> T2 = Test2()
>>> T2.name = 'T2'
>>> T2.haha = 11
>>> T2.yo = 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Test2' object has no attribute 'yo'
'''
【【将类方法变成类属性：@property , 用于检查或者设置类属性时，不用调用复杂的类函数】】
'''
Python内置的 @property 装饰器可以将class中的一个函数（方法）变成属性：
-------------------------------------------------------------------------
>>> class Student(object):
...     @property
...     def score(self):
...             return self._score
...     @score.setter
...     def score(self, value):
...             if not isinstance(value, int):
...                     raise ValueError('score must be an integer!')
...             if value < 0 or value > 100:
...                     raise ValueError('score must between 0 ~ 100!')
...             self._score = value
...
>>> s = Student()
>>> s.score = 111
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    File "<stdin>", line 10, in score
    ValueError: score must between 0 ~ 100!
-------------------------------------------------------------------------
这里@property就将class的方法score变成了一个参数，让实例直接通过xxx.score这样调用，
其中@score.setter 是@property的一种装饰器，用来设置可写属性，如果没有.setter，则该属性为只读属性。@property有两个方法：setter , getter
'''

【【多重继承】】
'''
子类继承自多个父类，称之为多重继承：
class F1(object):
    pass
class F2(object):
    pass
class C1(F1, F2):
    pass
通过多重继承，一个子类可以同时获得多个父类的所有功能
为了更好的看出多重继承的继承关系，可以使用MixIn的写法：
class C2(F1, F2MixIn)
    pass
Python自带的很多库也使用了MixIn,例如Python自带的TCPServer和UDPServer这两类网络服务，要同时服务多个用户，就必须使用多进程或多线程模型，这两种模型由ForKingMixIn和ThreadingMixIn提供。另外还有一个更先进的：协程模型：CoroutineMixIN
'''

【【定制类】】
【【【__str__ , __repr__】】】
'''
>>> class F(object):
...     def __init__(self, name):
...             self.name = name
...
>>> class F1(object):
...     def __init__(self, name):
...             self.name = name
...     def __str__(self):
...             return "F's object (name: %s)" % self.name
...
>>> print(F('H'))
<__main__.F object at 0x7fa80bfcd950>
>>> print(F1('H'))
F's object (name: H)
这样使用print就能打印指定内容了，但是直接调用变量还是不行：
>>> f1 = F1('H')
>>> f1
<__main__.F1 object at 0x7fa80bfcdad0>
这是因为直接显示变量调用的不是__str__()，而是__repr()__(),两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，即__repr__()是为调试服务的。
解决办法是再定义一个__repr__():
>>> class F2(object):
...     def __init__(self, name):
...             self.name = name
...     def __str__(self):
...             return 'F object (name: %s)' % self.name
...     __repr__ = __str__
...
>>> f2 = F2('H')
>>> f2
F object (name: H)
'''
【【【__iter__】】】
'''
如果想让一个class被用于for...in循环，类似list或tuple那样，就必须在class里面实现一个__iter__()方法，该方法返回一个迭代对象，然后Python的for循环就会不断调用该迭代对象的__next__()方法，拿到循环的下一个值，知道遇见StopIteration错误时退出循环：
>>> class F(object):
...     def __init__(self):
...             self.a, self.b = 0, 1 # 初始化两个计数器a，b
...     def __iter__(self):
...             return self # 实例本身就是迭代对象，故返回自己
...     def next(self):
...             self.a, self.b = self.b, self.a + self.b # 计算下一个值
...             if self.a > 10:  #退出循环的条件
...                     raise StopIteration()
...             return self.a   #返回下一个值
...
>>> for n in F():
...     print(n)
...
1
1
2
3
5
8
'''
【【【__getitem__】】】
'''
__iter__()虽然能让class实现迭代，但是依然不能像list一样使用，比如取某个元素：
>>> F()[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'F' object does not support indexing
如果要实现像list那样按照下标取出元素，可以用__getitem__()方法：
>>> class F(object):
...     def __getitem__(self, n):
...             a, b = 1, 1
...             for x in range(n):
...                     a, b = b, a + b
...             return a
...
>>> f = F()
>>> f[0]
1
>>> f[5]
8
对于list的切片方法也能实现：
----------------------------------------
class F(object):
    def __getitem__(self, n):
        if isinstance(n, int):  #n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = F()
print(f[0:5])
print(f[:10])
-------------------------------------------
执行结果：
[1, 1, 2, 3, 5]
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
但是还有问题：
>>> f[:10:2]    #step=2，每隔两个输出
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
可以看出没有对step进行处理，并且他实际上也不会对负数进行处理
与__getitem__()对应的是__setitem__()方法，把对象试做list或dict来对集合赋值。还有__delitem__()方法用于删除某个元素。
'''

【【【__getattr__()】】】
'''
通常情况下如果对象调用一个不存在的class的方法或属性时，会报错，使用__getattr__()方法，可以动态的返回一个属性或者方法：
----------------------------------
class Student(object):
    def __init__(self):
        self.name = 'H'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)   #没有被定义的属性抛出错误

s = Student()
print(s.score)
print(a.age())
print(s.haha)
----------------------------------
执行后输出：
99
25
Traceback (most recent call last):
  File "./ha.py", line 147, in <module>
    print(s.haha())
  File "./ha.py", line 143, in __getattr__
    raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
AttributeError: 'Student' object has no attribute 'haha'

如果不定义AttributeError(),这里调用一个不存在的属性或方法就会返回None：
None    #如果不定义__getattr__()，这里获取一个不存在的属性就会报错
        #返回None是因为__getattr__()的默认返回就是None
这种完全动态的调用的应用场景之一：
    现在很多网站都搞REST API，调用API的URL类似：http://api.server/user/friends
    如果要写SDK，给每个URL对应的API都写一个方法，得累死，而且API一旦改动，SDK也要改，那更是崩溃的
    而利用__getattr__()，就可以写一个链式调用：
-------------------------------------------------
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s%s' % (self._path, path))
    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)
-------------------------------------------------
执行后输出：
statususertimelinelist
    这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且不随API的增加而改变

    有些REST API会把参数放到URL中，比如GitHub的API：
    GET /user/:user/repos
    调用时，需要把:user替换为实际用户名：
    Chain().users('Chen').repos
代码修改如下：
将__getattr__()修改如下：
--------------------------------------------------------------
    def __getattr__(self, path):
        if path == 'users':
            Chain('%s%s' % (self._path, path))
            return lambda s: Chain('%s%s' % (self._path, s))
        return Chain('%s%s' % (self._path, path))
print(Chain().status.user.timeline.list)
print(Chain().status.users('Chen').timeline.list)
--------------------------------------------------------------
执行后输出：
statususertimelinelist
statusChentimelinelist  #注意这里user被替换成真实的用户名了

注意：只有在没有找到属性的情况下才会调用__getattr__()，已有的属性比如默认自带的name，不会再__getattr__()中查找
'''
【【【__call__()】】】
'''
当我们调用实例方法时，用的是instance.method()的方法。使用__call__()可以实现直接在实例本身上调用,实现把实例当做一个函数来调用。这样就完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本区别：
class C(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('show %s' % self.name)
c = C('haha')
c()
执行输出：
show haha
__call__()还可以定义参数
如果把对象看成函数，因为类的实例都是运行期创建出来的，所以函数本身也就可以在运行期动态创建出来，这样一来就模糊了对象和函数的界限。
判断一个变量是函数还是对象：能够被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
>>> callable(max)
True
>>> callable('str')
False
'''
【【枚举类】】
'''
Python提供Enum类来实现枚举：
-----------------------------------------------------------------------------------------------------------
from enum import Enum

#床架Month；类型的枚举类：
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#可以使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
执行后输出：
('Jan', '=>', <Month.Jan: 1>, ',', 1)
('Feb', '=>', <Month.Feb: 2>, ',', 2)
('Mar', '=>', <Month.Mar: 3>, ',', 3)
('Apr', '=>', <Month.Apr: 4>, ',', 4)
('May', '=>', <Month.May: 5>, ',', 5)
('Jun', '=>', <Month.Jun: 6>, ',', 6)
('Jul', '=>', <Month.Jul: 7>, ',', 7)
('Aug', '=>', <Month.Aug: 8>, ',', 8)
('Sep', '=>', <Month.Sep: 9>, ',', 9)
('Oct', '=>', <Month.Oct: 10>, ',', 10)
('Nov', '=>', <Month.Nov: 11>, ',', 11)
('Dec', '=>', <Month.Dec: 12>, ',', 12)
-----------------------------------------------------------------------------------------------------------
value属性时自动赋给成员的int常量，默认从1开始计数

如果需要更精确的控制枚举类型，可以从Enum派生出自定义类：
-------------------------------
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 #Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
-------------------------------
@unique装饰器可以帮助我们检查保证没有重复值
若干种访问这些枚举类型的方法：
>>> d1 = Weekday.Mon
>>> print(d1)
Weekday.Mon
>>> print(Weekday['Tue'])
Weekday.Tue
>>> print(Weekday.Tue.value)
2
>>> print(d1 == Weekday.Mon)
True
>>> print(Weekday(1))
Weekday.Mon
>>> print(d1 == Weekday(1))
True
>>> Weekday(7)
Traceback (most recent call last):
  File "./ha.py", line 202, in <module>
    Weekday(7)
  File "/usr/lib/python2.7/site-packages/enum/__init__.py", line 347, in __call__
    return cls.__new__(cls, value)
  File "/usr/lib/python2.7/site-packages/enum/__init__.py", line 662, in __new__
    raise ValueError("%s is not a valid %s" % (value, cls.__name__))
ValueError: 7 is not a valid Weekday
>>> for name, member in Weekday.__members__.items():
...    print(name, '=>', member)
...
('Sun', '=>', <Weekday.Sun: 0>)
('Mon', '=>', <Weekday.Mon: 1>)
('Tue', '=>', <Weekday.Tue: 2>)
('Wed', '=>', <Weekday.Wed: 3>)
('Thu', '=>', <Weekday.Thu: 4>)
('Fri', '=>', <Weekday.Fri: 5>)
('Sat', '=>', <Weekday.Sat: 6>)

所以既可以用成员名称引用枚举常量，也可以直接根据value值获得枚举常量
'''

【【元类】】
【【【type()】】】
'''
动态语言与静态语言最大的不同就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
例：定义一个Hello的class，就写一个hello.py
-----------------------------------
# cat hello.py
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
# cat test.py
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
执行后输出：
Hello, world.
<type 'type'>
<class 'hello.Hello'>
-----------------------------------
type()函数可以查看一个类型或变量的类型，Hello是一个class所以它的类型就是type，而h是一个实例它的类型就是class Hello.
class的定义是运行时动态创建的，创建class的方法就是type()函数，type()函数既可以返回一个对象类型，又可以创建出新的类型.
例：通过type()函数创建出Hello类，而无需通过class Hello(object)...定义：
--------------------------------------------------------------------------
>>> def fn(self, name='world'): #先定义函数
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn))    #创建Hello class
>>> h = Hello()
>>> h.hello()
Hello, world.
>>> print(type(Hello))
<type 'type'>
>>> print(type(h))
<class '__main__.Hello'>
--------------------------------------------------------------------------
其中type()函数3个参数注解如下：
    1. class名
    2. 继承的父类集合. 注意：Python支持多重继承，如果只有一个父类，一定要用tuple的单元素写法
    3. class的方法名称与函数绑定。在上例中是将函数fn绑定到方法名hello上
通过type()函数创建的class和直接写class是完全一样的。因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
'''
【【【mataclass】】】
'''
除了使用type()函数动态创建类，要控制类的创建行为，还可以使用metaclass
metaclass直译就是元类：定义了类以后就能根据这个类创建出实例，但是要是想创建出类，就必须先定义metaclass，根据metaclass去创建类：定义metaclass --> 创建class --> 创建实例
例：使用metaclass给自定义的MyList增加一个add()方法
先定义ListMetaclass：   #按照默认习惯，metaclass的类名总是以Metaclass结尾
-----------------------------------------------------------------
# metaclass是类的模板，所以必须从'type'类型派生
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)   # 创建新的方法
        return type.__new__(cls, name, bases, attrs)    # 返回修改后的定义
# 使用ListMetaclass来定制类，传入关键字参数metaclass
#***python3的语法如下：
class MyList(list, metaclass=ListMetaclass):    #metaclass关键字参数指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
    pass
#***Python2.7的语法如下：
class MyList(list):
    __metaclass__ = ListMetaclass
    pass
L = MyList()
L.add(1)
L.add('END')
print(L)
执行后输出如下：
[1, 'END']
# 普通的list()函数是没有add()方法的
>>> L = list()
>>> L.add(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'add'
-----------------------------------------------------------------
__new__()方法参数注解如下：
    1. 当前准备创建的类的对象
    2. 类的名字
    3. 类继承的父类集合
    4. 类的方法集合

像上面那样的栗子，实际不必要用metaclass来写，直接在MyList定义中写才对。但是metaclass总有它的应用场景，比如ORM：
ORM：Object Relational Mapping, 对象-关系映射， 把关系数据库的一行映射为一个对象，即一个class对应一个表，这样就不用直接操作SQL语句，代码更简单：
要编写ORM框架，所有的class都只能动态定义，因为只有使用者才能根据表的结构定义出对应的class：
1. 编写底层模块（编写调用接口）
例如使用者想定义一个User类来操作对应数据库表User：
----------------------------------------------------------------------------
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
# 创建一个实例
u = User(id=12345, name='CTT', email='test@ctt.com', password='mypassword')
# 保存到数据库
u.save()
----------------------------------------------------------------------------
其中父类Model和属性类型StringField、IntegerField都是由ORM框架提供的，剩下的方法save()全部由metaclass自动完成。
虽然metaclass的编写比较复杂，但是ORM的使用者用起来却十分简单。

2. 按照接口来实现ORM
首先定义Field类，负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
在Field的基础上进一步定义各种类型的Field，如StringField，IntegerField等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

3. 编写最复杂的 ModelMetaclass和Model
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mapping[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name   # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self. **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
这一段不懂，先不写了：https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000
'''


【报错】：
1. Python2和Python3
    2: print reduce(func, [1, 2, 3])
    3: reduce()已经从内建函数移动到库functools中
        需要先from functools import reduce 才能使用

