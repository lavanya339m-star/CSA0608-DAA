def count_ways(dice, faces, target):
    count = 0

    for d1 in range(1, faces + 1):
        for d2 in range(1, faces + 1):
            for d3 in range(1, faces + 1):
                if d1 + d2 + d3 == target:
                    count += 1

    return count


dice = 3
faces = 6
target = 8

ways = count_ways(dice, faces, target)

print("Number of ways =", ways)
