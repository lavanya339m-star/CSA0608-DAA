def bubble_sort_plain(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons
def bubble_sort_optimized(arr):
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, comparisons
alerts = [2, 1, 3, 2, 1, 4, 3, 2, 5, 1, 2, 3, 4, 1, 2]
r1, c1 = bubble_sort_plain(alerts)
r2, c2 = bubble_sort_optimized(alerts)
assert r1 == r2 == sorted(alerts)
assert c2 <= c1
print("Sorted alerts:", r1)
print("Plain comparisons:", c1, "| Optimized comparisons:", c2)
print("All test cases passed!")
