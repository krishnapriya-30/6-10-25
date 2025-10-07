words=input("Enter words separated by spaces:").split()
longest_word=" "
max_length=0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print("Longest word:", longest_word)
print("Length of the longest word:", max_length)







