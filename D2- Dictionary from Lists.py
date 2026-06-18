list1 = [1,2,3]
list2 = ["first", "second", "third"]

def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

result = create_dict_from_lists(list1, list2)
print("The dictionary created from the two lists is:", result)