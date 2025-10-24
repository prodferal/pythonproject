# Printa ut statistik för vald textfil
import Dictionaries

def basic_statistics(): # när input är 2
    print()
    print(f'--- Basic Statistics for "{Dictionaries.current_file}" ---')
    totWords = sum(Dictionaries.common_words_dict.values())
    uniqueWords = len(Dictionaries.common_words_dict)
    avgWordsLine = totWords / Dictionaries.count_lines
    avgWordLength = Dictionaries.chars_no_spaces / totWords
    avgWordSentence = totWords / Dictionaries.count_sentences

    print(f'Lines: {Dictionaries.count_lines:,}')
    print(f'Paragraphs: {Dictionaries.count_paragraph:,}')
    print(f'Sentences: {Dictionaries.count_sentences:,}')
    print(f'Words: {totWords:,}')
    print(f'Unique Words: {uniqueWords:,}')
    print(f'Characters (with spaces): {Dictionaries.chars_with_spaces:,}')
    print(f'Characters (no spaces): {Dictionaries.chars_no_spaces:,}')
    print(f'Average words per line: {avgWordsLine:.1f}')
    print(f'Average word length: {avgWordLength:.1f}')
    print(f'Average words per sentence: {avgWordSentence:.1f}')

def short_long_word():
    d = Dictionaries.common_words_dict
    longest_word = None
    shortest_word = None
    for word in d:
        if longest_word is None or len(word) > len(longest_word):
            longest_word = word
        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word

    return longest_word, shortest_word

def unique_avg():
    d = Dictionaries.common_words_dict
    total_counts = 0
    total_chars_in_words = 0
    unique_words = 0

    for w in d:
        c = d[w]
        total_counts += c
        total_chars_in_words += len(w) * c
        if c == 1:
            unique_words += 1

    avg_word_len = (total_chars_in_words / total_counts)
    
    return avg_word_len, unique_words

def top_ten_words():
    d = Dictionaries.common_words_dict
    pairs = list(d.items())
    totWords = sum(Dictionaries.common_words_dict.values())
    items = [[count, word] for (word, count) in pairs]
    items.sort(reverse = True) # Sort pairs in items
    count_freq = 1

    for count, word in items[ : 10]: # Slice the first 10 items
        percentage = (count / totWords) * 100
        print(f'{count_freq:>2}. ', end='')
        count_freq += 1
        print(f'{word:<5} {count:>10,} ({round(percentage, 1):>3}%)')

def word_frequency_analysis(): # när input är 3
    print()
    print(f'--- Word Analysis for "{Dictionaries.current_file}" ---')
    print('Top 10 most common words: ')

    longest_word, shortest_word = short_long_word()
    
    avg_word_len, unique_words = unique_avg()

    top_ten_words()
    print()
    print('Word length statistics:')
    print(f' - Shortest word: {len(shortest_word)}')
    print(f' - Longest word: {len(longest_word)}')
    print(f' - Average word length: {round(avg_word_len, 1)}')
    print(f' - Words appearing only once: {unique_words:,}')
