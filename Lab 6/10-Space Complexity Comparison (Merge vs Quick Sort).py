import sys

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
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

def quick_sort(arr,low,high):
    if low<high:
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if arr[j]<=pivot:
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        p=i+1
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

n=int(input())
arr=list(map(int,input().split()))

merge_result=merge_sort(arr.copy())
quick_result=arr.copy()
quick_sort(quick_result,0,n-1)

merge_space=n*32
quick_space=n*16

print("Sorted :",*merge_result,sep=",")
print("Merge Space :",merge_space,"bytes")
print("Quick Space :",quick_space,"bytes")
