def brute_force(text,pattern):
    positions=[]
    comparisons=0
    for i in range(len(text)-len(pattern)+1):
        print("Shift",i,end=": ")
        match=True
        for j in range(len(pattern)):
            comparisons+=1
            if text[i+j]!=pattern[j]:
                print("Mismatch")
                match=False
                break
        else:
            print("Match")
        if match:
            positions.append(i)
    return positions,comparisons

text="TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
pattern="TATCTT"

positions,comparisons=brute_force(text,pattern)

print("Pattern occurrences:",positions)
print("Total comparisons:",comparisons)
print("Best-case complexity: O(n)")
print("Worst-case complexity: O(n*m)")
print("Space complexity: O(1)")
