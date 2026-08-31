def multiply_polynomials_naive(p1,p2):
    result=[0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i+j]+=p1[i]*p2[j]
    return result

def add_poly(a,b):
    n=max(len(a),len(b))
    result=[0]*n
    for i in range(n):
        if i<len(a):
            result[i]+=a[i]
        if i<len(b):
            result[i]+=b[i]
    return result

def sub_poly(a,b):
    n=max(len(a),len(b))
    result=[0]*n
    for i in range(n):
        if i<len(a):
            result[i]+=a[i]
        if i<len(b):
            result[i]-=b[i]
    return result

def karatsuba_poly(p1,p2):
    if not p1 or not p2:
        return []

    if len(p1)==1 or len(p2)==1:
        return multiply_polynomials_naive(p1,p2)

    n=max(len(p1),len(p2))
    m=n//2

    p1=p1+[0]*(n-len(p1))
    p2=p2+[0]*(n-len(p2))

    low1=p1[:m]
    high1=p1[m:]
    low2=p2[:m]
    high2=p2[m:]

    z0=karatsuba_poly(low1,low2)
    z2=karatsuba_poly(high1,high2)

    sum1=add_poly(low1,high1)
    sum2=add_poly(low2,high2)
    z1=karatsuba_poly(sum1,sum2)

    middle=sub_poly(sub_poly(z1,z2),z0)

    result=[0]*(2*n-1)

    for i in range(len(z0)):
        result[i]+=z0[i]

    for i in range(len(middle)):
        result[i+m]+=middle[i]

    for i in range(len(z2)):
        result[i+2*m]+=z2[i]

    while len(result)>1 and result[-1]==0:
        result.pop()

    return result

assert multiply_polynomials_naive([1,2],[3,4])==[3,10,8]

p1=[1,2,3,4]
p2=[5,6,7,8]

naive_result=multiply_polynomials_naive(p1,p2)
karatsuba_result=karatsuba_poly(p1,p2)[:len(naive_result)]

assert karatsuba_result==naive_result

print("All test cases passed!")
