def selection_sort_min_writes(arr):
    arr = arr.copy()
    swaps = 0
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap only if needed
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, swaps


# Test Cases
res, sw = selection_sort_min_writes(
    [23.5, 19.2, 25.1, 18.8, 21.4]
)

assert res == sorted([23.5, 19.2, 25.1, 18.8, 21.4])
assert sw <= len(res) - 1

res2, sw2 = selection_sort_min_writes([1, 2, 3, 4, 5])

assert sw2 == 0

print("All test cases passed!")
