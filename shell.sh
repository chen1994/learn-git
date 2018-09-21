#!/bin/sh

# 10进制转换为其他进制：bc
# echo "obase=进制;值"|bc
# echo "obase=2;9999"|bc
10011100001111
# echo "obase=8;9999"|bc
23417
# echo "obase=16;9999"|bc
270F

# 其他进制转换为10进制：((表达式))
# ((num=2#10011100001111));echo $num
9999
# ((num=8#23417));echo $num
9999
# ((num=0x270F));echo $num
9999

