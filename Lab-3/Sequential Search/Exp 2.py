def sequential_search(arr,key):
    comparisons=0
    for i in range(len(arr)):
        comparisons+=1
        if arr[i]==key:
            return i+1,comparisons
    return -1,comparisons

arr=[5,10,15,20,25,30,35]
key=18
position,comparisons=sequential_search(arr,key)

if position!=-1:
    print("Element found at position",position)
else:
    print("Element not found")

print("Number of comparisons =",comparisons)
