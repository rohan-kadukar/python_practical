string = str(input("Enter Words: "))
words = string.split()
words = list(reversed(words))
print(" ".join(words))