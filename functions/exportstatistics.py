from datetime import datetime

def report_exp(data):
    exp_lst = [
    '============================================================',
    'TEXT ANALYSIS RESULTS',
    '============================================================'
]
    exp_lst.append(f'File analyzed: {data['current_file']}')
    exp_lst.append(f"Analysis date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    
    #Basic statistics
    exp_lst.append('\n')
    totWords = data['word_count']
    lc = data.get('count_lines', 0)
    sc = data['sentence_data'].get('count_sentences', 0)
    wc = data.get('word_count', 0)
    uw = len(data['word_data'].get('unique_word_set', set()))
    cs = data.get('chars_with_spaces', 0)
    cns = data.get('chars_no_spaces', 0)
    pc = data.get('count_paragraph', 0)
    awl = totWords / data['count_lines']
    avgWl = data['chars_no_spaces'] / totWords
    aws = totWords / data['sentence_data']['count_sentences']
    
    exp_lst.append("BASIC STATISTICS")
    exp_lst.append('--------------------')
    exp_lst.append(f'Lines: {lc}')
    exp_lst.append(f'Paragraphs: {pc}')
    exp_lst.append(f'Sentences: {sc}')
    exp_lst.append(f'Words: {wc}')
    exp_lst.append(f'Unique words: {uw}')
    exp_lst.append(f'Characters (with spaces): {cs}')
    exp_lst.append(f'Characters (no spaces): {cns}')
    exp_lst.append(f'Avg words per line: {round(wc / lc, 1)}')
    exp_lst.append(f'Avg word length: {round(avgWl, 1)}')
    exp_lst.append(f'Avg words per sentence: {round(aws, 1)}')
    


    # Word frequency analysis
    exp_lst.append('\n')
    exp_lst.append('TOP 10 MOST COMMON WORDS')
    exp_lst.append('------------------------------')
    d = data['word_data']['common_words_dict']
    pairs = list(d.items())
    totWords = sum(d.values())
    items = [[count, word] for (word, count) in pairs]
    items.sort(reverse = True) # Sort pairs in items
    count_freq = 1

    for count, word in items[ : 10]: # Slice the first 10 items
        percentage = (count / totWords) * 100
        exp_lst.append(f'{count_freq:>2}. {word:<5} {count:>10,} ({round(percentage, 1):>3}%)')
        count_freq += 1

    exp_lst.append('\n')
    exp_lst.append('WORD STATISTICS')
    exp_lst.append('--------------------')
    exp_lst.append(f'Shortest word: {len(data['word_data']['shortest_word'])}')
    exp_lst.append(f'Longest word: {len(data['word_data']['longest_word'])}')
    exp_lst.append(f'Words appearing only once: {len(data['word_data']['unique_word_set'])}')



    # Sentence analysis
    sd = data['sentence_data']
    exp_lst.append('\n')
    exp_lst.append('SENTENCE STATISTICS')
    exp_lst.append('-------------------------')
    exp_lst.append(f'Total sentences: {sd['count_sentences']}')
    exp_lst.append(f'Shortest sentence: {sd['shortest_len']}')
    exp_lst.append(f'Longest sentence: {sd['longest_len']}')
    exp_lst.append(f'Shortest sentence text: {sd['shortest_sentence']}')
    exp_lst.append(f'Longest sentence text: {sd['longest_sentence']}')


    # Character analysis
    cd = data['character_data']
    exp_lst.append('\n')
    exp_lst.append('CHARACTER STATISTICS')
    exp_lst.append('-------------------------')
    exp_lst.append(f'Letters: {cd['tot_letters']}')
    exp_lst.append(f'Digits: {cd['tot_digits']}')
    exp_lst.append(f'Spaces: {cd['tot_spaces']}')
    exp_lst.append(f'Punctuation: {cd['tot_punctuation']}')
    
    sorted_by_count = sorted(cd['all_letters_dict'].items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_by_count[:10]

    index = 1
    for i in top_10:
        exp_lst.append(f'{index:>2}. "{i[0]}" - {i[1]:,} times ({100 * (i[1] / cd['tot_letters'] ):.1f}%) ')
        index += 1

    exp_lst.append('''============================================================
End of Analysis Report
============================================================''')
    
    with open('report.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(exp_lst))