threshold=4

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

def hybrid_merge_sort(arr):
    if len(arr)<=threshold:
        return insertion_sort(arr)
    mid=len(arr)//2
    left=hybrid_merge_sort(arr[:mid])
    right=hybrid_merge_sort(arr[mid:])
    return merge(left,right)

n=int(input())
arr=list(map(int,input().split()))

result=hybrid_merge_sort(arr)

print(*result,sep=",")
