def optimized_bubble_sort(arr):
    n = len(arr)
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr, passes


# Test Case 1: Nearly sorted roll numbers
sorted_rolls, passes = optimized_bubble_sort(
    [101, 102, 104, 103, 105, 107, 106, 108]
)

assert sorted_rolls == sorted(
    [101, 102, 104, 103, 105, 107, 106, 108]
)
assert passes < 8


# Test Case 2: Already sorted roll numbers
sorted_ok, passes_ok = optimized_bubble_sort([1, 2, 3, 4, 5])

assert passes_ok == 1


print("Sorted roll numbers:", sorted_rolls)
print("Number of passes:", passes)
print("Already sorted list:", sorted_ok)
print("Passes for already sorted list:", passes_ok)
print("All test cases passed!")
