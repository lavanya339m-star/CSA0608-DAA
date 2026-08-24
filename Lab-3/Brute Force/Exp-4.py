def brute_force(text,pattern):
    comparisons=0
    matches=0
    mismatches=0
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            comparisons+=1
            if text[i+j]==pattern[j]:
                matches+=1
            else:
                mismatches+=1
                break
    return comparisons,matches,mismatches

text="ABABABABAB"
pattern="ABAB"
comparisons,matches,mismatches=brute_force(text,pattern)

print("Total character comparisons =",comparisons)
print("Total matches =",matches)
print("Total mismatches =",mismatches)
