def count_ways(dice, faces, target):
    if dice == 0:
        return 1 if target == 0 else 0

    count = 0

    for value in range(1, faces + 1):
        count += count_ways(dice - 1, faces, target - value)

    return count


dice = 2
faces = 4
target = 5

ways = count_ways(dice, faces, target)

print("Number of ways =", ways)
