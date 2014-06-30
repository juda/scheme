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
        print statement
        
