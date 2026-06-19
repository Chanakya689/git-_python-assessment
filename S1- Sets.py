#Perform Basic Set Operations

#creation of set 

my_set=set()
n=int(input("Enter the size of set:"))
for i in range(n):
    ele=int(input("Enter the size of set {}:".format(i)))
    my_set.add(ele)

print(my_set)  

#Adding set
my_set.add(9)
print(my_set)


set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Union
print(set1 | set2)

# Intersection
print(set1 & set2)

# Difference and gives set1 elements
print(set1 - set2)

# Symmetric Difference
print(set1 ^ set2)


#Using union()
a = {1, 2, 3}
b = {3, 4, 5}

result = a.union(b)
print(result)

#Intersection of Sets
a = {1, 2, 3}
b = {2, 3, 4}

result = a.intersection(b)
print(result)

#Add a List of Elements to a Set
s = {1, 2, 3}
lst = [4, 5, 6]

s.update(lst)
print(s)


#Set Difference Update

a = {1, 2, 3, 4}
b = {3, 4}

a.difference_update(b)
print(a)


#Remove Items From Set Simultaneously
s = {1, 2, 3, 4, 5}
s.difference_update({2, 3})
print("Difference update:")
print(s)

#Check Subset
a = {1, 2}
b = {1, 2, 3}
print("Subset check:")
print(a.issubset(b))

#Check Superset
a = {1, 2, 3}
b = {1, 2}
print("Superset check")
print(a.issuperset(b))

# Set Intersection Check
a = {1, 2, 3}
b = {3, 4, 5}
print("Intersection check:")
print(a.isdisjoint(b))

#Set Symmetric Difference Update
a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)
print(a)

#Set Intersection Update
a = {1, 2, 3}
b = {2, 3, 4}

a.intersection_update(b)
print(a)

#Find Common Elements in Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))
print(common)


#Frozen Set
fs = frozenset([1, 2, 3])

print(fs)
print("Immutable set (cannot add/remove items)")

#Count Unique Words
text = "apple banana apple orange banana"

print("length of text before set {}".format(len(text)))
words = text.split()
unique_words = set(words)
print(unique_words)
print("length of unique_words after set {}".format(len(unique_words)))