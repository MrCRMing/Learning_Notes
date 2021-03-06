# 计算机基本知识整理

### 1.16位 32位 64位
是指计算机内部一次性处理数据的位数，位数越高，cpu处理数据能力越强。
字节是指一小组相邻的二进制数码。通常是8位作为一个字节。它是构成信息的一个小单位，并作为一个整体来参加操作，比字小，是构成字的单位。
字节和字长的区别：由于常用的英文字符用8位二进制就可以表示，所以通常就将8位称为一个字节。
字长的长度是不固定的，对于不同的CPU、字长的长度也不一样。8位的CPU一次只能处理一个字节，
而32位的CPU一次就能处理4个字节，同理字长为64位的CPU一次可以处理8个字节。 
8个二进制构成一字节 若干个字节构成一个字 电脑技术中对CPU在单位时间内(同一时间)能一次处理的二进制数的位数叫字长。
### 2.int 与 long int（简称 long） 的区别
占内存长度不同和取值范围不同。
在32位系统：int是4字节32位 取值范围-2^31到2^31-1； long是4字节32位取值范围是-2^31到2^31-1 此时int和long没区别
在64位系统：int是4字节32位  取值范围-2^31到2^31-1 ；long int是8字节64位 取值范围是-2^63到2^63-1
### 3.unsigned int 与int 的区别
整型的每一种都有无符号（unsigned）和有符号（signed）两种类型（float和double总是带符号的），
在默认情况下声明的整型变量都是有符号的类型，如果需声明无符号类型的话就需要在类型前加上unsigned。
无符号版本和有符号版本的区别就是无符号类型能保存2倍于有符号类型的正整数数据。比如当字节数为4时，int取值范围-2^31到2^31-1
usigned int 取值范围是0到2^32-1
### 4.云计算
云计算是一种在互联网上提供储存空间和其他资源的服务，主要是把我们从管理数据的任务中解放出来，并且使我们无论在哪里数据都能被访问到。
###深度优先搜索和广度优先搜索性能的比较
深度优先搜素算法：不全部保留结点，占用空间少；有回溯操作(即有入栈、出栈操作)，运行速度慢。
广度优先搜索算法：保留全部结点，占用空间大； 无回溯操作(即无入栈、出栈操作)，运行速度快。