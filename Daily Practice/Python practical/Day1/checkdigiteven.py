result = []
for num in range(1000, 3001):
    temp = 0
    for digit in str(num):
        if int(digit) % 2 != 0:
            temp = 1
            break
    if temp == 0:
        print(num)