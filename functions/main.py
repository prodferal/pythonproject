# Använderens input/output
import meny as meny
import filselektion as filselektion

def main():
    print('''
Welcome to the Text Analyser!
This programme analyses text files and provides statistical
insights.
          ''')
    meny.meny()
    user_inp = int(input('Enter your choice (1-7): '))

    if user_inp == 1:
        filselektion.fileselection()

main()