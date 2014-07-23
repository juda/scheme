#!/usr/bin/python2
from mutual_with_text import *
from global_dict import *
from process import process
from parse import *
import pdb
from pair import *

def repl():
    '''read-eval-print-loop'''
    global_env=mydict()
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
        statement=statement.split(';')[0]
        if statement=='exit':
            exit(0)
        else:
            if statement[0]!='(':
                if isnumber(statement):
                    print transnumber(statement)
                elif isQuoted(statement):
                    print statement[1:]
                else:
                    print tostring(global_env.findObject(statement))
            else:
                try:
                    #pdb.set_trace()
                    val=process(parse(statement),global_env)
                    if val is not None:
                        if isinstance(val,Pair):
                            print '(%s)'%(showPair(val),)
                        elif isinstance(val,bool):
                            if val==True:
                                print '#t'
                            elif val==False:
                                print '#f'
                        else:
                            print tostring(val)
                except Exception as err:
                    print "[error]%s"%(err,)
        
if __name__=="__main__":
    repl()
