def check(s):
    if len(s)==1:
        return s[0]=='*'
    else:
        left=[]
        star=[]
        for index,item in enumerate(s):
            if item=='(':
                left.append(index)
            elif item=='*':
                star.append(index)
            else:
                if len(left)==0 and len(star)==0:
                    return False
                if len(left)>0:
                    left.pop()
                else:
                    star.pop()
        
        if len(left)==0:
            return True
        else:
            left.reverse()
            for item in left:
                if len(star):
                    if item>star[-1]:
                        return False
                    else:
                        star=star[:-1]
                else:
                    return False
            return True
                    
print(check("()*()(()(*()(((())()()())*))()*()(*)(((*))(())(())((*()*(()(())()*(((*(**))((())*)(((()()))(())()))"))
                    
