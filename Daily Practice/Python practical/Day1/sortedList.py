s = input("Enter the words: ")
words = s.split(',')
sorted_words = sorted(words)
print(','.join(sorted_words))