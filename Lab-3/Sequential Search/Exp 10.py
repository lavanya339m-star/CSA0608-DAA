def sequential_search(arr,key):
    comparisons=0
    for i in range(len(arr)):
        comparisons+=1
        print("Comparison",comparisons,":",arr[i],"==",key)
        if arr[i]==key:
            return i+1,comparisons
    return -1,comparisons

arr=[45,23,67,12,89,34,56,78,90,11,29,73,18,64,37]
keys=[73,18,100]

for key in keys:
    print("\nSearching for",key)
    position,comparisons=sequential_search(arr,key)
    if position!=-1:
        print("Element found at position",position)
    else:
        print("Element not found")
    print("Total comparisons =",comparisons)

print("\nBest-case complexity: O(1)")
print("Average-case complexity: O(n)")
print("Worst-case complexity: O(n)")
print("Space complexity: O(1)")
