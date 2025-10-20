# Printa ut statistik för vald textfil
import Dictionaries

def basic_statistics():
    print()
    print(f'--- Basic Statistics for "{Dictionaries.current_file}" ---')
    totWords = sum(Dictionaries.common_words_dict.values())
    uniqueWords = len(Dictionaries.common_words_dict)
    print(f'Lines: {Dictionaries.count_lines}')
    print(f'Words: {totWords}')
    print(f'Unique Words: {uniqueWords}')
    print(f'Characters (with spaces): {Dictionaries.chars_with_spaces}')