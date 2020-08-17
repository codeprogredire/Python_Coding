from sys import stdin,stdout
import math

for _ in range(int(stdin.readline())):
    Pc,Pr=list(map(int,stdin.readline().split()))

    dc=math.ceil(Pc/9)
    dr=math.ceil(Pr/9)

    if dc==dr or dr<dc:
        ans=str(1)+' '+str(dr)+'\n'
        stdout.write(ans)
    else:
        ans=str(0)+' '+str(dc)+'\n'
        stdout.write(ans)