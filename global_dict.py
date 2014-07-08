#-*-coding:utf8-*-

######### global_dict class
import operator as op
from mutual_with_text import *
import math
from process import process

class mydict:
    def __init__(self,father=None):
        self.father=father
        self.procedure={}
        self.variable={}

    def findProcedure(name):
        w-self.procedure
        while w!=None:
            if name in w:
                return w[name]
            else:
                w=w.father
        raise NameError("Doesn't exist the procedure %d"%(name,))

    def addVariable(name,value):
        self.variable[name]=value

    def findVariable(name):
        w=self.variable
        while w!=None:
            if name in w:
                if isnumber(w[name]):
                    return w[name]
                else:
                    return self.findVariable(w[name])
            else:
                w=w.father
        raise NameError("Doesn't Exist the variable %d"%(name,))

    def setVariable(name,value):
        w=self.variable
        while w!=None:
            if name in w:
                w[name]=value
                return
            else:
                w=w.father
        raise NameError("Don't Exist the variable %d"%(name,))
