l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)   

print("The original list is:", l)

def sort_list(lst):
    return sorted(lst)

print("The sorted list is:", sort_list(l))