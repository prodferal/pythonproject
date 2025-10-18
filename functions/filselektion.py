# Filselektion, och analysering av vald fil

import os


def chosen_file(file_name):
    # Funktion som väljer och analyserar vald fil

    print(f'Analysing "{file_name}"...')
    with open(f'txtfiles/{file_name}', 'r', encoding='utf-8') as file:

        # Kolla ifall fil existerar (temporär för test)
        if os.path.isfile(f"txtfiles/{file_name}"):
            print(f"{file_name} exists")
            
        countLines = 0

        for line in file:
            countLines += 1
        print(f'Analysis complete! Processed {countLines} lines.')

    return countLines
    
    input.close()




def file_selection_menu():
    # Meny för filselektion

    txt_files = ['art_of_music_text.txt', 'testtxt.txt']

    print('''
--- File Selection ---
Available text files: 
          ''')
    print(f'1. {txt_files[0]}\n2. {txt_files[1]}\n')
    
    # Fungerar bara med nummer just nu
    user_file_selection = int(input('Enter filename or number from list above: '))

    chosen_file(txt_files[user_file_selection - 1])
    print(f'Successfully loaded and analysed "{txt_files[user_file_selection - 1]}"')
    