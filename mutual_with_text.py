'''mutual with text'''
import numbers

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
