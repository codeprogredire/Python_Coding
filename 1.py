'''Finding minimum element in an array'''

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

min = arr[0]
for i in range(1,len(arr)):
    if int(arr[i]) < min:
        min = arr[i]

print(min)
