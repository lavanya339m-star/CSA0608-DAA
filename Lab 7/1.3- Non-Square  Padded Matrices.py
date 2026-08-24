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

def strassen_arbitrary_size(A,B):
    rows=len(A)
    common=len(B)
    cols=len(B[0])

    size=1
    while size<max(rows,common,cols):
        size*=2

    AP=[[0]*size for _ in range(size)]
    BP=[[0]*size for _ in range(size)]

    for i in range(rows):
        for j in range(common):
            AP[i][j]=A[i][j]

    for i in range(common):
        for j in range(cols):
            BP[i][j]=B[i][j]

    C=strassen(AP,BP)

    return [row[:cols] for row in C[:rows]]

def standard_multiply(A,B):
    n=len(A)
    m=len(B)
    p=len(B[0])
    C=[[0]*p for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j]+=A[i][k]*B[k][j]

    return C

A5=[[i+j for j in range(5)] for i in range(5)]
B5=[[1 if i==j else 0 for j in range(5)] for i in range(5)]

assert strassen_arbitrary_size(A5,B5)==standard_multiply(A5,B5)

A_rect=[[1,2,3],[4,5,6]]
B_rect=[[7,8],[9,10],[11,12]]

assert strassen_arbitrary_size(A_rect,B_rect)==standard_multiply(A_rect,B_rect)

print("All test cases passed!")S?
