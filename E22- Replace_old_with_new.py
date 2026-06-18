l=[]
n = int(input("Enter the size of the list: "))

for i in range(n):
    element = int(input("Enter the element: "))
    l.append(element)

print("The original list is:", l)

old = int(input("Enter the element to be replaced: "))
new = int(input("Enter the new element: "))

def replace_old_with_new(lst, old, new):
    if old in lst:
        index = lst.index(old)
        lst[index] = new
    return lst

result = replace_old_with_new(l, old, new)
print("The list after replacing the element is:", result)