def sequential_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i+1
    return -1

arr=[101,102,103,104,105,106]
key=104
position=sequential_search(arr,key)

if position!=-1:
    print("Register Number found at position",position)
else:
    print("Register Number not found")
