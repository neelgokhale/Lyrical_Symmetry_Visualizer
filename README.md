# VOX Project: Visualizing Lyrical Symmertry

Inspired by the VOX EARWORM video 'Why we really really really like repetition in music'. This program creates a symmetrical matrix based on the lyrics of a song (stored in the lyrics.txt file), and generates a beautiful lyrical map!

## Imports and Set-up

```python
import re
import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import pandas as pd
```

## Function Definations


```python
def extract_words(s):
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

```

## Reading Lyrics from File


```python
file = open("lyrics.txt")
input_string = file.read().replace("\n", " ")
file.close()

input_string = input_string.lower()
List = extract_words(input_string)
```

## Building Lyrical Map


```python
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

```

## Defining Background and Unique Colors


```python
tab20 = cm.get_cmap('tab20', 255)
newcolors = tab20(np.linspace(0, 1, 255))
bool_flip = int(input('Flip colors? (1: Yes, 0: No): '))
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
```

    Flip colors? (1: Yes, 0: No):  1
    

## Plotting Color Map


```python
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
plt.savefig(savefile, dpi=1000)
```

    Input song name:  Tell Me What to Do
    Input artist name:  Shinee
    


![png](/img/output_12_1.png)


## Sorted Word Count


```python
df_sorted = pd.DataFrame(sorted_repeat_dict.items(), columns=['Word', 'Count'])
df_sorted
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Word</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>me</td>
      <td>24</td>
    </tr>
    <tr>
      <th>1</th>
      <td>do</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>to</td>
      <td>23</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tell</td>
      <td>23</td>
    </tr>
    <tr>
      <th>4</th>
      <td>what</td>
      <td>23</td>
    </tr>
    <tr>
      <th>5</th>
      <td>naega</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>don't</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>meonjeo</td>
      <td>6</td>
    </tr>
    <tr>
      <th>8</th>
      <td>da</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>more</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>lonely</td>
      <td>4</td>
    </tr>
    <tr>
      <th>11</th>
      <td>dagaga</td>
      <td>4</td>
    </tr>
    <tr>
      <th>12</th>
      <td>cry</td>
      <td>4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>no</td>
      <td>4</td>
    </tr>
    <tr>
      <th>14</th>
      <td>du</td>
      <td>4</td>
    </tr>
    <tr>
      <th>15</th>
      <td>gyesok</td>
      <td>3</td>
    </tr>
    <tr>
      <th>16</th>
      <td>i</td>
      <td>3</td>
    </tr>
    <tr>
      <th>17</th>
      <td>heullin</td>
      <td>3</td>
    </tr>
    <tr>
      <th>18</th>
      <td>jeojeobeorin</td>
      <td>3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>boreul</td>
      <td>3</td>
    </tr>
    <tr>
      <th>20</th>
      <td>geu</td>
      <td>3</td>
    </tr>
    <tr>
      <th>21</th>
      <td>nunmure</td>
      <td>3</td>
    </tr>
    <tr>
      <th>22</th>
      <td>makdareun</td>
      <td>3</td>
    </tr>
    <tr>
      <th>23</th>
      <td>mureobollae</td>
      <td>3</td>
    </tr>
    <tr>
      <th>24</th>
      <td>uri</td>
      <td>3</td>
    </tr>
    <tr>
      <th>25</th>
      <td>kkeuteseo</td>
      <td>3</td>
    </tr>
    <tr>
      <th>26</th>
      <td>gil</td>
      <td>3</td>
    </tr>
    <tr>
      <th>27</th>
      <td>dakkajugo</td>
      <td>3</td>
    </tr>
    <tr>
      <th>28</th>
      <td>siganeun</td>
      <td>2</td>
    </tr>
    <tr>
      <th>29</th>
      <td>maeumi</td>
      <td>2</td>
    </tr>
    <tr>
      <th>30</th>
      <td>know</td>
      <td>2</td>
    </tr>
    <tr>
      <th>31</th>
      <td>nareul</td>
      <td>2</td>
    </tr>
    <tr>
      <th>32</th>
      <td>mal</td>
      <td>2</td>
    </tr>
    <tr>
      <th>33</th>
      <td>marhaejugil</td>
      <td>2</td>
    </tr>
    <tr>
      <th>34</th>
      <td>barae</td>
      <td>2</td>
    </tr>
    <tr>
      <th>35</th>
      <td>for</td>
      <td>2</td>
    </tr>
    <tr>
      <th>36</th>
      <td>neoui</td>
      <td>2</td>
    </tr>
    <tr>
      <th>37</th>
      <td>one</td>
      <td>2</td>
    </tr>
    <tr>
      <th>38</th>
      <td>anhado</td>
      <td>2</td>
    </tr>
    <tr>
      <th>39</th>
      <td>nega</td>
      <td>2</td>
    </tr>
    <tr>
      <th>40</th>
      <td>the</td>
      <td>2</td>
    </tr>
    <tr>
      <th>41</th>
      <td>ne</td>
      <td>2</td>
    </tr>
    <tr>
      <th>42</th>
      <td>nan</td>
      <td>2</td>
    </tr>
    <tr>
      <th>43</th>
      <td>deo</td>
      <td>2</td>
    </tr>
    <tr>
      <th>44</th>
      <td>you</td>
      <td>2</td>
    </tr>
    <tr>
      <th>45</th>
      <td>manhi</td>
      <td>2</td>
    </tr>
    <tr>
      <th>46</th>
      <td>bondamyeon</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>
