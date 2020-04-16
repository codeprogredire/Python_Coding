'''

Leetcode weekly 184
'''

def processQueries(queries,m):
        ans=[]
        P=[]
        for i in range(1,m+1):
            P.append(i)
    
        for i in range(len(queries)):
            index=P.index(queries[i])
            ans.append(index)
            del(P[index])
            P=[queries[i]]+P
        return ans

queries=[7,5,5,8,3]
m=8
print(processQueries(queries,m))