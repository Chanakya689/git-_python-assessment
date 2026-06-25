list1 = [[1, 2], [3, 4], [5, 6]]
list2 = [7,8]

print("The original nested list is:", list1)
def extend_sublist(nested_list, sublist):
    for i in range(len(nested_list)):
        nested_list[i].extend(sublist)
    return nested_list

result = extend_sublist(list1, list2)
print("The nested list after extending with the sublist is:", result)
print("The original nested list after extending with the sublist is:", list1)