"""
CP1404 Practical
Word Occurrences
Estimate: 20 minutes
Actual: 30 minutes
"""

sentence = input("Text: ").casefold().split()
word_to_count = {}
for word in sentence:
    count = word_to_count.get(word, 0)
    word_to_count[word] = count + 1

max_length = max(len(word) for word in word_to_count.keys())
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {count}")


