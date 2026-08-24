def brute_force(text,pattern):
    text=text.lower()
    pattern=pattern.lower()
    for i in range(len(text)-len(pattern)+1):
        j=0
        while j<len(pattern) and text[i+j]==pattern[j]:
            j+=1
        if j==len(pattern):
            return i
    return -1

text="DataStructuresAndAlgorithms"
pattern="ALGORITHMS"
position=brute_force(text,pattern)

if position!=-1:
    print("Pattern found at position",position)
else:
    print("Pattern not found")
