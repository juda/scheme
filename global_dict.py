#-*-coding:utf8-*-

######### global_dict class
import operator as op
from mutual_with_text import *
import math

class mydict:
    def __init__(self,father=None):
        self.father=father
        self.procedure={}
        self.variable={}

    def findProcedure(self,name):
        w=self
        while w!=None:
            if name in w.procedure:
                return w.procedure[name]
            else:
                w=w.father
        return False

    def addVariable(self,name,value):
        self.variable[name]=value

    def findVariable(self,name):
        w=self
        while w!=None:
            if name in w.variable:
                if isnumber(w.variable[name]):
                    return w.variable[name]
                else:
                    return self.findVariable(w.variable[name])
            else:
                w=w.father
        return False

    def setVariable(self,name,value):
        w=self
        while w!=None:
            if name in w.variable:
                w.variable[name]=value
                return
            else:
                w=w.father
        raise NameError("Doesn't Exist the variable %s"%(name,))
