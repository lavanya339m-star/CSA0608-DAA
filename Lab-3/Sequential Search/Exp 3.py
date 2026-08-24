def sequential_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i+1
    return -1

arr=[10,25,15,25,30,25,40]
key=25
position=sequential_search(arr,key)

if position!=-1:
    print("First occurrence at position",position)
else:
    print("Element not found")
