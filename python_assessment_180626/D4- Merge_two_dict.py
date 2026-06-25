d1={1:"Lee", 2:"Kim"}
d2={3:"Park", 4:"Choi"}
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

result = merge_dicts(d1, d2)
print("The merged dictionary is:", result)
