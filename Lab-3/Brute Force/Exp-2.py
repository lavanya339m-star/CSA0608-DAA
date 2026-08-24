def brute_force(text,pattern):
    positions=[]
    for i in range(len(text)-len(pattern)+1):
        j=0
        while j<len(pattern) and text[i+j]==pattern[j]:
            j+=1
        if j==len(pattern):
            positions.append(i)
    return positions

text="BANANABANANA"
pattern="ANA"
positions=brute_force(text,pattern)

print("Occurrences at positions:",",".join(map(str,positions)))
