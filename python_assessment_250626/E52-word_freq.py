text = "Python is great. Python is fast, and learning Python is fun!" 
#Expected Output: {'python': 3, 'is': 3, 'great': 1, 'fast': 1, 'and': 1, 'learning': 1, 'fun': 1}

import string

def word_freq(text):
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
print(word_freq(text))