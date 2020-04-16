s=input()

def steps(s):
    length=len(s)
    if length==1:
        return 0
    else:
        num=int(s)
        dec=0
        for i in range(1,length+1):
            dec+= int(s[i-1])*(2**(length-i))
        
        count=0
        while dec!=1:
            count+=1
            if dec%2==0:
                dec=dec//2
            else:
                dec+=1

    return count

print(steps(s))