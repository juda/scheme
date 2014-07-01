######### global_dict class
import operator as op
import math

class global_dict:
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
    def __init__(self):
        env.update(vars(math))
        env.update(
            {'+':op.add,
             '-':op.sub,
             '*':op.mul,
             '/':op/div,
             'not':op.not_,
             '>':op.gt,
             '<':op.lt,
             '>=':op.ge,
             '<=':op.le,
             '=':op.eq,
             'equal?':op.eq,
             'eq?':op.is_,
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

