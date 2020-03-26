m = int(input('Enter m : '))
n = int(input('Enter n : '))
p = int(input('Enter p : '))

mat1 = []


for i in range(m):
	temp = []
	for j in range(n):
		temp.append(int(input()))
	mat1.append(temp)

mat2 = []

for i in range(n):
	temp = []
	for j in range(p):
		temp.append(int(input()))
	mat2.append(temp)

print('First matrix : ')

for i in range(m):
	for j in range(n):
		print(mat1[i][j],end=' ')
	print()
	
print('Second matrix : ')

for i in range(n):
	for j in range(p):
		print(mat2[i][j],end=' ')
	print()

mat4 = []

for i in range(m):
	temp = []
	for j in range(p):
		temp.append(0)
	mat4.append(temp)
	
# Martix multiplication

for i in range(m):
	for j in range(n):
		for k in range(p):
			mat4[i][k]+=mat1[i][j]*mat2[j][k]
			
print('Resultant matrix (Multiplication) :')

for i in range(m):
	for j in range(p):
		print(mat4[i][j],end=' ')
	print()
