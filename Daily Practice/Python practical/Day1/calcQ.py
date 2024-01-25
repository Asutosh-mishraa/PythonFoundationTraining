C = 50
H = 30
s = input("Enter values for D: ")
D = s.split(',')
result = []
for i in D:
    Q = int(((2 * C * int(i)) / H)**0.5)
    result.append(str(Q))

# Print the result as a comma-separated sequence
print(','.join(result))