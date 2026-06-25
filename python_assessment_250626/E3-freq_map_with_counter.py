s  = "python programming"

from collections import defaultdict
fm=defaultdict(int)

for i in s:
    fm[i]+= 1 
print(fm)

#-----------[or]-----------||

from collections import Counter

freq_map = Counter(s)
    
print(freq_map)