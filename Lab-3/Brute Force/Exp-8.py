def brute_force(text,pattern):
    comparisons=0
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            comparisons+=1
            if text[i+j]!=pattern[j]:
                break
        else:
            return comparisons
    return comparisons

text="PROGRAMMINGLAB"
pattern1="LAB"
pattern2="TEST"

comparisons1=brute_force(text,pattern1)
comparisons2=brute_force(text,pattern2)

print("Successful search comparisons:",comparisons1)
print("Unsuccessful search comparisons:",comparisons2)
