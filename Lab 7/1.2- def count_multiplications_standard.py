def count_multiplications_standard(n):
    return n**3

def count_multiplications_strassen(n):
    size=1
    while size<n:
        size*=2
    k=0
    while size>1:
        size//=2
        k+=1
    return 7**k

assert count_multiplications_strassen(2)==7
assert count_multiplications_standard(2)==8
assert count_multiplications_strassen(4)==49
assert count_multiplications_standard(4)==64
assert count_multiplications_strassen(64)<count_multiplications_standard(64)

print("All test cases passed!")
