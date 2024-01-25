def minimise_max_difference(arr, k):
    n = len(arr)
    min_height = min(arr)
    max_height = max(arr)
    diff = max_height - min_height

    new_min = min_height + k
    new_max = max_height - k
    if new_min > new_max:
        new_min, new_max = new_max, new_min

    for i in range(n):
        if arr[i] < new_min:
            arr[i] += k
        elif arr[i] > new_max:
            arr[i] -= k
        else:
            if new_max - arr[i] < arr[i] - new_min:
                arr[i] += k
            else:
                arr[i] -= k
    new_min = min(arr)
    new_max = max(arr)

    return min(diff, new_max - new_min)

size = int(input("Enter the size of array : "))
arr=[]
for i in range(size):
    a = int(input("Enter element : "))
    arr.append(a)
k = int(input("Enter the value of k : "))
print(minimise_max_difference(arr,k))