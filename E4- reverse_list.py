l=[]
n = int(input("Enter the size of the list: "))

for i in range(n):
    element = int(input("Enter the element: "))
    l.append(element)   

print("The original list is:", l)
print("The reversed list is:", l[::-1])    
l.reverse()
print("The reversed list using reverse() method is:", l)