def Product(myLst):
 
    result = 1
    for x in myLst:
        result = result * x
    return result


size = int(input("Enter the size of array : "))
arr=[]
for i in range(size):
    a = int(input("Enter element : "))
    arr.append(a)

arr2 = []

for i in range(size):
    arr2.append(Product(arr[i+1:size]) * Product(arr[0:i]))

print(arr2)