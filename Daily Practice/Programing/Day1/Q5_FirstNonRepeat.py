size = int(input("Enter the size of array : "))
arr=[]
for i in range(size):
    a = int(input("Enter element : "))
    arr.append(a)

for x in arr:
    if arr.count(x) == 1:
        print(x)
        break

    