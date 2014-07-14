scheme
======

Implement a scheme Interpretation

#Reference

1. http://norvig.com/lispy.html

2. http://norvig.com/lispy2.html

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


=======

