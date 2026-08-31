def combination(n, r):
    result = 1

    for i in range(1, r + 1):
        result = result * (n - i + 1) // i

    return result


servers = 8
selected = 3

combinations = combination(servers, selected)

print("Number of Combinations =", combinations)
