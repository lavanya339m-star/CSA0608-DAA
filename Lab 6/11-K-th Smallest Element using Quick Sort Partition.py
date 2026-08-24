def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def kth_smallest(arr,low,high,k):
    if low<=high:
        p=partition(arr,low,high)
        if p==k-1:
            return arr[p]
        elif p>k-1:
            return kth_smallest(arr,low,p-1,k)
        else:
            return kth_smallest(arr,p+1,high,k)

n=int(input())
arr=list(map(int,input().split()))
k=int(input())

print(kth_smallest(arr,0,n-1,k))
