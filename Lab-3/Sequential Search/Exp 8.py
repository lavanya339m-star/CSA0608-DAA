def sequential_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i+1
    return -1

arr=["Anu","Bala","Charan","Deepa","Esha","Farhan"]
key="Deepa"
position=sequential_search(arr,key)

if position!=-1:
    print("Name found at position",position)
else:
    print("Name not found")
