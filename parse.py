#-*-coding:utf8-*-

def tokenize(statement):
    flag=False
    i=0
    while True:
        try:
            statement[i]
        except IndexError:
            break
        if statement[i]=='"':
            flag=not flag
        elif statement[i]==' ':
            if flag:
                statement=statement[:i]+'[blank]'+statement[i+1:]
                i+=6
        elif statement[i:i+2]=="'(":
            if not flag:
                statement=statement[:i]+'(quote '+statement[i+2:]
                i+=6
        i+=1
    statement=statement.replace('(',' ( ').replace(')',' ) ').split()
    j=len(statement)
    for i in xrange(j):
        statement[i]=statement[i].replace('[blank]',' ')
    return statement

def parse_recursion(token):
    token=token[1:-1]
    #print token
    res=[]
    level=[]
    num=0
    flag=0
    for i in token:
        if i==')':
            num-=1
            if num<0:
                raise SyntaxError('Unmatched parentheses')
            level.append(i)
            if num==0:
                res.append(parse_recursion(level))
                level=[]
        elif i=='(':
            num+=1
            level.append(i)
        else:
            if i[0]=='"':
                flag=1
            if num==0:
                res.append(i)
            else:
                level.append(i)
    if num!=0:
        raise SyntaxError('Unmatched parentheses')
    return res

def parse(statement):
    '''
    对一个语句进行分词，结果返回分词后的字符流
    
    >>> parse("(define (x y) (+ y 3))")
    ['define', ['x', 'y'], ['+', 'y', '3']]
    '''
    token=tokenize(statement)
    #print token
    return parse_recursion(token)
