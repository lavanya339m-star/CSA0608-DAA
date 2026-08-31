def schoolbook(x, y):
    sx = str(x)[::-1]
    sy = str(y)[::-1]
    result = [0] * (len(sx) + len(sy))

    operations = 0

    for i in range(len(sx)):
        for j in range(len(sy)):
            result[i + j] += int(sx[i]) * int(sy[j])
            operations += 1

    for i in range(len(result) - 1):
        result[i + 1] += result[i] // 10
        result[i] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return int(''.join(map(str, result[::-1]))), operations


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


for digits in [2, 4, 8, 16, 32]:
    x = int('7' * digits)
    y = int('3' * digits)

    school_result, school_ops = schoolbook(x, y)
    kara_result = karatsuba(x, y)

    assert kara_result == x * y
    assert school_result == x * y

    print("Digits:", digits)
    print("Schoolbook operations:", school_ops)
    print("Results match:", kara_result == school_result)
    print()

print("All test cases passed!")
