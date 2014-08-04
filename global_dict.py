#-*-coding:utf8-*-

######### global_dict class
import operator as op
from mutual_with_text import *
import math

class mydict:
    BaseFunctions=('+','-','*','/','not','modulo','>','<','>=','<=',
                  '=','length','cons','list','number?','integer?','quotient',
                   'append','list?','null?','pair?','list-ref','memq','assq',
                  'symbol?','display','newline')
    
    def __init__(self,father=None):
        self.father=father
        self.object={}
        if father==None:
            self.addObject('#t',True)
            self.addObject('#f',False)

    def findObject(self,name):
        if isinstance(name,list) or isinstance(name,tuple):
            return None
        w=self
        while w!=None:
            if name in w.object:
                return w.object[name]
            else:
                w=w.father
        return None

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

    def update(self,x):
        for i in x.object.iteritems():
            self.object[i[0]]=i[1]
