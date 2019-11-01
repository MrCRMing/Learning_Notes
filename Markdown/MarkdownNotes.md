# Head 1
## Head 2 （可以加1-6个#）
Head 3
======
Head 4
------
>This is a blockquote with two paragraphs,
>only 'enter' it can not change the line  
>You should pause+pause+enter can make it change the line.

>>this is a nested blockquote.
 
>### 这是一个嵌套的标题

### 无序列表
* red
* green
* blue
+ red
+ green
+ bule
- red
- blue
- green

* red
* green
* blue

*	Lorem ipsum dolor sit amet, consectetuer adipiscing
*	Suspendisse id sem consectetuer libero luctus 	adipiscing.

*	Suspendisse id sem consectetuer libero luctus adipiscing.	
### 有序列表
1. A
2. B
3. C  

*OR* 
 
4. E
5. F
6. G

*OR* 

9. H
8. I
10. J

1.    This is a list item with two paragraphs. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aliquam hendrerin mi posuere lectus.
	
	列表项目可以包含多个段落，但每个项目下的段落都必须缩进四个空格或一个制表符。
2.	试试在列表里面用引用

	>在列表里用引用“>"也要缩进四个空格或一个制表符
3. 如果要放代码区块的话，该区块就需要缩进两次，也就是 8 个空格或是 2 个制表符


4\. 为避免项目列表会不小心产生，可以在句点前面加上反斜杠.

### 5. 代码区块
	//这是一个代码区
		int main()
		{
		int a =0;
		int *b =1;
		if（a<b && a==0)
		a=b;
		return 0;
		}
	//代码区结束

### 6. 分割线  
***
---
————————————————————————————————
* * * 
- - -
—— —— —— —— —— —— —— —— —— —— ——

### 7.链接
行内式：链接文字用[]标记，行内式链接只要在[]后面紧接着（）并插入网址链接即可，如果想加上title，只要在网址后面用双引号把title包起来即可，例如：
> This is [an example][http://example.com/"Title"] inline link  

如果是要链接到同样的主机资源，可以使用相对路径：
>See my [about](/about/) page for details.

参考式的链接式在连接文字的括号后面再接上一个方括号，而在第二个方括号里面要填入用以辨识链接的标记：
>This is [an expemle] [id] reference-style link.

然后在文件的任意处可以把这个标记的链接内容定义出来：
>[id]: http://example.com/ "Optional title here"

注意id里面式不区分大小写的  

隐式链接标记功能可以省略指定的id，这种情况下链接标记会视为等同于链接文字，如：
>[Google][]
>[Google]: http://gogle.com/ "Google is here"

### 强调
用*或_左右包围，可以用1-3个如：  
*强调1*  
_强调2_  
**强调3**  
__强调4__   
但如果*和_两边都有空白的话，就只会被当成普通的符号
### 代码
如果要标记一小段行内代码，可以用方括号包起来如：
>Use the `printf()` function
### 图片
仍用行内式和参考式：
行内式：相同目录下 
>![Alt text](01.jpg "Luffy")

  
参考式：
>![Alt text][id]
>>[id]: https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1518889977316&di=01adee49f1266ae57bfa70b75d1a5eba&imgtype=0&src=http%3A%2F%2Fp4.gexing.com%2Fshaitu%2F20120729%2F1056%2F5014a66cc640c.jpg "草帽海贼团"
>**[id]:URL/to/image "Optional title attribute"**


要改变大小需要用HTML语言。如：
<img src="01.jpg" width=256 height=256/>
若是按比例显示，则是：
<img src="01.jpg" width="50%" height="50%"/>
若是要加标注，可以是：
<center>
<img src="01.jpg" width="50%" height="50%"/>
# **Luffy**
</center>

### 反斜杆
Markdown支持一下的符号前面加上反斜杠来帮助插入普通符号:   
\\   反斜线  
\`   反引号  
\*   星号  
\_   底线  
\{}  花括号  
\[]  方括号  
\()  括弧  
\#   井字符  
\+   加号  
\-   减号  
\.   英文句点  
\!   惊叹号