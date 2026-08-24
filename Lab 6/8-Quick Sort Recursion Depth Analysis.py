max_depth=0

def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quick_sort(arr,low,high,depth):
    global max_depth
    if low<high:
        max_depth=max(max_depth,depth)
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1,depth+1)
        quick_sort(arr,pi+1,high,depth+1)

n=int(input())
arr=list(map(int,input().split()))

quick_sort(arr,0,n-1,1)

print(*arr,sep=",")
print("Max Depth :",max_depth)
