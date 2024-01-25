n= int(input("Enter the term you want : "))

prev = "1"

for i in range(2,n+1):
    res = ""
    c = 1
    for j in range(1,len(prev)):
        if prev[j] == prev[j-1]:
            c+=1
        else:
            res += str(c) + prev[j-1]
            c = 1
    res += str(c) + prev[-1]
    prev = res

print(prev)