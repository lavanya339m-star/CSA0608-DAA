import random
import time

def add(A,B):
    n=len(A)
    return [[A[i][j]+B[i][j] for j in range(n)] for i in range(n)]

def sub(A,B):
    n=len(A)
    return [[A[i][j]-B[i][j] for j in range(n)] for i in range(n)]

def strassen(A,B):
    n=len(A)
    if n==1:
        return [[A[0][0]*B[0][0]]]

    m=n//2

    A11=[row[:m] for row in A[:m]]
    A12=[row[m:] for row in A[:m]]
    A21=[row[:m] for row in A[m:]]
    A22=[row[m:] for row in A[m:]]

    B11=[row[:m] for row in B[:m]]
    B12=[row[m:] for row in B[:m]]
    B21=[row[:m] for row in B[m:]]
    B22=[row[m:] for row in B[m:]]

    M1=strassen(add(A11,A22),add(B11,B22))
    M2=strassen(add(A21,A22),B11)
    M3=strassen(A11,sub(B12,B22))
    M4=strassen(A22,sub(B21,B11))
    M5=strassen(add(A11,A12),B22)
    M6=strassen(sub(A21,A11),add(B11,B12))
    M7=strassen(sub(A12,A22),add(B21,B22))

    C11=add(sub(add(M1,M4),M5),M7)
    C12=add(M3,M5)
    C21=add(M2,M4)
    C22=add(sub(add(M1,M3),M2),M6)

    C=[]
    for i in range(m):
        C.append(C11[i]+C12[i])
    for i in range(m):
        C.append(C21[i]+C22[i])

    return C

def strassen_multiply(A,B):
    n=len(A)
    size=1
    while size<n:
        size*=2

    AP=[[0]*size for _ in range(size)]
    BP=[[0]*size for _ in range(size)]

    for i in range(n):
        for j in range(n):
            AP[i][j]=A[i][j]
            BP[i][j]=B[i][j]

    C=strassen(AP,BP)
    return [row[:n] for row in C[:n]]

def standard_multiply(A,B):
    n=len(A)
    C=[[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j]+=A[i][k]*B[k][j]

    return C

def random_matrix(n):
    return [[random.randint(1,10) for _ in range(n)] for _ in range(n)]

def benchmark(n):
    A=random_matrix(n)
    B=random_matrix(n)

    start=time.perf_counter()
    standard_multiply(A,B)
    std_t=time.perf_counter()-start

    start=time.perf_counter()
    strassen_multiply(A,B)
    strassen_t=time.perf_counter()-start

    return std_t,strassen_t

A,B=random_matrix(8),random_matrix(8)

assert strassen_multiply(A,B)==standard_multiply(A,B)

std_t,strassen_t=benchmark(16)

assert std_t>=0 and strassen_t>=0

print("Standard Time :",std_t)
print("Strassen Time :",strassen_t)
print("All test cases passed!")
