# Filselektion, och analysering av vald fil

import os


def chosen_file(file_name):
    # Funktion som analyserar vald fil

    print(f'Analysing "{file_name}"...')
    with open(f'txtfiles/{file_name}', 'r', encoding='utf-8') as file:

        countLines = 0

        for line in file:
            countLines += 1
        print(f'Analysis complete! Processed {countLines} lines.')

    return countLines
    


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
    