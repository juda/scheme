#-*-coding:utf8-*-
from global_dict import *
from mutual_with_text import *
import operator as op
import re
import pdb

def selfEvaluating(exp):
    #print exp[0]
    return (isnumber(exp[0]) or isQuoted(exp[0]))

def isVariable(exp,env):
    try:
        return  isinstance(exp[0],str) and env.findVariable(exp)
    except Exception():
        return False

def isQuoted(exp):
    try:
        return exp[0][0]=='"' and exp[0][-1]=='"'
    except Exception():
        return False

def lookupVariableValue(exp,env):
    return env.findVariable(exp)

def evalAssignment(exp,env):
    env.setVariable(exp[1],exp[2])


def evalDefinition(exp,env):
    #print exp
    if isinstance(exp[1],list):
        env.procedure[exp[1][0]]=makeProcedure(exp[1][1:],exp[2])
    else:
        env.addVariable(exp[1],process(exp[2],env))

def evalIf(exp,env):
    if process(exp[1],env):
        #print 't'
        return process(exp[2],env)
    else:
        #print 'f'
        return process(exp[3],env)

def makeProcedure(para,body):
    return (body,para)

def evalSequence(exp,env):
    if len(exp)==1:
        return process(exp[0],env)
    else:
        process(exp[0],env)
        return evalSequence(exp[1:],env)

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
        return catch(command[:-1],alist[0])
    else:
        return catch(command[:-1],alist[1:])

def applyPrimitiveFunction(foo,agruments):
    pattern=re.compile(r'c[a|d]+r')
    #print foo
    if foo=='+':
           return reduce(op.add,agruments,0)
    elif foo=='-':           
        if len(agruments)==1:
            return -agruments[0]
        else:
               return reduce(op.sub,agruments[1:],agruments[0])
    elif foo=='*':
           return reduce(op.mul,agruments,1)
    elif foo=='/':
           return reduce(op.div,agruments[1:],agruments[0])
    elif foo=='not':
           return not agruments[0]
    elif foo=='>':
           return reduce(op.and_,map(op.gt,agruments[:-1],agruments[1:]),True)
    elif foo=='<':
           return reduce(op.and_,map(op.lt,agruments[:-1],agruments[1:]),True)
    elif foo=='>=':
           return reduce(op.and_,map(op.ge,agruments[:-1],agruments[1:]),True)
    elif foo=='<=':
           return reduce(op.and_,map(op.le,agruments[:-1],agruments[1:]),True)
    elif foo=='=' or foo=='equal?':
        return reduce(op.and_,map(op.eq,agruments[:-1],agruments[1:]),True)
    elif foo=='eq?':
           return reduce(op.and_,map(op.is_,agruments[:-1],agruments[1:]),True)
    elif foo=='length':
           return len(agruments)
    elif foo=='and':
        return reduce(op.and_,map(op.and_,agruments[:-1],agruments[1:]),True)
    elif foo=='or':
        return reduce(op.and_,map(op.or_,agruments[:-1],agruments[1:]),True)
    elif foo=='cons':
        if len(agruments)!=2:
            raise SyntaxError("the number of parameters of cons is uncorrect")
        if isinstance(agruments[1],list):
            return [agruments[0]]+agruments[1]
        else:
            return agruments
    elif foo=='list':
        return agruments
    elif foo=='list?':
           return len(agruments)==1 and isinstance(agruments[0],list)
    elif foo=='null?':
        return agruments==[]
    elif foo=='symbol?':
        return len(agruments)==1 and isinstance(agruments[0],str)
    elif foo=='display':
        print tostring(agruments[0])
    elif foo=='newline':
        print
    elif pattern.match(foo)!=None and foo==foo[pattern.match(foo).start():pattern.match(foo).end()]:
        if not (isinstance(agruments[0],list) and len(agruments)==1):
            raise SyntaxError("error parameters in %s"%(foo,))
        return catch(foo[1:-1],agruments[0])
    else:
        raise NameError("Doesn't exist or lock of implementation this primitive procedure %s"%(foo,))


def preProcess(exp,env):
    if isinstance(exp,list):
           return process(exp,env)
    else:
           return exp

def applyPrimitiveProcedure(body,env):
    #print 'noe',body
    foo=body[0]
    local_env=mydict(env)
    #print 1,env.variable
    parameters=map(lambda x:preProcess(x,local_env),body[1:])
    #print 2,env.variable
    #print 'aaa'
    agruments=[]
    for i in parameters:
        if isinstance(i,int):
            agruments.append(i)
        elif isVariable(i,env):
            agruments.append(transnumber(env.findVariable(i)))
        elif isnumber(i):
            agruments.append(transnumber(i))
    #print foo,agruments
    return applyPrimitiveFunction(foo,agruments)

def applyFunction(exp,env):
    #pdb.set_trace()
    if isinstance(exp[0],list):
        foo=process(exp[0],env)
    else:
                try:
                        #print 'hea'
                        return applyPrimitiveProcedure(exp,env)
                except Exception:
                        foo=env.findProcedure(exp[0])
    body,parameters=foo
    #print body,parameters
    agruments=exp[1:]
    if len(parameters)!=len(agruments):
        raise SyntaxError("Can't match the agruments and parameters")
    local_env=mydict(env)
    temp=len(agruments)
    #print parameters,agruments
    for i in range(temp):
        local_env.addVariable(parameters[i],process(agruments[i],env))
    if env.findProcedure(body[0]):
        return applyPrimitiveProcedure(body,env)
    else:
        #sprint local_env.variable
        return process(body,local_env)

def process(exp,env):
    if not isinstance(exp,list):
        if selfEvaluating(exp):
            return exp
        elif isVariable(exp,env):
            return lookupVariableValue(exp,env)
        elif isQuoted(exp):
            return exp
        else:
            return env.findProcedure(exp)
    if selfEvaluating(exp[0]):
        return exp[0]
    elif isVariable(exp[0],env):
        return lookupVariableValue(exp[0],env)
    elif isQuoted(exp[0]):
        return exp[0]
    elif exp[0]=='set!':
        evalAssignment(exp,env)
    elif exp[0]=='define':
        evalDefinition(exp,env)
    elif exp[0]=='if':
        return evalIf(exp,env)
    elif exp[0]=='lambda':
        return makeProcedure(exp[1],exp[2],env)
    elif exp[0]=='begin':
        return evalSequence(exp[1:],env)
    elif exp[0]=='cond':
        return condIf(exp,env)
    else:
        return applyFunction(exp,env)
