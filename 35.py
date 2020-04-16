'''
For a binary array,
calculate max length of subarray containing 
equal  no. of 0s and 1s.
'''

nums=list(map(int,input().split()))

maxlen=0
n=len(nums)

for i in range(n):
    zeroCount=0
    oneCount=0
    for j in range(i,n):
        if nums[j]==0:
            zeroCount+=1
        else:
            oneCount+=1
        if zeroCount==oneCount:
            maxlen=max(maxlen,j-i+1)

print(maxlen)