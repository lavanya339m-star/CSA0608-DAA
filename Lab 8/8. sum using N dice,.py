def count_ways(dice, faces, target):
    count = 0

    def generate(d, total):
        nonlocal count

        if d == dice:
            if total == target:
                count += 1
            return

        for value in range(1, faces + 1):
            generate(d + 1, total + value)

    generate(0, 0)

    return count


dice = 2
faces = 6
target = 7

ways = count_ways(dice, faces, target)

print("Number of ways =", ways)
