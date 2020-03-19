'''
Multiplication of two square matrices
'''
n = int(input('Enter order of matrix : '))

print('Enter {} elements : '.format(n*n))
a=[]
for _ in range(n):
    temp=[]
    for _ in range(n):
        temp.append(int(input()))
    a.append(temp)

print('Enter {} elements : '.format(n*n))
b=[]
for _ in range(n):
    temp=[]
    for _ in range(n):
        temp.append(int(input()))
    b.append(temp)

c=[]
for _ in range(n):
    temp=[]
    for _ in range(n):
        temp.append(0)
    c.append(temp)

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]

print(a)
print(b)
print(c)




