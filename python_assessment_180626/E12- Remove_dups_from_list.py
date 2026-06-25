l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)
print("The original list is:", l)

def remove_duplicates(lst):
    return list(set(lst))

print("The list after removing duplicates is:", remove_duplicates(l))