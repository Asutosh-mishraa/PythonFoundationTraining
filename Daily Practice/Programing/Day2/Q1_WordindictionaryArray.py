ip_string = "ilikesamsung"
dictionary = ["i","like", "sam", "sung", "samsung", "mobile", "ice","cream", "icecream", "man", "go", "mango"]

n= len(ip_string)
test = [False] * (n+1)
test[0] = True
for i in range(1, n + 1):
    for j in range(i):
        if test[j] and ip_string[j:i] in dictionary:
            test[i] = True
            print(ip_string[j:i])
            break
if test[n]:
    print("Yes")
else:
    print("No")