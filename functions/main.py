# Använderens input/output

import importlib
import matplot
import fileselection as fileselection
import basicstatistics as basicstatistics
import exportstatistics as exportstatistics
importlib.reload(fileselection) 
importlib.reload(matplot) 
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
        menu()
        if data is None:
            print('No file loaded.')
        else:
            print(f"Current file: {data['current_file']}")      
        print()
        
        user_inp = int(input('Enter your choice (1-7): '))

        if user_inp == 1: # Välj fil och gör analys
            data = fileselection.file_selection_menu()
            continue
        
        if user_inp == 2: #basic statistics
            if data is None:
                print('Load a file first')
            else:
                # Printar basic stats
                basicstatistics.basic_statistics(data)
            print()
            
            mat_user = int(input('Would you like a matplot of this data? (1 for yes, 0 for no): '))
            if mat_user == 1:
                matplot.basic_statistics_plot(data)
            continue
            
        if user_inp == 3: #word frequency
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.word_frequency_analysis(data)
            print()
            
            mat_user = int(input('Would you like a matplot of this data? (1 for yes, 0 for no): '))
            if mat_user == 1:
                matplot.word_analysis_plot(data)
            continue
            
        if user_inp == 4: # Sentence analysis
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.sentence_analysis(data)
            print()
            
            mat_user = int(input('Would you like a matplot of this data? (1 for yes, 0 for no): '))
            if mat_user == 1:
                matplot.sentence_analysis_plot(data)
            continue
            
        if user_inp == 5: # Character analysis
            if data is None:
                print('Load a file first')
            else:
                basicstatistics.character_analysis(data)
            print()
            
            mat_user = int(input('Would you like a matplot of this data? (1 for yes, 0 for no): '))
            if mat_user == 1:
                matplot.character_analysis_plot(data)
            continue 
            
        if user_inp == 6:
            if data is None:
                print('Load a file first')
            else:
                exportstatistics.report_exp(data)
            print(f"Results exported to 'report.txt' \nResults saved in simple text format - easy to read and understand!")
            continue
            
        if user_inp == 7:
            print('Thank you for using text analyzer!')
            return


def menu():
    print('''
==================================================
                TEXT ANALYSER
==================================================
1. Load text file
2. Display basic statistics
3. Word frequency analysis
4. Sentence analysis
5. Character analysis
6. Export results
7. Exit
==================================================
          ''')
    
main()