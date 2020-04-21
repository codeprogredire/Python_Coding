from sys import stdin,stdout

test=int(stdin.readline())

for _ in range(test):
    n,q=[int(i) for i in stdin.readline().split()]
    curr=0
    total=0
    for _ in range(q):
        f,d=[int(i) for i in stdin.readline().split()]
        temp=abs(f-curr)+abs(d-f)
        total+=temp
        curr=d
    stdout.write(str(total)+'\n')
