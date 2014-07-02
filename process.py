#-*-coding:utf8-*-
def process(statement,env):
    '''
    处理statement语句，使之成为正确python语法
    '''
    translation(statement,env)
    if len(statement)==1:
        return statement
    else:
        if statement[0]=='if':
            
