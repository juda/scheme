scheme
======

Implement a scheme Interpretation

#Reference
-----------

1. http://norvig.com/lispy.html

2. http://norvig.com/lispy2.html


#工作日志

##2014/6/30 

新建github仓库

选择使用python2.7编写解释器。python符合平时命令式编程习惯同时支持一些函数式编程的语法（比如lambda函数，map，filter，reduce），语法和scheme有类似之处，而且有丰富的package，给编写带来了方便。

实现了命令行输入

输入时难以实现自动缩进到正确的位置，于是调整为用户手动输入缩进

实现了简单的define

##2014/7/1
	
增加了对注释的判断

重新布局整体设计，模块化

重写了分词

完善了全局环境的class

语法分析的想法：设置2个class，一个存储函数名，一个存储变量名。对一个过程，变量名存储为一棵树。

在处理函数时，使用lambda维护。由于python的lambda的缺陷，需要使用时再求值（惰性求值）

例如(define (plus x y) (+ x y))，对应的python实现为plus=eval('lambda x,y:process([+ x y])')

process(string)为处理一个scheme语法语句的python语法糖

##2014/7/2

>待增加if和cond函数的语法糖

修改了基本算术操作的语法糖，使之能处理一个列表