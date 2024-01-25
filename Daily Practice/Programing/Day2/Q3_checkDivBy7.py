def check_div(n):
    #print(n)
    if n < 0:
        return check_div(-n)
    if n == 0 or n == 7:
        return True
    elif n < 7:
        return False
    else:
        #print(n)
        return check_div(n // 10 - (2 * (n - n//10 * 10)))

number = 14
result = check_div(number)

if result:
    print("Yes")
else:
    print("No")