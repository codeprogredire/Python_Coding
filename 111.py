'''
Link: https://leetcode.com/problems/trapping-rain-water/submissions/
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n==0:
            return 0
        maxleft=[height[0]]*n
        maxright=[height[n-1]]*n

        for i in range(1,n):
            maxleft[i]=max(maxleft[i-1],height[i])
            maxright[n-1-i]=max(maxright[n-i],height[n-1-i])


        tot=0

        for i in range(1,n-1):
            tot+=max(min(maxleft[i-1],maxright[i+1])-height[i],0)

        return tot

        