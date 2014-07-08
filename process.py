#-*-coding:utf8-*-
from global_dict import mydict,PrimitiveProcedure
from mutual_with_text import *

def selfEvaluatiing(exp):
	return isnumber(exp) or isQuoted(exp)

def isVariable(exp):
	return  isinstance(exp,str)

def isQuoted(exp):
	return exp[0]=='"' and exp[-1]=='"'

def lookupVariableValue(exp,env):
	env.findVariable(exp)


def evalAssignment(exp,env):
	env.setVariable(exp[1],exp[2])


def evalDefinition(exp,env):
	if isinstance(exp[1],list):
		makeProcedure(exp[1:][1:],exp[2],env)
	else:
		env.addVariable(exp[1],process(exp[2]))

def evalIf(exp,env):
	if process(exp[1],env):
		return process(exp[2],env)
	else:
		return process(exp[3],env)

def makeProcedure(para,body,env):
	env.addLambda(body,para)

def evalSequence(exp,env):
	if len(exp)==1:
		return process(exp[0],env)
	else:
		process(exp[0],env)
		return evalSequence(exp[1:],env)

def condIf(exp,env):
	'''
	wating for completing
	'''
	pass

def isPrimitiveProcedure(procedure):
	for i in procedure:
		if isinstance(i,list):
			return False
	return procedure[0] in PrimitiveProcedure

def applyPrimitiveProcedure(procedure,agruments):
	pass

def procedureBody(procedure):
	pass

def extendEnvironment(para,agruments,env):
	pass

def procedureEnvironment(procedure):
	pass

def applyFunction(procedure,agruments):
	if isPrimitiveProcedure(procedure):
		return applyPrimitiveProcedure(procedure,agruments)
	else:
		return evalSequence(procedureBody(procedure),(extendEnvironment(proecedureParameters(procedure),agruments,procedureEnvironment(procedure))))

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
    elif exp[0]=='set!':
    	return evalAssignment(exp,env)
    elif exp[0]=='define':
    	return evalDefinition(exp,env)
    elif exp[0]=='if':
    	return evalIf(exp,env)
    elif exp[0]=='lambda':
    	return makeProcedure(exp[1],exp[2],env)
    elif exp[0]=='begin':
    	return evalSequence(exp[1:],env)
    elif exp[0]=='cond':
    	return condIf(exp,env)
    elif isApplication(exp):
    	return applyFunction((process(evalOperator(exp),env)),(listOfValues(operands(exp)),env))
    else:
    	raise SyntaxError("unknown expression type -- Eval")
