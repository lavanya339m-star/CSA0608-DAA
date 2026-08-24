def brute_force(text,pattern):
    positions=[]
    alignment=1
    for i in range(len(text)-len(pattern)+1):
        match=True
        for j in range(len(pattern)):
            if text[i+j]!=pattern[j]:
                match=False
                break
        print("Alignment",alignment,":","Match" if match else "Mismatch")
        if match:
            positions.append(i)
        alignment+=1
    return positions

text="ABCDABCABCDA"
pattern="ABCDA"
positions=brute_force(text,pattern)

print("Pattern occurrence positions:",positions)
