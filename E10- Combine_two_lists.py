l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)
print("The original list is:", l)
l2=[]
m=int(input("Enter the size of the second list: "))
for i in range(m):
    element=int(input("Enter the element: "))
    l2.append(element)
print("The second list is:", l2)

combined_list = l + l2
print("The combined list is:", combined_list)   
l.extend(l2)
print("The combined list using extend() method is:", l)