#-*-coding:utf8-*-

######### global_dict class
import operator as op
import math
from process import process

class fun_dict:
    env={}
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
    
    def __init__(self):
        self.env.update(vars(math))
        self.env.update(
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
             'symbol?':lambda x:isinstance(x,str)
             })
    def find(self,name):
        if name in self.env:
            return self.env[name]
        else:
            raise NameError("Can't find this function")
    def add(self,name,exp):
        self.env[name]=exp


class name_dict():
    num=0
    env={}
    def __init__(self,father=0):
        self.father=father
    def add(self,name):
        if name not in self.env:
            num+=1
            self.env[name]='fun%d'%(num,)
    def exist(self,name):
        return name in self.env
    def find(self,name):
        return self.env[name]
