def sequential_search(arr,key):
    comparisons=0
    for i in range(len(arr)):
        comparisons+=1
        if arr[i]==key:
            return i+1,comparisons
    return -1,comparisons

arr=[12,25,8,45,32,19,50]
key=32
position,comparisons=sequential_search(arr,key)

if position!=-1:
    print("Element found at position",position)
    print("Number of comparisons =",comparisons)
else:
    print("Element not found")
    print("Number of comparisons =",comparisons)
