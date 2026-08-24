n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))

i=0
j=0
result=[]

while i<n and j<m:
    if a[i]<=b[j]:
        result.append(a[i])
        i+=1
    else:
        result.append(b[j])
        j+=1

while i<n:
    result.append(a[i])
    i+=1

while j<m:
    result.append(b[j])
    j+=1

print(*result,sep=",")
