#creation of tuple

t=()
n=int(input("Enter the size of tuple:"))

for i in range(n):
    ele=int(input("Enter element {}:-".format(i)))
    t+=(ele,)
print(t)  

#removing elements in tuple needs Conversion into list 
l = list(t)
l.pop()
#l.remove()
t = tuple(l)
print("After removing element:-{}".format(t))
#Minimum element in tuple
print(min(t))

#Maximum element in tuple
print(max(t))

#occurence of element count
print(t)
ele = int(input("Enter the element you want to count:"))
c = t.count(ele)
print("Occurence of the element:-{}".format(c))

#Returning the index of the value
i = t.index(ele)
print("Index of the value:-{}".format(i))

#length of the tuple
print("Length of the tuple:-{}".format(len(t)))

#Sum of the tuple
print("Sum of the tuple:-{}".format(sum(t)))

#Sorting of tuple
print("Sorted tuple:-{}".format(sorted(t)))

#Converting list into tuple
l=[1,2,3,4,5]
t1 = tuple(l)
print("The list:{}".format(l))
print("The converted tuple:{}".format(t1))