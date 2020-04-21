from sys import stdin,stdout

n,m,c=[int(i) for i in stdin.readline().split()]

arr=[c]*n

for _ in range(m):
    op=stdin.readline().split()

    if len(op)==2:
        stdout.write(str(arr[int(op[1])-1])+'\n')
    else:
        start=int(op[1])-1
        end=int(op[2])
        k=int(op[3])

        for i in range(start,end):
            arr[i]+=k

