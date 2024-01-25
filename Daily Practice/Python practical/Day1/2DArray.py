X, Y = map(int, input("Enter two digits X and Y separated by a comma: ").split(','))
result_array = [[i*j for j in range(Y)] for i in range(X)]
print(result_array)
