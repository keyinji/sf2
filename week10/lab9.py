from urllib.request import urlopen

def readFileURLString(url):
    try:
        data = urlopen(url)
        html_data = data.read()
        encoding = data.headers.get_content_charset('utf-8')
        return html_data.decode(encoding)
    except Exception as e:
        print(f"Error reading URL {url}: {e}")
        return None

books = {
    "Alice in Wonderland": "https://www.gutenberg.org/cache/epub/11/pg11.txt",
    "Pride and Prejudice": "https://www.gutenberg.org/cache/epub/1342/pg1342.txt",
    "Moby Dick": "https://www.gutenberg.org/cache/epub/2701/pg2701.txt",
    "Treasure Island": "https://www.gutenberg.org/cache/epub/120/pg120.txt",
    "Fifth Book (Not Processed)": "https://www.gutenberg.org/cache/epub/1661/pg1661.txt"
}

for title, url in list(books.items())[:4]:
    try:
        content = readFileURLString(url)
        if not content:
            continue
            
        start_marker = "*** START OF THE PROJECT GUTENBERG EBOOK"
        end_marker = "*** END OF THE PROJECT GUTENBERG EBOOK"
        start_idx = content.find(start_marker) + len(start_marker)
        end_idx = content.find(end_marker)
        story = content[start_idx:end_idx].strip()

        filename = title.lower().replace(' ', '_') + '.txt'
        f = open(filename, 'w', encoding='utf-8')
        f.write(story)
        f.close()

        # Word count and frequency
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
        
        word_count = len(words)
        word_freq = {}
        for word in words:
            if word in word_freq:
                word_freq[word] = word_freq[word] + 1
            else:
                word_freq[word] = 1

        # Paragraph counting
        paragraphs = 0
        lines = story.split('\n')
        prev_line_empty = True
        for line in lines:
            line = line.strip()
            if line and prev_line_empty:
                paragraphs += 1
                prev_line_empty = False
            elif not line:
                prev_line_empty = True

        # Sentences
        sentences = 0
        for i in range(len(story)-1):
            if story[i] in '.!?' and (story[i+1].isspace() or story[i+1] == '\n'):
                sentences += 1
        if story and story[-1] in '.!?':
            sentences += 1

        # Word lengths
        min_length = len(words[0]) if words else 0
        max_length = len(words[0]) if words else 0
        total_length = 0
        for word in words:
            length = len(word)
            total_length += length
            if length < min_length:
                min_length = length
            if length > max_length:
                max_length = length
        avg_length = total_length / len(words) if words else 0

        # Most common vowel
        vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        for char in story.lower():
            if char in vowels:
                vowels[char] += 1
        most_common_vowel = 'a'
        max_count = vowels['a']
        for v in 'eiou':
            if vowels[v] > max_count:
                max_count = vowels[v]
                most_common_vowel = v

        # Most common punctuation mark
        punctuation = {'.': 0, ',': 0, '!': 0, '?': 0, ';': 0, ':': 0, '"': 0, "'": 0, '-': 0}
        for char in story:
            if char in punctuation:
                punctuation[char] += 1
        most_common_punct = '.'
        max_punct_count = punctuation['.']
        for p in ',!?;:"\'-':
            if punctuation[p] > max_punct_count:
                max_punct_count = punctuation[p]
                most_common_punct = p

        print(f"\nAnalysis for {title}:")
        print(f"Word count: {word_count}")
        print(f"Paragraphs: {paragraphs}")
        print(f"Sentences: {sentences}")
        print(f"Word length - Min: {min_length}, Max: {max_length}, Avg: {avg_length:.2f}")
        print(f"Most common vowel: {most_common_vowel}")
        print(f"Most common punctuation mark: {most_common_punct}")

    except Exception as e:
        print(f"Error processing {title}: {e}")

print("\nNote: Fifth book was selected but not processed.")