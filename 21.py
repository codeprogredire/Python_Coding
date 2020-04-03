'''
Max sum contiguous sub-array
Linear time
'''

A = list(map(int,input().split()))

def maxSubArray(A):
        windowSum = A[0]
        maxSum = A[0]
        
        for i in range(1,len(A)):
            windowSum = max(windowSum + A[i],A[i])
            maxSum = max(maxSum,windowSum)
        return maxSum

print(maxSubArray(A))