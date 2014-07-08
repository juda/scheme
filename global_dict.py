#-*-coding:utf8-*-

######### global_dict class
import operator as op
import math
from process import process

class mydict:
    def __init__(self,father=None):
        self.father=father
        self.procedure={}
        self.variable={}

    def addLambda(body,para):
        self.procedure[body]=para

    def addVariable(name,value):
        self.variable[name]=value

    def findVariable(name):
        w=self
        while w!=None:
            if name in w:
                return w[name]
            else:
                w=w.father
        raise NameError("Don't Exist the variable %d"%(name,))

    def setVariable(name,value):
        w=self
        while w!=None:
            if name in w:
                w[name]=value
                return
            else:
                w=w.father
        raise NameError("Don't Exist the variable %d"%(name,))
