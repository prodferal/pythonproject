import matplotlib.pyplot as plt
import numpy as np

def basic_statistics_plot(data): #Basic statistics, när input är 2
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Plot 1, histogram / bar
    x_1 = np.array(['Lines', 'Paragraphs', 'Sentences', 'Unique Words'])
    y_1 = np.array([
        data['count_lines'],
        data['count_paragraph'],
        data['sentence_data']['count_sentences'],
        len(data['word_data']['unique_word_set'])
    ])
    colors = ['skyblue', 'lightgreen', 'salmon', 'gold']

    bars = ax1.bar(x_1, y_1, color=colors, width=0.65)  # a bit wider bars
    ax1.set_title('Text Composition')
    ax1.set_ylabel('Count')
    ax1.set_ylim(0, max(y_1) * 1.15)  # headroom

    # Plot 2, cirkeldiagram / piechart
    cd = data['character_data']
    total = sum([data['chars_no_spaces'], cd['tot_punctuation'], cd['tot_spaces']])
    perc1 = str(round((data['chars_no_spaces'] / total) * 100, 1))
    perc2 = str(round((cd['tot_punctuation'] / total) * 100, 1))
    perc3 = str(round((cd['tot_spaces'] / total) * 100, 1))
    
    labels = ['Characters' + '\n' + '(' + perc1 + '%' + ')',
              'Punctuation' + '\n' '(' + perc2 + '%' + ')',
              'Spaces' + '\n' '(' + perc3 + '%' + ')']
    
    y_2 = np.array([data['chars_no_spaces'], cd['tot_punctuation'], cd['tot_spaces']])
    
    ax2.pie(y_2, labels=labels, colors=colors, startangle = 90)
    ax2.set_title('Character Type Distribution')
    ax2.set_aspect('equal')

    fig.tight_layout()
    plt.show()



def word_analysis_plot(data): # När input är 3
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    d = data['word_data']['common_words_dict']
    pairs = list(d.items())
    items = [[count, word] for (word, count) in pairs]
    items.sort(reverse = True) # Sort pairs in items
    top = items[:10]
    
    counts = [c for c, _ in top]
    words = [w for _, w in top]

    x_1 = np.array([w for w in words])
    y_1 = np.array([c for c in counts])

    bars = ax1.bar(x_1, y_1, width=0.65)  # a bit wider bars
    ax1.set_xlabel('Words')
    ax1.set_ylabel('Count')
    ax1.tick_params(axis='x', rotation=45) # rotera texten 45 grader så att orden inte krockar
    plt.setp(ax1.get_xticklabels(), rotation=25, fontsize=8)

    
    
    plt.show()


def sentence_analysis_plot(data):  # Defines a function that takes 'data' (your dataset) as input
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4)) #skapar en mall av 1 rad med 2 stycken matplots 
    
    sd = data['sentence_data']  # tar fram sentence_data ur data-dictionaryn
    
    sorted_by_count = sorted(sd['length_hist'].items(), key=lambda x: x[1], reverse=True) #lista med tuples
    # sd['length_hist'].items() skapar en lista där varje element är en tuple med key som första element och value/count som andra element
    # key=lambda x: x[1] att sortera men att alltid baserat på det andra elementet x[1], istället för första x[0]
    # reverse=True, på default så sorteras detta från minsta till största, men vi vill ha motsatsen, för vi vill ha top_8 största.
    
    top_8 = sorted_by_count[:8]  # skapar en lista (med tuples) med enbart första 8 elementen
    top_8_words = [str(i) + ' words' for i, v in top_8]  # skapar en lista med enbart första elementen av varje tuple i top_8 + ' words'
    top_8_value = [v for i, v in top_8]  # skapar en lista med enbart korresponderande andra elementen av varje tuple

    # Plot 1, histogram 
    sentence_lengths = []  # en tom lista för att spara alla längder och även hur många gånger de uppstår
    # Empty list to store one entry per sentence (used for histogram plotting)
    for length, count in sd['length_hist'].items():  # loopar igenom varje tuple, med mening längden och dess frekvens
        sentence_lengths.extend([length] * count)  # lägger till varje längd i listan, mängden gånger som den uppstår.
    
    ax1.hist(sentence_lengths, bins=15, color='lightgreen', edgecolor='green', alpha=0.5) #skapar histogram, med 15 'intervall'/bins
    ax1.set_title('Sentence Length Distribution')
    ax1.set_xlabel('Sentence Length (words)')
    ax1.set_ylabel('Frequency')


    # Plot 2, histogram också
    x_2 = np.array(top_8_words)  # konverterar listan till en Numpy array för matplotting
    y_2 = np.array(top_8_value)  

    bars = ax2.bar(x_2, y_2, color='orange', width=0.65) # skapar 1 'bar' för varje värde i listan (8st)
    ax2.set_title('Most common sentence lengths')  
    ax2.set_ylabel('Number of sentences')  
    ax2.set_ylim(0, max(y_2) * 1.15)  # höjer y axeln till det största y värdet plus 15%, för att få plats med allt
    ax2.tick_params(axis='x', rotation=45)  # roterar x axelns texter med 45 grader för att de inte ska överlappa

    plt.tight_layout()  # justerar titlar och matplotten
    plt.show()

    
def character_analysis_plot(data): # Character analysis, input 5
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    d = data['character_data']['all_letters_dict']

    sorted_by_count = sorted(d.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_by_count[:10]
    top_10_letters = [letter for letter, value in top_10] # en lista med alla top 10 bokstäver
    top_10_values = [value for letter, value in top_10] #en lista med alla värden (mängden gånger de dyker upp)


    # Plot 1, histogram / bar 
    x_1 = np.array(top_10_letters) #konvertera listan till numpy array för matplotting
    y_1 = np.array(top_10_values)
    colors = ['skyblue', 'gold', 'lightcoral'] #lista av fina färger, valt ifrån matplotlibs webbsida

    bars = ax1.bar(x_1, y_1, color=colors, width=0.65) #skapa bars med färger i ordningen av listan
    ax1.set_title('Top 10 most common letters')
    ax1.set_ylabel('Frequency')
    ax1.set_ylim(0, max(y_1) * 1.15)  # rum 


    # Plot 2, cirkeldiagram / piechart
    cd = data['character_data']
    total = sum([cd['tot_letters'], cd['tot_punctuation'], cd['tot_spaces']]) #plussa alla mängd tal, totala punctiation, och mellanslag
    perc1 = str(round((cd['tot_letters'] / total) * 100, 1)) #beräkna procenten med: andel/totalen
    perc2 = str(round((cd['tot_punctuation'] / total) * 100, 1))
    perc3 = str(round((cd['tot_spaces'] / total) * 100, 1))
    

    labels = ['Letters'     + '\n' + '(' + perc1 + '%' + ')', #texten som ska va vid varje piechart slice, namnet och dess procent
              'Punctuation' + '\n' + '(' + perc2 + '%' + ')',
              'Spaces'      + '\n' + '(' + perc3 + '%' + ')',
             ]
    
    y_2 = np.array([cd['tot_letters'], cd['tot_punctuation'], cd['tot_spaces']]) #en numpy array med dessa 3 totaler
    
    ax2.pie(y_2, labels=labels, colors=colors, startangle = 90) #gjord till en piechart/cirkeldiagram
    ax2.set_title('Character Type Distribution')
    ax2.set_aspect('equal')

    plt.tight_layout()
    plt.show()
