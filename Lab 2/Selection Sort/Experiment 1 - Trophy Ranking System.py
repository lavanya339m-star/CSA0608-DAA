def top_k_scores(scores, k):
    arr = scores.copy()
    n = len(arr)

    k = min(k, n)

    for i in range(k):
        max_index = i

        # Find the maximum score in the remaining portion
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j

        # Move the maximum score to the front
        arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr[:k]


# Test Cases
assert top_k_scores([72, 88, 65, 90, 77, 95, 60, 83, 91, 68], 5) == [95, 91, 90, 88, 83]

assert top_k_scores([5, 3, 1], 5) == [5, 3, 1]

assert top_k_scores([], 3) == []

print("All test cases passed!")
