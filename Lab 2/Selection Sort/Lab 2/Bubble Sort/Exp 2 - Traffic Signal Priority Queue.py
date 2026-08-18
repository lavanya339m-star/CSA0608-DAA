def bubble_sort_queue(queue):
    priority = {
        'ambulance': 1,
        'bus': 2,
        'car': 3
    }

    n = len(queue)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if priority[queue[j]] > priority[queue[j + 1]]:
                queue[j], queue[j + 1] = queue[j + 1], queue[j]
                swapped = True

        if not swapped:
            break

    return queue



queue = ['car', 'car', 'bus']
queue.append('ambulance')

result = bubble_sort_queue(queue)

assert result == ['ambulance', 'bus', 'car', 'car']


assert bubble_sort_queue(['ambulance']) == ['ambulance']


print("Final priority queue:", result)
print("All test cases passed!")
