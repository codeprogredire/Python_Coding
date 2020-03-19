'''
Sum of two matrices
'''

rows=int(input())
cols=int(input())

a=[]
print('Enter {} elements : '.format(rows*cols))
for _ in range(rows):
    temp=[]
    for _ in range(cols):
        temp.append(int(input()))
    a.append(temp)

b=[]
print('Enter {} elements : '.format(rows*cols))

for _ in range(rows):
    temp=[]
    for _ in range(cols):
        temp.append(int(input()))
    b.append(temp)

c=[]
for _ in range(rows):
    temp=[]
    for _ in range(cols):
        temp.append(0)
    c.append(temp)

for i in range(rows):
    for j in range(cols):
        c[i][j]=a[i][j]+b[i][j]

print(a)
print(b)
print(c)