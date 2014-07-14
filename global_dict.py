#-*-coding:utf8-*-

######### global_dict class
import operator as op
from mutual_with_text import *
import math

class mydict:
    def __init__(self,father=None):
        self.father=father
        self.object={}

    def findObject(self,name):
        w=self
        while w!=None:
            if name in w.object:
                return w.object[name]
            else:
                w=w.father
        return False

    def addObject(self,name,value):
        self.object[name]=value

    def setObject(self,name,value):
        w=self
        while w!=None:
            if name in w.object:
                w.object[name]=value
                return
            else:
                w=w.father
        raise NameError("Doesn't Exist the variable %s"%(name,))
