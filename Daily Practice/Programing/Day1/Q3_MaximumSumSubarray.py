n = int(input("Enter the size of array : "))
arr=[]
for i in range(n):
    a = int(input("Enter element : "))
    arr.append(a)


max_sum = 9999999999
start = end = temp_start = 0
found_wrap = False

#Without wrapping
for i in range(n):
    curr_sum = 0
    for j in range(n):
        curr_sum += arr[(i + j) % n]
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = (i + j) % n
        if curr_sum < 0:
            curr_sum = 0
            temp_start = (i + j + 1) % n

#With wrapping
total_sum = sum(arr)
min_sum = float('inf')
curr_sum = 0
temp_start = 0

for i in range(n):
    curr_sum += arr[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
        start = temp_start
        end = i
        found_wrap = True
    if curr_sum < 0:
        curr_sum = 0
        temp_start = i + 1


print("Maximum sum is : ",max_sum)