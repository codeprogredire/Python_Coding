def mergesort(arr,p,r):
    if p<r:
        q=(p+r)//2
        mergesort(arr,p,q)
        mergesort(arr,q+1,r)
        merge(arr,p,q,r)

def merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*n1
    R=[0]*n2

    for i in range(n1):
        L[i]=arr[i+p]

    for j in range(n2):
        R[j]=arr[j+q+1]

    i=0;j=0;k=p

    while i<n1 and j<n2:
        if L[i]<R[j]:
            arr[k]=L[i]
            k+=1
            i+=1
        else:
            arr[k]=R[j]
            k+=1
            j+=1
    
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1

    while j<n2:
        arr[k]=R[j]
        k+=1
        j+=1




arr=list(map(int,input().split()))
mergesort(arr,0,len(arr)-1)
print(arr)
