l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)

print("The original list is:", l)
print("The maximum element in the list is:", max(l))
print("The minimum element in the list is:", min(l))