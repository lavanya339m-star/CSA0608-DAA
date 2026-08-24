n=int(input())
arr=list(map(int,input().split()))
target=int(input())

low=0
high=n-1
index=-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        index=mid
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1

print("Index =",index)
