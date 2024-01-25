lines = []
while True:
    line = input("Enter a line: ")
    if not line:
        break
    lines.append(line)
for line in lines:
    capitalized_line = line.upper()
    print(capitalized_line)