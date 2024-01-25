s = input("Enter a sentence: ")
letters = 0
digit = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digit += 1
print("LETTERS", letters)
print("DIGITS", digit)
