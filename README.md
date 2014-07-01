scheme
======

Implement a scheme Interpretation

Reference
-----------

1 http://norvig.com/lispy.html

2 http://norvig.com/lispy2.html


工作日志
-----------
#2014/6/30 

	新建github仓库
	选择使用python2.7编写解释器。python符合平时命令式编程习惯同时支持一些函数式编程的语法（比如lambda函数，map，filter，reduce），语法和scheme有类似之处，而且有丰富的package，给编写带来了方便。

	实现了命令行输入
	输入时难以实现自动缩进到正确的位置，于是调整为用户手动输入缩进

	实现了简单的define，比如
	> (define pi 3.14)
	> pi
	3.14
	> exit

#2014/7/1
	
	增加了对注释的判断

	重新布局整体设计，模块化
	重写了分词
