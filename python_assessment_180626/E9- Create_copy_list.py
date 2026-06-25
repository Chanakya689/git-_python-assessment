l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)
print("The original list is l:", l)

copy_list = l.copy()
print("The copied list is copy_list:", copy_list)