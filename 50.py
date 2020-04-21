from sys import stdin,stdout

test=int(stdin.readline())

for _ in range(test):
    n,a=[int(i) for i in stdin.readline().split()]

    mat=[]
    temp=[]
    for i in range(n):
        temp.append(a)

    for i in range(n):
        mat.append(temp)

    for i in range(n):
        for j in range(n):
            stdout.write(str(mat[i][j])+' ')
        stdout.write('\n')



