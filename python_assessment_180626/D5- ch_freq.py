s = "python programming"

def ch_freq(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

result = ch_freq(s)
print("The character frequency in the string is:", result)