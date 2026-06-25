d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4} 
#Expected Output: {'a': [1], 'b': [2, 3], 'c': [4]}

from collections import defaultdict
df = defaultdict(list)

def dict_merge(d1,d2):
    
    for k1,v1 in d1.items():
        df[k1].append(v1)

    for k2,v2 in d2.items():
        if k2 in df:
            df[k2].append(v2) 
        else:
            df[k2].append(v2)       

    print(df)

dict_merge(d1,d2)        

        
