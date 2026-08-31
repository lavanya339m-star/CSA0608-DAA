def combination(n, r):
    result = 1

    for i in range(1, r + 1):
        result = result * (n - i + 1) // i

    return result


volunteers = 20
group_size = 6

groups = combination(volunteers, group_size)

print("Number of Groups =", groups)
