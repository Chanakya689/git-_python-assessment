#Creating a List

l=[]
n = int(input("Enter the size of the list: "))

for i in range(n):
    element = int(input("Enter the element: "))
    l.append(element)

print("The list is:", l)

#Finding the length of the list
print("The length of the list is:", len(l))

#Finding the sum of the list
print("The sum of the list is:", sum(l))

#Finding the maximum and minimum of the list
print("The maximum element in the list is:", max(l))
print("The minimum element in the list is:", min(l))

#Finding the average of the list
average = sum(l) / len(l)
print("The average of the list is:", average)

#Finding the median of the list
l.sort()    
n = len(l)
if n % 2 == 0:
    median1 = l[n//2]
    median2 = l[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = l[n//2]
print("The median of the list is:", median)

#appending an element to the list
element = int(input("Enter the element to append: "))
l.append(element)
print("The list after appending the element is:", l)

#extending the list with another list
n = int(input("Enter the size of the second list: "))   
l2 = []
for i in range(n):
    element = int(input("Enter the element: "))
    l2.append(element)
l.extend(l2)
print("The list after extending with the second list is:", l)

#popping an element from the list
l.pop()
print("The list after popping the last element is:", l)
print("The last element popped from the list")

#removing an element from the list
element = int(input("Enter the element to remove: "))
l.remove(element)
print("The list after removing the element is:", l) 


