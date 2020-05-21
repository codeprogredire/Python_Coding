'''
Counting number of inversions in an array
'''

def mergesort(arr):
    # temp_arr to store sorted array in merge function
    temp_arr=[0]*len(arr)
    return _mergesort(arr,temp_arr,0,len(arr)-1)



def _mergesort(arr,temp_arr,p,r):
    inv_count=0
    if p<r:
        q=(p+r)//2
        inv_count+=_mergesort(arr,temp_arr,p,q)
        inv_count+=_mergesort(arr,temp_arr,q+1,r)
        inv_count+=merge(arr,temp_arr,p,q,r)

    return inv_count

def merge(arr,temp_arr,p,q,r):
    inv_count=0
    i=p
    j=q+1
    k=p

    while i<=q and j<=r:
        if arr[i]<arr[j]:
            temp_arr[k]=arr[i]
            k+=1
            i+=1
        else:
            inv_count+=(q-i+1)
            temp_arr[k]=arr[j]
            j+=1
            k+=1

    while i<=q:
        temp_arr[k]=arr[i]
        k+=1
        i+=1

    while j<=r:
        temp_arr[k]=arr[j]
        k+=1
        j+=1

    for index in range(p,r+1):
        arr[index]=temp_arr[index]

    return inv_count


arr=list(map(int,input().split()))
print(mergesort(arr))