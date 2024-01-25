size = int(input("Enter the size of array : "))
l=[]
for i in range(size):
    a = int(input("Enter element : "))
    l.append(a)
target_sum = int(input("Enter the target sum : "))
result=[]
for i in range(size):
    for j in range(i + 1, size):
            if l[i] + l[j] == target_sum:
                result.append([l[i],l[j]])

print(result)