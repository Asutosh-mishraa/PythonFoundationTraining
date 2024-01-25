s = input("Enter a sentence: ")
upper_count = 0
lower_count = 0
for c in s:
    if c.isupper():
        upper_count += 1
    elif c.islower():
        lower_count += 1
print("UPPER CASE", upper_count)
print("LOWER CASE", lower_count)