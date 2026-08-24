def bubble_sort_with_frames(arr):
    frames = []
    frames.append(arr.copy())
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        frames.append(arr.copy())
        if not swapped:
            break
    return frames
frames = bubble_sort_with_frames([5, 1, 4, 2, 8])
assert frames[-1] == sorted([5, 1, 4, 2, 8])
assert frames[0] == [5, 1, 4, 2, 8]
assert len(frames) >= 2
print("Bubble Sort Frames:")
for i, frame in enumerate(frames):
    print("Pass", i, ":", frame)
print("All test cases passed!")
