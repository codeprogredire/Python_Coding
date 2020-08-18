'''
Link: https://www.interviewbit.com/problems/add-one-to-number/
'''


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        digit=1
        n=len(A)
        for i in range(n-1,-1,-1):
            temp=A[i]+digit
            digit=temp//10
            A[i]=temp%10
            if digit==0:
                break
        
        if digit:
            A=[digit]+A
            
        while A[0]==0:
            A.remove(A[0])
            
        return A
            
