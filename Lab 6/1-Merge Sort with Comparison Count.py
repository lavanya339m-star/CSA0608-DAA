count=0

def merge_sort(arr):
    global count
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        count+=1
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result

n=int(input())
arr=list(map(int,input().split()))
arr=merge_sort(arr)

print(*arr,sep=",")
print("Comparisons :",count)
