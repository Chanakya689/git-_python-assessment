d = {1:"Lee",2:"Kim",3:"Park",4:"Choi"}

print("The original dictionary is:", d)
def clear_dict(dictionary):
    dictionary.clear()
    return dictionary

d = clear_dict(d)
print("The dictionary after clearing is:", d)   