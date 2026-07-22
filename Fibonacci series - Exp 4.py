def fibonacci_iterative(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = 6

print("Iterative Fibonacci:", fibonacci_iterative(n))

recursive_series = []
for i in range(n):
    recursive_series.append(fibonacci_recursive(i))

print("Recursive Fibonacci:", recursive_series)
