def sequential_search(matrix,key):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==key:
                return i+1,j+1
    return -1,-1

matrix=[[12,8,15],[5,18,27],[9,11,24]]
key=24
row,column=sequential_search(matrix,key)

if row!=-1:
    print("Element found at Row",row,"Column",column)
else:
    print("Element not found")
