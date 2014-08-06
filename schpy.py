#!/usr/bin/python

from mutual_with_text import *
from global_dict import *
from process import process
from parse import *
import pdb
from pair import *
import sys

def repl():
    '''read-eval-print-loop'''
    global_env=mydict()
    sys.setrecursionlimit(10000)
    while True:
        print
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
        statement=statement.split(';')[0]
        if statement=='exit':
            exit(0)
        else:
            if statement[0]!='(':
                if isnumber(statement):
                    print transnumber(statement)
                elif isQuoted(statement):
                    print statement[1:]
                elif global_env.findObject(statement):
                    display(global_env.findObject(statement))
                else:
                    print tostring(statement)
            else:
                try:
                    pdb.set_trace()
                    temp=parse(statement)
                    val=process(temp,global_env)
                    display(val)
                except Exception as err:
                    print "[error]%s"%(err,)

def runFile():
    sys.setrecursionlimit(100000)
    global_env=mydict()
    f=open(sys.argv[1])
    statement=''
    #pdb.set_trace()
    for buff in f.xreadlines():
        statement+=buff.split(';')[0]
        statement=statement.strip()
        if not statement or not parentheseBalance(statement):
            continue
        if statement:
            try:
                val=process(parse(statement),global_env)
                display(val)
            except Exception as err:
                print "[error]%s"%(err,)
            statement=''
        
if __name__=="__main__":
    if len(sys.argv)==1:
        print "[mode]shell"
        repl()
    elif len(sys.argv)==2:
        print "[mode]file"
        runFile()
    else:
        print "<usage> python schpy.py [file]"
