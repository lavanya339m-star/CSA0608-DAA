def brute_force(text,pattern):
    m=len(pattern)
    n=len(text)
    for i in range(n-m+1):
        comparisons=[]
        result="Match"
        for j in range(m):
            comparisons.append(text[i+j]+"="+pattern[j])
            if text[i+j]!=pattern[j]:
                result="Mismatch"
                break
        print("Shift:",i,"Comparisons:",", ".join(comparisons),"Result:",result)

text="MISSISSIPPI"
pattern="ISSI"
brute_force(text,pattern)
