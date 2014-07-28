#-*-coding:utf8-*-
from global_dict import *
from mutual_with_text import *
import operator as op
import re
import pdb
import fractions
import numbers
from pair import *

def selfEvaluating(exp):
    return (isnumber(exp) or isQuoted(exp))

def isObject(exp,env):
    try:
        return  isinstance(exp,str) and env.findObject(exp)!=None
    except:
        return False


def isstring(exp):
    return len(exp)>1 and exp[0]=='"' and exp[-1]=='"' 

def evalAssignment(exp,env):
    env.setObject(exp[1],exp[2])


def evalDefinition(exp,env):
    if len(exp)>3:
        temp=exp[2:]
    else:
        temp=exp[2]
    if isinstance(exp[1],list):        
        env.object[exp[1][0]]=makeObject(exp[1][1:],temp)
    else:
        env.addObject(exp[1],process(temp,env))

def evalIf(exp,env):
    if process(exp[1],env):
        return process(exp[2],env)
    else:
        return process(exp[3],env)

def makeObject(para,body):
    return (body,para)

def evalSequence(exp,env):
    for i in exp:
        temp=process(i,env)
    return temp

def evalQuoted(exp,env):
    res=Pair.Nil
    for i in xrange(len(exp)-1,-1,-1):
        if isinstance(exp[i],list):
            temp=process(exp[i],env)
        elif isnumber(exp[i]):
            temp=transnumber(exp[i])
        elif isQuoted(exp[i]):
            temp=transQuoted(exp[i])
        else:
            temp=exp[i]
        res=cons(temp,res)
    return res

def condIf(exp,env):
    for i in exp[1:]:
        if i[0]=='else':
            return process(i[1],env)
        else:
            if process(i[0],env):
                return process(i[1],env)

def catch(command,alist):
    if command=='':
        return alist
    elif command[-1]=='a':
        return catch(command[:-1],alist.car())
    else:
        return catch(command[:-1],alist.cdr())

def isList(exp):
    if exp==Pair.Nil:
        return True
    try:
        return isList(exp.cdr())
    except:
        return False

def applyPrimitiveFunction(foo,agruments):
    pattern=re.compile(r'c[a|d]+r')
    if foo=='+':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.add,agruments,0)
    elif foo=='-':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        if len(agruments)==1:
            return -agruments[0]
        else:
            return reduce(op.sub,agruments[1:],agruments[0])
    elif foo=='*':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.mul,agruments,1)
    elif foo=='/':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        if isinstance(agruments[0],float):
            return reduce(op.div,agruments[1:],agruments[0])
        else:
            return reduce(op.div,agruments[1:],fractions.Fraction(agruments[0],1))
    elif foo=='not':
        return not agruments[0]
    elif foo=='modulo':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return agruments[0]%agruments[1]
    elif foo=='>':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.and_,map(op.gt,agruments[:-1],agruments[1:]),True)
    elif foo=='<':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.and_,map(op.lt,agruments[:-1],agruments[1:]),True)
    elif foo=='>=':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.and_,map(op.ge,agruments[:-1],agruments[1:]),True)
    elif foo=='<=':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.and_,map(op.le,agruments[:-1],agruments[1:]),True)
    elif foo=='=':
        if isinstance(agruments[0],Pair):
            agruments=transList(agruments[0])
        return reduce(op.eq,map(op.eq,agruments[:-1],agruments[1:]),True)
    elif foo=='length':
        return Length(agruments[0])
    elif foo=='cons':
        if len(agruments)!=2:
            raise SyntaxError("the number of parameters of cons is uncorrect")
        return cons(agruments[0],agruments[1])
    elif foo=='list':
        return List(agruments)
    elif foo=='append':
        return len(agruments)>1 and evalAppend(agruments)
    elif foo=='list?':
           return len(agruments)==1 and isList(agruments[0])
    elif foo=='null?':
        return len(agruments)==1 and agruments[0]==Pair.Nil
    elif foo=='symbol?':
        return len(agruments)==1 and isQuoted(agruments[0])
    elif foo=='display':
        print tostring(agruments[0])
    elif foo=='pair?':
        return len(agruments)==1 and agruments[0]!=Pair.Nil and isinstance(agruments[0],Pair)
    elif foo=='newline':
        print
    elif pattern.match(foo)!=None and foo==foo[pattern.match(foo).start():pattern.match(foo).end()]:
        if not (isinstance(agruments[0],Pair) and len(agruments)==1):
            raise SyntaxError("error parameters in %s"%(foo,))
        return catch(foo[1:-1],agruments[0])
    else:
        raise NameError("Doesn't exist or lock of implementation this primitive Object %s"%(foo,))

def isBaseFunctions(foo,env):
    if foo in env.BaseFunctions:
        return True
    pattern=re.compile(r'c[a|d]+r')
    if pattern.match(foo)!=None and foo==foo[pattern.match(foo).start():pattern.match(foo).end()]:
        return True
    return False

def preProcess(exp,env):
    if isinstance(exp,list):
           return process(exp,env)
    else:
           return exp

def applyPrimitiveObject(body,env):
    foo=body[0]
    local_env=mydict(env)
    parameters=map(lambda x:preProcess(x,local_env),body[1:])
    agruments=[]
    for i in parameters:
        if isinstance(i,int):
            agruments.append(i)
        elif isObject(i,env):
            temp=env.findObject(i)
            if isinstance(temp,list):
                agruments.append(temp)
            elif isnumber(temp):
                agruments.append(transnumber(temp))
            else:
                agruments.append(temp)
        elif isnumber(i):
            agruments.append(transnumber(i))
        elif isQuoted(i):
            agruments.append(i[1:])
        else:
            agruments.append(i)
    return applyPrimitiveFunction(foo,agruments)

def isMatch(para,agru):
    if '.' in para:
        return len(para)-2<=len(agru)
    else:
        return len(para)==len(agru)

def applyFunction(exp,env):
    if isinstance(exp[0],list):
        foo=process(exp[0],env)
        if isBaseFunctions(foo,env):
            temp=[foo]+exp[1:]
            return applyPrimitiveObject(temp,env)
    else:
                if isBaseFunctions(exp[0],env):
                        return applyPrimitiveObject(exp,env)
                else:
                        foo=env.findObject(exp[0])
                        if isinstance(foo,bool):
                            raise Exception("Can't find this object")
    body,parameters=foo
    agruments=exp[1:]
    if not isMatch(parameters,agruments):
        raise SyntaxError("Can't match the agruments and parameters")
    local_env=mydict(env)
    temp=len(agruments)
    for i in xrange(temp):
        if parameters[i]=='.':            
            local_env.addObject(parameters[i+1],List(map(lambda x:process(x,env),agruments[i:])))
            break
        local_env.addObject(parameters[i],process(agruments[i],env))
    return process(body,local_env)

def isFunction(exp,env):
    temp=process(exp,env)
    return isBaseFunctions(temp,env) or  isinstance(temp,tuple)

def evalAnd(exp,env):
    temp=process(exp[0],env)
    if temp==False:
        return False
    else:
        if len(exp)==1:
            return temp
        return evalAnd(exp[1:],env)

def evalOr(exp,env):
    temp=process(exp[0],env)
    if temp==True:
        return True
    else:
        if len(exp)==1:
            return temp
        return evalOr(exp[1:],env)

def evalEqv(obj1,obj2,env):
    obj1=process(obj1,env)
    obj2=process(obj2,env)
    if obj1==obj2:
        return True
    return False

def process(exp,env):
    if not isinstance(exp,list):
        if isinstance(exp,numbers.Number):
            return exp
        elif isnumber(exp):
            return transnumber(exp)
        elif isstring(exp):
            return exp
        elif isQuoted(exp):
            return exp[1:]
        elif env.findObject(exp)!=None:
            return env.findObject(exp)
        else:
            return exp
    if isinstance(exp[0],list) and not isFunction(exp[0],env):
        return evalSequence(exp,env)
    if exp[0]=='set!':
        evalAssignment(exp,env)
    elif exp[0]=='define':
        evalDefinition(exp,env)
    elif exp[0]=='if':
        return evalIf(exp,env)
    elif exp[0]=='lambda':
        if len(exp)>3:
            return makeObject(exp[1],exp[2:])
        else:
            return makeObject(exp[1],exp[2])
    elif exp[0]=='begin':
        return evalSequence(exp[1:],env)
    elif exp[0]=='cond':
        return condIf(exp,env)
    elif exp[0]=='and':
        return evalAnd(exp[1:],env)
    elif exp[0]=='or':
        return evalOr(exp[1:],env)
    elif exp[0]=='eqv?' or exp[0]=='eq?':
        return evalEqv(exp[1],exp[2],env)
    elif exp[0]=='equal?':
        return evalEqueal(exp[1],exp[2],env)
    elif exp[0]=='quote':
        if isinstance(exp[1],list):
            return Pair.Nil
        return transQuoted(exp[1])
    elif exp[0]=='apply':
        return applyFunction(exp[1:],env)
    elif exp[0]=='QUOTE':
        if len(exp)==1:
            return Pair.Nil
        return evalQuoted(exp[1:],env)
    else:
        return applyFunction(exp,env)
