def brute_force(text,pattern):
    comparisons=0
    found=False
    for i in range(len(text)-len(pattern)+1):
        j=0
        while j<len(pattern):
            comparisons+=1
            if text[i+j]!=pattern[j]:
                break
            j+=1
        if j==len(pattern):
            found=True
    return found,comparisons

text="AAAAAAAAAB"
pattern="AAAAB"
found,comparisons=brute_force(text,pattern)

print("Pattern found:",found)
print("Number of comparisons:",comparisons)

if comparisons==len(pattern):
    print("Case: Best Case")
elif comparisons==(len(text)-len(pattern)+1)*len(pattern):
    print("Case: Worst Case")
else:
    print("Case: Average Case")
