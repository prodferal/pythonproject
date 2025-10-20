# Printa ut statistik för vald textfil
import Dictionaries

def basic_statistics(): # när input är 2
    print()
    print(f'--- Basic Statistics for "{Dictionaries.current_file}" ---')
    totWords = sum(Dictionaries.common_words_dict.values())
    uniqueWords = len(Dictionaries.common_words_dict)
    print(f'Lines: {Dictionaries.count_lines}')
    print(f'Paragraphs: {Dictionaries.count_paragraph}')
    print(f'Sentences: {Dictionaries.count_sentences}')
    print(f'Words: {totWords}')
    print(f'Unique Words: {uniqueWords}')
    print(f'Characters (with spaces): {Dictionaries.chars_with_spaces}')


def word_frequency_analysis(): # när input är 3
    print("hej")