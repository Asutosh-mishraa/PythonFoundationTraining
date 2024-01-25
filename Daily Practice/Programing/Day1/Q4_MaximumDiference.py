size = int(input("Enter the size of array : "))
arr=[]
for i in range(size):
    a = int(input("Enter element : "))
    arr.append(a)
max_diff = arr[1] - arr[0]
res = [arr[0],arr[1]]

for i in range(size):
    for j in range(i+1,size):
        if arr[j] - arr[i] > max_diff:
            max_diff = arr[j] - arr[i]
            res = [arr[i],arr[j]]

print("The maximum difference is " + str(max_diff) + ".The pair is " + str(res))