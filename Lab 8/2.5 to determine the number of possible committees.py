def binomial_coefficient(n, r):
    dp = [[0] * (r + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][r]


n = 10
r = 4

result = binomial_coefficient(n, r)

print("C(10,4) =", result)
