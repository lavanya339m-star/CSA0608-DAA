def brute_force(text,pattern):
    positions=[]
    comparisons=0
    for i in range(len(text)-len(pattern)+1):
        j=0
        while j<len(pattern):
            comparisons+=1
            if text[i+j]!=pattern[j]:
                break
            j+=1
        if j==len(pattern):
            positions.append(i)
    return positions,comparisons

text="AABAACAADAABAABA"
pattern="AABA"
positions,comparisons=brute_force(text,pattern)

print("Position(s):",positions)
print("Total number of comparisons:",comparisons)
