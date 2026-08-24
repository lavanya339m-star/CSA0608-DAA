def sequential_search(arr,key):
    comparisons=0
    for i in range(len(arr)):
        comparisons+=1
        if arr[i]==key:
            return i+1,comparisons
    return -1,comparisons

def sentinel_search(arr,key):
    a=arr.copy()
    a.append(key)
    i=0
    comparisons=0
    while a[i]!=key:
        comparisons+=1
        i+=1
    comparisons+=1
    if i<len(arr):
        return i+1,comparisons
    return -1,comparisons

arr=[14,9,22,35,18,41,27]
key=18

pos1,comp1=sequential_search(arr,key)
pos2,comp2=sentinel_search(arr,key)

print("Ordinary Sequential Search")
print("Position found:",pos1)
print("Comparison count:",comp1)
print("Sentinel Sequential Search")
print("Position found:",pos2)
print("Comparison count:",comp2)
