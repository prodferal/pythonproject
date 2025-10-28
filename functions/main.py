# Använderens input/output

import importlib
import menu as menu
import functions.matplot as matplot
import fileselection as fileselection
import basicstatistics as basicstatistics
import functions.exportstatistics as exportstatistics
importlib.reload(fileselection) 
importlib.reload(basicstatistics) 
importlib.reload(exportstatistics) 

def main():
    print('''
Welcome to the Text Analyser!
This programme analyses text files and provides statistical
insights.
          ''')
 
    data = None # För att kunna printa 'no file loaded' innan data dicten är loadad
    
    while True:
        menu.menu()
        if data is None:
            print('No file loaded.')
        else:
            print(f'Current file: {data['current_file']}')      
        print()
        
        user_inp = int(input('Enter your choice (1-7): '))

        if user_inp == 1:
            data = fileselection.file_selection_menu()
            continue
        
        if user_inp == 2:
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.basic_statistics(data)
            print()
            
            mat_user = int(input('Would you like a matplot of this data? (1 for yes, 0 for no): '))
            if mat_user == 1:
                matplot.basic_statistics_plot(data)
            continue
            
        if user_inp == 3:
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.word_frequency_analysis(data)
            print()
            
            mat_user = int(input('Would you like a matplot of this data? (1 for yes, 0 for no): '))
            if mat_user == 1:
                matplot.word_analysis_plot(data)
            continue
            
        if user_inp == 4:
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.sentence_analysis(data)
            print()
            input('Press Enter to continue...')
            continue
            
        if user_inp == 5:
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.character_analysis(data)
            print()
            input('Press Enter to continue...')
            continue
            
        if user_inp == 6:
            if data is None:
                print('Load a file first')
            else:
                exportstatistics.report_exp(data)
            print(f'Results exported to "Project/{data['current_file']}.report.txt \nResults saved in simple text format - easy to read and understand!')
            continue
            
        if user_inp == 7:
            print('Thank you for using text analyzer!')
            return

main()