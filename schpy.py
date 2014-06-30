#!/usr/bin/python2


def parentheseBalance(statement):
    res=0
    for i in statement:
        if i=='(':
            res+=1
        elif i==')':
            res-=1
        if res<0:
            raise SyntaxError('Unmatched parentheses')
    return res==0

def isnumber(number):
    try:
        int(number)
    except ValueError:
        try:
            float(number)
        except ValueError:
            return False
        return True
    return True

def transnumber(number):
    try:
        return int(number)
    except ValueError:
        return float(number)

def decompose(statement):
    res=[]
    statement+=' '
    count=0
    now=''
    for i in statement:
        if i==' ':
            if now!='' and count==0:
                res.append(now)
                now=''
            else:
                now+=i
        elif i=='(':
            now+=i
            count+=1
        elif i==')':
            now+=i
            count-=1
        else:
            now+=i
    return res

def calc(statement,mapping):
    if statement[0]!='(':
        if isnumber(statement):
            return transnumber(statement)
        else:
            return mapping.env[statement]
    else:
        statement=decompose(statement[1:-1])
        if statement[0]=='define':
            mapping.addvar(statement[1],calc(statement[2],mapping))

class global_Env():
    env={}
    def addvar(self,name,exp):
        self.env[name]=exp

global_env=global_Env()
while True:
    statement=''
    isline=True
    while True:
        if isline:
            statement+=raw_input('> ')
        else:
            statement+=raw_input('  ')
        if parentheseBalance(statement):
            break
        else:
            isline=False
    if statement=='exit':
        exit(0)
    else:
        if statement[0]!='(':
            if isnumber(statement):
                print transnumber(statement)
            else:
                print global_env.env[statement]
        else:
            calc(statement,global_env)
        
