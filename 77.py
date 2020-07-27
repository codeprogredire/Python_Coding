from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    s=stdin.readline()
    n=len(s)
    
    i=0;count=0;
    while i<n:
        temp=s[i:i+2]
        if temp=='xy' or temp=='yx':
            count+=1
            i+=2
        else:
            i+=1

    stdout.write(str(count)+'\n')