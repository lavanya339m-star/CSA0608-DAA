from itertools import combinations

numbers=[15,10,12,7,5]
target=22

for r in range(1,len(numbers)+1):
    for subset in combinations(numbers,r):
        if sum(subset)==target:
            print("Subset found:",list(subset))
            print("Sum:",sum(subset))
            break
    else:
        continue
    break
