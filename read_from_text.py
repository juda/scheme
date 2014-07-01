'''read from text'''

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
