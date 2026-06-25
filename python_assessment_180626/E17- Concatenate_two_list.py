l=[1,2,3]
m=[4,5,6]

def concatenate_lists(list1, list2):
    return [a+b for a, b in zip(list1, list2)]
n = concatenate_lists(l, m)
print("The concatenated list is:", n)