def combination(n, r):
    result = 1

    for i in range(1, r + 1):
        result = result * (n - i + 1) // i

    return result


players = 15
required = 5

selections = combination(players, required)

print("Number of Selections =", selections)
