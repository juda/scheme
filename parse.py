def tokenize(statement):
    return statement.replace('(',' ( ').replace(')',' ) ').split()

def parse_recursion(token):
    token=token[1:-1]
    #print token
    res=[]
    level=[]
    num=0
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
            if num==0:
                res.append(i)
            else:
                level.append(i)
    if num!=0:
        raise SyntaxError('Unmatched parentheses')
    return res

def parse(statement):
    token=tokenize(statement)
    #print token
    return parse_recursion(token)
