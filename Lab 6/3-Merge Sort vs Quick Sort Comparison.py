merge_count=0
quick_count=0

def merge_sort(arr):
    global merge_count
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        merge_count+=1
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

def partition(arr,low,high):
    global quick_count
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        quick_count+=1
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)

n=int(input())
arr=list(map(int,input().split()))

merge_result=merge_sort(arr.copy())

quick_result=arr.copy()
quick_sort(quick_result,0,n-1)

print("Sorted Array :",*merge_result,sep=",")
print("Merge Comparisons :",merge_count)
print("Quick Comparisons :",quick_count)
