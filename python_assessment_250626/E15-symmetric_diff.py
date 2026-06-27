list1 = [101, 102, 103]
list2 = [103,104, 105] 

#Expected Output: {101, 102, 104, 105}

s1 = set(list1)
s2 = set(list2)

def symmetric_diff(s1,s2):
    return s1.symmetric_difference(s2)

print(symmetric_diff(s1,s2))

