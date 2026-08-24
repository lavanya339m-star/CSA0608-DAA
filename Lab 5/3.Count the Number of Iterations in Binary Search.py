n=int(input())
arr=list(map(int,input().split()))
key=int(input())

low=0
high=n-1
iterations=0
found=False

while low<=high:
    iterations+=1
    mid=(low+high)//2
    if arr[mid]==key:
        found=True
        break
    elif arr[mid]<key:
        low=mid+1
    else:
        high=mid-1

if found:
    print("Element found")
else:
    print("Element not found")

print("Iterations =",iterations)
