# Printa ut statistik för vald textfil

def basic_statistics(data): # när input är 2
    totWords = data['word_count']
    uniqueWords = len(data['word_data']['unique_word_set'])
    avgWordsLine = totWords / data['count_lines']
    avgWordLength = data['chars_no_spaces'] / totWords
    data['sentence_data']['avgWordSentence'] = totWords / data['sentence_data']['count_sentences']
    
    print()
    print(f'--- Basic Statistics for "{data['current_file']}" ---')
    print(f'Lines: {data['count_lines']:,}')
    print(f'Paragraphs: {data['count_paragraph']:,}')
    print(f'Sentences: {data['sentence_data']['count_sentences']:,}')
    print(f'Words: {totWords:,}')
    print(f'Unique Words: {uniqueWords:,}')
    print(f'Characters (with spaces): {data['chars_with_spaces']:,}')
    print(f'Characters (no spaces): {data['chars_no_spaces']:,}')
    print(f'Average words per line: {avgWordsLine:.1f}')
    print(f'Average word length: {avgWordLength:.1f}')
    print(f'Average words per sentence: {data['sentence_data']['avgWordSentence']:.1f}')


def short_long_word(data):
    d = data['word_data']['common_words_dict']
    longest_word = ''
    shortest_word = None

    for word in d.keys():
        if longest_word == '' or len(word) > len(longest_word):
            longest_word = word
        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word

    data['word_data']['longest_word'] = longest_word
    data['word_data']['shortest_word'] = shortest_word


def unique_avg(data):
    d = data['word_data']['common_words_dict']
    total_counts = 0
    total_chars_in_words = 0
    words_appearing_once = 0

    for w in d:
        c = d[w]
        total_counts += c
        total_chars_in_words += len(w) * c
        if c == 1:
            words_appearing_once += 1

    data['word_data']['words_appearing_once'] = words_appearing_once
    data['word_data']['avg_word_len'] = round((total_chars_in_words / total_counts), 1)
    
def top_ten_words(data):
    d = data['word_data']['common_words_dict']
    pairs = list(d.items())
    totWords = sum(d.values())
    items = [[count, word] for (word, count) in pairs]
    items.sort(reverse = True) # Sort pairs in items
    count_freq = 1

    for count, word in items[ : 10]: # Slice the first 10 items
        percentage = (count / totWords) * 100
        print(f'{count_freq:>2}. ', end='')
        count_freq += 1
        print(f'{word:<5} {count:>10,} ({round(percentage, 1):>3}%)')

def word_frequency_analysis(data): # när input är 3
    print()
    print(f'--- Word Analysis for "{data['current_file']}" ---')
    print('Top 10 most common words: ')
    top_ten_words(data)
    
    short_long_word(data)
    unique_avg(data)
    print()
    print('Word length statistics:')
    print(f' - Shortest word: {len(data['word_data']['shortest_word'])}')
    print(f' - Longest word: {len(data['word_data']['longest_word'])}')
    print(f' - Average word length: {data['word_data']['avg_word_len']}')
    print(f' - Words appearing only once: {data['word_data']['words_appearing_once']:,}')
    print()


def length_histogram(data):
    sd = data.get('sentence_data', {})
    hist = sd.get('length_hist', {})
    pairs = list(hist.items())
    items = [[count, word] for (word, count) in pairs]
    items.sort(reverse = True) # Sort pairs in items

    for count, length in items[ : 5]: # Slice the first 10 items
        print(f'{length:<5} words: {count:>10,} sentences')

def sentence_analysis(data): # när input är 4
    sd = data['sentence_data']
    totWords = data['word_count']
    totSent = sd['count_sentences']
    print()
    print(f'Total sentences: {sd['count_sentences']:,}')
    print(f'Average words per sentence: {round(totWords / totSent, 1)}')
    print(f'Shortest sentence: {sd['shortest_len']} words')
    print(f'Longest sentence: {sd['longest_len']} words')
    print()
    print(f'Shortest sentence text: {sd['shortest_sentence']}')
    print(f'Longest sentence text: {(sd['longest_sentence'])[:200].rstrip() + '...'}')
    print()
    print('Sentence length distribution (top 5): ')
    length_histogram(data)

    
def character_analysis(data): #när input är 5
    cd = data['character_data']
    print()
    print('Character type distribution: ')
    print(f'{' ':<2} Letters: {cd['tot_letters']:,} ({100*(cd['tot_letters'] / cd['tot_characters']) :.1f}%)')
    print(f'{' ':<2} Digits: {cd['tot_digits']:,} ({100*(cd['tot_digits'] / cd['tot_characters']) :.1f}%)')
    print(f'{' ':<2} Spaces: {cd['tot_spaces']:,} ({100*(cd['tot_spaces'] / cd['tot_characters']) :.1f}%)')
    print(f'{' ':<2} Punctuation: {cd['tot_punctuation']:,} ({100*(cd['tot_punctuation'] / cd['tot_characters']) :.1f}%)')
    print()
    print('Most common letters:')

    sorted_by_count = sorted(cd['all_letters_dict'].items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_by_count[:10]

    index = 1
    for i in top_10:
        print(f'{index:>2}. "{i[0]}" - {i[1]:,} times ({100 * (i[1] / cd['tot_letters'] ):.1f}%) ')
        index += 1