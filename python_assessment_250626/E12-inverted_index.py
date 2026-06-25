d = {"Orwell": ["1984", "Animal Farm"], "Huxley": ["Brave New World"]}

#o/p = {'1984': 'Orwell', 'Animal Farm': 'Orwell', 'Brave New World': 'Huxley'}

from collections import defaultdict
fd=defaultdict(str)

def inverted_index(d):

    for k,v in d.items():
        if isinstance(v,list):
            for i in v:
                 fd[i] = k

    return fd             
    
new_dict = inverted_index(d)
print(dict(new_dict))
    