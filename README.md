# VOX Project: Visualizing Lyrical Symmertry

![Lyrics, visualized](img/Every%20Breath%20You%20Take%20-%20The%20Police.png)

I love data visualization and finding hidden patterns in data!

Inspired by the VOX EARWORM video 'Why we really really really like repetition in music'. This program creates a symmetrical matrix based on the lyrics of a song, and generates a beautiful lyrical map! All credit goes to Collin Morris, who came up with this amazing idea. The visualization above is [*Every breath you take* by The Police](https://www.youtube.com/watch?v=OMOGaugKpzs).

## Required Imports

```python
import re
import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import pandas as pd
```

## How to Run

1. Drop the lyrics of your favorite song in `lyrics.txt`
2. Run `main.py`
3. Select your output options in CMD / Terminal. You can set Sorted Word List to `Yes` to generate a list of words in the song sorted by their propensity.
4. Look for your image in `/img/YOUR_IMAGE`

Enjoy!
