# Imports

import re
import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import pandas as pd

# Function definations

def extract_words(s: str):
    return [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in s.split()]

def diag(list1):
    return 256*np.eye(len(list1), dtype=int)

def unique_words(word_list):
    unique_list = []
    for i in word_list:
        counter = 0
        for j in word_list:
            if i == j:
                counter += 1
        if counter == 1:
            unique_list.append(i)
    return unique_list

def diff(list1, list2):
    difference = [i for i in list1 + list2 if i not in list1 or i not in list2]
    return difference

def repeated_words(difference):
    return list(set(difference))

def find_index(list1, word):
    index_num = []
    for i in range(len(list1)):
        if word == list1[i]:
            index_num.append(i)
    return index_num

def repeat_index_dict(list1, rep_words):
    dictionary = {}
    for i in rep_words:
        dictionary.update({i:find_index(list1, i)})
    return dictionary

def main():

    # Read file

    file = open("lyrics.txt")
    input_string = file.read().replace("\n", " ")
    file.close()

    input_string = input_string.lower()
    List = extract_words(input_string)

    # Build similar matrix

    A = diag(List)
    unique_list = unique_words(List)
    list_diff = diff(unique_list, List)
    rep_words = repeated_words(list_diff)
    repeat_index = repeat_index_dict(List, rep_words)
    repeat_dict = {}
    sorted_repeat_dict = {}
    C = np.random.randint(1, 256, size=len(rep_words))

    for i in rep_words:
        repeat_dict.update({i:len(repeat_index[i])})

    sorted_words = sorted(repeat_dict.items(), key=lambda x: x[1], reverse=True)

    for i in sorted_words:
        sorted_repeat_dict.update({i[0]:i[1]})

    for i in rep_words:
        for j in repeat_index[i]:
            for k in repeat_index[i]:
                A[j][k] = C[rep_words.index(i)]

    # Defining BG and unique colors

    tab20 = cm.get_cmap('tab20', 255)
    newcolors = tab20(np.linspace(0, 1, 255))
    bool_flip = int(input('Black Background? (1: Yes, 0: No): '))
    if bool_flip:
        bg_color = np.array([0, 0, 0, 1])
        unique_color = np.array([1, 1, 1, 1])
        bord_width = 0
        bool_plot = 0
    else:
        bg_color = np.array([1, 1, 1, 1])
        unique_color = np.array([0, 0, 0, 1])
        bord_width = 0.01
        bool_plot = 1

    newcolors[:1, :] = bg_color
    newcolors[254:, :] = unique_color
    newcmp = ListedColormap(newcolors)

    # Plotting color map

    font = {'family': 'Helvetica',
        'color': 'black',
        'weight': 'bold',
        'size': 4}

    plt.figure()
    plt.imshow(A, cmap=newcmp)
    plt.box(bool_plot)
    plt.rcParams['axes.linewidth'] = bord_width
    plt.xticks([])
    plt.yticks([])
    song_name = input("Input song name: ")
    artist_name = input("Input artist name: ")
    track_label = song_name + " - " + artist_name
    plt.xlabel(track_label, horizontalalignment='right', x=1.0, fontdict=font)
    savefile = track_label + '.png'
    plt.savefig('img/' + savefile, dpi=1000)

    # Displaying sorted word list

    sorted_input = int(input('Sorted word list? (Yes: 1, No: 0): '))

    if sorted_input:
        df_sorted = pd.DataFrame(sorted_repeat_dict.items(), columns=['Word', 'Count'])
        df_sorted.head(len(List))

# Run main function

if __name__ == "__main__":

    main()