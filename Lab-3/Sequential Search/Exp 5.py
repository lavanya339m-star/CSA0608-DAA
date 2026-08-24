def sequential_search(arr,key):
    comparisons=0
    matches=0
    mismatches=0
    for i in range(len(arr)):
        comparisons+=1
        if arr[i]==key:
            matches+=1
        else:
            mismatches+=1
    return comparisons,matches,mismatches

arr=[3,6,9,12,15,18,21]
key=15
comparisons,matches,mismatches=sequential_search(arr,key)

print("Total comparisons =",comparisons)
print("Total matches =",matches)
print("Total mismatches =",mismatches)
