'''mutual with text'''
import numbers
from pair import *

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
    return isinstance(exp,str) and exp[0]=="'"

def transQuoted(exp):
    if isQuoted(exp):
        return exp
    return "'%s"%(exp,)

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
    if exp==Pair.Nil or exp==None:
        return ''
    if isnumber(exp):
        return transnumber(exp)
    if isQuoted(exp):
        return transQuoted(exp)
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
                          
