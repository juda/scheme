#-*-coding:utf8-*-

class Pair:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y

    def car(self):
        return self.x

    def cdr(self):
        return self.y

Nil=Pair()

def evalAppend(parameters):
    if isinstance(parameters,Pair):
        parameters=transList(parameters)
    now=parameters[-1]
    for i in xrange(len(parameters)-2,-1,-1):
        now=Append(parameters[i],now)
    return now

def Append(x,y):
    if x==Nil:
        return y
    else:
        return cons(x.car(),Append(x.cdr(),y))

def Length(x):
    if x==Nil:
        return 0
    else:
        return 1+Length(x.cdr())

def List(*args):
    if len(args[0])==0:
        return Nil
    now=Nil
    for i in xrange(len(args[0])-1,-1,-1):
        now=cons(args[0][i],now)
    return now

def cons(x,y):
    return Pair(x,y)

def transList(x):
    res=[]
    while x!=Nil and x.car()!=None:
        res.append(x.car())
        x=x.cdr()
    return res

def pairEqual(obj1,obj2):
    if obj1==obj2:
        return True
    if isinstance(obj1,Pair) and isinstance(obj2,Pair):
        return pairEqual(obj1.car(),obj2.car()) and pairEqual(obj1.cdr(),obj2.cdr())
    return False
