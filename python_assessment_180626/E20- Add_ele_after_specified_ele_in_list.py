l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)
print("The original list is:", l)

ele = int(input("Enter the element after which you want to add a new element: "))
if ele in l:
    new_ele = int(input("Enter the new element to add: "))
    index = l.index(ele)
    l.insert(index + 1, new_ele)
    print("The list after adding the new element is:", l)
else:
    print("The specified element is not in the list.")  
    