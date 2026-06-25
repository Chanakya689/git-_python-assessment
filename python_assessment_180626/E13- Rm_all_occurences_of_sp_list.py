l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)
print("The original list is:", l)

element_to_remove = int(input("Enter the element to remove: "))
while element_to_remove in l:
    l.remove(element_to_remove)
print("The list after removing all occurrences of", element_to_remove, "is:", l)