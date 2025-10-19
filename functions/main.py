# Använderens input/output
# Lägger till kommentarer så det blir mindre förvirrande i början

import meny as meny
import filselektion as filselektion
import Dictionaries

def main():
    print('''
Welcome to the Text Analyser!
This programme analyses text files and provides statistical
insights.
          ''')
    meny.meny()
    user_inp = int(input('Enter your choice (1-7): '))

    if user_inp == 1:
        filselektion.file_selection_menu()
    if user_inp == 2:
        return 'Yuh chief beef'
    if user_inp == 3:
        return 'Yuh chief beef'
    if user_inp == 4:
        return 'Yuh chief beef'
    if user_inp == 5:
        print(Dictionaries.letter_dict)
            
    if user_inp == 6:
        return 'Yuh chief beef'
    if user_inp == 7:
        print('Thank you for using text analyzer!')
        return

main()