l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)

squared_list = list(map(lambda x: x**2, l))
print("The squared list is:", squared_list)