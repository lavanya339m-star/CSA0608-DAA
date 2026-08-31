def median_of_medians_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    groups = []

    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i + 5])
        groups.append(group[len(group) // 2])

    if len(groups) <= 5:
        pivot = sorted(groups)[len(groups) // 2]
    else:
        pivot = median_of_medians_select(groups, len(groups) // 2)

    low = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    high = [x for x in arr if x > pivot]

    if k < len(low):
        return median_of_medians_select(low, k)
    elif k < len(low) + len(equal):
        return pivot
    else:
        return median_of_medians_select(
            high,
            k - len(low) - len(equal)
        )


data = [12, 3, 5, 7, 4, 19, 26]

for k in range(len(data)):
    assert median_of_medians_select(data, k) == sorted(data)[k]


import random

random.seed(1)

big_data = [random.randint(0, 10000) for _ in range(500)]

sorted_big = sorted(big_data)

for k in [0, 10, 250, 499]:
    assert median_of_medians_select(big_data, k) == sorted_big[k]


print("All test cases passed!")
