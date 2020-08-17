'''
Given an array of n elements. We need to answer q 
queries telling the sum of elements in range l to 
r in the array.

Prefix sum
'''


from sys import stdin,stdout

n=int(stdin.readline())

arr=list(map(int,stdin.readline().split()))

tot=0
preSum=[]

for i in range(n):
    tot+=arr[i]
    preSum.append(tot)

q=int(stdin.readline())

for i in range(q):
    query=list(map(int,stdin.readline().split()))

    L,R=query[0],query[1]

    if L>0:
        ans=preSum[R]-preSum[L-1]
    else:
        ans=preSum[R]

    stdout.write(str(ans)+'\n')
