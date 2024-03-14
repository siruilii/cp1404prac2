input = input("text: ")
words = input.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

max_length = max(len(word) for word in word_count)
