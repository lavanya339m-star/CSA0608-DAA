def find_min_max(arr,low,high):
    if low==high:
        return arr[low],arr[low]
    mid=(low+high)//2
    min1,max1=find_min_max(arr,low,mid)
    min2,max2=find_min_max(arr,mid+1,high)
    return min(min1,min2),max(max1,max2)

n=int(input())
arr=list(map(int,input().split()))

minimum,maximum=find_min_max(arr,0,n-1)

print("Minimum Mark =",minimum)
print("Maximum Mark =",maximum)
