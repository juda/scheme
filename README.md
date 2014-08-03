scheme
======

Implement a scheme Interpretation

#工作日志

##2014/7/8
实现了环境求值模型，并能成功实现基础过程

##2014/7/9
修复了参数为过程时的bug

修复了-号未区分减号和负号

能实现一层递归过程，但答案未能正确输出

##2014/7/10
修复了global_dict里面共享变量的bug

正确计算递归函数

    >(define (f x) (if (= x 1) 1 (* x (f (- x 1)))))
    >(f 5)
    120

##2014/7/14
实现了内部定义

    > (define (f x) (
      (define (g x) (* x x))
      (+ x (g x))))
    > (f 10)
    110

修复了lambda函数定义时存在的bug

修复了对list处理时的bug，但对空表操作会存在实现上的bug


##2014/7/15
完善了对列表的操作，成功执行以下代码：

    > (define (zipWith f x y) (if (or (null? x) (null? y))
                              (quote ())
                              (cons (f (car x) (car y))
                                    (zipWith f (cdr x) (cdr y)))))
    > (define x (list))
    > (define y (list 1 2 3))
    > (define f (lambda (x y) (* x y)))
    > (zipWith f x y)
    ()
    > (define x (list 5 6 7 8))
    > (zipWith f x y)
    (5 12 21)

##2014/7/19
完善了有理数的计算

##2014/7/21
修复了牛顿迭代法的bug，现能正确计算牛顿迭代法

重写了list的底层实现，完善了单引号‘的语法糖实现

增加了对可变长参数的支持

##2014/7/23
实现了对list的打印，正确计算汉诺塔

首先了apply过程，增加了底层操作符的重载版本

发布了第一个不完全版本v1，代号unicorn

##2014/7/25
完善了当底层操作符号为对象时的处理

    > (define (f x) (if (= x 0) + *))
    > ((f 1) 3 4)
    12
    > ((f 0) 3 4)
    7
    
##2014/7/28
增加了若干底层函数，把and和or当成语法结构进行短路求值

增加了文件处理，修复了若干bug

##2014/8/3
实现了let绑定，包括let,let*,letrec

=======

