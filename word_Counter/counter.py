text = input("Enter text: ")
words = text.split()
print(type(words))
frequency = {}
print(type(frequency))
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)