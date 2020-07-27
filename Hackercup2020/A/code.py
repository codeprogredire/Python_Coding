from sys import stdin,stdout
import math

stdin=open('input.txt','r')
stdout=open('output.txt','w')

test=int(stdin.readline())

for t in range(1,test+1):
    n=int(stdin.readline())
    inc=stdin.readline().rstrip('\n')
    out=stdin.readline().rstrip('\n')

    mat=[]

    for _ in range(n):
        temp=[]
        for _ in range(n):
            temp.append(0)
        mat.append(temp)

    for i in range(n):
        for j in range(i,n):
            if i==j:
                mat[i][j]='Y'
            elif (j-i)==1:
                if out[i]=='Y' and inc[j]=='Y':
                    mat[i][j]='Y'
                else:
                    mat[i][j]='N'
            elif mat[i][j-1]=='N':
                mat[i][j]='N'
            elif out[j-1]=='Y' and inc[j]=='Y':
                mat[i][j]='Y'
                mat[j-1][j]='Y'
            else:
                mat[i][j]='N'
                mat[j-1][j]='N'

    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            if (i-j)==1:
                if out[i]=='Y' and inc[j]=='Y':
                    mat[i][j]='Y'
                else:
                    mat[i][j]='N'
            elif mat[i][j+1]=='N':
                mat[i][j]='N'
            elif out[j+1]=='Y' and inc[j]=='Y':
                mat[i][j]='Y'
                mat[j+1][j]='Y'
            else:
                mat[i][j]='N'
                mat[j+1][j]='N'

    stdout.write('Case #'+str(t)+':\n')
    for i in range(n):
        for j in range(n):
            stdout.write(str(mat[i][j]))
        stdout.write('\n')




    


