# Printa ut statistik för vald textfil
import Dictionaries

def basic_statistics():
    print()
    print(f'--- Basic Statistics for "{Dictionaries.current_file}" ---')
    totWords = sum(Dictionaries.common_words_dict.values())
    print(f'Words: {totWords}')
    