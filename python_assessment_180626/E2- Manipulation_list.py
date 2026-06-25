#Manuplation list
l = [1, 2, 3, 4, 5]
l.append(6)
print("List after appending 6:", l)

l.extend([7, 8, 9])
print("List after extending with [7, 8, 9]:", l)

l.insert(0, 0)
print("List after inserting 0 at index 0:", l) 

l.sort()
print("List after sorting:", l)

print(list(map(lambda x: x*2, l)))
print(list(filter(lambda x: x%2==0, l)))

#slicing a list
print("Slicing the list from index 2 to 5:", l[2:5])
print("Slicing the list from index 0 to 3:", l[0:3])
print("Slicing the list from index 3 to the end:", l[3:]) 
print("Slicing the list from the start to index 4:", l[:4])  

#copying a list
l2 = l.copy()
print("Copied list l2 :", l2)

#extending a list with string
l3 = "HI"
l.extend(l3)
print("List after extending with l3:", l)

