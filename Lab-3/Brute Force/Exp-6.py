def brute_force(text,pattern):
    comparisons=0
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            comparisons+=1
            if text[i+j]!=pattern[j]:
                break
        else:
            return i,comparisons
    return -1,comparisons

text="COMPUTERSCIENCE"
pattern="SCI"
position,comparisons=brute_force(text,pattern)

print("First occurrence position:",position)
print("Number of comparisons:",comparisons)
