# Write a program that, given a paragraph string, will create a frequency table for each of the words in the paragraph string

paragraph = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."

frequency_table = {}
paragraph = paragraph.split(" ")

for word in paragraph:
    frequency_table[word] = frequency_table.get(word, 0) + 1

print(frequency_table)
