l=["chan","lee","", "chung", "space", "", "chung"]

print("The original list is:", l)
print(len(l))

def remove_empty_strings(lst):
    return [x for x in lst if x != ""]

cleaned_list = remove_empty_strings(l)
print("The list after removing empty strings is:", cleaned_list)
print("The length of the cleaned list is:", len(cleaned_list))