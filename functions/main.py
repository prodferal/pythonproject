# Använderens input/output
# Lägger till kommentarer så det blir mindre förvirrande i början

import meny as meny
import filselektion as filselektion
import Dictionaries
import basicstatistik as basikstatistik

def main():
    print('''
Welcome to the Text Analyser!
This programme analyses text files and provides statistical
insights.
          ''')
 

    while True:
        meny.meny()
        print(f'Current file: {Dictionaries.current_file}')
        print()
        user_inp = int(input('Enter your choice (1-7): '))

        if user_inp == 1:
            filselektion.file_selection_menu()
            continue
        
        if user_inp == 2:
            basikstatistik.basic_statistics()
            print()
            enter_pressed = input('Press Enter to continue...')
            continue
        if user_inp == 3:
            basikstatistik.word_frequency_analysis()
            print()
            enter_pressed = input('Press Enter to continue...')
            continue
        if user_inp == 4:
            basikstatistik.sentence__analysis()
            print()
            enter_pressed = input('Press Enter to continue...')
            continue
        if user_inp == 5:
            print(Dictionaries.letter_dict)
                
        if user_inp == 6:
            return 'Yuh chief beef'
        if user_inp == 7:
            print('Thank you for using text analyzer!')
            return

main()