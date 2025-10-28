import matplotlib.pyplot as plt
import numpy as np

def basic_statistics_plot(data):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Plot 1, bar
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

    # Plot 2, piechart
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



def word_analysis_plot(data):
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
    plt.setp(ax1.get_xticklabels(), rotation=25, fontsize=8)

    
    
    plt.show()

