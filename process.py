#-*-coding:utf8-*-
from global_dict import mydict
from mutual_with_text import *

def selfEvaluatiing(exp):
	return isnumber(exp) or isQuoted(exp)

def isVariable(exp):
	return  isinstance(exp,str)

def isQuoted(exp):
	return exp[0]=='"' and exp[-1]=='"'

def lookupVariableValue(exp,env):
	'''
	wating for completing
	'''
	pass

def isAssignment(exp):
	'''
	wating for completing
	'''
	pass

def evalAssignment(exp,env):
	'''
	wating for completing
	'''
	pass

def isDefinition(exp):
	'''
	wating for completing
	'''
	pass

def evalDefinition(exp,env):
	'''
	wating for completing
	'''
	pass

def evalIf(exp,env):
	'''
	wating for completing
	'''
	pass

def makeProcedure(para,body,env):
	'''
	wating for completing
	'''
	pass

def lambdaParameters(exp):
	'''
	wating for completing
	'''
	pass

def lambdaBody(exp):
	'''
	wating for completing
	'''
	pass

def evalSequence(exp,env):
	'''
	wating for completing
	'''
	pass

def beginActions(exp):
	'''
	wating for completing
	'''
	pass

def condIf(exp,env):
	'''
	wating for completing
	'''
	pass

def applyFunction(exp,para):
	'''
	wating for completing
	'''
	pass

def evalOperator(exp):
	'''
	wating for completing
	'''
	pass

def listOfValues(exp):
	'''
	wating for completing
	'''
	pass

def operands(exp):
	'''
	wating for completing
	'''
	pass

def process(exp,env):
    if selfEvaluating(exp):
    	return exp
    elif isVariable(exp):
    	return lookupVariableValue(exp,env)
    elif isQuoted(exp):
    	return exp
    elif isAssignment(exp):
    	return evalAssignment(exp,env)
    elif isDefinition(exp):
    	return evalDefinition(exp,env)
    elif exp[0]=='if':
    	return evalIf(exp,env)
    elif exp[0]=='lambda':
    	return makeProcedure(lambdaParameters(exp[1]),lambdaBody(exp[2]),env)
    elif exp[0]=='begin':
    	return evalSequence(beginActions(exp),env)
    elif exp[0]=='cond':
    	return condIf(exp,env)
    elif isApplication(exp):
    	return applyFunction((process(evalOperator(exp),env)),(listOfValues(operands(exp)),env))
    else:
    	raise SyntaxError("unknown expression type -- Eval")
