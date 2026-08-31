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


def kth_smallest_delivery_time(delivery_times, k):
    if not delivery_times:
        raise ValueError("Delivery time list cannot be empty")

    if k < 0 or k >= len(delivery_times):
        raise IndexError("K is out of range")

    return median_of_medians_select(delivery_times, k)


already_sorted = list(range(1, 501))

assert kth_smallest_delivery_time(already_sorted, 0) == 1
assert kth_smallest_delivery_time(already_sorted, 499) == 500
assert kth_smallest_delivery_time(already_sorted, 250) == 251

delivery_times = [45, 30, 60, 25, 50, 40, 35, 55, 20, 65]

assert kth_smallest_delivery_time(
    delivery_times, 0
) == min(delivery_times)

print("All test cases passed!")
