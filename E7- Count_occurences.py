l=[]
n=int(input("Enter the size of the list: "))
for i in range(n):
    element=int(input("Enter the element: "))
    l.append(element)

print("The original list is:", l)

from collections import Counter
counter = Counter(l)
l=list(counter.items())
print("The count of each element in the list is:", l) 
