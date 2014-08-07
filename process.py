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

def evalAssignment(exp,env):
    env.setObject(exp[1],exp[2])


def evalDefinition(exp,env):
    if len(exp)>3:
        temp=exp[2:]
    else:
        temp=exp[2]
    if isinstance(exp[1],list):        
        env.object[exp[1][0]]=makeObject(exp[1][1:],temp,env)
    else:
        env.addObject(exp[1],process(temp,env))

def evalIf(exp,env):
    if process(exp[1],env):
        return process(exp[2],env)
    else:
        return process(exp[3],env)

def makeObject(para,body,env):
    return (body,para,env)

def evalSequence(exp,env):
    for i in exp:
        temp=process(i,env)
    return temp

def evalQuoted(exp,env):
    res=Nil
    for i in xrange(len(exp)-1,-1,-1):
        if isnumber(exp[i]):
            temp=transnumber(exp[i])
        elif isQuoted(exp[i]):
            temp=transQuoted(exp[i])
        elif isinstance(exp[i],list):
            temp=evalQuoted(exp[i],env)
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
    if exp==Nil:
        return True
    try:
        return isList(exp.cdr())
    except:
        return False

def listref(List,k):
    temp=List
    for i in xrange(k):
        temp=temp.cdr()
    return temp.car()

def evalmemq(obj,List,env):
    temp=List
    while temp!=Nil:
        if evalEqv(temp.car(),obj,env):
            return temp
        else:
            temp=temp.cdr()
    return False

def evalassq(obj,alist,env):
    temp=alist
    while temp!=Nil:
        if evalEqv(temp.car().car(),obj,env):
            return temp.car()
        else:
            temp=temp.cdr()
    return False

def applyPrimitiveFunction(foo,agruments):
    pattern=re.compile(r'c[a|d]+r')
    if foo=='+':
    	agruments=transList(agruments)
        return reduce(op.add,agruments,0)
    elif foo=='-':
    	agruments=transList(agruments)
        if len(agruments)==1:
            return -agruments[0]
        else:
            return reduce(op.sub,agruments[1:],agruments[0])
    elif foo=='*':
    	agruments=transList(agruments)
        return reduce(op.mul,agruments,1)
    elif foo=='/':
    	agruments=transList(agruments)
        if isinstance(agruments[0],float):
            return reduce(op.div,agruments[1:],agruments[0])
        else:
            return reduce(op.div,agruments[1:],fractions.Fraction(agruments[0],1))
    elif foo=='not':
        return not agruments.car()
    elif foo=='modulo':
    	agruments=transList(agruments)
        return agruments[0]%agruments[1]
    elif foo=='>':
    	agruments=transList(agruments)
        return reduce(op.and_,map(op.gt,agruments[:-1],agruments[1:]),True)
    elif foo=='<':
    	agruments=transList(agruments)
        return reduce(op.and_,map(op.lt,agruments[:-1],agruments[1:]),True)
    elif foo=='>=':
    	agruments=transList(agruments)
        return reduce(op.and_,map(op.ge,agruments[:-1],agruments[1:]),True)
    elif foo=='<=':
    	agruments=transList(agruments)
        return reduce(op.and_,map(op.le,agruments[:-1],agruments[1:]),True)
    elif foo=='=':
    	agruments=transList(agruments)
        return reduce(op.eq,map(op.eq,agruments[:-1],agruments[1:]),True)
    elif foo=='length':
        return Length(agruments.car())
    elif foo=='cons':
        return cons(agruments.car(),agruments.cdr().car())
    elif foo=='list':
        return agruments
    elif foo=='quotient':
    	agruments=transList(agruments)
        if len(agruments)!=2:
            raise SyntaxError("the number of parameters of quotient is uncorrect")
        if not isinstance(agruments[0],int) or not isinstance(agruments[1],int):
            raise SyntaxError("at least one parameter isn't integer")
        return agruments[0]/agruments[1]
    elif foo=='number?':
    	agruments=transList(agruments)
        if len(agruments)!=1:
            raise SyntaxError("the number of parameter of number? is uncorrect")
        return isnumber(agruments[0])
    elif foo=='integer?':
    	agruments=transList(agruments)
        if len(agruments)!=1:
            raise SyntaxError("the number of parameter of integer? is uncorrect")
        return isinstance(agruments[0],numbers.Number) and agruments[0]==int(agruments[0])
    elif foo=='append':
    	agruments=transList(agruments)
        return evalAppend(agruments)
    elif foo=='list?':
    	return isList(agruments.car())
    elif foo=='null?':
        return agruments.car()==Nil
    elif foo=='symbol?':
        return isQuoted(agruments.car())
    elif foo=='display':
        display(agruments.car())
    elif foo=='list-ref':
    	agruments=transList(agruments)
        return listref(agruments[0],agruments[1])
    elif foo=='memq':
    	agruments=transList(agruments)
        return evalmemq(agruments[0],agruments[1],mydict())
    elif foo=='assq':
    	agruments=transList(agruments)
        return evalassq(agruments[0],agruments[1],mydict())
    elif foo=='pair?':
        return agruments.car()!=Nil and isinstance(agruments.car(),Pair)
    elif foo=='newline':
        print
    elif pattern.match(foo)!=None and foo==foo[pattern.match(foo).start():pattern.match(foo).end()]:
        return catch(foo[1:-1],agruments.car())
    else:
        raise NameError("Doesn't exist or lock of implementation this primitive Object %s"%(foo,))

def isBaseFunctions(foo,env):
    if not isinstance(foo,str):
        return False
    if foo in env.BaseFunctions:
        return True
    pattern=re.compile(r'c[a|d]+r')
    if pattern.match(foo)!=None and foo==foo[pattern.match(foo).start():pattern.match(foo).end()]:
        return True
    return False

def applyPrimitiveObject(body,env):
    foo=body[0]
    parameters=map(lambda x:transValue(process(x,env),env),body[1:])
    agruments=List(parameters)
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
			if not isinstance(foo,tuple):
				foo=process(foo,env)
			if isinstance(foo,bool):
				raise Exception("Can't find this object")
	if not isinstance(foo,tuple):
		return foo
	body,parameters,ENV=foo
	agruments=exp[1:]
	local_env=mydict(ENV)
	#if not isinstance(exp[0],list) and not isinstance(exp[0],tuple):
		#local_env.addObject(exp[0],makeObject(parameters,body,local_env))
	temp=len(agruments)
	for i in xrange(temp):
		if parameters[i]=='.':            
			local_env.addObject(parameters[i+1],List(map(lambda x:process(x,env),agruments[i:])))
			break
		local_env.addObject(parameters[i],process(agruments[i],env))
	return process(body,local_env)

def isFunction(exp,env):
	if isinstance(exp,tuple) and len(exp)==3:
		return True
	if exp[0]=='lambda':
		return True
	if isinstance(env.findObject(exp[0]),tuple):
		return True
	return False

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
    if isinstance(obj1,str) and isinstance(obj2,str) and obj1[:2]=='#\\' and obj2[:2]=='#\\':
        return obj1==obj2
    if isQuoted(obj1) and isQuoted(obj2):
        return obj1.lower()==obj2.lower()
    if isnumber(obj1) and isnumber(obj2):
        return obj1==obj2
    if isstring(obj1) and isstring(obj2):
    	return obj1==obj2
    if isinstance(obj1,str) and isinstance(obj2,str) and obj1[0]!='"':
        return obj1==obj2
    return obj1 is obj2

def evalEqual(obj1,obj2,env):
    obj1=process(obj1,env)
    obj2=process(obj2,env)
    if isinstance(obj1,Pair) and isinstance(obj2,Pair):
        return pairEqual(obj1,obj2)
    else:
        return evalEqv(obj1,obj2,env)

def evalLetstar(blinding,body,env):
    local_env=mydict(env)
    for i in blinding:
        local_env.addObject(i[0],process(i[1],local_env))
    return process(body,local_env)

def evalLetrec(blinding,body,env):
    local_env=mydict(env)
    for i in blinding:
        local_env.addObject(i[0],i[1])
    return process(body,local_env)

def evalLet(blinding,body,env):
    foo=['lambda']
    para=[]
    var=[]
    for i in blinding:
        var.append(i[0])
        para.append(i[1])
    foo.append(var)
    temp=None
    for i in body:
    	temp=process([foo+[i]]+para,env)
    return temp

def evalMap(fun,lst,env):
	lsts=[]
	for i in lst:
		lsts.append(transList(process(i,env)))
	l=len(lsts[0])
	res=[]
	for i in xrange(l):
		temp=[]
		for j in lsts:
			temp.append(j[i])
		res.append(applyFunction([fun]+temp,env))
	return List(res)


def evalApply(fun,lst,env):
	lst=process(lst,env)
	return applyFunction([fun]+transList(lst),env)

def process(exp,env):
    if not isinstance(exp,list):
        if isinstance(exp,numbers.Number):
            return exp
        elif isnumber(exp):
            return transnumber(exp)
        elif isstring(exp):
            return exp
        elif isQuoted(exp):
            return exp
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
            return makeObject(exp[1],exp[2:],env)
        else:
            return makeObject(exp[1],exp[2],env)
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
        return evalEqual(exp[1],exp[2],env)
    elif exp[0]=='let':
        return evalLet(exp[1],exp[2:],env)
    elif exp[0]=='let*':
        return evalLetstar(exp[1],exp[2:],env)
    elif exp[0]=='letrec':
        return evalLetrec(exp[1],exp[2:],env)
    elif exp[0]=='quote':
        if isinstance(exp[1],list):
            return Nil
        return transQuoted(exp[1])
    elif exp[0]=='apply':
        return evalApply(exp[1],exp[2],env)
    elif exp[0]=='map':
    	return evalMap(exp[1],exp[2:],env)
    elif exp[0]=='QUOTE':
        if len(exp)==1:
            return Nil
        return evalQuoted(exp[1:],env)
    else:
        return applyFunction(exp,env)
