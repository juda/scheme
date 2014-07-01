#!/usr/bin/python2
from read_from_text import *
from global_dict import *

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
            else:
                print global_env.env[statement]
        else:
            process(statement)
        
