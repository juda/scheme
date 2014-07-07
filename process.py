#-*-coding:utf8-*-
from global_dict import mydict
from mutual_with_text import *

def selfEvaluatiing(exp):
	if len(exp)==1  and isnumber(exp):
		return True
	else:
		return False

def isVariable(exp):
	return  len(exp)==1 and isinstance(exp,str)

def isQuoted(exp):
	for i in exp:
		if not isinstance(exp,str):
			return False
	return exp[0][0]=='"' and exp[-1][-1]=='"'


def process(exp,env):
    if selfEvaluating(exp):
    	return exp
    elif isVariable(exp):
    	return lookup
