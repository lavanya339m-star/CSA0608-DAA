def merge_sort(arr):
    if len(arr)<=1:
        return arr,0
    mid=len(arr)//2
    left,left_count=merge_sort(arr[:mid])
    right,right_count=merge_sort(arr[mid:])
    result=[]
    i=j=0
    count=left_count+right_count
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            count+=len(left)-i
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result,count

n=int(input())
arr=list(map(int,input().split()))

sorted_arr,inversions=merge_sort(arr)

print("Sorted :",*sorted_arr,sep=",")
print("Inversions :",inversions)
