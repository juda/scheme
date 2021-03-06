'''mutual with text'''
import numbers
from pair import *
import sys

def parentheseBalance(statement):
    res=0
    for i in statement:
        if i=='(':
            res+=1
        elif i==')':
            res-=1
        if res<0:
            raise SyntaxError('Unmatched parentheses')
    return res==0

def isnumber(number):
    if isinstance(number,numbers.Number):
        return True
    try:
        int(number)
    except:
        try:
            float(number)
        except:
            return False
        return True
    return True

def isQuoted(exp):
    return isinstance(exp,str) and exp.find("'")==0

def isObject(exp,env):
    try:
        return  isinstance(exp,str) and env.findObject(exp)!=None
    except:
        return False


def isstring(exp):
    return isinstance(exp,str) and len(exp)>1 and exp[0]=='"' and exp[-1]=='"' 

def transQuoted(exp):
    if isQuoted(exp):
        return exp[1:]
    return exp

def transnumber(number):
    if isinstance(number,numbers.Number):
        return number
    else:
        try:
            return int(number)
        except:
            return float(number)

def tostring(exp):
    if isinstance(exp,list):
        return '('+' '.join(map(tostring,exp))+')'
    else:
        return str(exp)

def showPair(exp):
    if exp==Nil:
        return ''
    if isnumber(exp):
        return transnumber(exp)
    if isQuoted(exp):
        return transQuoted(exp)
    if isstring(exp):
        return exp[1:-1]
    if isinstance(exp,list):
        return tostring(exp)
    if isinstance(exp,tuple):
        return exp
    if isinstance(exp,str):
        return exp
    if isinstance(exp.car(),Pair):
        res='(%s)'%(showPair(exp.car()),)
    else:
        res='%s'%(showPair(exp.car()),)
    temp=showPair(exp.cdr())
    if temp!='':
        res+=' %s'%(temp,)
    return res
                          
def display(val):
    if val is not None:
        if isinstance(val,Pair):
            sys.stdout.write('(%s)'%(showPair(val),))
        elif isinstance(val,bool):
            if val==True:
                sys.stdout.write('#t')
            elif val==False:
                sys.stdout.write('#f')
        elif isstring(val):
            sys.stdout.write(val[1:-1])
        elif isQuoted(val):
            sys.stdout.write(val[1:])
        else:
            sys.stdout.write(tostring(val))

def transValue(i,env):
    if isinstance(i,numbers.Number):
        return i
    elif isObject(i,env):
        temp=env.findObject(i)
        if isinstance(temp,list):
            return temp
        elif isnumber(temp):
            return transnumber(temp)
        else:
            return temp
    elif isnumber(i):
        return transnumber(i)
    elif isQuoted(i):
        return i
    elif isstring(i):
        return i
    else:
        return i