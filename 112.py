'''
Link: https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        n=len(A)
        
        tot=0
        
        for i in range(n-1):
            x=abs(A[i]-A[i+1])
            y=abs(B[i]-B[i+1])
            
            #tot+=min(x,y)+abs(x-y)
            tot+=max(x,y)
        
        return tot
            
            
