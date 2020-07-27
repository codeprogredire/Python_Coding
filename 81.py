def merge(arr1,arr2):
    i=0;j=0;n1=len(arr1);k=0;ans=[];n2=len(arr2)

    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            ans.append(arr1[i])
            i+=1
        else:
            ans.append(arr2[j])
            j+=1

    while i<n1:
        ans.append(arr1[i])
        i+=1
    
    while j<n2:
        ans.append(arr2[j])
        j+=1

    return ans

k=int(input('Enter k : '))
n=int(input('Enter n : '))


arr=[]
for i in range(k):
    temp=list(map(int,input().split()))
    arr.append(temp)

print(arr)


'''
arr1=[1,3,5,7]
arr2=[2,4,16,18]
arr3=[6,8,10,12]
print(merge(merge(arr1,arr2),arr3))
            '''