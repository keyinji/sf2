f = open('alice_in_wonderland.txt', 'r', encoding='utf-8')
story = f.read()
f.close()

# (a) Print the story
print("Story Content:")
print(story)
print("\n" + "="*50 + "\n")

# (b) Count total words
words = []
current_word = ''
for char in story.lower():
    if char.isalpha():
        current_word += char
    elif current_word:
        words.append(current_word)
        current_word = ''
if current_word:
    words.append(current_word)
total_words = len(words)
print(f"Total number of words: {total_words}")

# (c) Word frequency and sorting
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1

# Convert to list and sort by frequency (highest to lowest) then alphabetically
freq_list = []
for word in word_freq:
    freq_list.append((word, word_freq[word]))

# Simple bubble sort by frequency (descending) and then alphabetically
for i in range(len(freq_list)):
    for j in range(len(freq_list)-1):
        if freq_list[j][1] < freq_list[j+1][1]:
            freq_list[j], freq_list[j+1] = freq_list[j+1], freq_list[j]
        elif freq_list[j][1] == freq_list[j+1][1] and freq_list[j][0] > freq_list[j+1][0]:
            freq_list[j], freq_list[j+1] = freq_list[j+1], freq_list[j]

print("\nWord Frequencies (sorted by frequency, highest to lowest):")
for word, freq in freq_list:
    print(f"{word}: {freq}")