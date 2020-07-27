from sys import stdin,stdout

test=int(stdin.readline())

def check(TS,JS):
    while TS%2==0 and JS%2==0:
        TS//=2
        JS//=2
    if JS%2:
        return False
    elif TS%2 and JS%2==0:
        return True




for _ in range(test):
    TS=int(stdin.readline())
    if test<=100 and TS<=100:
        if TS%2: #TS is odd
            ans=TS//2
        else:
            #TS is even
            ans=0
            for i in range(2,TS+2,2):
                ans+=check(TS,i)
        stdout.write(str(ans)+'\n')
    else:
        if TS%2:
            ans=TS//2
        else:
            ans=0
            for i in range(2,TS+2,2):
                ans+=check(TS,i)
        stdout.write(str(ans)+'\n')
        

    