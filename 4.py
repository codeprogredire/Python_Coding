'''
Matrix multiplication a[m][n] * b[n][p]
'''

row1 = int(input('Enter number of rows in first matrix : '))
col1 = int(input('Enter number of columns in first matrix : '))

a=[]

print('Enter {} elements : '.format(row1*col1))

for _ in range(row1):
    temp=[]
    for _ in range(col1):
        temp.append(int(input()))
    a.append(temp)

row2 = int(input('Enter number of rows in second matrix : '))
col2 = int(input('Enter number of columns in second matrix : '))

b=[]

print('Enter {} elements : '.format(row2*col2))

for _ in range(row2):
    temp=[]
    for _ in range(col2):
        temp.append(int(input()))
    b.append(temp)

if col1!=row2:
    print('Matrix multiplication is not possible here.')
else:
    c=[]
    for _ in range(row1):
        temp=[]
        for _ in range(col2):
            temp.append(0)
        c.append(temp)
    
    for i in range(row1):
        for j in range(col2):
            for k in range(row2):
                c[i][j]+=a[i][k]*b[k][j]

    print('First matrix : ')
    for i in range(row1):
        for j in range(col1):
            print(a[i][j],end=' ')
        print()

    print('Second matrix : ')
    for i in range(row2):
        for j in range(col2):
            print(b[i][j],end=' ')
        print()

    print('Resultant matrix : ')
    for i in range(row1):
        for j in range(col2):
            print(c[i][j],end=' ')
        print()
