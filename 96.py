def submat(mat):
    rows=len(mat)
    cols=len(mat[0])
    
    if rows==1 and cols==1:
        return mat[0][0]==1
    else:
        ans=[]

        for _ in range(rows):
            temp=[0]*cols
            ans.append(temp)

        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==1:
                    count=0
                    k=i;l=j;c=j;
                    width=1
                    while k<rows and mat[k][c]==1:
                        l=c
                        while l<cols and mat[k][l]==1:
                            count+=1
                            l+=1
                        width=l
                        k+=1
                    ans[i][j]=count
                        
        tot=0
        for arr in ans:
            tot+=sum(arr)
        
        print(ans)
        return tot
                
mat=[[1,1],[1,0]]
print(submat(mat))