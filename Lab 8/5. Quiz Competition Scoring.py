def count_ways(dice, faces, target):
    count = 0

    def generate(roll, total):
        nonlocal count

        if roll == dice:
            if total == target:
                count += 1
            return

        for value in range(1, faces + 1):
            generate(roll + 1, total + value)

    generate(0, 0)

    return count


dice = 5
faces = 6
target = 15

ways = count_ways(dice, faces, target)

print("Number of ways =", ways)
