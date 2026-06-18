list1=["Chan","Bruce"]
list2=["Lee","Wayne"]
res=[]
def concatenate_lists(list1, list2):
    for i in list1:
        for j in list2:
            res.append(i+j)
    return res
n = concatenate_lists(list1, list2)
print("The concatenated list is:", n)
