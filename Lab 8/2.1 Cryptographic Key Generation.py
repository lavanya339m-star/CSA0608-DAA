def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1, low1 = divmod(x, 10 ** m)
    high2, low2 = divmod(y, 10 ** m)

    z2 = karatsuba(high1, high2)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(high1 + low1, high2 + low2) - z2 - z0

    return z2 * 10 ** (2 * m) + z1 * 10 ** m + z0


assert karatsuba(1234, 5678) == 1234 * 5678
assert karatsuba(123456789, 987654321) == 123456789 * 987654321
assert karatsuba(9, 9) == 81
assert karatsuba(0, 12345) == 0

big1, big2 = int('9' * 50), int('8' * 50)

assert karatsuba(big1, big2) == big1 * big2

print("All test cases passed!")
