#-*-coding:utf8-*-

class Pair:
    Nil=(None,None)
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y

    def car(self):
        return self.x

    def cdr(self):
        return self.y

def evalAppend(parameters):
    now=parameters[-1]
    for i in xrange(len(parameters)-2,-1,-1):
        now=Append(parameters[i],now)
    return now

def Append(x,y):
    if x==Pair.Nil or x==None:
        return y
    else:
        return cons(x.car(),Append(x.cdr(),y))

def Length(x):
    if x==Pair.Nil:
        return 0
    else:
        return 1+Length(x.cdr())

def List(*args):
    if len(args[0])==0:
        return Pair.Nil
    now=None
    for i in xrange(len(args[0])-1,-1,-1):
        now=cons(args[0][i],now)
    return now

def cons(x,y):
    return Pair(x,y)

