'''
Max sum contioguous sub-array
quadratic time complexity : Brute force
'''

a=[-2,1,-3,4,-1,2,1,-5,4]
n=len(a)
sub_array=[]
for i in range(1,n+1):
    for j in range(n):
        if i+j<=n:
            sub_array.append(a[j:i+j])


max_sum=float('-inf')
for i in sub_array:
    sum=0
    for j in i:
        sum+=j
    if sum>=max_sum:
        max_sum=sum

print(max_sum)
 

