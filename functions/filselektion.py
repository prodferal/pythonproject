# Filselektion, och analysering av vald fil

import os


def chosen_file(user_inp, file_name):
    # Funktion som väljer och analyserar vald fil
    if user_inp == 2:
        print(f'Analysing "{file_name}"...')
        input = open("txtfiles/testtxt.txt", "r")

        # Kolla ifall fil existerar (temporär)
        if os.path.isfile("txtfiles/testtxt.txt"):
            print("testtxt.txt exists")
        
        countLines = 0
        for line in input:
            countLines += 1
        print(f'Analysis complete! Processed {countLines} lines.')

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

    chosen_file(user_file_selection, txt_files[user_file_selection - 1])
    