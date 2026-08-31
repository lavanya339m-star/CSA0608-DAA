def combination(n, r):
    result = 1

    for i in range(1, r + 1):
        result = result * (n - i + 1) // i

    return result


developers = 10
required = 3

teams = combination(developers, required)

print("Number of Teams =", teams)
