# Filselektion, och analysering av vald fil

import os
import Dictionaries

def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&°()_-+=<>?/,.;:!{}[]|":
            line = line.replace(ch, ' ')
    return line

def processLine(line, common_words_dict):
    line = replacePunctuation(line) # Replace punctuation with space
    words = line.split() # Get words from each line
    
    for word in words:
        if word in common_words_dict:
            common_words_dict[word] += 1 # Increase count for word
        else:
            common_words_dict[word] = 1 # Add an item to the dictionary


def chosen_file(file_name):
    # Funktion som analyserar vald fil

    print(f'Analysing "{file_name}"...')
    with open(f'txtfiles/{file_name}', 'r', encoding='utf-8') as file:

        for line in file:
            Dictionaries.count_lines += 1
            processLine(line.lower(), Dictionaries.common_words_dict) #common words
            Dictionaries.chars_with_spaces += len(line)



            file_letter_list = list(line) # list of all characters in line
            for i in file_letter_list: #counts all the letters in the text file (letter_dict)
                for letter, v in Dictionaries.letter_dict.items():

                    if letter == i.lower():
                        Dictionaries.letter_dict[i.lower()] += 1
            

            for i in file_letter_list:
                if i == '.' or i == '?' or i == '!':
                    Dictionaries.count_sentences += 1
            
            
        


        #for char in string.punctuation:
            #text = file.replace(char, '')
                

        print(f'Analysis complete! Processed {Dictionaries.count_lines} lines.')
        #print(Dictionaries.letter_dict)


def handling_input(txt_files):
    while True:
        user_file_selection = input('Enter number of filename (or q to quit): ').strip()
        if user_file_selection.lower() == 'q':
                return user_file_selection
            
        try:
            if user_file_selection.isdigit():
                user_value = int(user_file_selection)
                if 1 <= user_value <= len(txt_files):
                    path_way = txt_files[user_value - 1]

                else:
                    raise ValueError(f'Number out of range.')

            else:
                if user_file_selection.lower().endswith('.txt'):
                    path_way = user_file_selection 

                else: path_way = user_file_selection + '.txt'

            if not os.path.isfile(f'txtfiles/{path_way}'):
                raise FileNotFoundError(f'File not found.')
            
            Dictionaries.current_file = path_way
            return path_way

        except ValueError as v:
            print(v)
            continue

        except FileNotFoundError as f:
            print(f)
            continue

def file_selection_menu():
    # Meny för filselektion

    txt_files = ['artofmusic.txt', 'testtxt.txt']

    print('''
--- File Selection ---
Available text files: 
          ''')
    print(f'1. {txt_files[0]}\n2. {txt_files[1]}\n')
    
    user_file_selection = handling_input(txt_files)
    if user_file_selection.lower() == 'q':
        print('Bye bye!')
        return None
    
    chosen_file(user_file_selection)
    print(f'Successfully loaded and analysed "{user_file_selection}"')
    