scheme
======

Implement a scheme Interpretation

#学习的内容
    1. Scheme的基本操作

        a. 前缀表达式
    
        b. lambda匿名函数
        
        c. 应用序与正则序
        
        d. 统一数据结构list

    2. 实现一个解释器的基本步骤

        a. 读入字符流进行处理
        
        b. 分词
        
        c. read-eval-print-loop (REPL)

#实现解释器

    1. tokenizer
        利用python自带的string操作，把括号分开。
        如果一个字符串里面存着空格，先用一个另外的字符串代替。然后通过python的split操作分开个个元素。
        再通过替换把token转化成正确的格式。此时特殊语法'也会被转化成正确的语法
        
    2. parse
        递归进行分词。同一级别的token放在同一个list中。
        
    3. eval过程
        手动判断各种特殊语法结构，对于复合过程执行apply过程，否则根据特殊过程执行相应的函数
        
    4. apply过程
        计算参数绑定到环境里面，如果遇到底层函数如加减乘除执行底层过程，否则执行eval过程

#遇到的问题

    1. 最早的时候参考了资料

#思考与感想

#参考资料

1. 《计算机程序的构造和解释（原书第二版）》 （美）爱伯森 (Abelson.H) 等著；裘宗燕译 北京：机械工业出版社 2004.2 

2. How to Write a (Lisp) Interpreter (in Python) http://norvig.com/lispy.html

=======

