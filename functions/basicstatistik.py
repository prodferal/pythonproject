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

    print(f'Lines: {Dictionaries.count_lines}')
    print(f'Paragraphs: {Dictionaries.count_paragraph}')
    print(f'Sentences: {Dictionaries.count_sentences}')
    print(f'Words: {totWords}')
    print(f'Unique Words: {uniqueWords}')
    print(f'Characters (with spaces): {Dictionaries.chars_with_spaces}')
    print(f'Characters (no spaces): {Dictionaries.chars_no_spaces}')
    print(f'Average words per line: {avgWordsLine:.1f}')
    print(f'Average word length: {avgWordLength:.1f}')
    print(f'Average words per sentence: {avgWordSentence:.1f}')



def word_frequency_analysis(): # när input är 3
    print("hej")