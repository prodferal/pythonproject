# Filselektion, och analysering av vald fil
import os

def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&°()_-+=<>?/,.;:!{}[]|":
            line = line.replace(ch, ' ')
    return line

def processLine(line, data):
    line = replacePunctuation(line) # Replace punctuation with space
    words = line.split()
    wd = data['word_data']
    wdf = wd['common_words_dict']
    unique_words = wd['unique_word_set']

    for word in words:
        wdf[word] = wdf.get(word, 0) + 1
        unique_words.add(word) 
            
def paragraphChecker(line, in_paragraph, data):
    if line.strip() != '':
        if not in_paragraph:
            data['count_paragraph'] += 1
            in_paragraph = True
    else:
        in_paragraph = False  

    return in_paragraph

def sentenceChecker(line, data): # longest, shortest sentence
    sd = data['sentence_data']
    tokens = line.strip().split()
    
    for i in tokens:
        while i and i[-1] in "\"')]}”’":   # strip certain characters
            i = i[:-1]
        if i == '' or i is None:
            continue   # after stripping i is empty
            
        end_sent = False
        if i[-1] in ".!?":     # is the sentence over
            end_sent = True
            sd['count_sentences'] += 1
            
        if i != '' or i is not None:
            sd['cur_sen'].append(i)
            
        if end_sent is True:
            n = len(sd['cur_sen'])
            hist = sd['length_hist']
            if n in hist:
                hist[n] += 1
            else:
                hist[n] = 1
            if n > 0:
                sentence_text = ' '.join(sd['cur_sen'])
                if sd['longest_sentence'] == '' or n > sd['longest_len']:
                    sd['longest_sentence'] = sentence_text
                    sd['longest_len'] = n
                    
                if sd['shortest_sentence'] == '' or sd['shortest_len'] == 0 or n < sd['shortest_len']:
                    sd['shortest_sentence'] = sentence_text
                    sd['shortest_len'] = n

            sd['cur_sen'] = []

def characterFunc(line, data):
    cd = data['character_data']
    for i in line:
        cd['tot_characters'] += 1
                    
        if i == ' ':
            cd['tot_spaces'] += 1
        elif i.isdigit():
            cd['tot_digits'] += 1
        elif i == '.':
            cd['tot_punctuation'] += 1
        else:
            cd['tot_letters'] += 1
                    
            if i in cd['all_letters_dict']:
                cd['all_letters_dict'][i] += 1
            else:
                cd['all_letters_dict'][i] = 1


def chosen_file(file_name):
    # Funktion som analyserar vald fil
    
    data = {
        'current_file': file_name,
        'count_lines': 0,
        'word_count': 0,
        'chars_with_spaces': 0,
        'chars_no_spaces': 0,
        'count_paragraph': 0,

        'word_data': {
            'common_words_dict': {}, 
            'unique_word_set': set(),
            'longest_word': '',
            'shortest_word': '',
            'words_appearing_once': 0,
            'avg_word_len': 0
        },

        'sentence_data': {
            'count_sentences': 0,
            'avgWordSentence': 0.0,
            'longest_sentence': '',
            'shortest_sentence': '',
            'longest_len': 0,
            'shortest_len': 0,
            'cur_sen': [],
            'length_hist': {}
        },

        'character_data': {
            'tot_spaces': 0,
            'tot_digits': 0,
            'tot_characters': 0,
            'tot_punctuation': 0,
            'tot_letters': 0,
            'all_letters_dict': {}
        }
    }
    
    print(f'Analysing "{file_name}"...')

    in_paragraph = False
    
    with open(f'txtfiles/{file_name}', 'r', encoding='utf-8') as file:

        for line in file:
            data['count_lines'] += 1
            data['word_count'] += len(line.split())
            data['chars_with_spaces'] += len(line)         
            data['chars_no_spaces'] += len(line.replace(' ', ''))
            processLine(line.lower(), data) #common words
            in_paragraph = paragraphChecker(line, in_paragraph, data) # paragraph checker
            sentenceChecker(line, data) # sentence analysis
            characterFunc(line, data) # character analysis
            
        print(f'Analysis complete! Processed {data['count_lines']} lines.')
        return data

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
                else: 
                    path_way = user_file_selection + '.txt'

            if not os.path.isfile(f'txtfiles/{path_way}'):
                raise FileNotFoundError(f'File not found.')
            
            return path_way

        except ValueError as v:
            print(v)
            continue

        except FileNotFoundError as f:
            print(f)
            continue

        except Exception as e:
            print(e)
            continue

def file_selection_menu():
    # Meny för filselektion

    path = 'txtfiles'

    print('''
--- File Selection ---
Available text files: 
          ''')
    txt_files = [f for f in os.listdir(path) if f.endswith('.txt')]

    for i, file in enumerate(txt_files, start=1):
        print(f'{i}. {file}')
    
    user_file_selection = handling_input(txt_files)
    if user_file_selection.lower() == 'q':
        print('Bye bye!')
        return None
    
    data = chosen_file(user_file_selection)
    print(f'Successfully loaded and analysed "{user_file_selection}"')

    return data
    