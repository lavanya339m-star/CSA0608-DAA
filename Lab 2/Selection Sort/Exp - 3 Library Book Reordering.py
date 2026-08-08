def reorder_shelf(books):
    books = books.copy()
    moves = 0
    n = len(books)

    for i in range(n - 1):
        min_index = i

        # Find the book with the smallest ID
        for j in range(i + 1, n):
            if books[j] < books[min_index]:
                min_index = j

        # Perform a physical move only when required
        if min_index != i:
            books[i], books[min_index] = books[min_index], books[i]
            moves += 1

    return books, moves


# Test Cases
ordered, moves = reorder_shelf(
    [305, 102, 250, 118, 199, 400, 101]
)

assert ordered == sorted([305, 102, 250, 118, 199, 400, 101])
assert moves <= len(ordered) - 1

ordered2, moves2 = reorder_shelf([100, 200, 300])

assert moves2 == 0

print("All test cases passed!")
