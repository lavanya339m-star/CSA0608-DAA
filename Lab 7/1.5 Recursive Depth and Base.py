import random

def standard_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def subtract(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen_hybrid(A, B, threshold=2):
    n = len(A)

    if n <= threshold:
        return standard_multiply(A, B)

    mid = n // 2

    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    M1 = strassen_hybrid(add(A11, A22), add(B11, B22), threshold)
    M2 = strassen_hybrid(add(A21, A22), B11, threshold)
    M3 = strassen_hybrid(A11, subtract(B12, B22), threshold)
    M4 = strassen_hybrid(A22, subtract(B21, B11), threshold)
    M5 = strassen_hybrid(add(A11, A12), B22, threshold)
    M6 = strassen_hybrid(subtract(A21, A11), add(B11, B12), threshold)
    M7 = strassen_hybrid(subtract(A12, A22), add(B21, B22), threshold)

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])
    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C

A = [[random.randint(-5, 5) for _ in range(4)] for _ in range(4)]
B = [[random.randint(-5, 5) for _ in range(4)] for _ in range(4)]

assert strassen_hybrid(A, B, threshold=2) == standard_multiply(A, B)
assert strassen_hybrid(A, B, threshold=4) == standard_multiply(A, B)

print("A =", A)
print("B =", B)
print("All test cases passed!")
