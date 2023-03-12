with open("Find The Longest Word\Find the Longest Word from.txt", "r") as file:
    words = file.read().split()

longest_word = max(words, key=len)
longest_words = [word for word in words if len(word) == len(longest_word)]

print(longest_words)