#Creating a list

l = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    element = int(input("Enter the element: "))
    l.append(element)
print("The list is:", l)

#Finding the sum of the list
print("The sum of the list is:", sum(l))

s = 0
for i in range(len(l)):
    s+= l[i]
print("The sum of the list Manually done is:", s)

#Finding the average of the list
average = sum(l) / len(l)
print("The average of the list is:", average)