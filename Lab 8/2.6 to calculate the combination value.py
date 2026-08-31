def combination(n, r):
    if r < 0 or r > n:
        return 0

    result = 1

    for i in range(1, r + 1):
        result = result * (n - i + 1) // i

    return result


n = 15
r = 6

result = combination(n, r)

print("C(15,6) =", result)
