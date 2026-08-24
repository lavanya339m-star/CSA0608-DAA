from itertools import combinations

def subset_sum(arr,target):
    for r in range(1,len(arr)+1):
        for subset in combinations(arr,r):
            if sum(subset)==target:
                return list(subset)
    return None

arr=[3,34,4,12,5,2]
target=9
subset=subset_sum(arr,target)

if subset:
    print("Subset found:",subset)
    print("Sum:",sum(subset))
else:
    print("No subset found")
