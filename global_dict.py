#-*-coding:utf8-*-

######### global_dict class
import operator as op
import math
from process import process

class mydict:
    fun_env={}
    name_env={}
    def cons(self,x,y):
        if isinstance(y,list):
            return [x]+y
        else:
            return [x,y]
    def append(self,x,y):
        if isinstance(y,list):
            return x+y
        else:
            return x+[y]
    def diff_operator(self,exp):
        return lambda *s:reduce(lambda x,y:exp(x,eval(process(y))),s[1:],eval(process(s[0])))
    def compare_expression(self,exp):
        def clousure(parms):
            leng=len(parms)
            x=eval(process(parms[i]))
            for i in range(1,leng):
                y=eval(process(parms[i]))
                if not exp(x,y):
                    return False
                x=y
            return True
        return clousure
    def if_expression(self,cond,exp1,exp2=None):
        if eval(process(cond,self)):
            pass
                
    def __init__(self,father=None):
        self.father=father
        my.fun_env.update(vars(math))
        my.fun_env.update(
            {'+':self.diff_operator(op.add),
             '-':self.diff_operator(op.sub),
             '*':self.diff_operator(op.mul),
             '/':self.diff_operator(op.div),
             'not':op.not_,
             '>':self.compare_expression(op.gt),
             '<':self.compare_expression(op.lt),
             '>=':self.compare_expression(op.ge),
             '<=':self.compare_expression(op.le),
             '=':self.compare_expression(op.eq),
             'equal?':self.compare_expression(op.eq),
             'eq?':self.compare_expression(op.is_),
             'length':len,
             'cons':self.cons,
             'car':lambda x:x[0],
             'cdr':lambda x:x[1:],
             'append':self.append,
             'list':lambda *x:list(x),
             'list?':lambda x:isinstance(x,list),
             'null?':lambda x:x==[],
             'symbol?':lambda x:isinstance(x,str),
             'if':self.if_expression
             })
    def find_fun(self,name):
        if name in self.fun_env:
            return self.fun_env[name]
        else:
            raise NameError("Can't find this function")
    def add_fun(self,name,exp):
        self.fun_env[name]=exp
    def add_name(self,name):
        if name.lower() not in self.env:
            num+=1
            self.env[name.lower()]='fun%d'%(num,)
    def find_name(self,name):
        if name.lower() in self.env:
            return self.name_env[name.lower()]
        elif self.father==None:
            raise NameError("Can't find this variable")
        else:
            return self.father.find_name(name)

