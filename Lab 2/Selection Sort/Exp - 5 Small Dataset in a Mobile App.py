import time
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
items = [499, 129, 899, 45, 275, 60, 310, 150]
start = time.perf_counter()
result = selection_sort(items)
end = time.perf_counter()
print("Original List:", items)
print("Sorted List:", result)
print("Execution Time:", (end - start) * 1000000, "microseconds")
assert selection_sort([499, 129, 899, 45, 275, 60, 310, 150]) == sorted(
    [499, 129, 899, 45, 275, 60, 310, 150]
)
assert selection_sort([]) == []
assert selection_sort([7]) == [7]
print("All test cases passed!")
