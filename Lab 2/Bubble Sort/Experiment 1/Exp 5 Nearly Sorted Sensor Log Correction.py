import random
def insertion_sort_count_shifts(log):
    arr = log.copy()
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
    return arr, shifts
log = [18.2, 18.5, 18.9, 17.9, 19.1, 19.4, 19.0]
sorted_log, shifts_nearly = insertion_sort_count_shifts(log)
assert sorted_log == sorted(log)
shuffled_log = log.copy()
random.shuffle(shuffled_log)
_, shifts_random = insertion_sort_count_shifts(shuffled_log)
print("Nearly-sorted shifts:", shifts_nearly,
      "| Random shifts:", shifts_random)
print("All test cases passed!")
