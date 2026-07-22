
arr = [10, 25, 30, 45, 50]
key = 30

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Key found at index", i)
        found = True
        break

if not found:
    print("Key not found")
