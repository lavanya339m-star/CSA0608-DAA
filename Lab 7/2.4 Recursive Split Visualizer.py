def karatsuba_with_count(x, y, counter):
    counter[0] += 1

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    high1, low1 = divmod(x, 10 ** m)
    high2, low2 = divmod(y, 10 ** m)

    z2 = karatsuba_with_count(high1, high2, counter)
    z0 = karatsuba_with_count(low1, low2, counter)
    z1 = karatsuba_with_count(
        high1 + low1,
        high2 + low2,
        counter
    ) - z2 - z0

    return z2 * 10 ** (2 * m) + z1 * 10 ** m + z0


counter = [0]

result = karatsuba_with_count(1234, 5678, counter)

assert result == 1234 * 5678
assert counter[0] > 0

counter2 = [0]

karatsuba_with_count(9, 9, counter2)

assert counter2[0] == 1

print("Karatsuba result:", result)
print("Recursive calls:", counter[0])

print("Base case calls:", counter2[0])

print("All test cases passed!")
