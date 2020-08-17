'''
Maximum sum of contiguous sub-array using DnC
'''


def helper(nums,l,m,h):
    tot=0;leftsum=float('-inf')
    for i in range(m,l-1,-1):
        tot+=nums[i]
        leftsum=max(leftsum,tot)
    
    tot=0;rightsum=float('-inf')
    for i in range(m+1,h+1):
        tot+=nums[i]
        rightsum=max(rightsum,tot)

    return max(leftsum,rightsum,leftsum+rightsum)




def maxSubArray(nums,l,h):
    if l==h:
        return nums[0]
    else:
        m=(l+h)//2
        lsum=maxSubArray(nums,l,m)
        rsum=maxSubArray(nums,m+1,h)
        
    return max(lsum,rsum,helper(nums,l,m,h))

while True:
    n=int(input())
    nums=list(map(int,input().split()))
    print(maxSubArray(nums,0,n-1))
