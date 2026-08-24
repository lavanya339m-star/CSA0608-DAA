n=int(input())
arr=list(map(int,input().split()))
key=int(input())

low=0
high=n-1
result=-1

while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        result=mid
        high=mid-1
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1

if result!=-1:
    print("First occurrence at index",result)
else:
    print("Element not found")Find the First Occurrence of an Element
