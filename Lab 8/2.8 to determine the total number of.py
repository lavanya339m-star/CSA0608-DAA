def combination(n, r):
    result = 1

    for i in range(1, r + 1):
        result = result * (n - i + 1) // i

    return result


professors = 12
committee_size = 4

committees = combination(professors, committee_size)

print("Number of Committees =", committees)
