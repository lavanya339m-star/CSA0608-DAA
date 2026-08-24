count=0

def partition(arr,low,high):
    global count
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        count+=1
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

quick_sort(arr,0,n-1)

print(*arr,sep=",")
print("Comparisons :",count)
